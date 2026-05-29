# Olist E-Commerce Data Pipeline

## Overview
This project is an end-to-end data engineering pipeline built using the Brazilian Olist E-Commerce dataset. The pipeline ingests raw CSV files into AWS S3, loads the data into Snowflake, and transforms it using dbt to create analytics-ready fact and dimension tables.

The project demonstrates modern data engineering concepts including:
- Cloud-based data storage
- ELT workflows
- Data warehouse modeling
- Data transformation using dbt
- Data quality testing
- Analytics-ready reporting layers

---

# Architecture

```text
Olist CSV Dataset
        ↓
Python Ingestion Script
        ↓
AWS S3 Raw Layer
(raw-data/date-partition/)
        ↓
Snowflake External/Internal Stage
        ↓
Raw Tables
        ↓
dbt Staging Models
        ↓
Fact & Dimension Models
        ↓
Analytics & Reporting
```

---

# Tech Stack

| Tool | Purpose |
|---|---|
| Python | Data ingestion automation |
| AWS S3 | Raw data storage |
| Snowflake | Cloud data warehouse |
| dbt | Data transformation and modeling |
| SQL | Data querying and transformations |
| GitHub | Version control |

---

# Dataset

Dataset used: Olist Brazilian E-Commerce Dataset

The dataset contains information related to:
- Customers
- Orders
- Payments
- Products
- Sellers
- Reviews
- Geolocation

---

# Project Structure

```text
Olist-data-pipeline/
│
├── data/
│
├── ingestion/
│   └── upload_to_s3.py
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   │
│   ├── macros/
│   ├── tests/
│   └── dbt_project.yml
│
├── screenshots/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

# Data Ingestion

The ingestion pipeline:
1. Reads raw CSV files locally
2. Uploads files to AWS S3
3. Stores files inside date-partitioned folders

Example S3 structure:

```text
s3://olist-data-lake/raw-data/2026-05-29/
```

This structure helps simulate production-style ingestion and historical tracking.

---

# Snowflake Data Warehouse

Raw data from S3 is loaded into Snowflake tables.

The warehouse layer includes:
- Raw ingestion tables
- Staging models
- Analytics marts

---

# dbt Transformations

dbt is used for:
- Cleaning raw data
- Standardizing column names
- Creating staging models
- Building fact and dimension tables
- Running data quality tests

---

# Data Models

## Staging Models
- stg_customers
- stg_orders
- stg_order_items
- stg_products
- stg_payments

## Mart Models
- fact_orders
- dim_customers
- dim_products
- dim_sellers

---

# Data Quality Tests

Implemented dbt tests include:
- unique
- not_null
- relationships
- accepted_values

Example:
- order_id must be unique
- customer_id cannot be null
- fact_orders.customer_id must exist in dim_customers

---

# Key Features

- End-to-end ELT pipeline
- Cloud storage using AWS S3
- Snowflake warehouse integration
- dbt transformation workflow
- Fact and dimension modeling
- Data quality validation
- Date-partitioned ingestion design

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/mvshraddha/Olist-data-pipeline.git
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure AWS Credentials

Set AWS credentials locally using AWS CLI or environment variables.

---

## 4. Run Ingestion Script

```bash
python upload_to_s3.py
```

---

## 5. Load Data into Snowflake

Create:
- stages
- file formats
- raw tables

Then load files using:

```sql
COPY INTO raw_orders
FROM @olist_stage;
```

---

## 6. Run dbt Models

```bash
dbt run
```

---

## 7. Run dbt Tests

```bash
dbt test
```

---

# Future Improvements

- Airflow orchestration
- Incremental dbt models
- CI/CD using GitHub Actions
- Monitoring and alerting
- Data lineage documentation
- Dashboard integration

---

# Learning Outcomes

Through this project, I gained hands-on experience with:
- Data engineering workflows
- ELT architecture
- Cloud data warehousing
- Data modeling
- dbt transformation practices
- S3-based raw data ingestion
- SQL optimization concepts

---

# Screenshots

Add screenshots for:
- S3 bucket structure
- Snowflake tables
- dbt lineage graph
- dbt test results

---

# Author

Shraddha Veeraghantimath

GitHub: https://github.com/mvshraddha
