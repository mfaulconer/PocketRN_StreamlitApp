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

st.pyplot(fig1)

## table of patients not seen in March
# Show just first name, last name, and MBI for patients not seen in March
st.subheader('Patients Not Seen in March')
not_seen_df = df[df['Patient_Seen'] == "No"]
not_seen_df = not_seen_df[['First_Name', 'Last_Name', 'MBI']]
page_size = 10
page_number = st.number_input("Page", min_value=1, step=1)
start = (page_number - 1) * page_size
end = start + page_size
st.dataframe(not_seen_df.iloc[start:end])

## table of patients seen in March
# Show first name, last name, MBI, date last seen, and appt type
st.subheader('Patients Seen in March')
seen_df = df[df['Patient_Seen'] == "Yes"]
seen_df = seen_df[['First_Name', 'Last_Name', 'MBI', 'Date_Seen', 'Appt_Type']]
page_size = 10
page_number = st.number_input("Page", min_value=1, step=1, key="seen_page")
start = (page_number - 1) * page_size
end = start + page_size
st.dataframe(seen_df.iloc[start:end])

## bar chart of appointment types for patients seen in March
st.subheader('Appointment Types for Patients Seen in March')
appt_counts = seen_df['Appt_Type'].value_counts().reset_index()
appt_counts.columns = ['Appt_Type', 'Count']
fig2 = px.bar(appt_counts, x='Appt_Type', y='Count', color='Appt_Type', title='Appointment Types for Patients Seen in March')
st.plotly_chart(fig2)

## list of patients whose appt type was "No Show" from whole dataset
st.subheader('Patients with "No Show" Appointment Type')
no_show_df = df[df['Appt_Type'] == "No Show"]
no_show_df = no_show_df[['First_Name', 'Last_Name', 'MBI', 'Date_Seen']]
st.dataframe(no_show_df)