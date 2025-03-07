import streamlit as st

# Set Page Configuration with Icon
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟")

# Custom CSS for Darker Background & Light Success Messages
st.markdown(
    """
    <style>
    /* Dark Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #1e1e2e, #3a3a5f, #252541, #16162a);
        background-size: 300% 300%;
        animation: gradientBG 6s ease infinite;
        color: white;
        padding: 20px;
    }

    /* Background Animation */
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Glassmorphism Effect */
    .stContainer {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
    }

    /* Light Colored Alerts */
    .stSuccess {background-color: #a0ffaf !important; color: black !important; font-weight: bold;}
    .stWarning {background-color: #ffeb99 !important; color: black !important; font-weight: bold;}
    .stInfo {background-color: #a8d8ff !important; color: black !important; font-weight: bold;}
    .stError {background-color: #ffb3b3 !important; color: black !important; font-weight: bold;}

    /* Stylish Inputs */
    .stTextInput, .stTextArea {
        width: 70% !important;
        margin: auto;
        border-radius: 12px;
        padding: 12px;
        border: 2px solid rgba(255, 255, 255, 0.4);
        background: rgba(255, 255, 255, 0.1);
        color: white;
        box-shadow: 0px 0px 12px rgba(255, 255, 255, 0.2);
    }

    /* Stylish Buttons */
    .stButton>button {
        width: 70%;
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 14px;
        transition: all 0.4s;
        box-shadow: 0px 5px 15px rgba(106, 17, 203, 0.4);
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #3a0ca3, #4cc9f0);
        transform: scale(1.05);
        box-shadow: 0px 8px 20px rgba(106, 17, 203, 0.6);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# 🌱 Title & Welcome Message
st.title("🌱 Growth Mindset Project: Web App With Streamlit")
st.header("👋 Welcome To Narmeen Adeel Siddiqui's Growth Mindset Journey")
st.write("💡 Embrace the growth mindset and learn how to overcome challenges and obstacles in your life.")

# 🌟 Quote Section
st.header("📜 Quote of the Day")
st.write("❝ *The only limit to our realization of tomorrow will be our doubts of today.* ❞ – Franklin D. Roosevelt")

# 🚀 Challenge Input
st.header("⚡ What's The Challenge Today?")
user_input = st.text_input("💭 Describe the challenge you are facing today:")

if user_input:
    st.markdown(f'<div class="stSuccess">🔥 You are Facing: <b>{user_input}</b>. Keep Going! You Got This! 💪</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stWarning">⚠️ Tell us about your challenge to get started!</div>', unsafe_allow_html=True)

# ✨ Reflection Section
st.header("📝 Reflection Time")
reflection = st.text_area("✍️ Write your thoughts here:")

if reflection:
    st.markdown(f'<div class="stSuccess">🌟 Great! You are reflecting on: <b>{reflection}</b>. Keep Growing & Glowing! ✨</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stInfo">💭 Reflecting on past experiences helps you grow & glow! 🌱</div>', unsafe_allow_html=True)

# 🏆 Achievements Section
st.header("🎉 Celebrate Your Achievements")
achievement = st.text_input("🏅 What did you achieve today?")

if achievement:
    st.markdown(f'<div class="stSuccess">🎊 Congratulations on achieving: <b>{achievement}</b>! Keep Going! 🚀</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="stWarning">💡 Celebrate your small wins to stay motivated!</div>', unsafe_allow_html=True)

# 🔗 Footer
st.write("💻 Developed by **Narmeen Adeel Siddiqui 🥰**")
st.write("🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/narmeenadeelsiddiqui/) 💙")
