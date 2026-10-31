# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positive

<!-- Your criterion. It must name a number. -->

<!--I submit 5 texts written by people, including 5 in plain, simple English. At most 2 get the AI label, in all 3 trials.-->
I run python calibrate.py 3 times. Of the 3 human texts (clearly human, formal human, plain human), at most 2 get the ai guess in any trial.


**Why this target:**

I got 2 wrong accusation from human text to AI. 

## 2. Score spread

<!-- Your criterion. -->
<!--I submit 3 clearly AI texts and 3 clearly human texts. The average confidence for the AI texts is at least 2 higher -->
I run python calibrate.py 3 times. In every trial, the average combined score of the 2 AI texts is at least 1 higher than the average of the 3 human texts.

**Why this target:**
It is for how far apart of text score ( Human vs AI). It checks the difference in average score. Ex a gap is 0.05 means the system can not tell the difference between human and AI 


---

## 3. Label coverage

<!-- Your criterion. -->

<!--I submit the 5 texts in calibrate.py. Each of the five labels appears at least 5 times.-->

I run python calibrate.py 3 times. In every trial, each of the three guesses (human, unsure, ai) appears at least 1 time across the 5 texts.


**Why this target:**

Is is for checking such as what input should produce each one? how many time is unsure label on.

The gab between AI and Human averages is 0.351

Every label need to be reachable because it is easy the system can be check. For example, 0.6 cap stops signal that disagree from reaching the AI label.
---

## 4. The appeal path

<!-- Your criterion. -->

I send 3 appeals with real content_ids. Every one returns status 200 and status: under_review, and adds an entry to GET /log. An appeal with a fake id returns 404.

.

**Why this target:**
A wrong accusation hurts a real writer, and the appeal is their only way to challenge it

Every appeal must be recorded because it is easy to tract if it match the expected. For example I appeal with a real id and expect [200], under_review, that match with my result.


---

## 5. Bad input

<!-- Your criterion. -->

I send missing, empty, and over-20,000-character text. Every request returns 400, none returns 500, and each one adds a rejected entry to GET /log.

**Why this target:**
For checking if it missing ot empty text when it return. For example, code 400 or 413. Not 500 or crash.

It is clear that 400 better for a writer than a crash because the system still running.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
