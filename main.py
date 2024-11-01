import streamlit as st
import pandas as pd

# Title and description
st.title("Daily Temperature Data Viewer 📈")
st.write("This app loads and displays daily temperature data from a CSV file.")

# Load data
url = "https://raw.githubusercontent.com/mksong52/2024python_edu/refs/heads/main/daily_temp.csv"
data = pd.read_csv(url)

# Display the data
st.subheader("Daily Temperature Data")
st.write("Below is the data loaded from the CSV file:")
st.dataframe(data)

# Summary statistics
st.subheader("Summary Statistics")
st.write("Basic statistical information about the dataset:")
st.write(data.describe())

# Plotting options
st.subheader("Temperature Data Visualization 📊")
st.write("Visualize temperature data over time.")

# Dropdown menu for columns to plot
columns = data.columns
column_to_plot = st.selectbox("Choose a column to plot:", columns)

# Plot the selected data
st.line_chart(data[column_to_plot])

# Display the first few rows
st.write("Preview of the data:")
st.write(data.head())

