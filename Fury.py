import streamlit as st

# Page settings
st.set_page_config(page_title="Medical Report Analyzer", page_icon=" ")

# Title
st.markdown("<h1 style='text-align: center; color: #2E86C1;'> FURY SUGGESTS REPORT </h1>", unsafe_allow_html=True)
st.write("Enter your medical values below:")

# Healthy ranges
healthy = {
    "Hemoglobin": (13, 16.5),
    "Cholesterol": (150, 200),
    "Blood Sugar": (70, 106),
    "thyroxin": (4.87,11.72),
    "Platelets": (150000, 410000),      # per microliter
    "Creatinine": (0.66, 1.25),           # mg/dL
    "Urea": (19.3, 43)                    # mg/dL
}

# Input fields
h = st.number_input("Hemoglobin (g/dL)")
c = st.number_input("Cholesterol (mg/dL)")
b = st.number_input("Blood Sugar (mg/dL)")
t = st.number_input("thyroxin(mg/mL)")
p = st.number_input("Platelets (per microliter)")
cr = st.number_input("Creatinine (mg/dL)")
u = st.number_input("Urea (mg/dL)")

# Button
if st.button("Analyze Report"):

    st.subheader(" Analysis Result")

    values = {
        "Hemoglobin": h,
        "Cholesterol": c,
        "Blood Sugar": b,
        "thyroxin":t,
        "Platelets": p,
        "Creatinine": cr,
        "Urea": u
    }

    for test in values:
        low, high = healthy[test]
        value = values[test]

        if value == 0:
            continue

        if value < low:
            st.error(f"{test} is LOW  Possible Anemia, Lever Problems, Hypoglycemia, Weakness, Dangue Risk.")
        elif value > high:
            st.warning(f"{test} is HIGH Possible Diabetes, Nausea, Clot Formation.")
        else:
            st.success(f"{test} is NORMAL ")

    # Extra Kidney Summary
    if cr > 1.2 or u > 40:
        st.warning("Kidney function may be affected. Please consult a doctor.")
    elif cr != 0 and u != 0:
        st.success("Kidney function appears normal based on given values.")

    st.info("INFO: This is not a medical diagnosis. Please consult a qualified doctor.")