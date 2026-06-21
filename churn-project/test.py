"""Telco Customer Churn Analysis
-------------------------------
Exploratory analysis supporting the Power BI churn dashboard.
Covers: overall churn rate, churn by contract type, churn by payment
method, and churn by customer tenure — the same four insights
visualized in the dashboard.
"""

import pandas as pd
df = pd.read_csv("data/churn.csv")
print(df.info())

print ("\nChurn counts:")
print (df["Churn"].value_counts())

print ("\nChurn Percentage:")
print (df["Churn"].value_counts(normalize=True)*100)

print("\n churn by contract type:")

contract_churn = pd.crosstab(df["Contract"], df["Churn"], normalize = " index")*100
contract_churn = contract_churn.sort_values(by = "Yes", ascending=False)
print(contract_churn.round(2))

print ("\nCustomer Count by Contract and Churn:")
print(pd.crosstab(df["Contract"],df["Churn"]))

print ("\nChurn Percentage by Contract:")
contract_churn = pd.crosstab(df["Contract"], df["Churn"], normalize = " index")*100
contract_churn = contract_churn.round(2).sort_values(by = "Yes", ascending=False)
print(contract_churn)

payment_churn = pd.crosstab(df["PaymentMethod"], df["Churn"], normalize = " index")*100
payment_churn = payment_churn.round(2).sort_values(by = "Yes", ascending=False)
print(payment_churn.round(2))

tenure_churn = pd.crosstab(df["PaymentMethod"], df["Churn"], normalize = " index")*100
tenure_churn = tenure_churn.round(2).sort_values(by = "Yes", ascending=False)
print(tenure_churn.round(2))

df.to.csv("powerbi/churn_data.csv", index= False)