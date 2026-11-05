# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 22:23
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `05bd1428-85d6-4db1-8e65-e87a11a8cf02` | human | 0.319 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c7f2b7ec-8684-4591-a1e9-b24dbdba099c` | human | 0.320 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `57655dfc-e3da-489d-be93-509a29e63a06` | unsure | 0.514 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `ec182719-504b-49e2-aa67-183ddcff68ad` | unsure | 0.542 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `44f4c025-6df1-46d8-954c-da0798ab29a3` | human | 0.267 |  BROKE|
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `be96766b-5915-4b46-a732-466653dc2d03` | human | 0.337 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0cde62fa-a417-424a-aabe-b37bc95f2d1f` | unsure | 0.652 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `50d5b253-33e6-44cc-bc49-0c44e967781b` | human | 0.327 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `ed99ec85-3a27-44ff-b100-764958f79a04` | unsure | 0.471 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `2f7567c1-08e6-4880-8cd8-51aa665d093a` | unsure | 0.600 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `acfb6872-0436-457a-a792-b5f098615599` | unsure | 0.471 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `1ba6fedf-7c84-49ed-b4b8-4b5f32f5f329` | unsure | 0.669 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `d6902e08-9ddf-4a4b-84f5-e4fa4bcd2102` | unsure | 0.600 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `8af3d09a-ed51-42c5-9a78-7ca83fbbe7b2` | unsure | 0.600 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `8c2b71ee-3451-4e91-adc0-c9e82dda723d` | unsure | 0.683 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `cf9140c6-cbfa-4041-b714-2647dd204f5d` | unsure | 0.568 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `0e3645ef-87c3-41e4-b696-ae6b41707fe7` | unsure | 0.524 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `b079654b-8ad6-43a8-84ca-ce36205e8e12` | human | 0.269 | BROKE |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b0d5ab42-aa84-4e73-a957-300f55565025` | human | 0.231 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `2327c52c-1454-4562-8d06-6055baa37122` | human | 0.134 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `6a2befac-890d-494a-b36b-6c51d9872b64` | unsure | 0.517 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `5374ad5f-5774-4c40-a320-2c17af31b543` | unsure | 0.526 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `080a7bdd-7e80-442a-b7ce-eafd7eef2fc7` | unsure | 0.603 |HELD  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `f41638bd-5338-40fd-b183-2bfcb7b0b8c5` | unsure | 0.446 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `37865fa5-624f-44db-92d9-a3ceb5bcced2` | human | 0.113 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `5e1c97d1-b0be-4fc8-a98e-59631561285d` | human | 0.306 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `e18e3d60-f3b7-469f-a196-2491fa6d82f1` | unsure | 0.600 | HELD |
| MF06 | malformed | text is emoji only | 200 | `7ff6fba2-1dde-49c5-9209-c084528052ea` | unsure | 0.600 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `f0cbc061-3c4c-421a-9574-b26bac1a8eba` | unsure | 0.600 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |HELD|
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8e1185cc-bda3-47cd-a736-9855f5151d50` | human | 0.127 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ab426fef-fe01-486f-aaa9-0bc9329b7fd0` | human | 0.127 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e3efdeb1-6bce-48a4-8f13-27b09de3fe0b` | human | 0.127 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `603b9a0b-6c3d-4779-8d15-5f95284555bc` | human | 0.127 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f50845bc-4a83-4024-8872-8f5a9258677e` | human | 0.127 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `29ef195a-2874-47fe-a4d2-88a82039a8e0` | human | 0.127 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d7428a97-a4e6-4a11-9582-102d155b274b` | human | 0.127 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4be72fe6-298e-4c53-a6bd-b6c14f10b1d8` | human | 0.127 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `12d529e0-9669-40d3-9715-bea7384d4e3c` | human | 0.127 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e4ba12bf-9aa4-4953-ad2e-505acb7cf9dd` | human | 0.127 | BROKE |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

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
  "content_id": "05bd1428-85d6-4db1-8e65-e87a11a8cf02",
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
  "content_id": "c7f2b7ec-8684-4591-a1e9-b24dbdba099c",
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
  "content_id": "57655dfc-e3da-489d-be93-509a29e63a06",
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
  "content_id": "ec182719-504b-49e2-aa67-183ddcff68ad",
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
  "content_id": "44f4c025-6df1-46d8-954c-da0798ab29a3",
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
  "content_id": "be96766b-5915-4b46-a732-466653dc2d03",
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
  "content_id": "0cde62fa-a417-424a-aabe-b37bc95f2d1f",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6522,
  "model_score": 0.5862,
  "style_score": 0.7183,
  "label": "We can't tell if a human or AI wrote this.",
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
  "content_id": "50d5b253-33e6-44cc-bc49-0c44e967781b",
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
  "content_id": "ed99ec85-3a27-44ff-b100-764958f79a04",
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
  "content_id": "2f7567c1-08e6-4880-8cd8-51aa665d093a",
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
  "content_id": "acfb6872-0436-457a-a792-b5f098615599",
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
  "content_id": "1ba6fedf-7c84-49ed-b4b8-4b5f32f5f329",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6694,
  "model_score": 0.7387,
  "style_score": 0.6,
  "label": "We can't tell if a human or AI wrote this.",
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
  "content_id": "d6902e08-9ddf-4a4b-84f5-e4fa4bcd2102",
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
  "content_id": "8af3d09a-ed51-42c5-9a78-7ca83fbbe7b2",
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
  "content_id": "8c2b71ee-3451-4e91-adc0-c9e82dda723d",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6829,
  "model_score": 0.8005,
  "style_score": 0.5654,
  "label": "We can't tell if a human or AI wrote this.",
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
  "content_id": "cf9140c6-cbfa-4041-b714-2647dd204f5d",
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
  "content_id": "0e3645ef-87c3-41e4-b696-ae6b41707fe7",
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
  "content_id": "b079654b-8ad6-43a8-84ca-ce36205e8e12",
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
  "content_id": "b0d5ab42-aa84-4e73-a957-300f55565025",
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
  "content_id": "2327c52c-1454-4562-8d06-6055baa37122",
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
  "content_id": "6a2befac-890d-494a-b36b-6c51d9872b64",
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
  "content_id": "5374ad5f-5774-4c40-a320-2c17af31b543",
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
  "content_id": "080a7bdd-7e80-442a-b7ce-eafd7eef2fc7",
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
  "content_id": "f41638bd-5338-40fd-b183-2bfcb7b0b8c5",
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
  "content_id": "37865fa5-624f-44db-92d9-a3ceb5bcced2",
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
  "content_id": "5e1c97d1-b0be-4fc8-a98e-59631561285d",
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
  "content_id": "e18e3d60-f3b7-469f-a196-2491fa6d82f1",
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
  "content_id": "7ff6fba2-1dde-49c5-9209-c084528052ea",
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
  "content_id": "f0cbc061-3c4c-421a-9574-b26bac1a8eba",
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
  "content_id": "8e1185cc-bda3-47cd-a736-9855f5151d50",
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
  "content_id": "ab426fef-fe01-486f-aaa9-0bc9329b7fd0",
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
  "content_id": "e3efdeb1-6bce-48a4-8f13-27b09de3fe0b",
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
  "content_id": "603b9a0b-6c3d-4779-8d15-5f95284555bc",
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
  "content_id": "f50845bc-4a83-4024-8872-8f5a9258677e",
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
  "content_id": "29ef195a-2874-47fe-a4d2-88a82039a8e0",
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
  "content_id": "d7428a97-a4e6-4a11-9582-102d155b274b",
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
  "content_id": "4be72fe6-298e-4c53-a6bd-b6c14f10b1d8",
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
  "content_id": "12d529e0-9669-40d3-9715-bea7384d4e3c",
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
  "content_id": "e4ba12bf-9aa4-4953-ad2e-505acb7cf9dd",
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
