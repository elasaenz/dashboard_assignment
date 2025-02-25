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

    def number_of_ongoing_projects_for_all_employees():
        proj_series = DATA.groupby(N_PROJECTS).size().sort_index()
        proj = proj_series.to_dict()
        fig = px.pie(
            names=list(str(p) + " Projects" for p in proj.keys()),
            values=list(proj.values()),
            title=None,
        )
        fig.update_traces(
            textposition='outside',
            textinfo='label+value+percent',
            texttemplate='%{label}<br>%{value} (%{percent:.1%})',
            showlegend=False,
        ) 
        st.plotly_chart(fig)

    def employee_salary_perception():
        salary_series = (
            DATA
            .groupby(EMPLOYEE_SALARY)
            .size()
            .reindex(["low", "medium", "high"])
            .rename(index={"low": "Poor", "medium": "Fine", "high": "Good"})
        )
        proj = salary_series.to_dict()
        fig = px.pie(
            names=list(str(p) for p in proj.keys()),
            values=list(proj.values()),
            title=None,
        )
        fig.update_traces(
            textposition='outside',
            textinfo='label+value+percent',
            texttemplate='%{label}<br>%{value} (%{percent:.1%})',
            showlegend=False,
        ) 
        st.plotly_chart(fig)

    def number_of_employees_per_department():
        proj_series = (
            DATA
            .groupby(EMPLOYEE_DEPARTMENT)
            .size()
            .sort_index()
            .rename(
                index={
                    "technical": "Technical",
                    "support": "Support",
                    "product_mng": "Product Management",
                    "marketing": "Marketing",
                    "RandD": "R&D",
                    "accounting": "Accounts",
                    "hr": "HR",
                    "management": "Management",
                    "sales": "Sales",
                }
            )
        )
        proj = proj_series.to_dict()
        fig = px.pie(
            names=list(str(p) for p in proj.keys()),
            values=list(proj.values()),
            title=None,
        )
        fig.update_traces(
            textposition='outside',
            textinfo='label+value+percent',
            texttemplate='%{label}<br>%{value} (%{percent:.1%})',
            showlegend=False,
        ) 
        st.plotly_chart(fig)

    def number_of_promotions_in_last_5_years():
        proj_series = DATA.groupby(RECEIVED_PROMOTION).size().sort_index().rename(index={0: "Not Promoted", 1: "Promoted"})
        proj = proj_series.to_dict()
        fig = px.pie(
            names=list(str(p) for p in proj.keys()),
            values=list(proj.values()),
            title=None,
        )
        fig.update_traces(
            textposition='outside',
            textinfo='label+value+percent',
            texttemplate='%{label}<br>%{value} (%{percent:.1%})',
            showlegend=False,
        ) 
        st.plotly_chart(fig)
    
    st.header("Summary")
    st.subheader("Employees per Department")
    col1, col2 = st.columns(2)
    with col1:
        number_of_employees_per_department()
    with col2:
        for _ in range(2):
            st.text('')
        st.info(
            """
            With 14,999 employees across ten departments, Sales remains the largest at 4,140 (27.6%), followed by Technical (2,720, 18.1%) and Support (2,229, 14.9%). Smaller yet vital groups—IT, R&D, Product Management, Accounts, HR, Marketing, and Management—ensure balanced capabilities. This distribution highlights a strong revenue focus, supported by robust technical and customer-facing teams, and a foundation for ongoing innovation and cultural growth.
            
            These figures indicate a balanced mix of operational and strategic capabilities. Continued focus on cross-functional collaboration—particularly among Sales, Technical, and Support—will help maintain efficiency and bolster long-term organizational health. Further skill development in R&D and Product Management will support innovation, while ensuring HR and Management capacities remain agile enough to guide growth and nurture company culture.
            """
        )
    st.subheader("Number of Ongoing Projects per Employee")
    col1, col2 = st.columns(2)
    with col1:
        number_of_ongoing_projects_for_all_employees()
    with col2:
        for _ in range(8):
            st.text('')
        st.info(
            """
            Out of 14,999 employees, the largest share (29.1%) manage 4 ongoing projects, followed by 3 projects (27.0%) and 2 projects (15.9%). Roughly one in five employees (18.4%) handle 5 projects, while 6 and 7 projects remain less common (7.8% and 1.7%, respectively). This distribution suggests most staff balance three to four active initiatives, with a smaller group carrying heavier workloads.
            """
        )

    st.subheader("Employees who received promotion in last 5 years")
    col1, col2 = st.columns(2)
    with col1:
        number_of_promotions_in_last_5_years()
    with col2:
        for _ in range(7):
            st.text('')
        st.info(
            """
            Out of 14,999 employees, 319 (2.1%) have been promoted within the last five years, while the vast majority—14,680 (97.9%)—has not. Though this indicates limited upward movement overall, those receiving promotions signal a pathway for career growth. Tracking these promotion rates over time helps HR evaluate internal mobility, identify high-potential talent, and ensure that performance and retention strategies align with the organization’s long-term leadership needs.
            """
        )

    st.subheader("Perception of Salary per Employee")
    col1, col2 = st.columns(2)
    with col1:
        employee_salary_perception()
    with col2:
        for _ in range(7):
            st.text('')
        st.info(
            """
            Out of 14,999 employees, 7,316 (48.8%) consider their salary “Poor,” 6,446 (43.0%) find it “Fine,” and 1,237 (8.2%) say it’s “Good.” The data shows nearly half of the workforce feels underpaid, which could impact engagement and retention. A smaller group reports satisfactory compensation. Monitoring these perceptions helps HR refine pay structures and maintain a motivated, competitive workforce.
            """
        )

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()