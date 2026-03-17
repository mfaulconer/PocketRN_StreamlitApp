import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

## streamlit
st.title('March Patient Report')

## data
df = pd.read_csv('Patients_Seen.csv')

## columns
col1, col2 = st.columns([0.7, 0.3])

## label for tab
with col1:
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

## Box that says appts to schedule per work day to meet 100% of patients seen in March, dynamic to todays date
    total_patients_seen = (df['Patient_Seen'] == "Yes").sum()
    patients_not_seen = (df['Patient_Seen'] == "No").sum()
    today = pd.to_datetime('today')
    march_start = pd.to_datetime('2026-03-01')
    march_end = pd.to_datetime('2026-03-31')
    weekends_remaining = len(pd.bdate_range(start=today, end=march_end, freq='W-SAT')) + len(pd.bdate_range(start=today, end=march_end, freq='W-SUN'))
    work_days_remaining = len(pd.bdate_range(start=today, end=march_end)) - weekends_remaining
    appts_to_schedule = patients_not_seen / work_days_remaining if work_days_remaining > 0 else 0

with col2:
    st.markdown(f"""
    <div style='border: 2px solid #3498db; border-radius: 10px; padding: 20px; background-color: #f5f5f5;'>
        <h3 style="font-size:14px; margin-bottom:8px;">
            Appointments to Schedule Per Work Day to Meet 100% of Patients Seen in March
        </h3>
        <p style="margin:0;">
        As of {today.strftime('%Y-%m-%d')}, to meet 100% of patients seen in March,
        you would need to schedule approximately <b>{appts_to_schedule:.2f}</b> appointments per work day.
        </p>
    </div>
    """, unsafe_allow_html=True)

## list of patients whose appt type was "No Show" from whole dataset
st.subheader('Patients with "No Show" Appointment Type')
no_show_df = df[df['Appt_Type'] == "No Show"]
no_show_df = no_show_df[['First_Name', 'Last_Name', 'MBI', 'Date_Seen']]
st.dataframe(no_show_df)

## bar chart of appointment types for patients seen in March
seen_march_df = df[df['Patient_Seen'] == "Yes"]

st.subheader('Appointment Types for Patients Seen in March')
appt_counts = seen_march_df['Appt_Type'].value_counts().reset_index()
appt_counts.columns = ['Appt_Type', 'Count']
fig2 = px.bar(appt_counts, x='Appt_Type', y='Count', color='Appt_Type', title='Appointment Types for Patients Seen in March')
st.plotly_chart(fig2)

