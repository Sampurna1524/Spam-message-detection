import streamlit as st
import requests

# Custom page config
st.set_page_config(page_title="Spam SMS Detector", page_icon="📱", layout="centered")

# Futuristic CSS styling
st.markdown("""
    <style>
    .main {
        background: #0f2027;
        background: linear-gradient(to right, #2c5364, #203a43, #0f2027);
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #1e1e1e;
        color: #00ffe1;
        border: 1px solid #00ffe1;
        border-radius: 8px;
    }
    .stTextArea > div > div > textarea {
        background-color: #1e1e1e;
        color: #00ffe1;
        border: 1px solid #00ffe1;
        border-radius: 8px;
    }
    .stButton > button {
        background-color: #00ffe1;
        color: black;
        border-radius: 12px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #00e6c3;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #00ffe1;'>🤖 Spam SMS Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Detect if an SMS is Spam or Legit using an AI model 🚀</p>", unsafe_allow_html=True)
st.markdown("---")

# Input box
user_input = st.text_area("📨 Enter SMS message here:", height=150)

# Predict button
if st.button("🔍 Analyze Message"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        try:
            response = requests.post("http://127.0.0.1:8000/predict", json={"text": user_input})
            prediction = response.json().get("prediction", "error")

            if prediction == "spam":
                st.error("🚫 Detected as **SPAM**! Be cautious.")
            elif prediction == "ham":
                st.success("✅ This is a **legitimate message** (HAM).")
            else:
                st.warning("Something went wrong. ❗")
        except:
            st.error("❌ Could not connect to the backend server.")
