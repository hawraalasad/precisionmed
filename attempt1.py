import streamlit as st
import pickle

# Set page config for better appearance
st.set_page_config(
    page_title="IGB outcomes prediction model",
    page_icon="🏥",
    layout="centered"
)

# Enhanced Professional UI CSS

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="stApp"] {
        background: #f6fafd !important;
        color: #1e293b !important;
        font-family: 'Inter', sans-serif !important;
    }
    .main {
        background: #fff;
        box-shadow: 0 4px 24px 0 rgba(31, 38, 135, 0.08);
        border-radius: 1.5rem;
        padding: 2.5rem 2rem;
        margin: 2rem auto;
        max-width: 64rem;
        border: 1px solid #e2e8f0;
    }
    h1 {
        font-size: 2.3rem;
        font-weight: 700;
        color: #2563eb;
        text-align: center;
        margin-bottom: 2rem;
        letter-spacing: 0.03em;
    }
    h3, h4, h5 {
        color: #2563eb !important;
        font-weight: 600;
        margin-bottom: 0.7rem;
        letter-spacing: 0.01em;
    }
    .stMarkdown h3, .stMarkdown h4, .stMarkdown h5 {
        color: #2563eb !important;
    }
    .stRadio label, .stSelectbox label, .stNumberInput label {
        color: #2563eb !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        margin-bottom: 0.2rem !important;
        letter-spacing: 0.01em;
        text-transform: none !important;
    }
    .stRadio > div, .stSelectbox > div, .stNumberInput > div {
        background: #f8fafc !important;
        border-radius: 1rem !important;
        box-shadow: 0 1px 6px 0 rgba(56,189,248,0.04);
        border: 1px solid #e2e8f0 !important;
        padding: 1.1rem 1rem !important;
        margin-bottom: 1.1rem !important;
    }
    .stRadio > div > div, .stRadio div[role="radio"] span {
        color: #1e293b !important;
        font-size: 1.05rem !important;
        font-weight: 500 !important;
        opacity: 1 !important;
        text-shadow: none !important;
        background: none !important;
        -webkit-background-clip: unset !important;
        -webkit-text-fill-color: unset !important;
    }
    .stRadio div[role="radio"] span {
        margin-left: 0.5rem !important;
    }
    .stRadio > div > div[data-checked="true"] span {
        color: #2563eb !important;
        font-weight: 700 !important;
    }
    .stRadio > div > div[data-checked="true"] > div {
        background: #2563eb !important;
        border-color: #2563eb !important;
        box-shadow: 0 0 0 2px #c7d2fe !important;
    }
    .stRadio > div > div > div {
        background: #fff !important;
        border: 2px solid #c7d2fe !important;
        border-radius: 50% !important;
        transition: all 200ms ease !important;
    }
    .stRadio > div > div:hover span {
        color: #60a5fa !important;
    }
    .stNumberInput > div > div > input {
        background: #fff !important;
        color: #1e293b !important;
        border: 1.2px solid #cbd5e1 !important;
        border-radius: 0.7rem !important;
        padding: 0.7rem !important;
        font-size: 1.05rem !important;
        font-family: 'Inter', sans-serif !important;
        box-shadow: 0 1px 2px 0 rgba(56,189,248,0.04);
        transition: border 0.2s, box-shadow 0.2s;
    }
    .stNumberInput > div > div > input:focus {
        border: 1.2px solid #2563eb !important;
        box-shadow: 0 0 0 2px #c7d2fe !important;
    }
    .stButton>button {
        width: 100%;
        background: #2563eb;
        color: #fff;
        padding: 1rem;
        border-radius: 0.9rem;
        border: none;
        font-size: 1.1rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        box-shadow: 0 2px 8px 0 rgba(56,189,248,0.08);
        transition: background 0.2s, box-shadow 0.2s, transform 0.2s;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        background: #174ea6;
        transform: translateY(-1px) scale(1.01);
        box-shadow: 0 4px 16px 0 rgba(56,189,248,0.12);
    }
    .stButton>button:disabled {
        background: #cbd5e1;
        color: #64748b;
        cursor: not-allowed;
    }
    div[data-testid="stSuccess"], div[data-testid="stInfo"] {
        background: #f0f9ff !important;
        color: #2563eb !important;
        border: 1.2px solid #c7d2fe !important;
        border-radius: 1rem !important;
        padding: 1.2rem !important;
        margin-top: 1.2rem !important;
        box-shadow: 0 1px 6px 0 rgba(56,189,248,0.06);
        font-size: 1.08rem !important;
        font-weight: 600 !important;
    }
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #c7d2fe, transparent);
        margin: 2rem 0;
    }
    .stMarkdown, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p, .stMarkdown strong, .stMarkdown span, .stMarkdown div {
        color: #1e293b !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Load your model
with open("./xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit app
st.title("IGB Outcomes Prediction Model")
st.markdown("### Enter the following information to get your prediction")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # PCOS input as radio buttons
    st.markdown("#### Clinical Features")
    pcos = st.radio("Do you have PCOS?", ["No", "Yes"], horizontal=True)
    pcos_value = 1 if pcos == "Yes" else 0
    
    # BMI input
    bmi = st.number_input("BMI", min_value=10.0, max_value=100.0, step=0.1,
                         help="Enter your Body Mass Index")

with col2:
    # SNP inputs
    st.markdown("#### Genetic Markers")
    snp08 = st.selectbox("BDNF (Brain-Derived Neurotrophic Factor)", 
                        options=["AA", "GG", "AG"],
                        help="Select BDNF genotype")
    snp08_value = 0 if snp08 == "AA" else (1 if snp08 == "AG" else 2)
    
    snp10 = st.selectbox("TCF7L2 (Transcription Factor 7 Like 2)", 
                        options=["TT", "CC", "TC"],
                        help="Select TCF7L2 genotype")
    snp10_value = 0 if snp10 == "TT" else (1 if snp10 == "TC" else 2)

# Add some spacing
st.markdown("---")

# Predict button
if st.button("Calculate Prediction"):
    # Prepare input as a list of features
    input_features = [[pcos_value, bmi, snp08_value, snp10_value]]
    
    # Make prediction
    prediction = model.predict(input_features)
    
    # Display result with better formatting
    st.markdown("### Prediction Result")
    if prediction[0] == 1:
        st.success("The model predicts a positive outcome: Expected weight loss > 10%")
    else:
        st.info("The model predicts a negative outcome: Expected weight loss ≤ 10%")
