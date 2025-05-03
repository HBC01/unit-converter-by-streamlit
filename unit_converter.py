import streamlit as st
# app setting
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Universal Unit Converter")
st.markdown("Convert between different units with ease. Powered by Python and good vibes! ✨")

# Converter Categories Or choices
category = st.selectbox("Choose a category:", ["📏 Length", "⚖️ Weight", "🌡️ Temperature"])

# Functions which we apply
def convert_length(value, from_unit, to_unit):
    units = {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701}
    return value / units[from_unit] * units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274}
    return value / units[from_unit] * units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Options per category
units_dict = {
    "📏 Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "⚖️ Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "🌡️ Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From Unit:", units_dict[category])
to_unit = st.selectbox("To Unit:", units_dict[category])
value = st.number_input("Enter value to convert:", format="%.4f", step=0.1)

if st.button("🔁 Convert"):
    if category == "📏 Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "⚖️ Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "🌡️ Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    st.success(f"✅ {value} {from_unit} = {round(result, 4)} {to_unit}")
    st.balloons()

# Footer
st.markdown("---")
st.markdown("Made with 🐍 + Streamlit, Created by Hazoor Ahmed  | Keep converting and exploring! 🚀")