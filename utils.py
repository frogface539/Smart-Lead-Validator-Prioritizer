import pandas as pd
import re

## email validation
## Returns true if email is syntactically valid using regex
def validate_email(email):
    if not isinstance(email, str) or email.strip() == '':
        return False

    email = email.strip()
    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    return bool(re.match(pattern, email))

## Returns True if the linkedin URL is present
def has_linkedin(url):
    if pd.isnull(url):
        return False
    
    return 'linkedin.com/in/' in url

## Job Title Scoring Function
def score_job_title(title):
    if pd.isnull(title):
        return 0
    
    title = title.lower().strip()

    if any(keyword in title for keyword in ['ceo', 'chief executive', 'founder', 'cto', 'co-founder', 'chief technology']):
        return 3
    
    elif any(keyword in title for keyword in ['vp', 'vice president', 'director', 'head']):
        return 2
    
    elif 'manager' in title:
        return 1
    
    return 0

def score_lead(row):
    score = 0
    score += score_job_title(row['job_title'])              
    score += 1 if validate_email(row['email']) else 0         
    score += 1 if has_linkedin(row['linkedin_url']) else 0
    return score

## applies all validation and scoring logic to the i/p Dataframe
## adds valid-email, linkedin_found and lead_score
def process_leads(df):
    df['valid_email'] = df['email'].apply(validate_email)
    df['linkedin_found'] = df['linkedin_url'].apply(has_linkedin)
    df['lead_score'] = df.apply(score_lead, axis=1)

    column_order = ['name', 'email', 'valid_email', 'job_title', 'company',
                    'website', 'linkedin_url', 'linkedin_found', 'location', 'lead_score']
    df = df[[col for col in column_order if col in df.columns]]

    return df.sort_values(by='lead_score', ascending=False).reset_index(drop=True)