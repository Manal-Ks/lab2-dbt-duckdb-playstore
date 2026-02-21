{{ config(materialized='view') }}

select
  app_id,
  source,
  cast(ingested_at as timestamp) as ingested_at_utc
from {{ ref('stg_raw_apps') }}