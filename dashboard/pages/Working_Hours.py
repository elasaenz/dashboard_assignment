import streamlit as st

import pandas as pd
import plotly.express as px

import pandas as pd

def main():
    # Dataset
    DATA = pd.read_csv("HR_capstone_dataset.csv").rename(
        columns={
            "satisfaction_level": "Employee Satisfaction",
            "last_evaluation": "Last Employee Performance Evaluation",
            "number_project": "Number of Ongoing Projects",
            "average_montly_hours": "Average Hours Worked per Month",
            "time_spend_company": "Years Spent in Company",
            "Work_accident": "Employee had Work Accident",
            "left": "Employee has Left",
            "promotion_last_5years": "Received Promotion",
            "Department": "Employee Department",
            "salary": "Employee Salary",
        }
    )

    #### DATASET COLUMNS ####
    # Employee-reported job satisfaction level [0–1]
    EMPLOYEE_SATISFACTION = "Employee Satisfaction"
    # Score of the employee's last performance review [0–1]
    SCORE_LAST_EVALUATION = "Last Employee Performance Evaluation"
    # Number of projects the employee contributes to
    N_PROJECTS = "Number of Ongoing Projects"
    # Average number of hours the employee worked per month
    AVERAGE_MONTHLY_HOURS = "Average Hours Worked per Month"
    # Duration of the employee's tenure with the company (in years)
    EMPLOYEE_TENURE_YEARS = "Years Spent in Company"
    # Whether or not the employee experienced an accident while at work
    WORK_ACCIDENT = "Employee had Work Accident"
    # Whether or not the employee left the company
    EMPLOYEE_HAS_LEFT = "Employee has Left"
    # Whether or not the employee was promoted in the last 5 years
    RECEIVED_PROMOTION = "Received Promotion"
    # The employee's department
    EMPLOYEE_DEPARTMENT = "Employee Department"
    # The employee's salary
    EMPLOYEE_SALARY = "Employee Salary"

    st.header("Employee Working Hours")
    col1, col2 = st.columns(2)
    with col1:
        groupby_option = st.selectbox(
            "Group By Attribute", 
            options=[None, N_PROJECTS, EMPLOYEE_TENURE_YEARS, WORK_ACCIDENT, EMPLOYEE_HAS_LEFT, EMPLOYEE_DEPARTMENT, EMPLOYEE_SALARY, RECEIVED_PROMOTION],
            help="Select an attribute to colour the data according to that attribute. Different categories can be selected or deselected by clicking on the categories in the plot legend."
        )
    with col2:
        filterby_option = st.selectbox(
            "Filter By Attribute Value", 
            options=[None, SCORE_LAST_EVALUATION, EMPLOYEE_SATISFACTION, N_PROJECTS, EMPLOYEE_TENURE_YEARS],
            help="Filter the data so that only the data with the attribute within the range specified is used."
        )
    if filterby_option is not None:
        unique_values = sorted(DATA[filterby_option].unique().tolist())
        min_value, max_value = st.select_slider(
            "Select Range",
            options=unique_values,
            value=(unique_values[0], unique_values[-1]),
        )
    else:
        st.divider()

    employee_satisfaction_data = DATA.copy()
    if filterby_option is not None:
        employee_satisfaction_data = employee_satisfaction_data.loc[
            (min_value <= employee_satisfaction_data[filterby_option]) &
            (employee_satisfaction_data[filterby_option] <= max_value)
        ]

    st.plotly_chart(
        px.histogram(employee_satisfaction_data, x=AVERAGE_MONTHLY_HOURS, nbins=30, color=groupby_option)
    )

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()