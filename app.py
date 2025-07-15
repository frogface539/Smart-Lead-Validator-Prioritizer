import streamlit as st
import pandas as pd
import plotly.express as px
from utils import process_leads

st.set_page_config(page_title="Smart Lead Prioritizer", page_icon="📊", layout="wide")
st.title("📊 Smart Lead Validator & Prioritizer")

st.write(
    "Upload a CSV of leads. This tool validates emails, checks LinkedIn presence, and scores each lead based on seniority and contactability."
)

uploaded_file = st.file_uploader("📁 Upload your leads CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        scored_df = process_leads(df)

        st.success("✅ Leads processed and scored successfully!")

        score_counts = scored_df['lead_score'].value_counts().sort_index()
        fig = px.pie(
            names=score_counts.index,
            values=score_counts.values,
            title="📊 Lead Score Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig, use_container_width=True)

        def highlight_top(row):
            color = "#0306ac" if row['lead_score'] >= 4 else ''
            return ['background-color: {}'.format(color)] * len(row)

        st.markdown("### 🧮 Scored Leads")
        styled_df = scored_df.style.apply(highlight_top, axis=1)
        st.dataframe(styled_df, use_container_width=True)

        st.markdown("### 📧 Top Leads (Score ≥ 4)")
        top_leads = scored_df[scored_df['lead_score'] >= 4]

        for _, row in top_leads.iterrows():
            with st.expander(f"👤 {row['name']} — {row['job_title']}"):
                st.write(f"📨 Email: `{row['email']}`")
                st.write(f"🏢 Company: {row['company']}")
                st.write(f"🔗 LinkedIn: {row['linkedin_url'] or 'N/A'}")
                if st.button(f"Send Email to {row['name']}"):
                    st.success(f"✅ Mock email sent to {row['email']} (simulated).")

        csv = scored_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Prioritized Leads as CSV",
            data=csv,
            file_name="prioritized_leads.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Failed to process the file: {e}")
else:
    st.info("👆 Please upload a CSV file to begin.")
