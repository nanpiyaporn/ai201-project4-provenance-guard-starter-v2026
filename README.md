# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->


1. Writer sends 'POST /submit' with 'text' and 'creator_id', so the system has raw text and knows who sent it.
2. app.py checks the input. Missing, empty or very long text gets a clear error instead of a crash.
3. 'detector.model_signal' turns the text into a 'model_score' (0–1).
4. 'stylometry.style_signal' turns it into a 'style_score' (0–1).
5. 'scoring.combine_signals' merges the two into one confidence score.
6. 'scoring.score_to_label' turns that number into a sentence a reader can understand.
7. 'audit.log_decision' saves everything under a 'content_id', and the response goes back to the writer. If they disagree, they can use that id with '/appeal'.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** 
It measure perplexity meaning how predictable the text is to GPT-2

**Why that might differ between human and AI writing:**
AI text is predictable because the model picks likely next words.

**What it can't see:**
Usually, people who use English as a second language as I am. I always try to use a simple word. But AI like to use a difference vocabulary that human (professional use).

### Signal two — the style signal

**What it measures:**
It measure shape of the text ( how long of the sentence)

**Why that might differ between human and AI writing:**
AI temps to write not to long and not too short. It seems like the same length mostly. 

**What it can't see:**
If AI writes more typos, it will more likely like a human style more.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
I averages the 2 signals out. If its disagree > 0.30 the score is capped at 0.60, so the text get 'unsure' instead of 'AI' because in general a good writer remains a good adjustment (not accused things) 

**The numbers:**
weights 0.5 and 0.5, gap 0.30, cap 0.60, thresholds 0.35 and 0.65.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->


**A case where my two signals split, and what my rule does with it:**

the plain human paragraph, with model 0.86 and style 0.49, a gap of 0.37. The 50/50 average would give 0.674 and label it AI. The cap brings it down to 0.60, so it's labeled unsure

---

## Design Notes (Milestone 1)

### The false positive

<!-- A real writer submits real work and the system calls it AI. Follow that
     person through the service. This is the scenario that decides the
     thresholds in Milestone 4. -->

**Who:**
A real person, for example a student who writes in English as a second language and uses simple words and short sentences. You wrote about this in your Signal one blind spot.

**Their scores:** model_score ≈ 0.86 , style_score ≈ 0.49→ combined ≈ 0.60

<!-- Thresholds in config.py: below 0.35 = human, 0.35–0.65 = unsure,
     above 0.65 = AI -->

**What the label said to them:**
"We can't tell if a human or AI wrote this."

**Does it read as an accusation?**
No, it is not an an accusation.

**What they can do about it:**
They can copy 'content_id' and 'send POST /appeal' with their reasoning. The status changes to under_review and a person reviews it.

**What this means for my thresholds:**
Without the disagreement cap, the 50/50 average gave 0.674, above 0.65, so the label would have been AI. The cap keeps them in "unsure". That's why I chose that rule.

### Endpoint contracts

<!-- Field by field: what goes in, what comes out. Could someone else build
     against this without asking a question? -->

**POST /submit**

- In: `text` (string, required, not empty, at most 20,000 characters), `creator_id` (string, required)
- Out (success, 200): `content_id`, `guess` ("human" / "unsure" / "ai"), `confidence` (0–1), `label` (the sentence the writer sees), `model_score` (0–1), `style_score` (0–1)
- Out (error, 400): `{error, message}` when text or creator_id is missing, empty, too long, or text is too short to score

**POST /appeal**

- In: `content_id` (string, must match a submission in the log), `reasoning` (string, required)
- Out (success, 200): `content_id`, `status` ("under_review"), `message` (confirmation for the writer)
- Out (error, 400): `{error, message}` when content_id or reasoning is missing
- Out (error, 404): `{error, message}` when no submission has that content_id


---------

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think a person wrote this. |
| unsure | 0.35 – 0.65 | We can't tell if a human or AI wrote this. |
| high-confidence AI | 0.65 – 1.00 | We think it was probably from AI. If you wrote this yourself, you can ask for a review. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

I use the word " can't tell" because it does not blame the writer

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Artificial intelligence has transformed the way we live and work. It offers numerous benefits, including increased efficiency, improved decision-making, and enhanced productivity. However, it is important to consider the ethical implications of this technology.", "creator_id": "student-01"}'
```

```json
{
  "confidence": 0.8699,
  "content_id": "4b8257ea-e969-4148-8a53-18153e4d3f43",
  "guess": "ai",
  "label": "We think it was probably from AI. If you wrote this yourself, you can ask for a review.",
  "model_score": 0.908,
  "style_score": 0.8318
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "4b8257ea-e969-4148-8a53-18153e4d3f43", "reasoning": "I wrote this myself for my class."}'
```

```json
{
  "content_id": "4b8257ea-e969-4148-8a53-18153e4d3f43",
  "message": "Thanks — your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.8699,
      "content_id": "4b8257ea-e969-4148-8a53-18153e4d3f43",
      "creator_id": "student-01",
      "guess": "ai",
      "label": "We think it was probably from AI. If you wrote this yourself, you can ask for a review.",
      "model_score": 0.908,
      "status": "decided",
      "style_score": 0.8318,
      "timestamp": "2026-10-30T02:12:37+00:00"
    },
    {
      "content_id": "4b8257ea-e969-4148-8a53-18153e4d3f43",
      "creator_id": "student-01",
      "event": "appeal",
      "reasoning": "I wrote this myself for my class.",
      "status": "under_review",
      "timestamp": "2026-10-30T02:19:04+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I ask AI explain the content step by steps. I also picked the combining rule and wrote the labels.
- *What came back:* AI explain it to me clearly and showed me which line what I did wrong. It told me to edit it.
- 
- For example: I wort this 
LABEL_HUMAN = "We think a person wrote this."
LABEL_UNSURE = "We can't tell if a human or AI wrote this."
LABEL_AI = "They might be wrong, and I have a way to fix it.

- *What I changed:*
LABEL_HUMAN = "We think a person wrote this."
LABEL_UNSURE = "We can't tell if a human or AI wrote this."
LABEL_AI = "We think it was probably from AI. If you wrote this yourself, you can ask for a review."

**Moment 2**

- *What I asked for:* I did not know how to run 'cure.exe'
- *What came back:* AI explain clearly how to run it.
- *What I changed:* I change a new terminal and run the code follow AI suggest. It works!
- 

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
I just leave the same that like you have.
It limits how many requests each caller can send to /submit  to 10 requests / min and 200 requests/day.

**What a caller counts as:** <!-- per address, or per creator_id? They fail differently — one script can look like a thousand callers, and one household can look like one. -->

Per `creator_id` when the request includes one, otherwise per IP address (`rate_limit_key()` in app.py.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 200
  [ 7/15] 200
  [ 8/15] 200
  [ 9/15] 200
  [10/15] 200
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429


============================================================
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
============================================================

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

56 attacks against http://127.0.0.1:5000
Signal one runs a model. The first request is slow while it loads;
after that, a second or two each.

  [ 1/56] EV01   evasion           200   human    ?
  [ 2/56] EV02   evasion           200   human    ?
  [ 3/56] EV03   evasion           200   unsure   ?
  [ 4/56] EV04   evasion           200   unsure   ?
  [ 5/56] EV05   evasion           200   human    ?
  [ 6/56] EV06   evasion           200   human    ?
  [ 7/56] EV07   evasion           200   ai       ?
  [ 8/56] EV08   evasion           200   human    ?
  [ 9/56] EV09   evasion           200   unsure   ?
  [10/56] EV10   evasion           200   unsure   ?
  [11/56] FP01   false_positive    200   unsure   ?
  [12/56] FP02   false_positive    200   ai       ?
  [13/56] FP03   false_positive    200   unsure   ?
  [14/56] FP04   false_positive    200   unsure   ?
  [15/56] FP05   false_positive    200   ai       ?
  [16/56] FP06   false_positive    200   unsure   ?
  [17/56] FP07   false_positive    200   unsure   ?
  [18/56] FP08   false_positive    200   human    ?
  [19/56] PI01   prompt_injection  200   human    ?
  [20/56] PI02   prompt_injection  200   human    ?
  [21/56] PI03   prompt_injection  200   unsure   ?
  [22/56] PI04   prompt_injection  200   unsure   ?
  [23/56] PI05   prompt_injection  200   unsure   ?
  [24/56] PI06   prompt_injection  200   unsure   ?
  [25/56] MF01   malformed         400   —        ?
  [26/56] MF02   malformed         400   —        ?
  [27/56] MF03   malformed         200   human    ?
  [28/56] MF04   malformed         200   human    ?
  [29/56] MF05   malformed         200   unsure   ?
  [30/56] MF06   malformed         200   unsure   ?
  [31/56] MF07   malformed         200   unsure   ?
  [32/56] MF08   malformed         400   —        ?
  [33/56] RQ01   malformed         400   —        ?
  [34/56] RQ02   malformed         400   —        ?
  [35/56] RQ03   malformed         400   —        ?
  [36/56] RQ04   malformed         400   —        ?
  [37/56] RQ05   malformed         400   —        ?
  [38/56] RQ06   malformed         400   —        ?
  [39/56] RQ07   malformed         400   —        ?
  [40/56] RQ08   malformed         400   —        ?
  [41/56] RQ09   malformed         400   —        ?
  [42/56] RQ10   malformed         400   —        ?
  [43/56] RQ11   malformed         400   —        ?
  [44/56] RQ12   malformed         400   —        ?
  [45/56] FL01_01 flood_same_creator 200   human    ?
  [46/56] FL01_02 flood_same_creator 200   human    ?
  [47/56] FL01_03 flood_same_creator 200   human    ?
  [48/56] FL01_04 flood_same_creator 200   human    ?
  [49/56] FL01_05 flood_same_creator 200   human    ?
  [50/56] FL01_06 flood_same_creator 200   human    ?
  [51/56] FL01_07 flood_same_creator 200   human    ?
  [52/56] FL01_08 flood_same_creator 200   human    ?
  [53/56] FL01_09 flood_same_creator 200   human    ?
  [54/56] FL01_10 flood_same_creator 200   human    ?
  [55/56] FL01_11 flood_same_creator 429   —        ?
  [56/56] FL01_12 flood_same_creator 429   —        ?

============================================================
Wrote results\attack_run_2026-11-04_2054_before.md
  auto-marked BROKE: 0
  left for you:      56
============================================================

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-05T01:54:12+00:00", "content_id": "ea1d2c96-3940-4c5b-8544-d45742b0faf4", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.6, "combined_score": 0.6694, "label": "We think it was probably from AI. If you wrote this yourself, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-05T01:54:12+00:00", "content_id": "09a3e3fa-755a-405a-a11d-61c6ea2621a5", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.5654, "combined_score": 0.6829, "label": "We think it was probably from AI. If you wrote this yourself, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-05T01:54:10+00:00", "content_id": "01f2a388-d062-4290-ad59-0b3c5a66131c", "creator_id": "attacker_EV01", "guess": "human", "model_score": 0.1635, "style_score": 0.4736, "combined_score": 0.3185, "label": "We think a person wrote this.", "status": "decided"}
{"timestamp": "2026-11-05T01:54:10+00:00", "content_id": "783e3e0e-ea57-4541-9f33-cbc88066ffce", "creator_id": "attacker_EV02", "guess": "human", "model_score": 0.5943, "style_score": 0.0455, "combined_score": 0.3199, "label": "We think a person wrote this.", "status": "decided"}
{"timestamp": "2026-11-05T01:54:11+00:00", "content_id": "3572760d-5694-47b4-9a4e-0329bff568bd", "creator_id": "attacker_EV05", "guess": "human", "model_score": 0.3212, "style_score": 0.2135, "combined_score": 0.2673, "label": "We think a person wrote this.", "status": "decided"}
{"timestamp": "2026-11-05T01:54:13+00:00", "content_id": "be4d27e3-d596-42cb-a1fe-0aa0e775b1c9", "creator_id": "attacker_PI01", "guess": "human", "model_score": 0.4625, "style_score": 0.0, "combined_score": 0.2313, "label": "We think a person wrote this.", "status": "decided"}
{"timestamp": "2026-11-05T01:54:13+00:00", "content_id": "26500521-8355-4b72-bd11-337f5dba21b0", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.064, "combined_score": 0.1342, "label": "We think a person wrote this.", "status": "decided"}
{"timestamp": "2026-11-05T01:54:14+00:00", "content_id": "876ba2f7-7f91-44cb-956a-f162f2cce57a", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.225, "combined_score": 0.1125, "label": "We think a person wrote this.", "status": "decided"}
{"timestamp": "2026-11-05T01:54:14+00:00", "content_id": "9898ae60-3191-4f47-9eb6-e3faf5d2dd74", "creator_id": "attacker_MF06", "guess": "unsure", "model_score": 0.9969, "style_score": 0.375, "combined_score": 0.6, "label": "We can't tell if a human or AI wrote this.", "status": "decided"}
{"timestamp": "2026-11-05T01:54:15+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}


```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP05: technical documentation written by a person, labeled ai at 0.683 confidence (model_score 0.801, style_score 0.565). This is the one I'd least want to explain. The writer did nothing unusual. They wrote clear, consistent, precise documentation, which is exactly what good technical writing looks like. My service then showed them "We think it was probably from AI." Both signals pointed the wrong way: the model reads predictable, low-surprise prose as machine-like, and the style signal reads uniform sentence length and vocabulary as machine-like.Technical docs have both traits because they're well written. The combining rule averaged two wrong signals into a confident wrong answer.

FP02 (formal register, 0.669) failed the same way, so this isn't a one-off. It means my service penalizes people who write carefully and formally, a group that includes professional writers and non-native speakers who stick to safe, regular phrasing. The appeal path exists, but it puts the burden on the person who was wrongly accused.
---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.False positive: human texts guessed ai  | ≤ 2 of 3 | 0/3 | 0/3 | 0/3 | MET |
| 2. Score spread: AI avg − human avg | ≥ 1 | 0.351 |0.351  | 0.351 | MISSED |
| 3.Label coverage: human / unsure / ai each appear  | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |
| 4.Appeal path: 3 real appeals + 1 fake id  | 4 of 4 | 4/4 | 4/4 |  4/4| MET |
| 5. Bad input: 400 + rejected entry in log | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |

**How I decided each verdict:**

1. **False positive — MET.** In all three trials, none of the 3 human texts got the "ai" guess, which is within "at most 2 of 3". To be honest, this target was too low: it would still pass if 2 of my 3 human writers were accused. The attack set also shows the problem my calibration texts missed. FP02 and FP05, both real human writing, were labeled "ai". This is the criterion I'd tighten, to "0 of 3 in every trial, and no false_positive attack labeled ai".
2. **Score spread — MISSED.** The gap was 0.351 in all three trials, against a target of at least 1. The gap was the same every time, so this is not run-to-run noise. It is a miss in every trial. A gap of 1.0 is also impossible unless every score sits at exactly 0 or 1. See diagnosis 1.
3. **Label coverage — MET.** Each of human, unsure and ai appeared at least once among the 5 texts in all three trials. The "running" text reached "unsure" only because the disagreement cap held it at 0.6.
4. **Appeal path — MET.** In each trial, all 3 real appeals returned 200 with `under_review` and had a matching entry in the log, and the fake id returned 404. That is 4/4 in all three trials.
5. **Bad input — MET.** Missing text, empty text and over-length text each returned 400, never 500, in all three trials, and each one wrote a rejected entry to the log. But the attack set found input this criterion didn't test: control characters, punctuation-only text and emoji were accepted with a 200. See diagnosis 5.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

**Trial 1**

```json
[
  {
    "kind": "real",
    "content_id": "ad790cfb-63a4-410f-8349-92c8a9d7244b",
    "appeal_status": 200,
    "response": {
      "content_id": "ad790cfb-63a4-410f-8349-92c8a9d7244b",
      "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
      "status": "under_review"
    },
    "log_entry": {
      "content_id": "ad790cfb-63a4-410f-8349-92c8a9d7244b",
      "creator_id": "eval_appeal_t1_1",
      "event": "appeal",
      "reasoning": "I wrote this myself and can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:19:32+00:00"
    },
    "passed": true
  },
  {
    "kind": "real",
    "content_id": "07ff66e8-51ea-4ea1-be14-25d806b63bda",
    "appeal_status": 200,
    "response": {
      "content_id": "07ff66e8-51ea-4ea1-be14-25d806b63bda",
      "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
      "status": "under_review"
    },
    "log_entry": {
      "content_id": "07ff66e8-51ea-4ea1-be14-25d806b63bda",
      "creator_id": "eval_appeal_t1_2",
      "event": "appeal",
      "reasoning": "I wrote this myself and can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:19:32+00:00"
    },
    "passed": true
  },
  {
    "kind": "real",
    "content_id": "bf9ca88b-d761-486b-8295-5d3298e44bc2",
    "appeal_status": 200,
    "response": {
      "content_id": "bf9ca88b-d761-486b-8295-5d3298e44bc2",
      "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
      "status": "under_review"
    },
    "log_entry": {
      "content_id": "bf9ca88b-d761-486b-8295-5d3298e44bc2",
      "creator_id": "eval_appeal_t1_3",
      "event": "appeal",
      "reasoning": "I wrote this myself and can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:19:32+00:00"
    },
    "passed": true
  },
  {
    "kind": "fake",
    "content_id": "fake-44d0a043-d0cc-45fc-a507-ecc15cd982cd",
    "appeal_status": 404,
    "response": {
      "error": "not_found",
      "message": "No submission with content_id 'fake-44d0a043-d0cc-45fc-a507-ecc15cd982cd'. Check it was copied exactly."
    },
    "passed": true
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

**1. Criterion 2 missed (gap 0.351, target ≥ 1): combining rule + signal one, and an unreachable target.**
Scores run 0–1, so a gap of 1.0 would need every AI text at exactly 1.0 and every human text at exactly 0.0. The target can't be met as written. But the gap is also small for a real reason: the AI average is 0.781 and the human average is 0.430. The human average is pulled up by the plain "running" text, where signal one reads simple, predictable prose as AI (model_score 0.859). My disagreement cap holds it at 0.6, which keeps it out of "ai" but parks it at the top of "unsure". The formal "committee" text adds 0.459. Plain and formal human writing both score high on signal one, so the two groups can't separate.

**2. Evasion EV02, EV06, PI01, PI02: combining rule. The disagreement cap only works in one direction.**
In all four, the signals split badly but the average landed under 0.35, so they were labeled "human". EV02: model 0.594, style 0.046 → 0.320. PI01: model 0.463, style 0.0 → 0.231. My rule caps a split *down* to 0.6 when the average is high, but never pulls a split *up* into "unsure" when the average is low. A split is supposed to mean uncertainty, yet here it produced a confident "human". Breaking sentences into uneven lengths (EV02, EV06) pushes signal two to near 0, because my style signal weights sentence-length spread at 0.45, so it is easy to game.

**3. Evasion EV01, EV05, EV08: signal one fooled.**
Typos (EV01, model 0.164) and a heavy editing pass (EV05, model 0.321) raise perplexity, so GPT-2 finds the text surprising and reads it as human. EV08 is too short to give the model enough tokens (model 0.245). Signal two didn't catch them either, so the combined score fell into "human".

**4. False positives FP02, FP05: both signals wrong in the same direction, so no cap.**
FP05: model 0.801, style 0.565 → 0.683 "ai". FP02: model 0.739, style 0.600 → 0.669 "ai". Careful formal and technical writing is predictable (signal one) and evenly shaped (signal two). The signals agree, so the disagreement cap never fires, and the 50/50 average crosses 0.65. My only safeguard handles disagreement, not two signals that are wrong together.

**5. Malformed MF03, MF04, MF05, MF06, MF07: the route.**
Input with no real words still got a 200 and a label. Control characters and punctuation-only text were labeled "human" (MF03 0.113, MF04 0.306). Emoji, a single long word, and right-to-left script all came back "unsure" at exactly 0.600 because of the cap. My route only rejects text that is empty, whitespace-only, or too long. It never checks that the text has enough real words to score, so both signals produce numbers for text they can't read.

**What held:** the rate limit (FL01: 429 after 10 requests), every RQ request-shape error (400), and MF01, MF02, MF08 (400).

---

## The Improvement

**What I changed:**

One change: `config.AI_THRESHOLD` raised from **0.65 to 0.70** in `config.py`. This widens the unsure band from 0.35–0.65 to 0.35–0.70. The signals and the combining rule are untouched, so every score is exactly the same as before. Only which label a score maps to has changed.

**Which diagnosis pointed at it:**

Diagnosis 4. FP02 (0.669) and FP05 (0.683) were real human writing labeled "ai". Both signals were wrong in the same direction, so my disagreement cap never fired. Both scores sat just above 0.65, so moving the line to 0.70 moves them out of the "ai" band. I picked this one because it is my single worst outcome: a real writer being told their work is AI.

### Attack Run — After

Produced by `run_attacks.py::main` → `results/attack_run_2026-11-04_2223_after.md`. Scores are identical in both runs. Only the rows below changed label. Every other attack got the same label as before.

| ID | Family | Score | Before (0.65) | After (0.70) | Verdict before → after |
|---|---|---|---|---|---|
| FP02 | false_positive | 0.669 | ai | unsure | BROKE → HELD |
| FP05 | false_positive | 0.683 | ai | unsure | BROKE → HELD |
| EV07 | evasion | 0.652 | ai | unsure | HELD (caught as ai) → HELD (only unsure) |

| Family | Labeled ai before | Labeled ai after |
|---|---|---|
| false_positive (human text) | 2 of 8 | **0 of 8** |
| evasion (AI text) | 1 of 10 | **0 of 10** |

### Run Log — After

Produced by `run_eval.py::main` → `results/run_2026-11-04_2223_after.md`, and `check_appeals.py::one_trial` → `results/appeals_2026-11-04_2223_after.md`.

| Criterion | Target | Before (×3) | After Run 1 | After Run 2 | After Run 3 | Verdict |
|---|---|---|---|---|---|---|
| 1. False positive | ≤ 2 of 3 | 0/3 | 0/3 | 0/3 | 0/3 | MET |
| 2. Score spread | ≥ 1 | 0.351 | 0.351 | 0.351 | 0.351 | MISSED |
| 3. Label coverage | 3 of 3 | 3/3 | 3/3 | 3/3 | 3/3 | MET |
| 4. Appeal path | 4 of 4 | 4/4 | 4/4 | 4/4 | 4/4 | MET |
| 5. Bad input | 3 of 3 | 3/3 | 3/3 | 3/3 | 3/3 | MET |

**Did it help, and how do I know:**

Yes for the problem I aimed at. It also created a new problem.

- **It helped:** the number of human writers in the attack set labeled "ai" went from 2 to 0 (FP02 and FP05 both moved to "unsure"). I know it was the threshold and not run-to-run noise because the scores are identical to three decimals in both runs (0.669 and 0.683). Only the label changed.
- **What it cost:** EV07 (AI text padded with punctuation, 0.652) used to be the only attack my service caught as "ai". Now it is "unsure". After the change, **no attack in the whole set gets the "ai" label.** The cost of a wrong accusation moved from real writers onto the site, which now lets more AI text through without a firm label.
- **It is fragile:** the plain AI calibration text scores 0.709, only 0.009 above the new line. That is the only thing keeping criterion 3 (every label reachable) MET. A small change to that text could leave "ai" with no examples at all.
- **What it didn't touch:** criterion 2 is still 0.351, because moving a threshold can't change scores. The evasion attacks that got "human" (diagnoses 2 and 3) and the malformed input (diagnosis 5) are unchanged.


---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
