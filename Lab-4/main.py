import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Generate a Random Dataset ---
def generate_random_sensor_data(num_entries=1000, start_date='2025-06-01', end_date='2025-06-30'):

    # Generate random timestamps
    start_ts = pd.to_datetime(start_date)
    end_ts = pd.to_datetime(end_date)
    time_range = (end_ts - start_ts).total_seconds()
    random_seconds = np.random.rand(num_entries) * time_range
    timestamps = [start_ts + pd.to_timedelta(s, unit='s') for s in random_seconds]

    # Generate random user_ids
    user_ids = np.random.randint(100, 150, num_entries) # 50 unique users

    # Generate random actions
    actions = np.random.choice(['click', 'view', 'submit', 'scroll', 'purchase', 'login'], num_entries, p=[0.3, 0.25, 0.15, 0.1, 0.1, 0.1])

    # Generate random time_spent
    time_spent = np.random.randint(5, 600, num_entries) # Time spent between 5 seconds and 10 minutes

    # Generate random error_flag with some NaNs
    error_flag = np.random.choice([0, 1, np.nan], num_entries, p=[0.7, 0.2, 0.1])

    data = {
        'timestamp': timestamps,
        'user_id': user_ids,
        'action': actions,
        'time_spent': time_spent,
        'error_flag': error_flag
    }

    df = pd.DataFrame(data)
    df = df.sort_values(by='timestamp').reset_index(drop=True)
    return df

df_sensor = generate_random_sensor_data(num_entries=10000, start_date='2025-06-01', end_date='2025-06-23')

# Convert 'timestamp' to datetime and sort (already done in generation, but good for consistency)
df_sensor['timestamp'] = pd.to_datetime(df_sensor['timestamp'])
df_sensor = df_sensor.sort_values(by='timestamp')
print("-----Sensor Data Sample-----")
print(df_sensor.head())

# Check missing values
print("\n-----Missing Values in Sensor Data-----")
print(df_sensor.isnull().sum())

# Handling missing values for 'error_flag' by filling missing with 0
df_sensor['error_flag'] = df_sensor['error_flag'].fillna(0)
print("\n-----Missing Values After Handling-----")
print(df_sensor.isnull().sum())

# --- Data Visualization ---

# Plot distribution of 'time_spent'
plt.figure(figsize=(10, 5))
sns.boxplot(x=df_sensor['time_spent'], color='purple')
plt.title('Boxplot of Time Spent')
plt.xlabel('Time Spent (seconds)')
plt.show()

# Bar plot for each type of 'action'
plt.figure(figsize=(10, 5))
sns.countplot(x='action', data=df_sensor, palette='Set2', order=df_sensor['action'].value_counts().index)
plt.title('Count of Each Action')
plt.xlabel('Action')
plt.ylabel('Count')
plt.show()

# Feature Engineering: Calculate error_rate per day
df_sensor['date'] = df_sensor['timestamp'].dt.date
error_rate = df_sensor.groupby('date')['error_flag'].mean().reset_index()

# Line plot for error_rate trend over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='error_flag', data=error_rate, marker='o')
plt.title('Daily Error Rate Trend')
plt.xlabel('Date')
plt.ylabel('Average Error Rate')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
