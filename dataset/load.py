# Helper function to load data
import pandas as pd
from config import config
from .preprocess import *

feature_list = ["RemoteWork", "EdLevel", "YearsCodePro", "DevType", "LanguageHaveWorkedWith", "PlatformHaveWorkedWith", 
"ToolsTechHaveWorkedWith", "Country", "Age", "ConvertedCompYearly"]

def load_csv():
    data = pd.read_csv(config.DATA_PATH)
    data.drop(["ResponseId"], axis=1, inplace=True)
    return data

def select_feature():
    df = load_csv()
    
    df = df[df["MainBranch"] == "I am a developer by profession"]
    df = df[df["Employment"].isin(["Employed, full-time", 
                "Independent contractor, freelancer, or self-employed", 
                "Employed, full-time;Independent contractor, freelancer, or self-employed"])]

    df = df[config.FEATURE_LIST]
    df = df.rename({
        "ConvertedCompYearly": "Salary"
    }, axis=1)

    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df.drop_duplicates()

    return df

def load_df():
    df = select_feature()

    # Age
    age_index_remove = df[df["Age"].isin(['Under 18 years old','65 years or older', 'Prefer not to say'])].index
    df.drop(age_index_remove, inplace=True)
    df["Age"] = df["Age"].apply(age_process)

    # EdLevel
    df["EdLevel"] = df["EdLevel"].apply(clean_education)

    # DevType
    dev_type = split_multicolumn(df["DevType"])
    dev_type_sum = dev_type.sum().sort_values(ascending=False)
    keep_col = dev_type_sum[dev_type_sum.values >= 900].index
    dev_type = dev_type[keep_col]
    df = pd.concat([df, dev_type], axis=1)
    df.drop(["DevType"], axis=1, inplace=True)

    # Country
    country_map = shorten_categories(df["Country"].value_counts(), 200)
    df["Country"] = df["Country"].map(country_map)

    # YearsCodePro
    df["YearsCodePro"] = df["YearsCodePro"].apply(YearCodeProProcess)

    # LanguageHaveWorkedWith
    language = split_multicolumn(df["LanguageHaveWorkedWith"])
    language_sum = language.sum().sort_values(ascending=False)
    keep_col = language_sum[language_sum.values >= 2000].index
    language = language[keep_col]
    df = pd.concat([df, language], axis=1)
    df.drop(["LanguageHaveWorkedWith"], axis=1, inplace=True)

    # PlatformHaveWorkedWith
    platform = split_multicolumn(df["PlatformHaveWorkedWith"])
    platform_sum = platform.sum().sort_values(ascending=False)
    keep_col = platform_sum[platform_sum.values >= 2000].index
    platform = platform[keep_col]
    df = pd.concat([df, platform], axis=1)
    df.drop(["PlatformHaveWorkedWith"], axis=1, inplace=True)

    # ToolTechHaveWorkedWith
    tool = split_multicolumn(df["ToolsTechHaveWorkedWith"])
    tool_sum = tool.sum().sort_values(ascending=False)
    keep_col = tool_sum[tool_sum.values >= 5000].index
    tool = tool[keep_col]
    df = pd.concat([df, tool], axis=1)
    df.drop(["ToolsTechHaveWorkedWith"], axis=1, inplace=True)

    # Salary
    df = df[df["Salary"] <= 0.3 * 1e6]

    return df
