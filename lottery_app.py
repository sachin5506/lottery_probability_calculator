import streamlit as st
import pandas as pd
import numpy as np
from math import comb

# Load the lottery dataset
@st.cache
def load_data():
    # Replace 'lottery.csv' with the path to your dataset
    data = pd.read_csv('649.csv')
    return data

# Function to calculate single ticket probability
def one_ticket_probability(user_numbers):
    n_combinations = comb(49, 6)
    probability = 1 / n_combinations
    percentage_form = probability * 100
    
    st.write(f"Your chances to win the big prize with the numbers {user_numbers} are {percentage_form:.7f}%.")
    st.write(f"In other words, you have a 1 in {n_combinations:,} chances to win.")

# Function to check historical occurrences
def check_historical_occurrence(user_numbers, data):
    occurrences = data[(data['Number1'] == user_numbers[0]) &
                       (data['Number2'] == user_numbers[1]) &
                       (data['Number3'] == user_numbers[2]) &
                       (data['Number4'] == user_numbers[3]) &
                       (data['Number5'] == user_numbers[4]) &
                       (data['Number6'] == user_numbers[5])]
    
    if not occurrences.empty:
        st.write("Your numbers have appeared in the past!")
    else:
        st.write("Your numbers have never appeared in historical data.")

# Function to calculate probability for multiple tickets
def multi_ticket_probability(n_tickets):
    n_combinations = comb(49, 6)
    probability = n_tickets / n_combinations
    percentage_form = probability * 100
    
    st.write(f"With {n_tickets} tickets, your chances to win the big prize are {percentage_form:.7f}%.")
    st.write(f"In other words, you have a 1 in {n_combinations / n_tickets:.0f} chances to win.")

# Streamlit app structure
def main():
    st.title("Lottery Probability Calculator")

    st.header("1. Single Ticket Probability")
    user_input = st.text_input("Enter your 6 lottery numbers separated by commas (e.g., 1, 2, 3, 4, 5, 6)")
    
    if user_input:
        user_numbers = list(map(int, user_input.split(',')))
        if len(user_numbers) == 6:
            one_ticket_probability(user_numbers)
        else:
            st.write("Please enter exactly 6 numbers.")

    st.header("2. Check Historical Occurrence")
    data = load_data()
    check_button = st.button("Check if your numbers appeared before")
    
    if check_button and user_input:
        check_historical_occurrence(user_numbers, data)

    st.header("3. Probability for Multiple Tickets")
    n_tickets = st.number_input("Enter the number of tickets you want to buy:", min_value=1, step=1)
    if n_tickets:
        multi_ticket_probability(n_tickets)

if __name__ == "__main__":
    main()
