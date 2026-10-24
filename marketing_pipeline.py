import pandas as pd
import numpy as np

# Load raw marketing dataset
df = pd.read_csv("global_ads_performance_dataset.csv")

# Ensure correct data types
df['date'] = pd.to_datetime(df['date'])
df['ad_spend'] = df['ad_spend'].astype(float)
df['revenue'] = df['revenue'].astype(float)

# Calculate/Verify Funnel Metrics
df['CTR_%'] = (df['clicks'] / df['impressions']) * 100
df['CPC'] = df['ad_spend'] / df['clicks'].replace(0, np.nan)
df['Conversion_Rate_%'] = (df['conversions'] / df['clicks']) * 100

# Calculate Financial Impact Metrics
df['CAC'] = df['ad_spend'] / df['conversions'].replace(0, np.nan)
df['ROAS'] = df['revenue'] / df['ad_spend'].replace(0, np.nan)
df['ROI_%'] = ((df['revenue'] - df['ad_spend']) / df['ad_spend'].replace(0, np.nan)) * 100

# Export enriched data for Power BI
df.to_csv("marketing_campaign_enriched.csv", index=False)
print("Pipeline executed successfully! Enriched file saved as 'marketing_campaign_enriched.csv'.")