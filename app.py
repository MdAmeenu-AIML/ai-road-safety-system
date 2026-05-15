import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="AI Road Safety Dashboard",
    page_icon="🚗",
    layout="centered"
)

# Load dataset
df = pd.read_csv("accidents.csv")

# Title
st.title("🚗 AI Road Safety Dashboard")

st.markdown(
    "### Accident Data Analysis & Dangerous Area Detection"
)

# Show dataset
st.subheader("📊 Accident Dataset")
st.dataframe(df)

# Bar chart
st.subheader("📈 Accident Visualization")

st.bar_chart(
    df.set_index("location")
)

# Most dangerous city
highest = df.loc[df["accidents"].idxmax()]

st.subheader("⚠️ Most Dangerous City")

st.error(
    f"{highest['location']} has the highest accidents: {highest['accidents']}"
)

# Safety tips
st.subheader("🛡️ Road Safety Tips")

st.info("""
- Wear helmets and seat belts
- Avoid overspeeding
- Follow traffic signals
- Avoid mobile phone usage while driving
""")
