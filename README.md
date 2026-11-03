# Healthcare Data Analysis

A full analysis of Kaggle's synthetic Healthcare Dataset, from data cleaning to exploration. The project focuses on resolving data quality issues, then analyzing billing, doctor workload, and medication patterns.

*This project is a work in progress.*

## Project Structure

| File | Purpose |
|------|---------|
| `01_explore.ipynb` | First look at the raw data and documentation of data quality issues |
| `02_clean.ipynb` | Cleaning steps, producing `data/healthcare_clean.csv` |
| `03_overview.ipynb` | General summary statistics and trends |
| `04_billing_analysis.ipynb` | Billing analysis, including negative billing scenarios |
| `05_doctor_analysis.ipynb` | Doctor workload analysis |
| `06_medication_analysis.ipynb` | Medication and prescribing patterns |
| `analysis_helper.py` | Shared function that loads the clean data and adds analysis columns |

## Key Cleaning Findings

- Found 5,500 duplicate records (10% of the data) that matched on every column except Age, including 534 exact duplicates. Kept the first occurrence and flagged records with conflicting ages, leaving 50,000 unique records.
- Standardized patient names with inconsistent capitalization and stray titles.
- Set negative billing amounts to missing and saved them separately for scenario analysis.

## Setup


## Data Disclaimer

This project uses the [Healthcare Dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset) by Prasad Patil on Kaggle. The dataset is entirely synthetic. It was generated with Python's Faker library to mimic the structure of hospital admission records, and it contains no real patient information.

Because the values were generated randomly, the relationships between variables do not reflect real clinical or financial patterns. Any trends shown in this project should not be interpreted as medical, clinical, or healthcare business insights. The purpose of this project is to demonstrate data analysis skills.