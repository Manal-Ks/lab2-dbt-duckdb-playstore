{{ config(materialized='view') }}

select
  app_id,
  review_id,
  -- keep raw strings, but normalize empties to null
  nullif(user_name, '') as user_name,
  nullif(content, '') as content,

  cast(score as integer) as score,
  cast(thumbs_up_count as integer) as thumbs_up_count,
  nullif(review_created_version, '') as review_created_version,

  cast(review_at as timestamp) as review_at_utc,
  nullif(reply_content, '') as reply_content,
  cast(replied_at as timestamp) as replied_at_utc,

  cast(ingested_at as timestamp) as ingested_at_utc,
  source,
  lang,
  country
from {{ ref('stg_raw_reviews') }}