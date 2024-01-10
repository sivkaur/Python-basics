import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Age Insights')

uploadedFile = st.file_uploader("Choose a CSV file", type=["csv"])

if uploadedFile is not None:
    df = pd.read_csv(uploadedFile)
    
    numberOfColumns = df.shape[1]
    
    if numberOfColumns == 2:
        if 'Name' in df.columns and 'Age' in df.columns:
            plt.hist(df['Age'], bins=20, color='green', edgecolor='black')
            plt.xlabel('Age')
            plt.ylabel('Frequency')
            plt.title('Age Distribution')
            st.pyplot(plt)
        else:
            st.error("This file is not valid, please upload a valid file with two columns, i.e, 'Name', 'Age'")
    else:
        st.error("This file is not valid, please upload a valid file with two columns, i.e, 'Name', 'Age'")

