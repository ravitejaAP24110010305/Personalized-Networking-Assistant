# frontend/streamlit_app.py

import streamlit as st
import requests
import json
from pathlib import Path
import sys

# Add root project directory to Python path to import app modules
sys.path.append(str(Path(__file__).resolve().parent.parent))
from app.services import feedback_logger

# Backend base URL
BASE_URL = "http://127.0.0.1:8000"

st.title("🤝 Personalized Networking Assistant")
st.markdown("Generate conversation starters for networking events based on your interests.")

# --- INPUT SECTION ---
event_description = st.text_area("📝 Enter Event Description")
user_interests = st.text_input("🎯 Your Interests (comma-separated)")

if st.button("Generate Conversation Starters"):
    if event_description and user_interests:
        payload = {
            "description": event_description,
            "interests": [i.strip() for i in user_interests.split(",")]
        }
        
        response = requests.post(f"{BASE_URL}/generate-conversation", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            # Store results in session state to persist after button clicks
            st.session_state["topics"] = data["topics"]
            st.session_state["suggestions"] = data["suggestions"]
        else:
            st.error("Failed to generate conversation starters.")
    else:
        st.warning("Please enter both description and interests.")
        
        # --- DISPLAY RESULTS + FEEDBACK ---
if "suggestions" in st.session_state:
    st.subheader("🔍 Extracted Topics:")
    st.write(st.session_state["topics"])
    
    st.subheader("💬 Conversation Starters:")
    for i, suggestion in enumerate(st.session_state["suggestions"]):
        st.markdown(f"- {suggestion}")
        
        # Create a 2-column layout for feedback buttons
        coll, col2 = st.columns([1, 1])
        
        with coll:
            if st.button("👍", key=f"like_{i}"):
                feedback_logger.log_feedback(suggestion, "like")
                st.success("Thanks for the feedback!")
                
        with col2:
            if st.button("👎", key=f"dislike_{i}"):
                feedback_logger.log_feedback(suggestion, "dislike")
                st.info("Feedback noted.")
                
                # --- FACT CHECK SECTION ---
st.markdown("---")
st.subheader("🔍 Quick Fact-Check")

query = st.text_input("Enter a topic to fact-check")

if st.button("Fact Check"):
    if query:
        response = requests.post(f"{BASE_URL}/fact-check", json={"query": query})
        if response.status_code == 200:
            st.success(response.json()["summary"])
        else:
            st.error("Fact-checking failed.")
            
            # --- CONVERSATION HISTORY ---
st.markdown("---")
st.subheader("📜 View Previous Conversations")

if st.button("Show History"):
    history_path = Path("history.json")
    if history_path.exists():
        with open(history_path, "r") as f:
            history = json.load(f)
            for item in reversed(history[-5:]):  # show latest 5
                st.markdown(f"***🕒 {item['timestamp']}***")
                st.write(f"**Event:** {item['description']}")
                st.write(f"**Interests:** {', '.join(item['interests'])}")
                st.write(f"**Topics:** {', '.join(item['topics'])}")
                st.write("**Suggestions:**")
                for s in item["suggestions"]:
                    st.markdown(f"- {s}")
                st.markdown("---")
    else:
        st.info("No history found yet.")
        
        # --- FEEDBACK HISTORY ---
st.markdown("---")
st.subheader("📂 View Feedback History")

feedback_path = Path("feedback.json")

if st.button("Show Feedback"):
    if feedback_path.exists():
        with open(feedback_path, "r") as f:
            feedback_data = json.load(f)
            for item in reversed(feedback_data[-10:]):  # show latest 10
                icon = "👍" if item["feedback"] == "like" else "👎"
                st.markdown(f"{icon} **{item['suggestion']}**")
                st.caption(f"🕒 {item['timestamp']}")
                st.markdown("---")
    else:
        st.info("No feedback submitted yet.")
        
        