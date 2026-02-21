{{ config(
    materialized='incremental',
    unique_key='review_id'
) }}

select
  r.review_id,
  a.app_key,
  d.date_key,

  r.score,
  r.thumbs_up_count,

  r.user_name,
  r.content,
  r.review_created_version,
  r.review_at_utc,

  r.lang,
  r.country,

  r.ingested_at_utc as loaded_at_utc
from {{ ref('stg_playstore_reviews') }} r
join {{ ref('dim_apps') }} a
  on r.app_id = a.app_id
join {{ ref('dim_date') }} d
  on cast(r.review_at_utc as date) = d.date_day

{% if is_incremental() %}
  where r.review_at_utc > (
      select max(review_at_utc) from {{ this }}
  )
{% endif %}