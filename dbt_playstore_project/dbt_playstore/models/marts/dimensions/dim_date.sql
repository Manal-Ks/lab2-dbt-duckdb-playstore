{{ config(materialized='table') }}

with bounds as (
  select
    cast(min(review_at_utc) as date) as min_date,
    cast(max(review_at_utc) as date) as max_date
  from {{ ref('stg_playstore_reviews') }}
),
dates as (
  select
    d as date_day
  from bounds,
  generate_series(min_date, max_date, interval 1 day) as t(d)
)

select
  cast(strftime(date_day, '%Y%m%d') as integer) as date_key,
  date_day,
  cast(strftime(date_day, '%Y') as integer) as year,
  cast(strftime(date_day, '%m') as integer) as month,
  cast(strftime(date_day, '%d') as integer) as day,
  cast(strftime(date_day, '%w') as integer) as day_of_week, -- 0=Sunday
  strftime(date_day, '%A') as day_name,
  strftime(date_day, '%B') as month_name
from dates