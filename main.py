import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

## streamlit
st.title('March Patient Report')

## data
df = pd.read_csv('Patients_Seen.csv')

## label for tab
st.write('Patient Analytics for March')
    
# pie chart of patients seen / not seen in March
labels = ['Seen in March', 'Not Seen in March']

sizes = [
    (df['Patient_Seen'] == "Yes").sum(),
    (df['Patient_Seen'] == "No").sum()
]

fig1, ax1 = plt.subplots()
colors = ['#2ecc71', '#e74c3c']
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')

annotation_text = "\n".join([f"{label}: {size}" for label, size in zip(labels, sizes)])

ax1.text(
    0.5, -0.1,
    annotation_text,
    ha='center',
    va='top',
    transform=ax1.transAxes
)

st.pyplot(fig1)

## bar chart of appointment types for patients seen in March
seen_march_df = df[df['Patient_Seen'] == "Yes"]

st.subheader('Appointment Types for Patients Seen in March')
appt_counts = seen_march_df['Appt_Type'].value_counts().reset_index()
appt_counts.columns = ['Appt_Type', 'Count']
fig2 = px.bar(appt_counts, x='Appt_Type', y='Count', color='Appt_Type', title='Appointment Types for Patients Seen in March')
st.plotly_chart(fig2)

## list of patients whose appt type was "No Show" from whole dataset
st.subheader('Patients with "No Show" Appointment Type')
no_show_df = df[df['Appt_Type'] == "No Show"]
no_show_df = no_show_df[['First_Name', 'Last_Name', 'MBI', 'Date_Seen']]
st.dataframe(no_show_df)