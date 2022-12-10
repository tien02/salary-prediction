DATA_PATH = "stack-overflow-developer-survey-2022/survey_results_public.csv"
CKPT_PATH = "best_model.joblib"

FEATURE_LIST = ["RemoteWork", "EdLevel", "YearsCodePro", "DevType", "LanguageHaveWorkedWith", "PlatformHaveWorkedWith", 
"ToolsTechHaveWorkedWith",
"Country", "Age", "ConvertedCompYearly"]

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
COUNTRY = ['United Kingdom of Great Britain and Northern Ireland',
       'United States of America', 'Other', 'Austria', 'Italy', 'Canada',
       'Germany', 'Poland', 'Israel', 'Netherlands', 'France', 'Spain',
       'Turkey', 'Sweden', 'India', 'Belgium', 'Brazil', 'Switzerland',
       'Australia', 'Portugal', 'Russian Federation', 'Mexico']