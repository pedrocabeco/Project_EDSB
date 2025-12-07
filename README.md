# Customer churn reduction – Analytical insights and recommended actions
Group EDSB25_5

We build a churn-risk model for a telecommunications operator, using customer-level data and translating the results into practical retention actions.



## 1. Project goals

- Build a predictive churn model.
- Identify key churn drivers.
- Translate findings into actionable retention levers.



## 2. Data and main features

We use the **Telco Customer Churn** dataset provided in the course, split into five tables:

- `Demographics` - age, senior citizen, marital status, dependents, etc.  
- `Location` - city, state, population density indicators.  
- `Population` - area-level income/population metrics.  
- `Services` - phone, internet type (DSL/Fiber/Cable), add-ons (security, backup, support, streaming, …).  
- `Status` - contract type, tenure (months), payment method, paperless billing, monthly charges, churn flag.

After merging and cleaning:

- **7043 customers**  
- **47 features** used in the final model  
- **Churn rate**: ~26.5% “Yes”, 73.5% “No” (unbalanced dataset)

The target variable is **`Churn Value`** (1 = churn, 0 = no churn).



## 3. Repository structure
```text ... 

├── README.md
├── requirements.txt
├── .gitignore
│
├── data
│   ├── model_ready
│   │   └── telco_churn_model_ready.csv
│   │
│   │── processed
│   │   └── telco_churn_master.csv
│   │
│   ├── raw
│   │   ├── Telco_customer_churn_demographics.csv
│   │   ├── Telco_customer_churn_location.csv
│   │   ├── Telco_customer_churn_population.csv
│   │   ├── Telco_customer_churn_services.csv
│   │   └── Telco_customer_churn_status.csv
│   │
│   └── xlsx_originals
│       ├── Telco_customer_churn_demographics.xlsx
│       ├── Telco_customer_churn_location.xlsx
│       ├── Telco_customer_churn_population.xlsx
│       ├── Telco_customer_churn_services.xlsx
│       └── Telco_customer_churn_status.xlsx
│
├── notebooks
│   ├── 01_Load_data_and_initial_EDA.ipynb
│   ├── 02_MergingTables.ipynb
│   ├── 03_EDA.ipynb
│   ├── 03.1_M2M_Customers_Analysis.ipynb
│   ├── 03.2_Churn_Reasons_M2M_Profile.ipynb
│   ├── 03.3_Tenure_Analysis.ipynb
│   ├── 04_FeatureEngineering.ipynb
│   └── 05_Modelling.ipynb
│
├── reports
│   └── profiling_raw_tables
│       ├── demographics_profiling.html
│       ├── location_profiling.html
│       ├── population_profiling.html
│       ├── services_profiling.html
│       └── status_profiling.html
│
└── src
    └── convert_to_csv.py
