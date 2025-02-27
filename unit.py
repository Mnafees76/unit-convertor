import streamlit as st

# Constants and conversion functions
def distance_converter(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    return value * units[from_unit] / units[to_unit]

def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

def weight_converter(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    return value * units[from_unit] / units[to_unit]

def pressure_converter(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    return value * units[from_unit] / units[to_unit]

# Streamlit UI Configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS for modern and attractive styling
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .stSelectbox, .stNumberInput {
            margin-bottom: 20px;
        }
        .stSelectbox>div>div>select, .stNumberInput>div>div>input {
            border-radius: 12px !important;
            padding: 10px !important;
            font-size: 16px !important;
        }
        .stButton>button {
            background-color: #3498db !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 12px 24px !important;
            font-size: 18px !important;
            font-weight: bold !important;
            transition: all 0.3s ease;
            border: none !important;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #2980b9 !important;
            transform: scale(1.05);
        }
        .stSuccess {
            background-color: #2ecc71 !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 15px !important;
            font-size: 18px !important;
            text-align: center;
            margin-top: 20px;
        }
        .stWarning {
            background-color: #e67e22 !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 15px !important;
            font-size: 18px !important;
            text-align: center;
            margin-top: 20px;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            color: #7f8c8d;
            font-size: 14px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown("<h1>🔄 Unit Converter</h1>", unsafe_allow_html=True)

# Category Selection
category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

# Converter Mapping
converters = {
    "Distance": (distance_converter, ["Meters", "Kilometers", "Feet", "Miles"]),
    "Temperature": (temperature_converter, ["Celsius", "Fahrenheit"]),
    "Weight": (weight_converter, ["Kilograms", "Grams", "Pounds", "Ounces"]),
    "Pressure": (pressure_converter, ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
}

# Get Converter Function and Units
converter_func, units = converters[category]
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Convert Button
if st.button("Convert", use_container_width=True):
    if from_unit == to_unit:
        st.warning("Please select different units for conversion.")
    else:
        result = converter_func(from_unit, to_unit, value)
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

# Footer
st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)  