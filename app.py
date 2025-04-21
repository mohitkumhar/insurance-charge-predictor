import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder

model = tf.keras.models.load_model('model.h5')

st.set_page_config(page_title="Insurance Charge Predictor", layout="centered")

st.title("💸 Insurance Charge Predictor")
st.markdown("Enter the details below to predict insurance charges.")

with st.form("input_form"):
    age = st.slider("Age", 18, 100, 25)
    sex = st.selectbox("Sex", ["male", "female"])
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
    children = st.slider("Number of Children", 0, 10, 0)
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])
    submit = st.form_submit_button("Predict 💡")

cat_data = pd.DataFrame([[sex, smoker, region]], columns=['sex', 'smoker', 'region'])

encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoder.fit(pd.DataFrame([
    ['male', 'yes', 'southwest'],
    ['female', 'no', 'southeast'],
    ['male', 'no', 'northwest'],
    ['female', 'yes', 'northeast']
], columns=['sex', 'smoker', 'region']))

if submit:
    try:
        encoded = encoder.transform(cat_data)
        num_data = np.array([[age, bmi, children]])
        final_input = np.concatenate([num_data, encoded], axis=1).astype(np.float32)
        prediction = model.predict(final_input)[0][0]
        st.success(f"💰 Predicted Insurance Charges: **${prediction:.2f}**")
    except Exception as e:
        st.error(f"Error: {e}")
