
import streamlit as st
from datetime import datetime, timedelta

# Function to calculate the amount for tractor work
def calculate_tractor_amount(time, price):
    return time * price

# Function to calculate the amount for seeding
def calculate_seeding_amount(acres, price_per_acre):
    return acres * price_per_acre

# Function to calculate the amount for spraying
def calculate_spraying_amount(tanks, price_per_tank):
    return tanks * price_per_tank

# Streamlit Sidebar for Tractor Functions
st.sidebar.title("Tractor Work Calculator")
option = st.sidebar.selectbox(
    "Select Tractor Function",
    ("గుంటుక", "రోటవేటర్‌", "Turning ప్లవ్", "3 ,7, 2 మడకలు", "టిల్లర్", "Bedding", "cross గుంటుక", "Spraying")
)

# Sidebar for Time Type Selection (Tractor Function, Seeding, or Spraying)
time_option = st.sidebar.radio("Select Time Type", ("Define Time", "Calculate Time", "Seeding", "Spraying"))

# Function to input time based on user selection for Tractor Functions
def get_time_input(time_option):
    if time_option == "Define Time":
        hours = st.number_input("Enter Hours", min_value=0, step=1)
        minutes = st.number_input("Enter Minutes", min_value=0, max_value=59, step=1)
        total_time = hours + (minutes / 60)
        return total_time
    elif time_option == "Calculate Time":
        start_time = st.time_input("Enter Start Time")
        end_time = st.time_input("Enter End Time")
        start_time = datetime.combine(datetime.today(), start_time)
        end_time = datetime.combine(datetime.today(), end_time)
        time_diff = (end_time - start_time)
        total_time = time_diff.total_seconds() / 3600
        return total_time
    elif time_option == "Seeding":
        acres = st.number_input("Enter Acres", min_value=0.0, step=0.1)
        price_per_acre = st.number_input("Enter Price per Acre (in currency)", min_value=1.0, step=1.0)
        return acres, price_per_acre
    elif time_option == "Spraying":
        # Allow both float and integer values for tanks
        tanks = st.number_input("Enter Number of Tanks", min_value=0.0, step=0.1)  # Allow float and integer input
        price_per_tank = st.number_input("Enter Price per Tank (in currency)", min_value=1.0, step=1.0)
        return tanks, price_per_tank

# If the user is working on tractor-related tasks
if time_option != "Seeding" and time_option != "Spraying":
    price = st.number_input("Enter Price per Hour (in currency)", min_value=1.0, step=1.0)
    time = get_time_input(time_option)

    if st.button("Calculate Amount"):
        total_amount = calculate_tractor_amount(time, price)
        st.success(f"Total Amount for {option}: ₹{total_amount:.2f}")
        st.balloons()

# If the user is working on Seeding
elif time_option == "Seeding":
    acres, price_per_acre = get_time_input(time_option)

    if st.button("Calculate Seeding Amount"):
        total_amount = calculate_seeding_amount(acres, price_per_acre)
        st.success(f"Total Amount for Seeding {acres} Acres: ₹{total_amount:.2f}")
        st.balloons()

# If the user is working on Spraying
elif time_option == "Spraying":
    tanks, price_per_tank = get_time_input(time_option)

    if st.button("Calculate Spraying Amount"):
        total_amount = calculate_spraying_amount(tanks, price_per_tank)
        st.success(f"Total Amount for Spraying {tanks} Tanks: ₹{total_amount:.2f}")
        st.balloons()

# CSS Customization for Farming UI with Colorful Highlights
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(145deg, #f0e5c9, #6a8d73);
        font-family: 'Arial', sans-serif;
        color: #4a4a4a;
        padding: 20px;
    }

    h1 {
        text-align: center;
        font-size: 36px;
        color: #388e3c;
        margin-bottom: 30px;
    }

    .sidebar .sidebar-content {
        background-color: #4caf50;
        color: white;
        padding: 20px;
        box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }

    .stButton>button {
        background-color: #388e3c;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 20px;
        font-size: 16px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #2c6b2f;
        box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.2);
    }

    .stSelectbox>div>div>input,
    .stNumberInput>div>div>input,
    .stTextInput>div>div>input {
        font-size: 16px;
        padding: 12px;
        border-radius: 8px;
        border: 2px solid #4caf50;
        background-color: #ffffff;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    .stSelectbox>div>div>input:focus,
    .stNumberInput>div>div>input:focus,
    .stTextInput>div>div>input:focus {
        border-color: #388e3c;
        box-shadow: 0px 0px 8px rgba(0, 150, 136, 0.6);
    }

    .stRadio>div>div>div>input {
        background-color: #f1f1f1;
        padding: 8px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    .stRadio>div>div>div>input:hover {
        background-color: #d0e6d5;
    }

    .stRadio>div>div>div>label {
        font-size: 18px;
        color: #388e3c;
    }

    .stTextInput>div>div>label {
        font-size: 16px;
        color: #388e3c;
    }

    .stSelectbox>div>div>label {
        font-size: 16px;
        color: #388e3c;
    }
    </style>
    """, unsafe_allow_html=True
)
