
import pickle
import streamlit as st

# Loading the saved models
diabetes_model = pickle.load(open("./models/diabetes_model_new.sav", 'rb'))
heart_model = pickle.load(open("./models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("./models/parkinsons_model.sav", 'rb'))
breast_model = pickle.load(open("./models/breast_cancer_model.sav", 'rb'))

# Top navigation bar
selected = st.selectbox('Choose Disease', 
                        ['Heart Disease Prediction',
                         'Diabetes Prediction',
                         'Parkinson\'s Prediction',
                         'Breast Cancer Prediction'])

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction': 
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    # Input fields
    st.write("Please enter the following details:")
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 1 = normal; 2 = fixed defect; 3 = reversible defect')
    
    # Prediction button
    if st.button('Heart Disease Test Result'):
        if not all([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            st.warning("Please fill in all the fields.")
        else:
            heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            if heart_prediction[0] == 1:
                st.success('The person has a heart disease')
            else:
                st.success('The person does not have any heart disease')

# Diabetes Prediction Page
elif selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')
    
    # Input fields
    st.write("Please enter the following details:")
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    # Prediction button
    if st.button('Diabetes Test Result'):
        if not all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            st.warning("Please fill in all the fields.")
        else:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if diab_prediction[0] == 1:
                st.success('The person is diabetic')
            else:
                st.success('The person is not diabetic')

# Parkinson's Prediction Page
elif selected == 'Parkinson\'s Prediction':
    # Page title
    st.title("Parkinson's Disease Prediction using ML")
    
    # Input fields
    st.write("Please enter the following details:")
    fo = st.text_input('MDVP: Fo(Hz)')
    fhi = st.text_input('MDVP: Fhi(Hz)')
    flo = st.text_input('MDVP: Flo(Hz)')
    Jitter_percent = st.text_input('MDVP: Jitter(%)')
    Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
    RAP = st.text_input('MDVP: RAP')
    PPQ = st.text_input('MDVP: PPQ')
    DDP = st.text_input('Jitter: DDP')
    Shimmer = st.text_input('MDVP: Shimmer')
    Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
    APQ3 = st.text_input('Shimmer: APQ3')
    APQ5 = st.text_input('Shimmer: APQ5')
    APQ = st.text_input('MDVP: APQ')
    DDA = st.text_input('Shimmer: DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')
    
    # Prediction button
    if st.button("Parkinson's Test Result"):
        if not all([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
            st.warning("Please fill in all the fields.")
        else:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
            if parkinsons_prediction[0] == 1:
                st.success("The person has Parkinson's disease")
            else:
                st.success("The person does not have Parkinson's disease")

# Breast Cancer Prediction Page
elif selected == 'Breast Cancer Prediction':
    # Page title
    st.title('Breast Cancer Prediction using ML')
    
    # Input fields
    st.write("Please enter the following details:")
    mean_radius = st.text_input('Mean Radius')
    mean_texture = st.text_input('Mean Texture')
    mean_perimeter = st.text_input('Mean Perimeter')
    mean_area = st.text_input('Mean Area')
    mean_smoothness = st.text_input('Mean Smoothness')
    mean_compactness = st.text_input('Mean Compactness')
    mean_concavity = st.text_input('Mean Concavity')
