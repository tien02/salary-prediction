import matplotlib.pyplot as plt
from config import config
import streamlit as st
import seaborn as sns
from dataset import load_df

def change_country_name(name):
    if name == "United Kingdom of Great Britain and Northern Ireland":
        return "UK"
    
    if name == "United States of America":
        return "US"
    return name

st.cache()
def load():
    df = load_df()
    df["Country"] = df["Country"].apply(change_country_name)
    return df

def plot_age(df):
    age = df["Age"].value_counts()
    age_df = age.to_frame()
    labels = age.index
    values = age.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=age_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

st.cache()
def plot_remotework(df):
    remotework = df["RemoteWork"].value_counts()
    remotework_df = remotework.to_frame()
    labels = remotework.index
    values = remotework.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=remotework_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

st.cache()
def plot_edlevel(df):
    edlevel = df["EdLevel"].value_counts()
    edlevel_df = edlevel.to_frame()
    labels = edlevel.index
    values = edlevel.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=edlevel_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

st.cache()
def plot_country(df):
    country = df["Country"].value_counts()
    country_df = country.to_frame()
    labels = country.index
    values = country.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=country_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

st.cache()
def plot_yearscodepro(df):
    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="YearsCodePro", hue="EdLevel", kde=True, bins=30)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="YearsCodePro", hue="RemoteWork", kde=True, bins=30)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

def plot_devtype(df):
    type = df[config.TYPES]
    type_sum = type.sum().sort_values(ascending=False)
    type_df = type_sum.to_frame()

    labels = type_sum.index
    values = type_sum.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=type_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

def plot_programlang(df):
    lang = df[config.LANGUAGE]
    lang_sum = lang.sum().sort_values(ascending=False)
    lang_df = lang_sum.to_frame()

    labels = lang_sum.index
    values = lang_sum.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=lang_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

def plot_platform(df): 
    platform = df[config.PLATFORM]
    platform_sum = platform.sum().sort_values(ascending=False)
    platform_df = platform_sum.to_frame()

    labels = platform_sum.index
    values = platform_sum.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=platform_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

def plot_tools(df):
    tools = df[config.TOOLS]
    tools_sum = tools.sum().sort_values(ascending=False)
    tools_df = tools_sum.to_frame()

    labels = tools_sum.index
    values = tools_sum.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=tools_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

def plot_salary(df):
    fig = plt.figure(figsize=(9, 7))
    ax = sns.boxplot(data=df, x="Country", y="Salary")
    plt.xticks(rotation=90)
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="Salary", hue="EdLevel", kde=True)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="Salary", hue="Age", kde=True)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="Salary", hue="RemoteWork", kde=True)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

def visual_page():
    df = load()
    st.header("Data Visualization :bar_chart:")
    st.write("Visualize Stack Overflow Annual Survey 2022 processed")
    
    st.markdown("## Age :birthday:")
    plot_age(df)

    st.markdown("## Remote Work :airplane_departure:")
    plot_remotework(df)

    st.markdown("## Education Level :female-teacher:")
    plot_edlevel(df)

    st.markdown("## Country :flag-vn:")
    plot_country(df)

    st.markdown("## Years of Experience :calendar:")
    plot_yearscodepro(df)
    
    st.markdown("## Developer Type :computer:")
    plot_devtype(df)

    st.markdown("## Programming Language :snake:")
    plot_programlang(df)

    st.markdown("## Platform :cloud:")
    plot_platform(df)

    st.markdown("## Tools :whale:")
    plot_tools(df)

    st.markdown("## Salary :money_with_wings:")
    plot_salary(df)