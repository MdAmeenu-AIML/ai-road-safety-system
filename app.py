import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("accidents.csv")

# Title
st.title("🚗 AI Road Safety Dashboard")

st.write("Accident Data Analysis")

# Show data
st.subheader("Accident Dataset")
st.dataframe(df)

# Find highest accident area
highest = df.loc[df["accidents"].idxmax()]

st.subheader("⚠️ Most Dangerous City")

st.error(
    f"{highest['location']} has the highest accidents: {highest['accidents']}"
)