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


st.info("🌦️ Don't forget to check the **local weather forecast** for your travel dates!")

# Inputs
destination = st.text_input("Destination", placeholder="Example: Goa, Paris")
budget = st.number_input("Budget (in ₹)", min_value=1000, step=500)
days = st.slider("Number of Days", 1, 15, 3)
preferences = st.multiselect(
    "Choose Your Preferred Outing Types",
    ["Beach", "Food", "Mountains", "Shopping", "Culture", "Adventure", "Nightlife", "Nature", "Relaxation"]
)

# Generate itinerary
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
            - Mention each location/place in a way that matches how it's listed on Google Maps

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

                map_query = f"https://www.google.com/maps/search/{destination.replace(' ', '+')}"
                st.markdown(f"🌍 [Open {destination} in Google Maps]({map_query})", unsafe_allow_html=True)

                st.download_button(
                    label="📄 Download Itinerary as .txt",
                    data=itinerary,
                    file_name=f"{destination}_itinerary.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error generating itinerary: {e}")
    else:
        st.warning("Please enter a destination and select at least one outing type.")
