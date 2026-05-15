import streamlit as st
import pandas as pd
import folium

from streamlit_folium import st_folium
from sklearn.tree import DecisionTreeClassifier

# Page settings
st.set_page_config(
    page_title="AI Road Safety Dashboard",
    page_icon="🚗",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: white;
}

[data-testid="stMetricValue"] {
    color: #FF4B4B;
}

.stButton > button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 18px;
}

.stButton > button:hover {
    background-color: #ff1e1e;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Load dataset
df = pd.read_csv("accidents.csv")

# Train model
X = df[["accidents"]]
y = df["risk"]

model = DecisionTreeClassifier()

model.fit(X, y)

# Title
st.title("🚗 AI Road Safety Dashboard")

st.markdown(
    "### AI-Powered Accident Risk Analysis & Alert System"
)

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Cities",
        len(df)
    )

with col2:
    st.metric(
        "Highest Accidents",
        df["accidents"].max()
    )

with col3:
    st.metric(
        "Average Accidents",
        round(df["accidents"].mean(), 1)
    )

# Dataset
st.subheader("📊 Accident Dataset")

st.dataframe(df)

# Visualization
st.subheader("📈 Accident Visualization")

st.bar_chart(
    df.set_index("location")["accidents"]
)

# AI prediction
st.subheader("🤖 AI Risk Prediction")

accident_input = st.number_input(
    "Enter accident count",
    min_value=0
)

if st.button("Predict Risk"):

    prediction = model.predict(
        [[accident_input]]
    )

    st.success(
        f"Predicted Risk Level: {prediction[0]}"
    )

# Dangerous city
highest = df.loc[df["accidents"].idxmax()]

st.subheader("⚠️ Most Dangerous City")

st.error(
    f"{highest['location']} has the highest accidents with {highest['accidents']} reported cases"
)

# Interactive map
st.subheader("🗺️ Accident Location Map")

m = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5
)

for _, row in df.iterrows():

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"{row['location']} - {row['risk']} Risk",
        tooltip=row["location"]
    ).add_to(m)

st_folium(m, width=1200, height=500)

# Safety tips
st.subheader("🛡️ Road Safety Tips")

st.info("""
✅ Wear helmets and seat belts

✅ Avoid overspeeding

✅ Follow traffic rules

✅ Avoid using mobile phones while driving

✅ Stay alert in high-risk areas
""")
