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
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

st.pyplot(fig1)

# # filter data
# position_df = df[df['POS'] == selected_position]

# ## plots
# if not selected_tests:
#     st.warning("Please select at least one test result to display.")
# else:
#     for test in selected_tests:
#         st.subheader(f'Histogram for {test}')
#         fig, ax = plt.subplots()
#         sns.histplot(data=position_df, x=test, bins = 10, kde=True, ax=ax)
#         ax.set_title(f"{test} Distribution ({selected_position})")
#         ax.set_xlabel(test)
#         ax.set_ylabel("Frequency")

#         st.pyplot(fig)

# ## results by teams
# with tab2:
#     st.write('Team Draft Pick Performances')

#     st.markdown("""
#     ## Instructions
#     - Enter a **team name** in the input box below (must include city).
#     - Select the **years** (2021-2024) using the checkboxes.
#     - The table below will display the player data for the selected team and years.
#     - For more all team options, click [here](https://www.espn.com/nba/teams).
# """)

#     # select teams
#     team_name = st.text_input("Enter Team Name:")
#     df['Year'] = df['Year'].astype(str)


#     # year options
#     year_2021 = st.checkbox("2021", value=True)
#     year_2022 = st.checkbox("2022", value=True)
#     year_2023 = st.checkbox("2023", value=True)
#     year_2024 = st.checkbox("2024", value=True)

#     # filter data
#     selected_years = []
#     if year_2021:
#         selected_years.append('2021')
#     if year_2022:
#         selected_years.append('2022')
#     if year_2023:
#         selected_years.append('2023')
#     if year_2024:
#         selected_years.append('2024')

#     if team_name:
#         team_df = df[df['Team'].str.contains(team_name, case = False, na= False)]
#         if selected_years:
#             team_df = team_df[team_df['Year'].isin(selected_years)]

#         # specify what I want to show
#         columns_to_show = ['Player', 'POS', 'Lane Agility Time (seconds)', 'Shuttle Run (seconds)', 'Three Quarter Sprint (seconds)', 'Standing Vertical Leap (inches)', 'Max Vertical Leap (inches)', 'Year', 'Affiliation', 'OverallPick']
#         team_df = team_df[columns_to_show]

#         # build table
#         if not team_df.empty:
#             summary = team_df[['Lane Agility Time (seconds)', 'Shuttle Run (seconds)', 'Three Quarter Sprint (seconds)', 'Standing Vertical Leap (inches)', 'Max Vertical Leap (inches)']].mean()
#             summary_row = pd.DataFrame({
#                 'Test Name': ['Lane Agility Time (seconds)', 'Shuttle Run (seconds)', 'Three Quarter Sprint (seconds)', 
#                             'Standing Vertical Leap (inches)', 'Max Vertical Leap (inches)'],
#                 'Average Value': summary.values
#             })
#             summary_row = summary_row.reset_index(drop=True)
#             st.subheader(f'Drafted Player Data for {team_name}')
#             st.dataframe(team_df)
#             st.subheader(f'Drafted Player Averages')
#             st.table(summary_row)
#         else:
#             st.warning(f"No data availiable for {team_name} in selected years.")
#     else:
#         st.warning("Please enter a team name.")
