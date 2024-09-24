import streamlit as st
from joblib import load
import numpy as np
import warnings

# Load the trained Random Forest model
model = load(
    r"C:\Users\USER\OneDrive\Desktop\capston project\random_forest_model.joblib"
)

# Create a Streamlit app
st.title("Allen Solly Monthly Sales Prediction Dashboard")

# Input fields for feature values on the main screen
st.header("ALLENSOLLY Monthly Sales Prediction")

# New input fields for Month and Year
Month = st.number_input("Month", min_value=1, max_value=12, value=1)
Year = st.number_input("Year", min_value=2000, max_value=2100, value=2024)

MRP = st.number_input("MRP", min_value=0, max_value=7999, value=1)
Salesman = st.selectbox(
    "Choose Salesman",
    (
        "ANCY SOBY",
        "Benson Yohannan",
        "MOSES GODWIN",
        "Priyan",
        "Muhammed Shiras BS",
        "SANGEETH S",
        "Vishnu S",
        "Arun Kumar S R",
        "AS-ECOM",
        "Sudheesh",
    ),
)
Class_Name = st.selectbox(
    "Category",
    (
        "Shirt",
        "Trouser",
        "T Shirt",
        "Jeans",
        "Kids Shirt",
        "Blazer",
        "Kids T Shirt",
        "Top",
        "Kids Dress",
        "Kids Jeans",
    ),
)
Transaction_Type = st.selectbox("Sales and Return", ("Sales", "Returns"))
Stock_No = st.text_input("Stock Number", value="Enter Stock Number")
Style_Code = st.text_input("Style Code", value="Enter Style Code")
SGST_Value = st.number_input("SGST Value", min_value=0.0, max_value=1000.0, value=0.0)
CGST_Value = st.number_input("CGST Value", min_value=0.0, max_value=1000.0, value=0.0)

# Map input values to numeric (if label encoding is required)
label_mapping = {
    "ANCY SOBY": 0,
    "Benson Yohannan": 1,
    "MOSES GODWIN": 2,
    "Muhammed Shiras BS": 3,
    "Priyan": 4,
    "SANGEETH S": 5,
    "Vishnu S": 6,
    "Arun Kumar S R": 7,
    "AS-ECOM": 8,
    "Sudheesh": 9,
    "Shirt": 0,
    "Trouser": 1,
    "T Shirt": 2,
    "Jeans": 3,
    "Kids Shirt": 4,
    "Blazer": 5,
    "Kids T Shirt": 6,
    "Top": 7,
    "Kids Dress": 8,
    "Kids Jeans": 9,
    "Sales": 0,
    "Returns": 1,
}

# Apply the label mapping to categorical inputs
Salesman = label_mapping.get(Salesman, 0)
Class_Name = label_mapping.get(Class_Name, 0)
Transaction_Type = label_mapping.get(Transaction_Type, 0)

# Convert Stock_No and Style_Code to integers or apply some encoding (e.g., hash encoding)
try:
    Stock_No = int(Stock_No)
    Style_Code = int(
        hash(Style_Code) % 10**8
    )  # This is one way to convert strings to integers
except ValueError:
    st.error(
        "Invalid input for Stock Number or Style Code. Please enter valid numbers."
    )

# Prepare the input for prediction
input_data = np.array(
    [
        [
            Month,  # Added Month
            Year,  # Added Year
            Transaction_Type,
            Salesman,
            Stock_No,
            Class_Name,
            Style_Code,
            MRP,
            SGST_Value,
            CGST_Value,
        ]
    ]
)

# Debugging: Print input data
st.write("Input Data:", input_data)

# Make a prediction using the model
try:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="X does not have valid feature names")
        prediction = model.predict(input_data)

    # Calculate sales value
    predicted_units = prediction[0]
    sales_value = predicted_units * MRP

    # Display the prediction result on the main screen
    st.header("Prediction Result")
    st.success(f"Predicted Sales: {predicted_units:.2f} units")
    st.success(f"Total Sales Value: ₹{sales_value:.2f}")

except Exception as e:
    st.error(f"An error occurred: {e}")
