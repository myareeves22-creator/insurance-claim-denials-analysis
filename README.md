# Medical Insurance Denials & Rvenue cycle Recovery Analysis

## Project overview
This project simulates a real-world **Healthcare Rvenue Cycle Managment (RCM)** data analysis pipeline. As a reporting analyst, the objective is to ingest raw claims data, build a strucutred relational database, annd excecute SQL queries to uncover root causes for insurance claim denials, lost revenue, and carrier performance.

## Tech Stack & Tools
* **Language:** Python (Pandas, SQLite3, OS)
* **Database:** SQLite ('Claims.db')
* **Version Control:** Git & GitHub

## Project Strucutre
'''text
insurance-claim-denials-analysis/
|
├── data/
│   ├── healthcare_data.csv       # Raw Kaggle dataset
│   └── claims.db                 # Processed SQLite database
│
├── scripts/
│   ├── load_data.py              # ETL pipeline script (Ingests CSV -> SQLite)
│   ├── analyze_denials.py        # Stakeholder report: Denials by Insurance Type
│   └── analyze_reasons.py        # Stakeholder report: Denials by Reason Code
│
└── README.md                     # Project documentation

## Key Business Insights Uncovered
1. Top loss by Insurance Type: Commercial insurance accounts for our highest financial loss ($27,386 across 89 denied claims), followed closely by self-pay. 
2. primary Denial Reason Codes: "Incorrect billing information" ($15,261) and "Authorization not obtained" ($13,636) are the leading operational bottlenecks driving revenue leakage.
