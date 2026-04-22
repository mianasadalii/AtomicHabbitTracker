import streamlit as st
from datetime import date

# Page config
st.set_page_config(page_title="Atomic Habit Tracker", page_icon="💪", layout="centered")

# Custom CSS for attractive UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
    }
    .card {
        padding: 15px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">💪 Atomic Habit Tracker</p>', unsafe_allow_html=True)
st.write("Build small habits daily — inspired by Atomic Habits 📘")

# Initialize session state
if "habits" not in st.session_state:
    st.session_state.habits = {}

# Add Habit
st.markdown("### ➕ Add New Habit")
new_habit = st.text_input("Habit Name")

if st.button("Add Habit"):
    if new_habit:
        if new_habit not in st.session_state.habits:
            st.session_state.habits[new_habit] = []
            st.success("Habit added successfully!")
        else:
            st.warning("Habit already exists!")

# Mark Habit Done
st.markdown("### ✅ Mark Habit as Done")
if st.session_state.habits:
    habit_choice = st.selectbox("Select Habit", list(st.session_state.habits.keys()))
    
    if st.button("Mark Done"):
        today = str(date.today())
        if today not in st.session_state.habits[habit_choice]:
            st.session_state.habits[habit_choice].append(today)
            st.success("Marked as completed for today!")
        else:
            st.info("Already marked today!")

# View Habits
st.markdown("### 📊 Your Progress")
if st.session_state.habits:
    for habit, days in st.session_state.habits.items():
        st.markdown(f"""
        <div class="card">
            <h4>{habit}</h4>
            <p>✅ Days Completed: {len(days)}</p>
            <p>📅 Dates: {days}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No habits added yet.")
