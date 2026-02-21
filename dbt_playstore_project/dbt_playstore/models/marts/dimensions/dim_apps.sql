{{ config(materialized='table') }}

select
  app_id as app_key,
  app_id as app_id,       -- natural key kept for traceability
  source,
  min(ingested_at_utc) as first_seen_at_utc,
  max(ingested_at_utc) as last_seen_at_utc
from {{ ref('stg_playstore_apps') }}
group by 1,2,3