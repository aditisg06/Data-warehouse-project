# SQL Data Warehouse Project with Python ETL Automation

## Project Overview

This project demonstrates the design and implementation of a modern SQL Server Data Warehouse using the Medallion Architecture approach (Bronze, Silver, Gold layers) combined with Python-based ETL orchestration, validation, logging, and reporting.

The pipeline ingests raw CRM and ERP CSV datasets into SQL Server, transforms and cleans the data across multiple warehouse layers, validates data quality, and exposes analytics-ready business views in the Gold layer.

In addition to SQL-based transformations, the project includes Python automation for:
- Stored procedure orchestration
- Data quality validation
- Source data profiling
- Logging and monitoring
- Pipeline summary reporting

---

# Architecture

```text
Source CSV Files
        ↓
Python Data Profiling
        ↓
Bronze Layer (Raw Ingestion)
        ↓
Silver Layer (Cleaned & Transformed Data)
        ↓
Gold Layer (Star Schema Views)
        ↓
Validation + Reporting + Logging
```

---

# Tech Stack

| Technology | Purpose |
|---|---|
| SQL Server | Data Warehouse |
| SSMS | SQL Development |
| Python | ETL Orchestration |
| pyodbc | SQL Server Connectivity |
| pandas | Data Profiling & Reporting |
| Git & GitHub | Version Control |
| VS Code | Development Environment |

---

# Medallion Architecture

## Bronze Layer
- Raw ingestion layer
- Loads CRM and ERP CSV datasets into SQL Server tables
- Minimal transformation
- Preserves source data

### Bronze Tasks
- CSV ingestion
- Initial loading
- Error handling
- Logging

---

## Silver Layer
- Cleans and standardizes Bronze data
- Handles:
  - Null values
  - Duplicate records
  - Data standardization
  - Type conversions

### Silver Tasks
- Data cleansing
- Deduplication
- Business rule application
- Standardization

---

## Gold Layer
The Gold layer exposes analytics-ready business datasets using a Star Schema model.

### Gold Components
- Fact Views
- Dimension Views

### Gold Views
- `gold.fact_sales`
- `gold.dim_customers`
- `gold.dim_products`

These views are optimized for reporting and analytical queries.

---

# Python ETL Automation

Python is used to orchestrate and monitor the warehouse pipeline.

## Features Implemented

### 1. Stored Procedure Orchestration
Python executes Bronze and Silver SQL stored procedures automatically.

### 2. Centralized Database Connectivity
A reusable `db.py` module centralizes SQL Server connections.

### 3. Logging Framework
Custom logging framework captures:
- Pipeline execution
- Errors
- Validation results
- Profiling information
- Execution duration

Logs are written to:
```text
logs/pipeline.log
```

### 4. Data Quality Validation
Validation framework performs:
- Row count checks
- Null checks
- Duplicate checks

### 5. Source Data Profiling
Python + pandas profile source CSV datasets before ingestion.

Profiling includes:
- Row counts
- Column counts
- Null percentage
- Unique value counts

### 6. Pipeline Reporting
Pipeline summary reports are generated automatically as CSV files.

Generated report:
```text
logs/pipeline_summary.csv
```

---

# Project Structure

```text
Data-warehouse-project/
│
├── datasets/
│
├── python/
│   ├── config.py
│   ├── db.py
│   ├── logger.py
│   ├── procedures.py
│   ├── load_bronze.py
│   ├── load_silver.py
│   ├── validate.py
│   ├── profile_data.py
│   ├── report.py
│   └── run_pipeline.py
│
├── scripts/
│
├── logs/
│
├── tests/
│
├── .env
├── .gitignore
└── README.md
```

---

# Pipeline Execution Flow

```text
run_pipeline.py
        ↓
Profile Source Data
        ↓
Load Bronze Layer
        ↓
Load Silver Layer
        ↓
Gold Views Refresh Automatically
        ↓
Run Data Validations
        ↓
Generate Pipeline Summary Report
        ↓
Write Logs
```

---

# Validation Framework

The project includes automated data quality checks for all warehouse layers.

## Validation Checks

### Row Count Validation
Ensures tables/views contain expected data.

### Null Validation
Checks critical columns for missing values.

### Duplicate Validation
Ensures key columns contain unique values.

---

# Logging & Monitoring

The logging framework captures:
- Pipeline start/end
- Execution duration
- Validation status
- Errors and exceptions
- Profiling statistics

Example Output:

```text
==================================================
PIPELINE STARTED
==================================================

Starting Bronze Layer Load
Executing bronze.load_bronze

Starting Silver Layer Load
Executing silver.load_silver

ALL VALIDATIONS PASSED

PIPELINE COMPLETED in 7.65 seconds
```

---

# Sample Gold Layer Queries

## Fact Table

```sql
SELECT TOP 10 * FROM gold.fact_sales;
```

## Customer Dimension

```sql
SELECT TOP 10 * FROM gold.dim_customers;
```

## Product Dimension

```sql
SELECT TOP 10 * FROM gold.dim_products;
```

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/aditisg06/Data-warehouse-project.git
```

---

## 2. Install Python Dependencies

```bash
pip install pyodbc pandas python-dotenv
```

---

## 3. Configure Environment Variables

Create a `.env` file:

```env
DB_SERVER=YOUR_SERVER_NAME
DB_DATABASE=DataWarehouse
DB_DRIVER=ODBC Driver 17 for SQL Server
```

---

## 4. Execute Pipeline

```bash
cd python
python run_pipeline.py
```

---

# Key Concepts Demonstrated

- Data Warehouse Design
- Medallion Architecture
- ETL Pipeline Development
- SQL Server Stored Procedures
- Python ETL Orchestration
- Data Validation
- Logging & Monitoring
- Data Profiling
- Modular Python Architecture
- Git Version Control

---

# Future Enhancements

Possible future improvements:
- Incremental loading
- Airflow orchestration
- Dockerization
- Cloud deployment
- Automated scheduling
- CI/CD integration
- Data lineage tracking

---

# Conclusion

This project demonstrates an end-to-end SQL Server Data Warehouse solution integrated with Python-based ETL automation and validation.

The pipeline transforms raw operational datasets into clean, analytics-ready business data while incorporating logging, monitoring, profiling, and reporting capabilities commonly used in modern data engineering workflows.
