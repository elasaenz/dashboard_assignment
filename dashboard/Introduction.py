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


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()