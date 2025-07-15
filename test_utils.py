import pandas as pd
from utils import process_leads

df = pd.read_csv("sample_data.csv")
scored_df = process_leads(df)
print(scored_df[['name', 'email', 'valid_email', 'job_title', 'linkedin_found', 'lead_score']])
