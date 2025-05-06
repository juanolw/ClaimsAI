import streamlit as st
import pandas as pd

   # Define the data
positions_data = [
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Jurisdictional Objection",
           "Position": "Arbitration limited to Contract MR-0010/1/2018/810 Rev6; other claims (e.g., additional works) governed by UAE law and Dubai Courts.",
           "Reference": "Response, Page 1",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Jurisdictional Objection",
           "Position": "KSS failed to comply with multi-tier dispute resolution (Clause 28d) before suspending works, rendering claims inadmissible.",
           "Reference": "Statement of Defence, Pages 32-39",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Defense",
           "Position": "Acknowledges AED 1,525,608.78 unpaid but deducts AED 1,868,571.00 for non-conforming works and delays, resulting in negative balance.",
           "Reference": "Response, Page 2",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Defense",
           "Position": "KSS’s suspension of works on 28 January 2020 was a fundamental breach, causing PCT hardship.",
           "Reference": "Statement of Defence, Pages 32, 37, 40",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Defense",
           "Position": "Retention monies (AED 426,790.86) not due until Taking Over Certificate issued, delayed by EXPO 2020 (COVID-19).",
           "Reference": "Response, Page 3",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Defense",
           "Position": "Rejects AED 1,865,270.97 for additional works due to lack of approved variations or cost breakdowns.",
           "Reference": "Response, Page 3",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Counterclaim",
           "Position": "Claims AED 1,868,571.00 for rectifying non-conforming works, delays, and scaffolding overruns.",
           "Reference": "Response, Page 2",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Counterclaim",
           "Position": "Five counterclaims for remedial works, scaffolding charges, and completion of KSS’s unfinished works.",
           "Reference": "Statement of Defence, Pages 25, 42",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Delay",
           "Position": "KSS failed to complete works by June 2019 per Contract program, causing overruns; no extension of time requested.",
           "Reference": "Response, Page 2",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Delay",
           "Position": "KSS’s delays in reflector works (completed 21 November 2019 vs. 26 September 2019 revised date) due to defective works.",
           "Reference": "Statement of Defence, Pages 18-19",
       },
       {
           "Party": "Respondent (PCT)",
           "Claim Type": "Settlement",
           "Position": "Proposes final settlement of AED 79,098.00 plus uncollected cheques, contingent on KSS completing works.",
           "Reference": "Response, Page 4",
       },
       {
           "Party": "Claimant (KSS)",
           "Claim Type": "Financial Claim",
           "Position": "Claims AED 1,525,608.78 for unpaid contract amount.",
           "Reference": "Response, Page 2 (KSS claim referenced by PCT)",
       },
       {
           "Party": "Claimant (KSS)",
           "Claim Type": "Financial Claim",
           "Position": "Claims AED 150,160.48, incorporated into contract amount.",
           "Reference": "Response, Page 2 (KSS claim referenced by PCT)",
       },
       {
           "Party": "Claimant (KSS)",
           "Claim Type": "Financial Claim",
           "Position": "Claims AED 659,757.60 for interim payment.",
           "Reference": "Response, Page 2 (KSS claim referenced by PCT)",
       },
       {
           "Party": "Claimant (KSS)",
           "Claim Type": "Financial Claim",
           "Position": "Claims AED 426,790.86 for retention monies.",
           "Reference": "Response, Page 3 (KSS claim referenced by PCT)",
       },
       {
           "Party": "Claimant (KSS)",
           "Claim Type": "Financial Claim",
           "Position": "Claims AED 1,865,270.97 for additional works.",
           "Reference": "Response, Page 3 (KSS claim referenced by PCT)",
       },
       {
           "Party": "Claimant (KSS)",
           "Claim Type": "Financial Claim",
           "Position": "Claims AED 9,933 for labor on separate project.",
           "Reference": "Response, Page 3 (KSS claim referenced by PCT)",
       },
       {
           "Party": "Claimant (KSS)",
           "Claim Type": "Financial Claim",
           "Position": "Claims AED 43,688.40 for brackets.",
           "Reference": "Response, Page 4 (KSS claim referenced by PCT)",
       },
   ]

# Convert data to DataFrame
df = pd.DataFrame(positions_data)

# Streamlit app
st.title("Arbitration Position Summarizer")

# Create two columns for filters
col1, col2 = st.columns(2)

# Filter by Party
with col1:
       unique_parties = ["All"] + sorted(df["Party"].unique().tolist())
       selected_party = st.selectbox("Filter by Party", unique_parties)

# Filter by Claim Type
with col2:
       unique_claim_types = ["All"] + sorted(df["Claim Type"].unique().tolist())
       selected_claim_type = st.selectbox("Filter by Claim Type", unique_claim_types)

# Apply filters
filtered_df = df
if selected_party != "All":
       filtered_df = filtered_df[filtered_df["Party"] == selected_party]
if selected_claim_type != "All":
       filtered_df = filtered_df[filtered_df["Claim Type"] == selected_claim_type]

# Display the filtered table
st.subheader("Positions Table")
st.dataframe(
       filtered_df,
       use_container_width=True,
       hide_index=True,
       column_config={
           "Party": st.column_config.TextColumn("Party", width="medium"),
           "Claim Type": st.column_config.TextColumn("Claim Type", width="medium"),
           "Position": st.column_config.TextColumn("Position", width="large"),
           "Reference": st.column_config.TextColumn("Reference", width="medium"),
       },
   )

# Instructions
st.markdown("""
   ### How to Use
   - Use the dropdown menus to filter by **Party** (Claimant or Respondent) or **Claim Type** (e.g., Financial Claim, Defense).
   - Select "All" to view all entries for a given filter.
   - The table displays the filtered positions with their respective references to source documents.
   """)
