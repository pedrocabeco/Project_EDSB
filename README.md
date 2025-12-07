# Customer churn reduction – Analytical insights and recommended actions
Group EDSB25_5

We build a churn-risk model for a telecommunications operator, using customer-level data and translating the results into practical retention actions.



## 1. Project goals

- Build a predictive churn model.
- Identify key churn drivers.
- Translate findings into actionable retention levers.



##2. Data and main features

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
