import joblib
import pandas as pd
import streamlit as st
from config import config


st.cache()
def load_model():
    return joblib.load(config.CKPT_PATH)

def predict_page():
    model = load_model()
    st.header("Salary Prediction :thinking_face:")
    st.write("Predict salary base on developer's skill, position, experience.")

    # RemoteWork
    st.markdown("## On-site/Remote :airplane_departure:")
    RemoteWork = st.selectbox("On-site, Remote or Hybrid?", ['Fully remote', 'Hybrid (some remote, some in-person)',
       'Full in-person'], key=1)

    # EdLevel
    st.markdown("## Education Level :female-teacher:")
    EdLevel = st.selectbox("Select your education level", ['Bachelor’s degree', 'Master’s degree', 'Post grad', 'Less than a Bachelors'], key=2)

    # YearsCodePro
    st.markdown("## Years of experience :calendar:")
    YearsCodePro = st.slider("Select years of experience", min_value=0, max_value=46, step=1, value=10)
    if YearsCodePro == 0:
        YearsCodePro = 0.5
    YearsCodePro = float(YearsCodePro)

    # Country
    st.markdown("## Country :flag-vn:")
    Country = st.selectbox("Select your country", config.COUNTRY, key=3)

    # Age
    st.markdown("## Age :birthday:")
    Age = st.selectbox("Select your age", ['18-24 years old', '25-34 years old', '35-44 years old', 'Over 45'], key=4)

    # DevType
    st.markdown("## Type of Developer :computer:")
    DevType = st.multiselect("You can select multiple position", config.TYPES)

    types = [0] * len(config.TYPES)
    if DevType:
        for type in DevType:
            types[config.TYPES.index(type)] = 1.
    
    # LanguageHaveWorkedWith
    st.markdown("## Programming Language :snake:")
    LanguageHaveWorkedWith = st.multiselect("You can select multiple programming language have worked with", config.LANGUAGE)

    languages = [0] * len(config.LANGUAGE)
    if LanguageHaveWorkedWith:
        for language in LanguageHaveWorkedWith:
            languages[config.LANGUAGE.index(language)] = 1.
    
    # PlatformHaveWorkedWith
    st.markdown("## Platform :cloud:")
    PlatformHaveWorkedWith = st.multiselect("You can select multiple platform have worked with", config.PLATFORM)

    platforms = [0] * len(config.PLATFORM)
    if PlatformHaveWorkedWith:
        for platform in PlatformHaveWorkedWith:
            platforms[config.PLATFORM.index(platform)] = 1.

    # ToolsHaveWorkedWith
    st.markdown("## Tools :whale:")
    ToolsTechHaveWorkedWith = st.multiselect("Tools tech have worked with", config.TOOLS)

    tools = [0] * len(config.TOOLS)
    if ToolsTechHaveWorkedWith:
        for tool in ToolsTechHaveWorkedWith:
            tools[config.TOOLS.index(tool)] = 1.

    INPUTS = [RemoteWork] + [EdLevel] + [YearsCodePro] + [Country] + [Age] + types + languages + platforms + tools
    INPUTS = [INPUTS]
    input_df = pd.DataFrame(INPUTS, columns=config.COLUMNS)

    predict_flag = st.button("Predict")

    if predict_flag:
        _, col2, _ = st.columns(3)
        pred = model.predict(input_df)
        with col2:
            st.metric("Prediction", '{:,.3f} $'.format(pred[0]))

    
