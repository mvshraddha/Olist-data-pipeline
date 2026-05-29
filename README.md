\# Olist E-Commerce Data Pipeline



\## Overview

End-to-end data pipeline built on real Brazilian e-commerce data 

from Olist. Raw CSV files are ingested into AWS S3, transformed 

using AWS Glue, loaded into Snowflake, and modelled using dbt.



\## Architecture

CSV files → S3 (raw) → Glue ETL → S3 (parquet) → Snowflake (raw tables) → dbt (staging + facts)



\## Tech Stack

\- Python + boto3 — S3 ingestion

\- AWS S3 — data lake storage

\- AWS Glue — ETL and schema detection

\- Snowflake — cloud data warehouse

\- dbt — data transformation and testing



\## Pipeline Steps

1\. Download Olist dataset from Kaggle

2\. Run `ingestion/script.py` to upload CSVs to S3

3\. Run Glue crawler to detect schema

4\. Run Glue ETL job to convert CSV to Parquet

5\. Load Parquet files into Snowflake using COPY INTO

6\. Run `dbt run` to build staging and fact models

7\. Run `dbt test` to validate data quality



\## dbt Models

\- `stg\_orders` — cleaned orders with proper timestamp casting

\- `stg\_customers` — cleaned customer data

\- `fact\_orders` — delivered orders joined with customer details



\## dbt Tests

\- unique and not\_null on order\_id

\- accepted\_values on order\_status

\- not\_null on customer\_id

\- relationships between fact\_orders and stg\_customers



\## What I Learned

\- How to partition S3 data by date for efficient querying

\- How Glue DynamicFrames handle schema evolution

\- How Snowflake storage integrations work with AWS IAM

\- The difference between source() and ref() in dbt

\- How dbt tests catch bad data before it reaches analysts

