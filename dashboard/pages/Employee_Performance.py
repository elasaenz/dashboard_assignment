import streamlit as st

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from scipy.stats import linregress


def linear_regression_plot(data: pd.DataFrame, x: str, y: str):
    # Perform linear regression
    slope, intercept, _, _, _ = linregress(data[x], data[y])

    # Generate regression line values
    data["y_pred"] = slope * data[x] + intercept

    # Create scatter plot
    fig = px.scatter(data, x=x, y=y, opacity=0.2, color_discrete_sequence=["gray"])

    # Add regression line
    fig.add_trace(go.Scatter(
        x=data[x],
        y=data["y_pred"],
        mode="lines",
        line=dict(color="blue", width=5),
        zorder=5
    ))
    fig.update_layout(showlegend=False)
    return fig, slope


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

    st.header("Employee Performance Scores")
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
            options=[None, EMPLOYEE_SATISFACTION, N_PROJECTS, EMPLOYEE_TENURE_YEARS, AVERAGE_MONTHLY_HOURS],
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

    employee_performance_data = DATA.copy()
    if filterby_option is not None:
        employee_performance_data = employee_performance_data.loc[
            (min_value <= employee_performance_data[filterby_option]) &
            (employee_performance_data[filterby_option] <= max_value)
        ]

    st.plotly_chart(
        px.histogram(
            employee_performance_data, 
            x=SCORE_LAST_EVALUATION, 
            nbins=30, 
            color=groupby_option,
            color_discrete_sequence=px.colors.qualitative.G10,
        )
    )
    st.info(f"""
        The mean of the plotted distribution is {round(employee_performance_data[SCORE_LAST_EVALUATION].mean(), 2)}
        
        The standard deviation of the plotted distribution is {round(employee_performance_data[SCORE_LAST_EVALUATION].std(), 2)}
    """)

    st.subheader("Employee Performance vs. Hours Worked Per Month")
    st.text("If you select") 
    st.code("Group By Attribute: None")
    st.code("Filter By Attribute Value: Average Hours Worked per Month")
    st.text("you can see by adjusting the slider that employees who work more hours per month tend to have higher performance scores.")
    st.text("The graph below illustrates this relationship more clearly.")

    fig, slope1 = linear_regression_plot(
        DATA,
        x=AVERAGE_MONTHLY_HOURS,
        y=SCORE_LAST_EVALUATION,
    )

    st.plotly_chart(fig)
    st.info(f"""
        The linear regression coefficient is {round(slope1, 5)} and the correlation coefficient is {round(float(DATA[SCORE_LAST_EVALUATION].corr(DATA[AVERAGE_MONTHLY_HOURS])), 2)}.

        This indicates that we should be encouraging employees to work more hours in order to increase their performance.
    """)

    st.subheader("Employee Performance vs. Number of Ongoing Projects")
    st.text("If you select") 
    st.code("Group By Attribute: None")
    st.code("Filter By Attribute Value: Number of Ongoing Projects")
    st.text("you can see by adjusting the slider that employees with more ongoing projects tend to have higher performance scores.")
    st.text("The graph below illustrates this relationship more clearly.")

    fig, slope2 = linear_regression_plot(
        DATA,
        x=N_PROJECTS,
        y=SCORE_LAST_EVALUATION,
    )

    st.plotly_chart(fig)
    st.info(f"""
        The linear regression coefficient is {round(slope2, 5)} and the correlation coefficient is {round(float(DATA[SCORE_LAST_EVALUATION].corr(DATA[N_PROJECTS])), 2)}.

        This indicates that we should be encouraging employees to take on new projects to increase their performance.
    """)

    st.subheader("Employee Performance vs. Employee Satisfaction")
    st.text("If you select") 
    st.code("Group By Attribute: None")
    st.code("Filter By Attribute Value: Employee Satisfaction")
    st.text("you can see by adjusting the slider that employees with more ongoing projects tend to have higher performance scores.")
    st.text("The graph below illustrates this relationship more clearly.")

    fig, slope3 = linear_regression_plot(
        DATA,
        x=EMPLOYEE_SATISFACTION,
        y=SCORE_LAST_EVALUATION,
    )

    st.plotly_chart(fig)
    st.info(f"""
        The linear regression coefficient is {round(slope3, 5)} and the correlation coefficient is {round(float(DATA[SCORE_LAST_EVALUATION].corr(DATA[EMPLOYEE_SATISFACTION])), 2)}.

        This demonstrates a weak positive relationship between employee satisfaction and their performance.
    """)


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()