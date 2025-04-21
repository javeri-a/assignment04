import streamlit as st
import random

st.markdown("<h1 style='text-align: center; color:#6C63FF;'>💭 Mood-Based Quotes</h1>", unsafe_allow_html=True)
st.markdown("### Choose your mood and get inspired ✨")
st.markdown("---")

quotes = {
    "😊 Happy": [
        "Happiness is not by chance, but by choice.",
        "Smile, it's the key that fits the lock of everybody's heart.",
        "The purpose of our lives is to be happy.",
    ],
    "😢 Sad": [
        "Tears come from the heart and not from the brain.",
        "Sometimes it's okay if the only thing you did today was breathe.",
        "Sadness flies away on the wings of time.",
    ],
    "🔥 Motivated": [
        "Push yourself, because no one else is going to do it for you.",
        "The harder you work for something, the greater you’ll feel when you achieve it.",
        "Success doesn’t just find you. You have to go out and get it.",
    ],
    "🌿 Calm": [
        "Keep calm and carry on.",
        "Peace begins with a smile.",
        "In the midst of movement and chaos, keep stillness inside of you.",
    ],
    "⚡ Energetic": [
        "Wake up with determination. Go to bed with satisfaction.",
        "Energy and persistence conquer all things.",
        "Don’t stop when you’re tired. Stop when you’re done.",
    ]
}

mood = st.selectbox("💬 What's your current mood?", list(quotes.keys()))

if st.button("🌟 Show Me a Quote"):
    quote = random.choice(quotes[mood])
    st.markdown(f"### Your {mood} quote:")
    st.markdown(f"<p style='font-size:22px; font-style: italic; color:#333;'>{quote}</p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color:gray;'>✨ Made with 💖 by <b>Javeria</b></p>", unsafe_allow_html=True)
