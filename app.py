import streamlit as st
import pandas as pd
import folium

from streamlit_folium import st_folium

from sklearn.tree import DecisionTreeClassifier

# Page config
st.set_page_config(
    page_title="AI Road Safety Dashboard",
    page_icon="🚗",
    layout="wide"
)

# Load dataset
df = pd.read_csv("accidents.csv")

# Train AI model
X = df[["accidents"]]
y = df["risk"]

model = DecisionTreeClassifier()

model.fit(X, y)

# Title
st.title("🚗 AI Road Safety Dashboard")

st.markdown(
    "### AI-Powered Accident Risk Analysis System"
)

# Show dataset
st.subheader("📊 Accident Dataset")
st.dataframe(df)

# Chart
st.subheader("📈 Accident Visualization")

st.bar_chart(
    df.set_index("location")["accidents"]
)

# AI prediction
st.subheader("🤖 Predict Accident Risk")

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
    f"{highest['location']} has the highest accidents"
)

# Map
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

st_folium(m, width=700, height=500)

# Safety tips
st.subheader("🛡️ Safety Tips")

st.info("""
- Follow speed limits
- Wear helmets and seat belts
- Avoid distracted driving
- Follow traffic signals
""")
