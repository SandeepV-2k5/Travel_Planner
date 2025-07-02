import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from fpdf import FPDF
import tempfile
from datetime import datetime

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("YOUR_GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Travel Planner Bot", page_icon="🧳", layout="centered")
st.title("🧭 Travel Planner")
st.write("Plan your perfect trip based on destination, dates, interests, budget, and more!")

# Inputs
destination = st.text_input("Destination", placeholder="e.g., Goa, Paris")

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date")
with col2:
    end_date = st.date_input("End Date")

# Calculate number of days
trip_days = (end_date - start_date).days
if trip_days <= 0:
    st.warning("Please ensure end date is after the start date.")

min_budget = st.number_input("Minimum Budget (in ₹)", min_value=1000, step=500)
max_budget = st.number_input("Maximum Budget (in ₹)", min_value=min_budget, step=500)

people = st.number_input("Number of People in Trip", min_value=1, step=1)

transport_mode = st.selectbox(
    "Preferred Mode of Transport (between cities/states)",
    ["Train", "Car", "Aeroplane", "Ship", "Bus", "Other"]
)

food_type = st.radio("Preferred Food Type", ["Vegetarian", "Non-Vegetarian"])

# Preferences
default_preferences = [
    "Beach", "Food", "Mountains", "Shopping", "Culture",
    "Adventure", "Nightlife", "Nature", "Relaxation", "Other"
]
selected_preferences = st.multiselect("Choose Your Preferred Outing Types", default_preferences)

# Handle "Other" preference
custom_preferences = []
if "Other" in selected_preferences:
    custom_input = st.text_input("Add your own outing types (press Enter to save)", key="custom")
    if custom_input:
        if custom_input not in custom_preferences:
            custom_preferences.append(custom_input)

final_preferences = [p for p in selected_preferences if p != "Other"] + custom_preferences

# Show final preferences visually
if final_preferences:
    st.success(f"✅ Selected Preferences: {', '.join(final_preferences)}")

# Generate Itinerary
if st.button("Generate Itinerary"):
    if not destination or not final_preferences or trip_days <= 0:
        st.warning("Please fill all fields correctly!")
    else:
        with st.spinner("Planning your dream trip..."):
            prompt = f"""
            Plan a detailed travel itinerary for {people} people visiting {destination} from {start_date.strftime('%d %B %Y')} to {end_date.strftime('%d %B %Y')} ({trip_days} days).
            Budget: ₹{min_budget} – ₹{max_budget}
            Interests: {', '.join(final_preferences)}
            Preferred Travel Mode: {transport_mode}
            Preferred Food: {food_type}
            Ensure:
            - The plan fits the budget range
            - Highlights 1–3 main things per day
            - Includes estimated cost, local travel, and food recommendations
            - Tailors activities to interests and chosen transport mode
            - Vegetarian/Non-Vegetarian options where applicable

            Format:
            Day 1: ...
            Day 2: ...
            ...
            """

            try:
                response = model.generate_content(prompt)
                itinerary = response.text
                st.subheader("🗓️ Your Itinerary:")
                st.markdown(itinerary)

                # Generate PDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                for line in itinerary.split("\n"):
                    try:
                        pdf.cell(200, 10, txt=line.encode("latin-1", "replace").decode("latin-1"), ln=True)
                    except:
                        pass

                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    pdf.output(tmp_file.name)
                    with open(tmp_file.name, "rb") as f:
                        st.download_button("📥 Download Itinerary as PDF", f, file_name="itinerary.pdf")

            except Exception as e:
                st.error(f"Error generating itinerary: {e}")
