# 🧭 AI-Based Travel Planner using Streamlit and Gemini

This project is a **Generative AI-powered travel assistant** that helps users plan their dream trip effortlessly. Built using **Google's Gemini API** and **Streamlit**, the app generates personalized multi-day travel itineraries based on user preferences like budget, destination, days, and interests — all within a clean, interactive interface.

---

## 🗺️ Project Overview

The goal of this project is to simplify travel planning using Generative AI.  
Users can:

- Enter their travel details (destination, budget, number of days)
- Select personal interests (e.g. Food, Nature, Beaches, etc.)
- Get a day-wise travel itinerary tailored to preferences
- See estimated expenses per spot
- Enjoy a beautiful, simple Streamlit UI

No travel agent, no planning stress — just your perfect trip, instantly crafted!

---

## ✨ Features

✅ Uses Google Gemini API to generate customized itineraries  
✅ Budget-friendly plans  
✅ Covers food, local transport, activities, and more  
✅ Clean & modern UI via Streamlit  
✅ Works for 1–15 days of travel  
✅ Real-time generation and output display  
✅ Mobile-responsive interface  
✅ Easily deployable on Streamlit Cloud

---

## 🌐 Live Demo

Deployed on Streamlit Cloud:  
🔗 https://travelplanner-bpjtyxmguim8pbyrab4zcu.streamlit.app/

---

## 🛠️ Tech Stack

 Tech                   ==> Purpose                             
 **Python**             ==> Main programming language           
 **Streamlit**          ==> UI framework for web app            
 **Google Gemini API**  ==> Generative AI for travel planning   
 **dotenv**             ==> Secure API key handling             

---

## 📦 Installation

To run this project locally:

### 1. Clone the Repository
git clone https://github.com/SandeepV-2k5/Travel_Planner.git
cd Travel_Planner

### 2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate  # For Windows

### 3. Install Required Dependencies
pip install -r requirements.txt

### 4. Set Your Gemini API Key
Create a .env file in the root directory:
YOUR_GEMINI_API_KEY=your_actual_api_key_here

### 5. Run the App
streamlit run app.py
