# Importing Libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Displaying Title
st.title("Dashboard for Scientist")

# Drag and Drop File For User
CSV_data = st.file_uploader("Upload CSV File", type=["csv"])
# ChatGPT Generated Code For Handling None Value of Variable CSV_data
if CSV_data is None:
    st.info("Please upload a CSV file to continue.")
    st.stop()

# Reading CSV File
Diabetes_df = pd.read_csv(CSV_data)
st.dataframe(Diabetes_df.head())

# Displaying Shape: (Rows and Columns)
st.text("Number of Rows:")
st.write(Diabetes_df.shape[0])
st.text("Number of Columns")
st.write(Diabetes_df.shape[1])
st.text("Overall Shape")
st.write(Diabetes_df.shape)

# Displaying Data Types of All Columns
st.text("All Coloumns and their Data Types : ")
st.dataframe(Diabetes_df.dtypes)

# Displaying NULL Values
st.text("Total NUll Values: ")
st.write(Diabetes_df.isnull().sum().sum())
st.text("Column Wise Null Values Are: ")
st.dataframe(Diabetes_df.isnull().sum())
st.text("Basic Statistics for Numerical Colums: ")

# Basic Statistics For All Column
st.dataframe(Diabetes_df.describe())

# Outlier Detection For A User Selected Column
st.text("Box Plot for Outlier Detection: Enter Column Name")
column_for_outlier_detection = st.text_input("Enter column name")
# ChatGPT Generated Code For Handling None Value of  Variable column_for_outlier_detection
if column_for_outlier_detection:  # only runs if not empty
    if column_for_outlier_detection in Diabetes_df.columns:
        fig, ax = plt.subplots()
        sns.boxenplot(Diabetes_df[column_for_outlier_detection])
        st.pyplot(fig)

    else:
        st.warning("❌ Column not found. Please enter a valid column name.")
else:
    st.info("👆 Please enter a column name to generate the boxplot.")

# Correlation Matrix and Graph For Whole Dataset
st.text("Correlations on Your dataset: ")
st.dataframe(Diabetes_df.corr())
fig2, ax = plt.subplots()
sns.heatmap(Diabetes_df.corr(), cmap="YlGnBu", annot=True)
st.pyplot(fig2)

# Histogram Generation For User Selected Column
st.text("Historgam for Distribtution: Enter Column Name")
histogram_Column = st.text_input("Enter Column Name for Histogram Visualization")
# ChatGPT Generated Code For Handling None Value of  Variable histogram_Column
if histogram_Column:  # only runs if not empty
    if histogram_Column in Diabetes_df.columns:
        fig3, ax = plt.subplots()
        hist = Diabetes_df[histogram_Column].hist(bins=8)
        st.pyplot(fig3)

    else:
        st.warning("❌ Column not found. Please enter a valid column name.")

else:
    st.info("👆 Please enter a column name to generate the Histogram.")
