import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("YOUR_GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Travel Planner Bot", page_icon="🧳", layout="centered")

st.title("🧭 Travel Planner")
st.write("Plan your perfect trip based on destination, budget, days, and your interests!")

# Input
destination = st.text_input("Destination", placeholder="Example: Goa, Paris")
budget = st.number_input("Budget (in ₹)", min_value=1000, step=500)
days = st.slider("Number of Days", 1, 15, 3)
preferences = st.multiselect(
    "Choose Your Preferred Outing Types",
    ["Beach", "Food", "Mountains", "Shopping", "Culture", "Adventure", "Nightlife", "Nature", "Relaxation"]
)

# Button to generate
if st.button("Generate Itinerary"):
    if destination and preferences:
        with st.spinner("Planning your adventure..."):
            prompt = f"""
            Create a detailed {days}-day travel itinerary for {destination}.
            Budget: ₹{budget}
            Interests: {', '.join(preferences)}.

            Ensure:
            - The plan fits the budget
            - Highlights 1–3 main things per day
            - Includes estimated costs, local travel, and food where possible
            - Tailors activities to the mentioned interests

            Format:
            Day 1: ...
            Day 2: ...
            ...
            """
            try:
                response = model.generate_content(prompt)
                st.subheader("🗓️ Your Itinerary:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error generating itinerary: {e}")
    else:
        st.warning("Please enter a destination and select at least one outing type.")
