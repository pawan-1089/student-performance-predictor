
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📘",
    layout="wide"
)

model = joblib.load("model.pkl")

st.markdown("""
<style>
.stApp {
    background: #f6f8fc;
    color: #172b4d;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: #17365d !important;
}

p, label, .stMarkdown {
    color: #334155;
}

.hero {
    background: linear-gradient(120deg, #17365d, #2563a6);
    padding: 30px;
    border-radius: 18px;
    margin-bottom: 25px;
}

.hero h1 {
    color: white !important;
    font-size: 34px;
    margin-bottom: 8px;
}

.hero p {
    color: #e2eaf5 !important;
    margin-bottom: 0;
}

.panel {
    background: white;
    border: 1px solid #e2e8f0;
    padding: 24px;
    border-radius: 16px;
    margin-bottom: 20px;
}


.result {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 5px solid #16a34a;
    padding: 20px;
    border-radius: 14px;
    margin-top: 18px;
    text-align: center;
}

.result-label {
    font-size: 15px;
    color: #64748b;
}

.result-number {
    font-size: 42px;
    font-weight: 750;
    margin: 8px 0;
}

.result-note {
    font-size: 13px;
    color: #64748b;
}




div.stButton > button {
    background-color: #2563eb !important;
    color: white !important;
    border: none !important;
    border-radius: 8px;
    min-height: 40px;
    width: auto;
    padding: 0.4rem 1.2rem;
    font-size: 15px;
    font-weight: 500;
}

div.stButton > button p {
    color: white !important;
}

div.stButton > button:hover {
    background-color: #1d4ed8 !important;
    color: white !important;
}

div.stButton > button:focus {
    color: white !important;
    box-shadow: 0 0 0 2px #93c5fd;
}


div[data-testid="stExpander"] {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Student Performance Predictor</h1>
    <p>Predict student performance using study habits and previous scores.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Student information")
st.write("Enter the details below to generate a prediction.")

left, right = st.columns(2)

with left:
    st.markdown("### Academic habits")

    hours = st.slider(
        "Hours studied per day",
        min_value=1, max_value=9, value=5
    )
    st.caption("Choose between 1 and 9 hours.")

    previous = st.slider(
        "Previous scores",
        min_value=40, max_value=99, value=70
    )
    st.caption("Choose a score between 40 and 99.")

    papers = st.slider(
        "Practice question papers",
        min_value=0, max_value=9, value=3
    )
    st.caption("Number of sample papers practiced: 0–9.")

with right:
    st.markdown("### Daily routine")

    activity = st.selectbox(
        "Extracurricular activities",
        ["No", "Yes"]
    )
    st.caption("Select whether the student participates in activities.")

    sleep = st.slider(
        "Sleep hours per day",
        min_value=4, max_value=9, value=7
    )
    st.caption("Choose between 4 and 9 hours.")

st.write("")

if st.button("Predict student performance", use_container_width=True):
    student = pd.DataFrame([{
        "Hours Studied": hours,
        "Previous Scores": previous,
        "Extracurricular Activities": 1 if activity == "Yes" else 0,
        "Sleep Hours": sleep,
        "Sample Question Papers Practiced": papers
    }])

    prediction = float(model.predict(student)[0])

    
    threshold = 33
    if prediction >= threshold:
        result_color = "#15803d"
        border_color = "#16a34a"
        status = "Above the reference threshold"
    else:
        result_color = "#dc2626"
        border_color = "#dc2626"
        status = "Below the reference threshold"

    st.markdown(
        '<div class="result" style="border-left: 5px solid '
        + border_color + ';">'
        '<div class="result-label">Predicted Performance Index</div>'
        '<div class="result-number" style="color: '
        + result_color + ';">'
        + str(round(prediction, 2))
        + '</div>'
        '<div style="color: ' + result_color + '; font-weight: 600;">'
        + status + '</div>'
        '<div class="result-label">'
        'Model estimate, not a guaranteed exam score.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    st.caption(
    "Reference threshold: 33. This is an illustrative "
    "benchmark, not an official passing mark."
    )

    
st.markdown("### Input summary")

summary = pd.DataFrame({
    "Student detail": [
        "Hours studied per day",
        "Previous scores",
        "Extracurricular activities",
        "Sleep hours",
        "Practice question papers"
    ],
    "Your input": [
        str(hours),
        str(previous),
        str(activity),
        str(sleep),
        str(papers)
    ]
})

st.dataframe(summary, hide_index=True, width="stretch")

st.write("")


with st.expander("About the model and evaluation"):
    st.write(
        "The app uses a trained Linear Regression model "
        "with five input features."
    )
    st.write(
        "On the grouped test set used in this project, "
        "the reported MAE was 1.600, RMSE was 2.018, "
        "and R² was 0.989."
    )
    st.write(
        "These metrics describe performance on the dataset. "
        "They do not guarantee similar accuracy for real-world students."
    )

st.divider()

st.caption(
    "Student Performance Predictor | Machine Learning Portfolio Project"
)
