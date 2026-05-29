# Olist E-Commerce Data Pipeline

## Overview

This project is an end-to-end data engineering pipeline built using the Brazilian Olist E-Commerce dataset. The pipeline ingests raw data into AWS S3, processes the data using AWS Glue, loads it into Snowflake, and transforms it using dbt to create analytics-ready models.

This project demonstrates modern data engineering workflows including:

* Data ingestion
* Cloud storage
* ETL/ELT processing
* Data warehousing
* Data transformation
* Data quality testing

---

# Architecture

```text
Olist Dataset
      ↓
Python Ingestion Script
      ↓
AWS S3 Raw Layer
      ↓
AWS Glue ETL Jobs
      ↓
Snowflake Data Warehouse
      ↓
dbt Transformations
      ↓
Analytics-ready Fact & Dimension Tables
```

---

# Tech Stack

| Tool      | Purpose                    |
| --------- | -------------------------- |
| Python    | Data ingestion             |
| AWS S3    | Raw data storage           |
| AWS Glue  | ETL processing             |
| Snowflake | Cloud data warehouse       |
| dbt       | Data transformation        |
| SQL       | Data modeling and querying |
| GitHub    | Version control            |

---

# Project Structure

```text
Olist-data-pipeline/
│
├── dbt/
│   └── my_project/
│
├── glue/
│   ├── glue_elt_job_orders.py
│   └── glue_elt_job_customers.py
│
├── ingestion/
│   └── script.py
│
├── .env
├── .gitignore
└── README.md
```

---

# Data Pipeline Flow

## 1. Data Ingestion

The ingestion script uploads raw Olist CSV datasets into AWS S3.

Features:

* Automated ingestion
* Date-partitioned raw storage
* Cloud-based raw layer

Example:

```text
s3://olist-raw-ap-south-1/raw-data/2026-05-29/
```

---

## 2. AWS Glue ETL Processing

AWS Glue jobs are used to:

* Read raw data from S3
* Perform cleaning and transformations
* Prepare structured datasets for Snowflake loading

Glue jobs included:

* glue_elt_job_orders.py
* glue_elt_job_customers.py

---

## 3. Snowflake Data Warehouse

Processed data is loaded into Snowflake for analytics and transformation.

The warehouse contains:

* Raw tables
* Staging tables
* Analytics marts

---

## 4. dbt Transformations

dbt is used to:

* Build staging models
* Create fact and dimension tables
* Standardize datasets
* Apply data quality tests

Example models:

* stg_orders
* stg_customers
* fact_orders
* dim_customers

---

# Data Quality Testing

Implemented dbt tests include:

* unique
* not_null
* accepted_values
* relationships

Examples:

* order_id must be unique
* customer_id cannot be null
* fact_orders.customer_id must exist in dim_customers

---

# Key Features

* End-to-end cloud data pipeline
* AWS S3 raw data lake
* AWS Glue ETL processing
* Snowflake cloud warehouse
* dbt transformations
* Fact and dimension modeling
* Data quality validation
* Modular project structure

---

# How to Run the Project

## Clone Repository

```bash
git clone https://github.com/mvshraddha/Olist-data-pipeline.git
```

---

```markdown
## Install Required Packages

Install the required Python libraries:

```bash
pip install boto3 python-dotenv

---

## Configure Environment Variables

Create a `.env` file and configure:

* AWS credentials
* Snowflake credentials
* Required connection variables

---

## Run Ingestion Script

```bash
python ingestion/script.py
```

---

## Run AWS Glue Jobs

Execute Glue ETL jobs:

* glue_elt_job_orders.py
* glue_elt_job_customers.py

---

## Run dbt Models

```bash
dbt run
```

---

## Run dbt Tests

```bash
dbt test
```

---

# Future Improvements

* Apache Airflow orchestration
* Incremental dbt models
* CI/CD using GitHub Actions
* Automated monitoring and alerts
* Dashboard integration
* Data lineage tracking

---

# Learning Outcomes

Through this project, I gained practical experience in:

* Building end-to-end data pipelines
* Cloud-based ETL workflows
* AWS data services
* Snowflake warehousing
* dbt transformations
* Data modeling
* Analytics engineering practices

---

# Author

Shraddha Veeraghantimath

GitHub: https://github.com/mvshraddha
