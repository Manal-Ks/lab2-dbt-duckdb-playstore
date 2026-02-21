# 📊 Play Store Data Pipeline – DuckDB + dbt

## 🎯 Project Overview

This project implements a complete data engineering pipeline using:

- Python for data ingestion
- DuckDB as analytical database
- dbt for data transformation
- A star schema data warehouse model
- Incremental loading strategy for production-like behavior

The goal is to extract Google Play Store data, transform it into a structured warehouse, and make it ready for analytics and BI tools.

---

## 🏗 Architecture
Play Store API
↓
Python Ingestion (JSONL files)
↓
DuckDB
↓
dbt Staging Layer
↓
dbt Marts (Star Schema)
↓
Analytics / BI

---

## 📁 Project Structure
lab2-dbt-duckdb-playstore/
│
├── ingestion/
│ └── src/
│ ├── fetch_apps.py
│ ├── fetch_reviews.py
│ └── run_ingestion.py
│
├── dbt_playstore_project/
│ └── dbt_playstore/
│ ├── models/
│ │ ├── staging/
│ │ └── marts/
│ ├── dbt_project.yml
│ └── README.md
│
├── data/ (ignored by git)
│
└── .gitignore


---

## 🚀 How to Run the Pipeline

### 1️⃣ Run ingestion (from project root)

```bash
python ingestion/src/run_ingestion.py
This generates:

- data/raw/apps.jsonl

- data/raw/reviews.jsonl
2️⃣ Run dbt (from dbt directory)
cd dbt_playstore_project/dbt_playstore
dbt run
dbt test
🧱 Data Warehouse Design
Star Schema
📌 Dimensions

dim_apps

dim_date

📌 Fact Table

fact_reviews

Fact table contains:

review_id

app_key

date_key

score

thumbs_up_count

review metadata

🔄 Incremental Strategy

The fact_reviews model is configured as:

materialized = 'incremental'
unique_key = 'review_id'

Only new reviews are inserted based on:

where review_at_utc > (select max(review_at_utc) from {{ this }})

This simulates a production-ready incremental pipeline.

✅ Data Quality

- dbt tests implemented:

- not_null

- unique

- relationships (foreign keys)

- All tests pass successfully.

🛠 Technologies Used

- Python 3.11

- DuckDB

- dbt (Core + DuckDB adapter)

- Git

📌 Key Learnings

- Building a full ELT pipeline

- Structuring a dbt project professionally

- Designing a star schema

- Implementing incremental models

- Managing data versioning with Git
