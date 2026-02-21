{{ config(materialized='view') }}

select
  app_id,
  review_id,
  user_name,
  content,
  score,
  thumbs_up_count,
  review_created_version,
  "at" as review_at,
  reply_content,
  replied_at,
  ingested_at,
  source,
  lang,
  country
from read_json_auto('../../data/raw/reviews.jsonl')