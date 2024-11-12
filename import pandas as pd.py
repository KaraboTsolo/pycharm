import pandas as pd

# Load your data
file_path = r'C:\Users\Capaciti\Documents\StudentPerformanceFactors.xlsx'
df = pd.read_excel(file_path)

# Display initial columns and data types
print("Original Columns:", df.columns.tolist())
print("Initial Data:\n", df.head())

#Drop Irrelevant Columns
# Define a list of columns that you find irrelevant
columns_to_drop = ['distance_from_home', 'physical_activity']
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

#Filter Out Irrelevant Rows
exam_score_column = 'exam_score'
school_type_column = 'school_type' 
hours_studied_column = 'hours_studied' 

# Ensure these columns exist before applying filters to prevent KeyErrors
if exam_score_column in df.columns:
    df = df[df[exam_score_column].notna()]

if school_type_column in df.columns:
    df = df[df[school_type_column].isin(['Public', 'Private'])]

if hours_studied_column in df.columns:
    df = df[df[hours_studied_column] <= 100]

# Reset index after filtering
df.reset_index(drop=True, inplace=True)

# Display cleaned DataFrame
print("\nCleaned Data with Irrelevant Data Removed:")
print(df.head())
print("Remaining Columns:", df.columns.tolist())
