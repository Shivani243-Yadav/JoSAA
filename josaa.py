import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("2022.csv")

# Convert ranks to numeric
df["Opening Rank"] = pd.to_numeric(df["Opening Rank"], errors="coerce")
df["Closing Rank"] = pd.to_numeric(df["Closing Rank"], errors="coerce")

st.title("🎓 JoSAA 2022 Dashboard")
st.markdown("Interactive dashboard built using Streamlit to explore JoSAA counselling data.")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_institutes = st.sidebar.multiselect("Select Institutes", df["Institute"].unique())
selected_quota = st.sidebar.multiselect("Select Quota", df["Quota"].unique())
selected_gender = st.sidebar.multiselect("Select Gender", df["Gender"].unique())
selected_seat = st.sidebar.multiselect("Select Seat Type", df["Seat Type"].unique())
selected_round = st.sidebar.multiselect("Select Round", sorted(df["Round"].unique()))

# Apply filters
filtered_df = df.copy()
if selected_institutes:
    filtered_df = filtered_df[filtered_df["Institute"].isin(selected_institutes)]
if selected_quota:
    filtered_df = filtered_df[filtered_df["Quota"].isin(selected_quota)]
if selected_gender:
    filtered_df = filtered_df[filtered_df["Gender"].isin(selected_gender)]
if selected_seat:
    filtered_df = filtered_df[filtered_df["Seat Type"].isin(selected_seat)]
if selected_round:
    filtered_df = filtered_df[filtered_df["Round"].isin(selected_round)]

# Summary
st.subheader("📊 Summary Statistics")
st.write(filtered_df.describe(include="all"))

# Gender Distribution
st.subheader("🙋 Admission Count by Gender")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x="Gender", palette="Set2", ax=ax1)
st.pyplot(fig1)

# Rank Distribution
st.subheader("📉 Closing Rank Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(data=filtered_df, x="Closing Rank", bins=50, kde=True, color="salmon", ax=ax2)
ax2.set_xlim(0, 100000)
st.pyplot(fig2)

# Round-wise count
st.subheader("📦 Seat Allocation by Round")
fig3, ax3 = plt.subplots()
sns.countplot(data=filtered_df, x="Round", palette="Blues", ax=ax3)
st.pyplot(fig3)

# Top programs
st.subheader("🎓 Top 10 Most Popular Programs")
top_programs = filtered_df["Academic Program Name"].value_counts().nlargest(10)
fig4, ax4 = plt.subplots()
sns.barplot(y=top_programs.index, x=top_programs.values, palette="viridis", ax=ax4)
ax4.set_xlabel("Number of Allotments")
st.pyplot(fig4)

# Optional heatmap: Avg closing rank by Institute vs Program (small subset for performance)
st.subheader("🔥 Heatmap: Avg Closing Rank by Institute vs Program (Top 10 x 10)")
top_inst = filtered_df["Institute"].value_counts().nlargest(10).index
top_prog = filtered_df["Academic Program Name"].value_counts().nlargest(10).index
heat_df = filtered_df[filtered_df["Institute"].isin(top_inst) & filtered_df["Academic Program Name"].isin(top_prog)]
pivot = heat_df.pivot_table(index="Institute", columns="Academic Program Name", values="Closing Rank", aggfunc="mean")

fig5, ax5 = plt.subplots(figsize=(12, 8))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="coolwarm", ax=ax5)
plt.xticks(rotation=45, ha="right")
st.pyplot(fig5)
