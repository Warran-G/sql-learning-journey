# Telco Customer Churn Analysis — Power BI Dashboard

An interactive Power BI dashboard analyzing customer churn patterns for a telecommunications company, identifying key drivers of customer loss and translating findings into actionable retention strategies.

## 📊 Project Overview

Customer churn — the rate at which customers stop doing business with a company — directly impacts revenue and long-term growth. This project analyzes a telecom customer dataset to answer three core questions:

1. **How many customers are we losing, and what's the overall churn rate?**
2. **What customer attributes are most strongly associated with churn?**
3. **What specific actions can reduce churn going forward?**

The result is a 5-page interactive dashboard built for a non-technical, decision-making audience — designed to be skimmed in under two minutes while still supporting deeper exploration through slicers and filters.

## 🗂️ Dataset

- **Source:** Telco Customer Churn dataset (7,043 customer records)
- **Fields used:** Contract type, Payment method, Tenure, Churn status, Customer ID, Monthly/Total charges
- **Processing:** Initial exploration and validation performed in Python (pandas) before building visuals in Power BI

## 🛠️ Tools Used

- **Power BI Desktop** — dashboard design, DAX measures, interactive visuals
- **Python (pandas)** — initial dataset exploration and analysis
- **GitHub** — version control and project hosting

## 📑 Dashboard Structure

| Page | Contents |
|---|---|
| **Overview** | Total Customers, Customers Lost, Churn Rate %, and a donut chart showing overall churn split |
| **Contract Analysis** | 100% stacked bar chart of churn by contract type, with interactive isolate buttons |
| **Payment Method Analysis** | 100% stacked bar chart of churn by payment method, with interactive isolate buttons |
| **Tenure Analysis** | Churn rate broken down by tenure bins (0–12, 13–24... months), showing risk over the customer lifecycle |
| **Key Findings & Recommendations** | Executive summary tying all insights together into a single action plan |

## 🔍 Key Insights

- **Overall churn rate: 26.54%** — roughly 1 in 4 customers (1,869 people) leave the company.
- **Contract type:** Month-to-month customers churn at **42.71%**, compared to just **2.83%** for two-year contracts.
- **Payment method:** Electronic check users churn at **45.29%**, nearly 3x the rate of customers on automatic payment methods (15–17%).
- **Tenure:** Churn is highest in the first 12 months (**48.28%**) and drops below 2% beyond 70 months — early-stage experience is a critical risk window.

## ✅ Recommendations

1. **Incentivize contract upgrades** — offer pricing discounts or loyalty perks to convert month-to-month customers into longer-term contracts.
2. **Drive automatic payment adoption** — reduce friction for electronic check users through incentives or simplified autopay onboarding.
3. **Strengthen early-stage retention** — focus onboarding, engagement, and support efforts on the first 90 days of the customer relationship.

**Bottom line:** New, short-contract, manually-billed customers represent the highest-risk segment. Concentrating retention spend on this overlapping group — rather than spreading it evenly — will deliver the greatest reduction in churn for the lowest cost.

## 📸 Screenshots

*(Add dashboard screenshots here — drag image files into this section or link to a `/screenshots` folder in the repo)*

## 🚀 How to View

1. Clone or download this repository
2. Open `churn_dashboard.pbix` in Power BI Desktop
3. Use the button slicers on the Contract and Payment Method pages to filter and explore the data interactively

## 👤 Author

Maxwel — Engineering diploma student | Self-directed Power BI / data analysis project

---

*This project was built as a hands-on exercise in data visualization, business storytelling, and translating raw data into stakeholder-ready recommendations.*
