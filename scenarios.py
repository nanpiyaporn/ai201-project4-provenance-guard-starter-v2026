"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

from calibrate import INPUTS  # the five texts criteria 1–3 are written against

HUMAN_TEXTS = [INPUTS["clearly human"], INPUTS["formal human"], INPUTS["plain human"]]
ALL_FIVE = list(INPUTS.values())  # clearly AI, clearly human, formal, plain, lightly-edited AI

SCENARIOS = [
    {
        # Criterion 1: of the 3 human texts, at most 2 get the `ai` guess.
        "name": "false positive",
        "criterion": 1,
        "texts": HUMAN_TEXTS,
    },
    {
        # Criterion 2: avg combined score of the 2 AI texts vs the 3 human texts.
        "name": "score spread",
        "criterion": 2,
        "texts": ALL_FIVE,
    },
    {
        # Criterion 3: human, unsure and ai each appear at least once.
        "name": "label coverage",
        "criterion": 3,
        "texts": ALL_FIVE,
    },
    # Criterion 4 (appeal path) can't be sent as text alone — it needs a
    # submission, then an appeal on the content_id that came back. It runs
    # from check_appeals.py instead:  python check_appeals.py --label before
    {
        # Criterion 5: missing, empty, and over-20,000-character text.
        # Every one should be a 400 (never 500) with a rejected entry in /log.
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},                  # no text field
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "a" * 20_001, "creator_id": "eval_bad_huge"},  # 1 over the cap
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
