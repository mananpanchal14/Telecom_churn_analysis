import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
#print(df.head(100))

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors='coerce')
#df.info()
#print(df.isnull().sum())
df["TotalCharges"] = df["TotalCharges"].fillna(df["MonthlyCharges"]* df["tenure"])
df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})
'''
print(df["tenure"].describe())
print(df["MonthlyCharges"].describe())


df_1 = df.groupby('tenure')['Churn'].mean().reset_index()
df_1["max_churn"] = df_1.groupby("tenure")['Churn'].transform("max")
df_1["min_churn"] = df_1.groupby("tenure")['Churn'].transform("min")
print(df_1)

plt.plot(df_1["tenure"],df_1["Churn"],label="Churn",marker="o")
plt.xlabel("Tenure")
plt.ylabel("Churn")
plt.legend()
plt.show()
df['tenure_segment'] = pd.cut(
    df['tenure'],
    bins=[0, 6, 40, 72],
    labels=['Early Risk', 'Mid Term', 'Loyal']
)
#print(df["tenure_segment"])
#print(df)
print(df.groupby('tenure_segment')['Churn'].mean())
churn_trend = df.groupby('tenure')['Churn'].mean().rolling(5).mean()
print(churn_trend)
#print(df[df['tenure'] > 40]['Churn'].mean())
#print(df[df['tenure'] <= 40]['Churn'].mean())
'''
print(df['Churn'].value_counts(normalize=True).reset_index())
#print(df.groupby('Contract')['Churn'].value_counts(normalize=True).reset_index())
#sample = df.groupby('tenure')["Churn"].value_counts(normalize=True).reset_index()
#sample = sample[sample["Churn"] == 1]
#print(sample)

#print(df.groupby('InternetService')['Churn'].value_counts(normalize=True).reset_index())
#print(df.groupby('PaymentMethod')['Churn'].value_counts(normalize=True).reset_index())
#print(df.groupby('TechSupport')['Churn'].value_counts(normalize=True).reset_index())
#print(df.groupby(["Contract","TechSupport"])["Churn"].value_counts(normalize=True).reset_index())
#print(df.groupby(["Contract","InternetService"])["Churn"].value_counts(normalize=True).reset_index())
#print(df.groupby(["Contract","PaymentMethod"])["Churn"].value_counts(normalize=True).reset_index())
#print(df.groupby("Contract")["Churn"].agg(["sum","count","mean"]))
#print(df.groupby("TechSupport")["Churn"].agg(["sum","count","mean"]))
#print(df.groupby("PaymentMethod")["Churn"].agg(["sum","count","mean"]))
#print(df.groupby("InternetService")["Churn"].agg(["sum","count","mean"]))

print(df.groupby('SeniorCitizen')['Churn'].mean())
print(df.groupby('Dependents')['Churn'].mean())
print(df.groupby('MultipleLines')['Churn'].mean())
print(df.groupby('OnlineBackup')['Churn'].mean())
print(df.groupby('StreamingTV')['Churn'].mean())
print(df.groupby('StreamingMovies')['Churn'].mean())
print(df.groupby('PaperlessBilling')['Churn'].mean())

#print(df.groupby(["Contract","TechSupport"])["Churn"].agg(["sum","count","mean"]))
#print(df.groupby(["Contract","InternetService"])["Churn"].agg(["sum","count","mean"]))
#print(df.groupby(["Contract","PaymentMethod"])["Churn"].agg(["sum","count","mean"]))



