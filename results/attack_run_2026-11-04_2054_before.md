# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 20:54
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `01f2a388-d062-4290-ad59-0b3c5a66131c` | human | 0.319 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `783e3e0e-ea57-4541-9f33-cbc88066ffce` | human | 0.320 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `164d8ca2-cfda-4e78-b1cc-942f9168c928` | unsure | 0.514 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `b2873dd6-a96c-43d5-922e-89f7aaa95172` | unsure | 0.542 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3572760d-5694-47b4-9a4e-0329bff568bd` | human | 0.267 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `9f908dae-de14-44cb-bbcb-83c0956b8a1c` | human | 0.337 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c9317463-e1b6-4c55-a19e-3dec10b79d14` | ai | 0.652 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `4741a7fd-0237-47e1-9a54-bb9bfe9ce086` | human | 0.327 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b4327bc2-45bd-4e4f-a1bf-9d62d3527aa3` | unsure | 0.471 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `24bdc281-4fc0-4062-a857-b1e71e5ebed9` | unsure | 0.600 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `04a7c72d-a3a3-4e2d-a986-1da14193cf64` | unsure | 0.471 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `ea1d2c96-3940-4c5b-8544-d45742b0faf4` | ai | 0.669 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `a9de60cc-d565-4c44-9c93-d01edae83f95` | unsure | 0.600 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `62ea0c8f-d636-4cf9-91f5-5d941a807a6b` | unsure | 0.600 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `09a3e3fa-755a-405a-a11d-61c6ea2621a5` | ai | 0.683 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `6bb9edf5-4b7f-47ba-b4aa-ced8b4a57443` | unsure | 0.568 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `076ceb18-b58d-4eda-b795-7b63e849b1a7` | unsure | 0.524 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `d398cada-1141-4b38-a35d-88583ebf8614` | human | 0.269 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `be4d27e3-d596-42cb-a1fe-0aa0e775b1c9` | human | 0.231 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `26500521-8355-4b72-bd11-337f5dba21b0` | human | 0.134 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `83db8655-f676-4f92-a6e8-374342ae4498` | unsure | 0.517 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `1a33cdd8-ccf0-44d1-9ac2-0c57e08d66b6` | unsure | 0.526 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `0d96f5ff-1cbf-4105-9a99-d43d33dcd26d` | unsure | 0.603 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `ddd6d121-9791-4a9c-aee0-f3ee9da35fdb` | unsure | 0.446 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `876ba2f7-7f91-44cb-956a-f162f2cce57a` | human | 0.113 |  |
| MF04 | malformed | text is only punctuation | 200 | `aeb4fee8-a138-4bb0-ae7c-eeccd53e68f1` | human | 0.306 |  |
| MF05 | malformed | text is a very long single word | 200 | `227c7ca3-36a8-4a78-86b9-2f5d337e8189` | unsure | 0.600 |  |
| MF06 | malformed | text is emoji only | 200 | `9898ae60-3191-4f47-9eb6-e3faf5d2dd74` | unsure | 0.600 |  |
| MF07 | malformed | text is right-to-left script | 200 | `3a58703e-f160-477a-8df8-861afa98927a` | unsure | 0.600 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `06d347af-1f93-4238-900e-fafaf44b34d2` | human | 0.127 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3a53de5e-3117-4a7a-ad71-4d02ea2b6b58` | human | 0.127 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `125507ed-da50-4cec-91a2-781e25e7b04e` | human | 0.127 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `aa685659-85f3-4464-9301-8234b4552372` | human | 0.127 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8433e963-9ee7-49db-ac23-36a018464d62` | human | 0.127 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b9417142-532a-4614-8da1-14fd96be9965` | human | 0.127 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5c176e8f-bd36-4a4b-9527-fa27a0c608b3` | human | 0.127 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cc723206-bb39-4b57-adbf-d9fda2d6d6d5` | human | 0.127 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c6467105-571d-48fc-b039-c1b03d2843ab` | human | 0.127 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1d1de4d3-c53d-4183-be09-c894a9a88262` | human | 0.127 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "01f2a388-d062-4290-ad59-0b3c5a66131c",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3185,
  "model_score": 0.1635,
  "style_score": 0.4736,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "783e3e0e-ea57-4541-9f33-cbc88066ffce",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.3199,
  "model_score": 0.5943,
  "style_score": 0.0455,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "164d8ca2-cfda-4e78-b1cc-942f9168c928",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5138,
  "model_score": 0.6662,
  "style_score": 0.3613,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "b2873dd6-a96c-43d5-922e-89f7aaa95172",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5416,
  "model_score": 0.6114,
  "style_score": 0.4718,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "3572760d-5694-47b4-9a4e-0329bff568bd",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2673,
  "model_score": 0.3212,
  "style_score": 0.2135,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "9f908dae-de14-44cb-bbcb-83c0956b8a1c",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.3367,
  "model_score": 0.5727,
  "style_score": 0.1006,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c9317463-e1b6-4c55-a19e-3dec10b79d14",
  "creator_id": "attacker_EV07",
  "guess": "ai",
  "confidence": 0.6522,
  "model_score": 0.5862,
  "style_score": 0.7183,
  "label": "We think it was probably from AI. If you wrote this yourself, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "4741a7fd-0237-47e1-9a54-bb9bfe9ce086",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3265,
  "model_score": 0.2452,
  "style_score": 0.4078,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "b4327bc2-45bd-4e4f-a1bf-9d62d3527aa3",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4706,
  "model_score": 0.7042,
  "style_score": 0.237,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "24bdc281-4fc0-4062-a857-b1e71e5ebed9",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.9792,
  "style_score": 0.415,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "04a7c72d-a3a3-4e2d-a986-1da14193cf64",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4714,
  "model_score": 0.6175,
  "style_score": 0.3253,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "ea1d2c96-3940-4c5b-8544-d45742b0faf4",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6694,
  "model_score": 0.7387,
  "style_score": 0.6,
  "label": "We think it was probably from AI. If you wrote this yourself, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "a9de60cc-d565-4c44-9c93-d01edae83f95",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.8051,
  "style_score": 0.4752,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "62ea0c8f-d636-4cf9-91f5-5d941a807a6b",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.8329,
  "style_score": 0.4236,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "09a3e3fa-755a-405a-a11d-61c6ea2621a5",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6829,
  "model_score": 0.8005,
  "style_score": 0.5654,
  "label": "We think it was probably from AI. If you wrote this yourself, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "6bb9edf5-4b7f-47ba-b4aa-ced8b4a57443",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5676,
  "model_score": 0.8814,
  "style_score": 0.2539,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "076ceb18-b58d-4eda-b795-7b63e849b1a7",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5245,
  "model_score": 0.8816,
  "style_score": 0.1673,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "d398cada-1141-4b38-a35d-88583ebf8614",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2685,
  "model_score": 0.3223,
  "style_score": 0.2147,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "be4d27e3-d596-42cb-a1fe-0aa0e775b1c9",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.2313,
  "model_score": 0.4625,
  "style_score": 0.0,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "26500521-8355-4b72-bd11-337f5dba21b0",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1342,
  "model_score": 0.2044,
  "style_score": 0.064,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "83db8655-f676-4f92-a6e8-374342ae4498",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5168,
  "model_score": 0.5943,
  "style_score": 0.4392,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "1a33cdd8-ccf0-44d1-9ac2-0c57e08d66b6",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5256,
  "model_score": 0.4998,
  "style_score": 0.5515,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "0d96f5ff-1cbf-4105-9a99-d43d33dcd26d",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.6027,
  "model_score": 0.6401,
  "style_score": 0.5653,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "ddd6d121-9791-4a9c-aee0-f3ee9da35fdb",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.5583,
  "style_score": 0.3331,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "876ba2f7-7f91-44cb-956a-f162f2cce57a",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.1125,
  "model_score": 0.0,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "aeb4fee8-a138-4bb0-ae7c-eeccd53e68f1",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3056,
  "model_score": 0.0112,
  "style_score": 0.6,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "227c7ca3-36a8-4a78-86b9-2f5d337e8189",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.9976,
  "style_score": 0.225,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "9898ae60-3191-4f47-9eb6-e3faf5d2dd74",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.9969,
  "style_score": 0.375,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "3a58703e-f160-477a-8df8-861afa98927a",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6,
  "model_score": 0.9064,
  "style_score": 0.375,
  "label": "We can't tell if a human or AI wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "06d347af-1f93-4238-900e-fafaf44b34d2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "3a53de5e-3117-4a7a-ad71-4d02ea2b6b58",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "125507ed-da50-4cec-91a2-781e25e7b04e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "aa685659-85f3-4464-9301-8234b4552372",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "8433e963-9ee7-49db-ac23-36a018464d62",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "b9417142-532a-4614-8da1-14fd96be9965",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "5c176e8f-bd36-4a4b-9527-fa27a0c608b3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "cc723206-bb39-4b57-adbf-d9fda2d6d6d5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "c6467105-571d-48fc-b039-c1b03d2843ab",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "1d1de4d3-c53d-4183-be09-c894a9a88262",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1268,
  "model_score": 0.0287,
  "style_score": 0.225,
  "label": "We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
