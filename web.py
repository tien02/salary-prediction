import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from config import config

LANGUAGE = ['JavaScript', 'HTML/CSS', 'SQL',
       'TypeScript', 'Python', 'Bash/Shell', 'Java', 'C#', 'PHP', 'Go', 'C++',
       'PowerShell', 'C', 'Kotlin', 'Ruby', 'Rust']
PLATFORM = ['AWS', 'Microsoft Azure', 'Google Cloud', 'Firebase', 'Heroku', 'DigitalOcean']
TOOLS = ['Docker', 'npm', 'Homebrew', 'Yarn', 'Kubernetes']
TYPES = ['Developer, full-stack', 'Developer, back-end', 'Developer, front-end',
       'DevOps specialist', 'Cloud infrastructure engineer',
       'Developer, desktop or enterprise applications', 'Developer, mobile',
       'Database administrator', 'Engineering manager', 'System administrator',
       'Engineer, data', 'Project manager', 'Developer, QA or test',
       'Developer, embedded applications or devices', 'Designer',
       'Data scientist or machine learning specialist',
       'Engineer, site reliability']
COLUMNS = ['RemoteWork', 'EdLevel', 'YearsCodePro', 'Country', 'Age',
       'Developer, full-stack', 'Developer, back-end', 'Developer, front-end',
       'DevOps specialist', 'Cloud infrastructure engineer',
       'Developer, desktop or enterprise applications', 'Developer, mobile',
       'Database administrator', 'Engineering manager', 'System administrator',
       'Engineer, data', 'Project manager', 'Developer, QA or test',
       'Developer, embedded applications or devices', 'Designer',
       'Data scientist or machine learning specialist',
       'Engineer, site reliability', 'JavaScript', 'HTML/CSS', 'SQL',
       'TypeScript', 'Python', 'Bash/Shell', 'Java', 'C#', 'PHP', 'Go', 'C++',
       'PowerShell', 'C', 'Kotlin', 'Ruby', 'Rust', 'AWS', 'Microsoft Azure',
       'Google Cloud', 'Firebase', 'Heroku', 'DigitalOcean', 'Docker', 'npm',
       'Homebrew', 'Yarn', 'Kubernetes']


st.cache()
def load_model():
    return joblib.load(config.CKPT_PATH)

if __name__ == "__main__":
    model = load_model()
    st.header("Developer's Salary Prediction 🤔")
    st.write("Predict salary base on developer's skill, position, experience.")

    # RemoteWork
    st.markdown("### On-site/Remote 🛫")
    RemoteWork = st.selectbox("On-site, Remote or Hybrid?", ['Fully remote', 'Hybrid (some remote, some in-person)',
       'Full in-person'], key=1)

    # EdLevel
    st.markdown("### Education Level 👩‍🏫")
    EdLevel = st.selectbox("Select your education level", ['Bachelor’s degree', 'Master’s degree', 'Post grad', 'Less than a Bachelors'], key=2)

    # YearsCodePro
    st.markdown("### Years of experience 📆")
    YearsCodePro = st.slider("Select years of experience", min_value=0, max_value=46, step=1, value=10)
    if YearsCodePro == 0:
        YearsCodePro = 0.5
    YearsCodePro = float(YearsCodePro)

    # Country
    st.markdown("### Country 🇻🇳")
    Country = st.selectbox("Select your country", ['United Kingdom of Great Britain and Northern Ireland',
       'United States of America', 'Other', 'Austria', 'Italy', 'Canada',
       'Germany', 'Poland', 'Israel', 'Netherlands', 'France', 'Spain',
       'Turkey', 'Sweden', 'India', 'Belgium', 'Brazil', 'Switzerland',
       'Australia', 'Portugal', 'Russian Federation', 'Mexico'], key=3)

    # Age
    st.markdown("### Age 🎂")
    Age = st.selectbox("Select your age", ['18-24 years old', '25-34 years old', '35-44 years old', 'Over 45'], key=4)

    # DevType
    st.markdown("### Type of Developer 💻")
    DevType = st.multiselect("You can select multiple position", TYPES)

    types = [0] * len(TYPES)
    if DevType:
        for type in DevType:
            types[TYPES.index(type)] = 1.
    
    # LanguageHaveWorkedWith
    st.markdown("### Programming Language 🐍")
    LanguageHaveWorkedWith = st.multiselect("You can select multiple programming language have worked with", LANGUAGE)

    languages = [0] * len(LANGUAGE)
    if LanguageHaveWorkedWith:
        for language in LanguageHaveWorkedWith:
            languages[LANGUAGE.index(language)] = 1.
    
    # PlatformHaveWorkedWith
    st.markdown("### Platform ☁️")
    PlatformHaveWorkedWith = st.multiselect("You can select multiple platform have worked with", PLATFORM)

    platforms = [0] * len(PLATFORM)
    if PlatformHaveWorkedWith:
        for platform in PlatformHaveWorkedWith:
            platforms[PLATFORM.index(platform)] = 1.

    # ToolsHaveWorkedWith
    st.markdown("### Tools 🐳")
    ToolsTechHaveWorkedWith = st.multiselect("Tools tech have worked with", TOOLS)

    tools = [0] * len(TOOLS)
    if ToolsTechHaveWorkedWith:
        for tool in ToolsTechHaveWorkedWith:
            tools[TOOLS.index(tool)] = 1.

    INPUTS = [RemoteWork] + [EdLevel] + [YearsCodePro] + [Country] + [Age] + types + languages + platforms + tools
    INPUTS = [INPUTS]
    input_df = pd.DataFrame(INPUTS, columns=COLUMNS)

    predict_flag = st.button("Predict")

    if predict_flag:
        pred = model.predict(input_df)
        st.metric("Prediction", str(round(pred[0], 2)) + " $" , )
    
