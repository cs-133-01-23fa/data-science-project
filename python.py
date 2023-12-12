import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path1 = 'Data/modified_dataset.csv'
file_path2 = 'Data/School Shootings USA - export-e539e0ac-0abf-4be7-a200-61ce9fdec074.csv'
# Initialize combined_df to None
combined_df = None
# Load the datasets
try:
    df1 = pd.read_csv(file_path1)
    print("df1 loaded successfully")
except Exception as e:
    print("Error reading file 1:", e)
    df1 = None

try:
    df2 = pd.read_csv(file_path2)
    print("df2 loaded successfully")
except Exception as e:
    print("Error reading file 2:", e)
    df2 = None

# Check if df1 and df2 are DataFrames and print their first few rows
if isinstance(df1, pd.DataFrame):
    print("df1 is a DataFrame.")
    print(df1.head())
else:
    print("df1 is not a DataFrame.")

if isinstance(df2, pd.DataFrame):
    print("df2 is a DataFrame.")
    print(df2.head())
else:
    print("df2 is not a DataFrame.")


# Data Cleaning and Standardization
if df1 is not None and df2 is not None:
    # Standardizing Date Format in df2 (if 'Incident Date' column exists)
    if 'Incident Date' in df2.columns:
        try:
            df2['Incident Date'] = pd.to_datetime(df2['Incident Date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
        except Exception as e:
            print("Error in date conversion:", e)

    # Ensure the same number of columns in df1 and df2 before renaming
    if len(df1.columns) == len(df2.columns):
        df2.columns = df1.columns
    else:
        print("Column length mismatch between df1 and df2")

    # Merging the datasets
    combined_df = pd.concat([df1, df2], ignore_index=True)

    # Convert 'Incident Date' to datetime for analysis
    if 'Incident Date' in combined_df.columns:
        combined_df['Incident Date'] = pd.to_datetime(combined_df['Incident Date'])


# Data Analysis and Visualization
if combined_df is not None:
    # Grouping data by year for trend analysis
    combined_df['Year'] = combined_df['Incident Date'].dt.year
    yearly_counts = combined_df.groupby('Year').size()

    # Plotting the trend over time
    plt.figure(figsize=(12, 6))
    yearly_counts.plot(kind='line', marker='o', color='b', linestyle='-')
    plt.title('School shootings in America over time')
    plt.xlabel('Year')
    plt.ylabel('Number of Shootings')
    plt.grid(True)
    plt.show()

    # Grouping data by state
    if 'State' in combined_df.columns:
        state_counts = combined_df.groupby('State').size().sort_values(ascending=False)

        # Plotting the number of incidents in each state
        plt.figure(figsize=(15, 8))
        state_counts.plot(kind='bar', color='skyblue')
        plt.title('Number of School Shootings by state')
        plt.xlabel('State')
        plt.ylabel('Number of Shootings')
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        plt.show()

# Calculating overall impact in terms of victims
total_killed = combined_df['Victims Killed'].sum()
total_injured = combined_df['Victims Injured'].sum()

# Visualizing the overall impact
labels = ['Victims Killed', 'Victims Injured']
values = [total_killed, total_injured]

plt.figure(figsize=(7, 7))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'gold'])
plt.title('Overall Impact: Victims Killed vs Injured in School Shootings')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

total_killed, total_injured

# Aggregating data by state for killed and injured victims
statewise_killed = combined_df.groupby('State')['Victims Killed'].sum().sort_values(ascending=False)
statewise_injured = combined_df.groupby('State')['Victims Injured'].sum().sort_values(ascending=False)

# Plotting the statewise impact
plt.figure(figsize=(15, 8))

# Creating a bar plot for victims killed
plt.subplot(1, 2, 1)
statewise_killed.plot(kind='bar', color='lightcoral')
plt.title('Victims Killed by State')
plt.xlabel('State')
plt.ylabel('Number of Victims Killed')
plt.xticks(rotation=90)

# Creating a bar plot for victims injured
plt.subplot(1, 2, 2)
statewise_injured.plot(kind='bar', color='gold')
plt.title('Victims Injured by State')
plt.xlabel('State')
plt.ylabel('Number of Victims Injured')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()
# Grouping data by year for killed and injured victims
yearly_killed = combined_df.groupby('Year')['Victims Killed'].sum()
yearly_injured = combined_df.groupby('Year')['Victims Injured'].sum()

# Plotting the temporal impact
plt.figure(figsize=(12, 6))

# Line plot for victims killed
plt.plot(yearly_killed, label='Victims Killed', color='lightcoral', marker='o')

# Line plot for victims injured
plt.plot(yearly_injured, label='Victims Injured', color='gold', marker='x')

plt.title('Yearly Trend of Victims (Killed and Injured) in School Shootings')
plt.xlabel('Year')
plt.ylabel('Number of Victims')
plt.legend()
plt.grid(True)
plt.show()


    
   

