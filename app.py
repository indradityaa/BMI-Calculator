import streamlit as st

st.title("BMI Calculator")

name = st.text_input("Enter your name:")
weight = st.number_input("Enter your weight in kg:", min_value=0.0, step=0.1)
height = st.number_input("Enter your height in meters:", min_value=0.0, step=0.01)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = round(weight / (height ** 2), 2)
        st.write(f"Your BMI is: {bmi}")

        if bmi > 0:
            if bmi < 18.5:
                st.write(f"{name}, you are underweight.")
            elif bmi <= 24.9:
                st.write(f"{name}, you have a normal weight.")
            elif bmi <= 29.9:
                st.write(f"{name}, you are overweight.")
            elif bmi <= 34.9:
                st.write(f"{name}, you are obese.")
            elif bmi <= 39.9:
                st.write(f"{name}, you are severely obese.")
            else:
                st.write(f"{name}, you are morbidly obese.")
        else:
            st.write("Invalid BMI calculated.")
    else:
        st.write("Please enter valid weight and height.")