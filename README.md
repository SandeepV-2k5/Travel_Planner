# 🧭 AI-Based Travel Planner using Streamlit & Gemini

This project is a **Generative AI-powered travel assistant** that helps users plan their **entire round-trip itinerary** — from transportation and stay to activities and food — in a few clicks! Built with **Google Gemini API** and **Streamlit**, it creates **smart, budget-friendly** travel plans customized to your preferences like destination, budget, food type, transport mode, and more.

---

## 🌍 Project Overview

The goal is to **simplify travel planning** using the power of **Generative AI**. No need to research, Google, or call travel agents — just enter your trip info, and get a full itinerary instantly.

### ✅ Users Can:
- Input **start and destination locations**
- Set **trip dates**, **number of travelers**, **food preference**, and **transport mode**
- Choose preferred **outing types** (e.g., Beach, Adventure, Nature, etc.)
- Add custom outing preferences via `"Other"` option
- Get a **day-wise itinerary** with:
  - Outbound and return journey
  - Estimated travel times
  - Hotel/accommodation suggestions
  - Local experiences and food tailored to your choices
- **Download the final itinerary as a PDF**
- All powered by **Gemini Pro (Generative AI)**

---

## ✨ Features

- 🔥 Powered by [Google Gemini API](https://ai.google.dev/)
- 🏨 Day-by-day plan with hotels, food, and activities
- 💸 Works within your **minimum–maximum budget**
- ✈️ Customizable transport: Train, Car, Plane, etc.
- 🧑‍🤝‍🧑 Choose number of travelers
- 🍱 Veg/Non-Veg food preference included
- 🧠 AI-generated, realistic, cost-conscious itineraries
- 📄 Downloadable **PDF itinerary**
- 📱 Fully responsive UI via **Streamlit**
- 🧠 Add your own outing preferences if not listed

---

## 🌐 Live Demo

Try it out live on **Streamlit Cloud**:

🔗 [https://travelplanner-bpjtyxmguim8pbyrab4zcu.streamlit.app/](https://travelplanner-bpjtyxmguim8pbyrab4zcu.streamlit.app/)

---

## 🛠️ Tech Stack

| Tech               | Purpose                            |
|--------------------|-------------------------------------|
| **Python**         | Core programming language           |
| **Streamlit**      | Frontend UI framework               |
| **Gemini API**     | Generates the travel itinerary      |
| **dotenv**         | Handles secure API keys             |
| **fpdf**           | Converts itinerary to PDF           |

---

## 📦 Installation Guide
Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/SandeepV-2k5/Travel_Planner.git
cd Travel_Planner
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a .env file in the root directory and add your Gemini API key:
```env
YOUR_GEMINI_API_KEY=your_actual_api_key_here
```

## 5. Run the App
```bash
streamlit run app.py
```

---

## How to run the website

## Enter your Starting Location, Desired Destination, Start Date & End Date, Minimum Budget (in ₹) & Maximum Budget (in ₹)

![image](https://github.com/user-attachments/assets/31a819fa-5dd7-4e5e-8625-59699968c7d4)

---

## Enter Number of people in Trip, Preferred Mode of Transport, Preferred Food Type and Preferred Outing Types

![image](https://github.com/user-attachments/assets/a22e8148-6b1b-46d3-ad62-955a0115a157)

---

 ## After filling all the fields, click on Generate Itinerary

 ![image](https://github.com/user-attachments/assets/4cebf1a5-2311-4fed-a298-28b0ed314e20)

 ---

 ## Output Itinerary is generated

 ![image](https://github.com/user-attachments/assets/a21f598e-93ba-4269-afb8-3f685f4c4a00)

 ![image](https://github.com/user-attachments/assets/75e61441-0679-4414-b10e-db13709c8aea)

 ![image](https://github.com/user-attachments/assets/290ec256-6d0d-4ecb-810e-815957d3a966)

 ---

 ## The Itinerary is also downloadable as pdf

 ![image](https://github.com/user-attachments/assets/78ef0ee9-edfb-4123-bcf0-0702e071c06f)
