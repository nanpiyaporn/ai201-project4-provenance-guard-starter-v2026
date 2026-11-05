#!/usr/bin/env python3
"""
Criterion 4 — the appeal path, three trials.  <- UNIT 8, MILESTONE 3

    python app.py                               # in one terminal
    python check_appeals.py --label before      # in another

run_eval.py only sends /submit, and an appeal needs a real content_id first,
so this does it in two steps per trial:

  1. Submit 3 texts and keep the content_id each one came back with.
  2. Appeal each one, then check GET /log has an `under_review` appeal entry
     for that content_id. Then appeal a made-up id and expect a 404.

Target (criteria.md #4): every real appeal returns 200 + status under_review
and lands in /log; the fake id returns 404. The script records what came back
and counts passes, but the Verdict is yours to write.
"""

import argparse
import datetime as dt
import json
import sys
import uuid

import config
from calibrate import INPUTS

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"
TEXTS = [INPUTS["clearly human"], INPUTS["formal human"], INPUTS["clearly AI"]]
REASONING = "I wrote this myself and can share my drafts."


def one_trial(requests, url, trial, timeout):
    results = []
    for i, text in enumerate(TEXTS, 1):
        creator = f"eval_appeal_t{trial}_{i}"
        sub = requests.post(f"{url}/submit", json={"text": text, "creator_id": creator},
                            timeout=timeout)
        content_id = sub.json().get("content_id") if sub.ok else None
        if not content_id:
            results.append({"kind": "real", "submit_status": sub.status_code,
                            "error": "submit gave no content_id", "passed": False})
            continue

        app_resp = requests.post(f"{url}/appeal",
                                 json={"content_id": content_id, "reasoning": REASONING},
                                 timeout=timeout)
        body = app_resp.json() if app_resp.content else {}
        log = requests.get(f"{url}/log", timeout=timeout).json().get("entries", [])
        logged = [e for e in log
                  if e.get("content_id") == content_id and e.get("event") == "appeal"]
        passed = (app_resp.status_code == 200 and body.get("status") == "under_review"
                  and len(logged) >= 1)
        results.append({
            "kind": "real",
            "content_id": content_id,
            "appeal_status": app_resp.status_code,
            "response": body,
            "log_entry": logged[-1] if logged else None,
            "passed": passed,
        })

    fake_id = f"fake-{uuid.uuid4()}"
    fake = requests.post(f"{url}/appeal",
                         json={"content_id": fake_id, "reasoning": REASONING},
                         timeout=timeout)
    results.append({
        "kind": "fake",
        "content_id": fake_id,
        "appeal_status": fake.status_code,
        "response": fake.json() if fake.content else {},
        "passed": fake.status_code == 404,
    })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0)
    args = parser.parse_args()

    import requests

    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}. Start it:  python app.py", file=sys.stderr)
        sys.exit(1)

    trials = []
    for t in range(1, args.trials + 1):
        results = one_trial(requests, args.url, t, args.timeout)
        passed = sum(r["passed"] for r in results)
        print(f"  trial {t}: {passed}/{len(results)} passed")
        trials.append(results)

    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"
    config.RESULTS_DIR.mkdir(exist_ok=True)

    counts = [f"{sum(r['passed'] for r in t)}/{len(t)}" for t in trials]
    lines = [
        f"# Appeal path (criterion 4){f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `check_appeals.py::one_trial`",
        "- Service: `app.py::submit`, `app.py::appeal`, `app.py::get_log`",
        f"- {args.trials} trials · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "- Each trial: 3 real appeals + 1 fake id",
        "",
        "| Criterion | Target | " + " | ".join(f"Run {i}" for i in range(1, args.trials + 1))
        + " | Verdict |",
        "|---|---|" + "|".join(["---"] * args.trials) + "|---|",
        f"| 4. The appeal path | 4 of 4 | {' | '.join(counts)} |  |",
        "",
        "---",
        "",
        "## What actually came back",
        "",
    ]
    for t, results in enumerate(trials, 1):
        lines += [f"**Trial {t}**", "", "```json", json.dumps(results, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
