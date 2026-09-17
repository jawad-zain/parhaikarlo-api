"""Provision a throwaway signed-in fixture for frontend QA.

Drives the real API against a locally running backend rather than writing
rows directly, so the attempt it leaves behind is shaped exactly like a
student's: snapshot questions, recorded answers, a finalized score.

    py -3.14 scripts/seed_qa_user.py [--api http://localhost:8000] [--answers 25]

Idempotent: re-running reuses the same account (signup 400s on the second
run, which is expected) and always starts a fresh mock attempt, so there is
a completed attempt to point /attempts/<id>/result at. Prints the login and
the attempt id as JSON on the last line for a harness to read.

Local dev only — it creates a real user with a known password.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request

EMAIL = "qa-typography@example.com"
USERNAME = "qa_typography"
PASSWORD = "qa-typography-2609"
FULL_NAME = "QA Typography"


def call(api, path, method="GET", body=None, token=None):
    req = urllib.request.Request(
        f"{api}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
    )
    req.add_header("Content-Type", "application/json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, raw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--api", default="http://localhost:8000")
    ap.add_argument("--answers", type=int, default=25,
                    help="how many questions to answer before submitting")
    args = ap.parse_args()
    api = args.api.rstrip("/")

    status, _ = call(api, "/api/auth/signup/", "POST",
                     {"email": EMAIL, "username": USERNAME, "password": PASSWORD})
    print(f"signup: {status}" + (" (already existed)" if status == 400 else ""))

    status, data = call(api, "/api/auth/login/", "POST",
                        {"email": EMAIL, "password": PASSWORD})
    if status != 200:
        sys.exit(f"login failed: {status} {data}")
    token = data["access"]

    status, me = call(api, "/api/auth/me/", token=token)
    if not me.get("profile"):
        status, exams = call(api, "/api/content/exams/", token=token)
        exam_list = exams["results"] if isinstance(exams, dict) else exams
        exam_id = exam_list[0]["id"]
        status, me = call(api, "/api/auth/me/", "PATCH",
                          {"full_name": FULL_NAME, "primary_exam_id": exam_id},
                          token=token)
        if status != 200:
            sys.exit(f"profile completion failed: {status} {me}")
        print(f"profile created on exam {exam_id}")
    else:
        print("profile already present")

    status, mocks = call(api, "/api/quiz/mocks/", token=token)
    mock_list = mocks["results"] if isinstance(mocks, dict) else mocks
    if not mock_list:
        sys.exit("no mocks available — is the content seeded?")
    mock = mock_list[0]

    status, started = call(api, f"/api/quiz/mocks/{mock['id']}/start/", "POST",
                           {"allow_breaks": True, "device_class": "desktop"},
                           token=token)
    if status not in (200, 201):
        sys.exit(f"mock start failed: {status} {started}")
    attempt_id = started.get("attempt_id") or started.get("id")

    status, state = call(api, f"/api/quiz/attempts/{attempt_id}/state/", token=token)
    items = state.get("items") or state.get("questions") or []
    answered = 0
    for i, item in enumerate(items[: args.answers]):
        aq_id = item.get("id") or item.get("attempt_question_id")
        opt = "abcd"[i % 4]          # spread the picks so the score isn't 0 or 100
        st, _ = call(api, f"/api/quiz/attempts/{attempt_id}/answer/", "POST",
                     {"attempt_question_id": aq_id, "selected_option": opt,
                      "time_spent_seconds": 12}, token=token)
        answered += st == 200

    status, result = call(api, f"/api/quiz/attempts/{attempt_id}/submit/", "POST",
                          {}, token=token)
    if status != 200:
        sys.exit(f"submit failed: {status} {result}")

    print(f"mock '{mock.get('name', mock['id'])}': answered {answered}/{len(items)}, "
          f"scored {result.get('correct_count')}/{result.get('total_questions')}")
    print(json.dumps({"email": EMAIL, "password": PASSWORD,
                      "attempt_id": attempt_id, "mock_id": mock["id"]}))


if __name__ == "__main__":
    main()
