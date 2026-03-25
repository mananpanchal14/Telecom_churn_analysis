# Telecom Customer Churn Analysis

## Project Title:
     Telecom Customer Churn Analysis using Python, SQL, and Power BI

## Problem Statement:
      The objective of this project is to analyze customer churn behavior in a telecom dataset and identify key factors contributing to customer churn, so that actionable insights can be derived and can help businesses improve customer retention strategies.

## Dataset Overview:
      Total unique customer IDs: 7043
      Columns: customerID, gender, SeniorCitizen, Partner,	Dependents,	tenure,	PhoneService,	MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod,	MonthlyCharges, TotalCharges, Churn
      Target Variable: Churn (Yes/No)

## Tools & Technologies Used:
      Python (Pandas) — Data Cleaning & Exploration
      MySQL — Data Analysis & Querying 
      Power BI — Data Visualization & interactive dashboard creation

## Data Cleaning & Preparation:
    Highlights:
      Handled missing values in TotalCharges.
      Converted target variable, i.e., churn, into numeric format (1/0) so that it could be used for further analysis.
      Validated dataset integrity (row counts, handling null values, data types of columns).

## Exploratory Data Analysis:
    Calculated overall churn rate (~26.5%).
    Analyzed churn across individual variables.
    Identified variables with significant churn differences.

## Key Drivers of Churn:
    Primary Drivers (Actionable):
       (1)Contract Type
       (2)Internet Service Type
       (3)Payment Method
       (4)Tech Support Availability

    Secondary Factors (Customer Profile):
      (1)Senior Citizen Status
      (2)Dependents
      (3)Paperless Billing
      (4)Online Backup

## Key Insights:
      Customers on month-to-month contracts show significantly higher churn (~43%) compared to long-term contracts. Hence, Month-to-month customers are the most at risk, and this risk significantly increases when combined with high-cost services, lack of support, or less stable payment methods.
      Fiber optic users exhibit higher churn rates, especially when combined with flexible contracts.
      Electronic check users show the highest churn among payment methods (~45%+). 

## High-Risk Customer Segment:
      Customers on month-to-month contracts using fiber optic services show the highest churn (~54%), indicating a critical segment for retention efforts.

## Business Recommendations:
      Encourage long-term contracts through incentives.
      Improve adoption of Tech Support and Online Backup services.
      Target high-risk customers with proactive retention strategies.
      Promote auto-payment methods to improve customer stability.

## Dashboard
     Developed an interactive Power BI dashboard to visualize churn trends, key drivers, and high-risk customer segments.
