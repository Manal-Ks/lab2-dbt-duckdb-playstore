import json
from pathlib import Path
from datetime import datetime, timezone

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

def write_apps_jsonl(app_ids: list[str], out_path: Path) -> None:
    """Writes a minimal raw apps.jsonl. Keep it 'raw' (no business transforms)."""
    now = datetime.now(timezone.utc).isoformat()
    with out_path.open("w", encoding="utf-8") as f:
        for app_id in app_ids:
            rec = {
                "app_id": app_id,
                "ingested_at": now,
                "source": "seed_list",
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    # Start with a small deterministic list (you can expand later)
    seed_app_ids = [
        "com.spotify.music",
        "com.instagram.android",
        "com.whatsapp",
        "com.snapchat.android",
        "com.twitter.android",
        "com.netflix.mediaclient",
    ]
    out = RAW_DIR / "apps.jsonl"
    write_apps_jsonl(seed_app_ids, out)
    print(f"Wrote {out} with {len(seed_app_ids)} apps.")
