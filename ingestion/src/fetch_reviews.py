import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Any

from google_play_scraper import reviews, Sort  # pip install google-play-scraper

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

def fetch_reviews_for_app(app_id: str, lang: str = "en", country: str = "us", n: int = 200) -> list[dict[str, Any]]:
    """Fetch up to n reviews for a given app_id."""
    result, _ = reviews(
        app_id,
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=min(n, 200),  # the lib fetches in chunks; keep simple
    )

    # Keep it raw: just map the library's fields + app_id + ingested_at
    now = datetime.now(timezone.utc).isoformat()
    out = []
    for r in result:
        out.append({
            "app_id": app_id,
            "review_id": r.get("reviewId"),
            "user_name": r.get("userName"),
            "content": r.get("content"),
            "score": r.get("score"),
            "thumbs_up_count": r.get("thumbsUpCount"),
            "review_created_version": r.get("reviewCreatedVersion"),
            "at": r.get("at").isoformat() if r.get("at") else None,
            "reply_content": r.get("replyContent"),
            "replied_at": r.get("repliedAt").isoformat() if r.get("repliedAt") else None,
            "ingested_at": now,
            "source": "google_play_scraper",
            "lang": lang,
            "country": country,
        })
    return out

def write_reviews_jsonl(app_ids: list[str], out_path: Path, per_app: int = 200) -> None:
    total = 0
    with out_path.open("w", encoding="utf-8") as f:
        for app_id in app_ids:
            rows = fetch_reviews_for_app(app_id, n=per_app)
            for rec in rows:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            total += len(rows)
            print(f"{app_id}: {len(rows)} reviews")
    print(f"Wrote {out_path} with {total} reviews total.")

if __name__ == "__main__":
    # Read apps from apps.jsonl created by fetch_apps.py
    apps_path = RAW_DIR / "apps.jsonl"
    app_ids = []
    with apps_path.open("r", encoding="utf-8") as f:
        for line in f:
            app_ids.append(json.loads(line)["app_id"])

    out = RAW_DIR / "reviews.jsonl"
    write_reviews_jsonl(app_ids, out, per_app=200)
