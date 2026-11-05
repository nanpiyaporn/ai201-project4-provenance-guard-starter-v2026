# Appeal path (criterion 4) — before

- Produced by: `check_appeals.py::one_trial`
- Service: `app.py::submit`, `app.py::appeal`, `app.py::get_log`
- 3 trials · 2026-11-04 21:19
- Each trial: 3 real appeals + 1 fake id

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 4. The appeal path | 4 of 4 | 4/4 | 4/4 | 4/4 |  |

---

## What actually came back

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

**Trial 2**

```json
[
  {
    "kind": "real",
    "content_id": "c1b3bead-5a74-465f-9795-ece879e472a9",
    "appeal_status": 200,
    "response": {
      "content_id": "c1b3bead-5a74-465f-9795-ece879e472a9",
      "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
      "status": "under_review"
    },
    "log_entry": {
      "content_id": "c1b3bead-5a74-465f-9795-ece879e472a9",
      "creator_id": "eval_appeal_t2_1",
      "event": "appeal",
      "reasoning": "I wrote this myself and can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:19:32+00:00"
    },
    "passed": true
  },
  {
    "kind": "real",
    "content_id": "4ee36c65-8dbc-4e08-9cf3-573784c55bf7",
    "appeal_status": 200,
    "response": {
      "content_id": "4ee36c65-8dbc-4e08-9cf3-573784c55bf7",
      "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
      "status": "under_review"
    },
    "log_entry": {
      "content_id": "4ee36c65-8dbc-4e08-9cf3-573784c55bf7",
      "creator_id": "eval_appeal_t2_2",
      "event": "appeal",
      "reasoning": "I wrote this myself and can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:19:33+00:00"
    },
    "passed": true
  },
  {
    "kind": "real",
    "content_id": "68d4bc17-75ae-4a7b-ac95-b20c5043bd6c",
    "appeal_status": 200,
    "response": {
      "content_id": "68d4bc17-75ae-4a7b-ac95-b20c5043bd6c",
      "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
      "status": "under_review"
    },
    "log_entry": {
      "content_id": "68d4bc17-75ae-4a7b-ac95-b20c5043bd6c",
      "creator_id": "eval_appeal_t2_3",
      "event": "appeal",
      "reasoning": "I wrote this myself and can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:19:33+00:00"
    },
    "passed": true
  },
  {
    "kind": "fake",
    "content_id": "fake-bc11af5b-a5ae-4a7d-9663-cd59c3061de0",
    "appeal_status": 404,
    "response": {
      "error": "not_found",
      "message": "No submission with content_id 'fake-bc11af5b-a5ae-4a7d-9663-cd59c3061de0'. Check it was copied exactly."
    },
    "passed": true
  }
]
```

**Trial 3**

```json
[
  {
    "kind": "real",
    "content_id": "7e1888b1-5ebd-4f2e-b9b7-396f71ea658c",
    "appeal_status": 200,
    "response": {
      "content_id": "7e1888b1-5ebd-4f2e-b9b7-396f71ea658c",
      "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
      "status": "under_review"
    },
    "log_entry": {
      "content_id": "7e1888b1-5ebd-4f2e-b9b7-396f71ea658c",
      "creator_id": "eval_appeal_t3_1",
      "event": "appeal",
      "reasoning": "I wrote this myself and can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:19:33+00:00"
    },
    "passed": true
  },
  {
    "kind": "real",
    "content_id": "5692e08e-c083-4739-ada7-6c2188f86b76",
    "appeal_status": 200,
    "response": {
      "content_id": "5692e08e-c083-4739-ada7-6c2188f86b76",
      "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
      "status": "under_review"
    },
    "log_entry": {
      "content_id": "5692e08e-c083-4739-ada7-6c2188f86b76",
      "creator_id": "eval_appeal_t3_2",
      "event": "appeal",
      "reasoning": "I wrote this myself and can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:19:33+00:00"
    },
    "passed": true
  },
  {
    "kind": "real",
    "content_id": "a939487f-010e-40c3-891a-204b32215785",
    "appeal_status": 200,
    "response": {
      "content_id": "a939487f-010e-40c3-891a-204b32215785",
      "message": "Thanks \u2014 your appeal has been recorded and a person will review this decision. The original result is on hold until then.",
      "status": "under_review"
    },
    "log_entry": {
      "content_id": "a939487f-010e-40c3-891a-204b32215785",
      "creator_id": "eval_appeal_t3_3",
      "event": "appeal",
      "reasoning": "I wrote this myself and can share my drafts.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:19:33+00:00"
    },
    "passed": true
  },
  {
    "kind": "fake",
    "content_id": "fake-828d32a9-0814-4a4e-a6cd-17b97227d095",
    "appeal_status": 404,
    "response": {
      "error": "not_found",
      "message": "No submission with content_id 'fake-828d32a9-0814-4a4e-a6cd-17b97227d095'. Check it was copied exactly."
    },
    "passed": true
  }
]
```
