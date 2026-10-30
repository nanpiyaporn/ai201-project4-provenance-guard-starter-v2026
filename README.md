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

- *What I asked for:* I ask AI explain the content step by steps. Do not do it for me.
- *What came back:* AI explain it to me clearly and showed me which line what I did wrong. It told me to edit it.
- For example: I wort this 
"LABEL_HUMAN = "We think a person wrote this."
LABEL_UNSURE = "We can't tell if a human or AI wrote this."
LABEL_AI = "They might be wrong, and I have a way to fix it.""

- *What I changed:*
LABEL_HUMAN = "We think a person wrote this."
LABEL_UNSURE = "We can't tell if a human or AI wrote this."
LABEL_AI = "We think it was probably from AI. If you wrote this yourself, you can ask for a review."
**Moment 2**

- *What I asked for:* I did not know how to run 'cure.exe'
- *What came back:* AI explain clearly how to run it.
- *What I changed:* I change a new terminal and run the code follow AI suggest. It works!

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



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
