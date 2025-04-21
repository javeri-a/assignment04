import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter your height (in meters)")
weight = st.number_input("Enter your weight (in kilograms)")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.write("Category: Underweight")
        elif 18.5 <= bmi < 25:
            st.write("Category: Normal weight")
        elif 25 <= bmi < 30:
            st.write("Category: Overweight")
        else:
            st.write("Category: Obesity")
    else:
        st.write("Please enter a valid height.")
