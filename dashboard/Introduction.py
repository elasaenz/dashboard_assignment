import streamlit as st

def main():
    st.title(":rainbow: Introduction")
    st.divider()
    st.markdown(
        """
        *The dataset used in this capstone project is sourced from the Google Advanced Data Analysis course. 
        It encompasses a comprehensive collection of attributes concerning employees, ranging from demographic details to job-related factors.*

        To view the analytics, navigate to the various pages using the sidebar on the left.

        The dataset was sourced from Kaggle at the following link

        [https://www.kaggle.com/datasets/raminhuseyn/hr-analytics-data-set](https://www.kaggle.com/datasets/raminhuseyn/hr-analytics-data-set)
        """
    )

    st.subheader("Sarah’s Journey: Navigating Career Growth, Workload, and Salary Perception")

    st.text("""
        Sarah had always been a dedicated professional. Five years ago, she joined the company as a Sales Associate, eager to prove herself in the fast-paced environment. Over time, she developed strong client relationships, consistently exceeded her targets, and worked closely with the Technical and Support teams to ensure smooth operations. Like many of her colleagues, she thrived in a company where Sales made up 27.6% of the workforce, playing a pivotal role in driving revenue.
            
        Despite her dedication, Sarah often found herself stretched thin. With a growing client base and expanding responsibilities, she was assigned four ongoing projects, aligning her with the largest employee group (29.1%) managing similar workloads. Some of her colleagues juggled even more—five, six, or even seven projects—but Sarah knew that balancing efficiency with effectiveness was key. She sometimes worried about burnout but took pride in her ability to multitask and deliver results.
        
        As the years passed, Sarah began setting her sights on career advancement. She had consistently outperformed expectations, mentored new hires, and even took on leadership responsibilities without the official title. Yet, when promotion cycles came around, she found herself among the 97.9% of employees who had not been promoted in the last five years. She watched as a select few (2.1%) moved up the ranks, wondering what more she could do to secure her own career progression.
        
        Compensation became another concern. Sarah was one of the 48.8% of employees who rated their salary as “Poor.”While she appreciated the company culture and the opportunities to develop her skills, she couldn’t ignore the fact that her pay had remained relatively stagnant despite her increased workload and responsibilities. Some of her colleagues felt their salaries were “Fine” (43.0%), while a small percentage (8.2%) were fully satisfied with their earnings. Sarah debated whether to continue pushing for a promotion internally or explore opportunities elsewhere.
        
        Her story mirrors the broader challenges faced by many employees in the company. While the organization has built a strong workforce structure, a well-balanced mix of departments, and an efficient approach to managing projects, issues such as limited career mobility and salary dissatisfaction could impact long-term employee retention.
        
        What Could Help Sarah and Employees Like Her?
        •⁠  ⁠Cross-Functional Collaboration: Encouraging better alignment between Sales, Technical, and Support teamscould optimize workflows and allow employees like Sarah to focus on high-impact work rather than being overburdened with too many responsibilities.
        •⁠  ⁠Workload Management: Ensuring employees aren’t consistently assigned excessive projects will help prevent burnout and maintain long-term productivity.
        •⁠  ⁠Career Development & Promotions: Expanding leadership development programs and offering more opportunities for internal promotions could improve engagement and motivation.
        •⁠  ⁠Compensation Strategy: Regular salary evaluations, performance-based incentives, and transparent discussions about pay structures could help address concerns about underpayment.
        
        Sarah’s story reflects the reality of many employees—ambitious, hardworking, and eager for growth, yet facing barriers in workload balance, career progression, and compensation. Addressing these challenges will not only benefit employees like Sarah but also strengthen the company’s long-term success by fostering a motivated, high-performing workforce.
    """)


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()