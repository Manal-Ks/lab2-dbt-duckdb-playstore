{{ config(materialized='view') }}

select
  app_id,
  ingested_at,
  source
from read_json_auto('../../data/raw/apps.jsonl')