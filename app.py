import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
model = joblib.load('thyroid_prediction_model.sav')

# Function to predict thyroid condition
def predict_thyroid(data):
    return model.predict(data)

# Main function for Streamlit app
def main():
    # Title
    st.title('Thyroid Condition Prediction App')

    # Input fields
    age = st.slider('Age', 18, 100, 25)
    sex = st.radio('Gender', ['Male', 'Female'])
    on_thyroxine = st.radio('On Thyroxine', ['No', 'Yes'])
    query_on_thyroxine = st.radio('Query on Thyroxine', ['No', 'Yes'])
    
    on_antithyroid_medication = st.radio('On Antithyroid Medication', ['No', 'Yes'])
    sick = st.radio('Sick', ['No', 'Yes'])
    pregnant = st.radio('Pregnant', ['No', 'Yes'])
    thyroid_surgery = st.radio('Thyroid Surgery', ['No', 'Yes'])
    i131_treatment = st.radio('I131 Treatment', ['No', 'Yes'])
    query_hypothyroid = st.radio('Query Hypothyroid', ['No', 'Yes'])
    query_hyperthyroid = st.radio('Query Hyperthyroid', ['No', 'Yes'])
    lithium = st.radio('Lithium', ['No', 'Yes'])
    goitre = st.radio('Goitre', ['No', 'Yes'])
    tumor = st.radio('Tumor', ['No', 'Yes'])
    hypopituitary = st.number_input('Hypopituitary')
    psych = st.radio('Psych', ['No', 'Yes'])
    tsh_measured = st.radio('TSH Measured', ['No', 'Yes'])
    tsh = st.number_input('TSH')
    t3_measured = st.radio('T3 Measured', ['No', 'Yes'])
    t3 = st.number_input('T3')
    tt4_measured = st.radio('TT4 Measured', ['No', 'Yes'])
    tt4 = st.number_input('TT4')
    t4u_measured = st.radio('T4U Measured', ['No', 'Yes'])
    t4u = st.number_input('T4U')
    fti_measured = st.radio('FTI Measured', ['No', 'Yes'])
    fti = st.number_input('FTI')
    tbg_measured = st.radio('TBG Measured', ['No', 'Yes'])
    tbg = st.number_input('TBG')
    
    referral_source_stmw = st.radio('Referral Source STMW', ['No', 'Yes'])
    referral_source_svhc = st.radio('Referral Source SVHC', ['No', 'Yes'])
    referral_source_svhd = st.radio('Referral Source SVHD', ['No', 'Yes'])
    referral_source_svi = st.radio('Referral Source SVI', ['No', 'Yes'])
    

    # Convert categorical input to numeric
    sex_encoded = 1 if sex == 'Female' else 0
    on_thyroxine_encoded = 1 if on_thyroxine == 'Yes' else 0
    query_on_thyroxine_encoded = 1 if query_on_thyroxine == 'Yes' else 0
    on_antithyroid_medication_encoded = 1 if on_antithyroid_medication == 'Yes' else 0
    sick_encoded = 1 if sick == 'Yes' else 0
    pregnant_encoded = 1 if pregnant == 'Yes' else 0
    thyroid_surgery_encoded = 1 if thyroid_surgery == 'Yes' else 0
    i131_treatment_encoded = 1 if i131_treatment == 'Yes' else 0
    query_hypothyroid_encoded = 1 if query_hypothyroid == 'Yes' else 0
    query_hyperthyroid_encoded = 1 if query_hyperthyroid == 'Yes' else 0
    lithium_encoded = 1 if lithium == 'Yes' else 0
    goitre_encoded = 1 if goitre == 'Yes' else 0
    tumor_encoded = 1 if tumor == 'Yes' else 0
    psych_encoded = 1 if psych == 'Yes' else 0
    tsh_measured_encoded = 1 if tsh_measured == 'Yes' else 0
    t3_measured_encoded = 1 if t3_measured == 'Yes' else 0
    tt4_measured_encoded = 1 if tt4_measured == 'Yes' else 0
    t4u_measured_encoded = 1 if t4u_measured == 'Yes' else 0
    fti_measured_encoded = 1 if fti_measured == 'Yes' else 0
    tbg_measured_encoded = 1 if tbg_measured == 'Yes' else 0
    
    # Prepare input data as DataFrame
    data = {
        'age': age,
        'sex': sex_encoded,
        'on_thyroxine': on_thyroxine_encoded,
        'query_on_thyroxine': query_on_thyroxine_encoded,
        'on_antithyroid_medication': on_antithyroid_medication_encoded,
        'sick': sick_encoded,
        'pregnant': pregnant_encoded,
        'thyroid_surgery': thyroid_surgery_encoded,
        'i131_treatment': i131_treatment_encoded,
        'query_hypothyroid': query_hypothyroid_encoded,
        'query_hyperthyroid': query_hyperthyroid_encoded,
        'lithium': lithium_encoded,
        'goitre': goitre_encoded,
        'tumor': tumor_encoded,
        'hypopituitary': hypopituitary,
        'psych': psych_encoded,
        'tsh_measured': tsh_measured_encoded,
        'tsh': tsh,
        't3_measured': t3_measured_encoded,
        't3': t3,
        'tt4_measured': tt4_measured_encoded,
        'tt4': tt4,
        't4u_measured': t4u_measured_encoded,
        't4u': t4u,
        'fti_measured': fti_measured_encoded,
        'fti': fti,
        'tbg_measured': tbg_measured_encoded,
        'tbg': tbg,
        'referral_source_STMW': 1 if referral_source_stmw == 'Yes' else 0,
        'referral_source_SVHC': 1 if referral_source_svhc == 'Yes' else 0,
        'referral_source_SVHD': 1 if referral_source_svhd == 'Yes' else 0,
        'referral_source_SVI': 1 if referral_source_svi == 'Yes' else 0,
        
    }
    
    # Create a DataFrame from the input data
    data_df = pd.DataFrame(data, index=[0])

    if st.button('Predict'):
        prediction = predict_thyroid(data_df.values)
        # You can customize the output based on your model's prediction
        st.success(f'Predicted Thyroid Condition: {prediction[0]}')

# Run the app
if __name__ == '__main__':
    main()
