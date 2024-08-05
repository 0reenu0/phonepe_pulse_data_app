import streamlit as st

# Streamlit app code
def main():
    st.set_page_config(
        page_title="Home",
        page_icon="👋",
    )

    st.write("# Welcome to Reenu's Phonepe Data Explorer Application! 👋")

    st.sidebar.success("Click a page link above.")

    st.markdown(
        """
        R.D.E.A- Reenu's Phonepe Data Explorer Application is an app to extract data from Phoenpe Github clone and provide visualization and exploration of the data.
        #### **👈 Click on the page links on the sidebar to navigate** 

        #### Want to learn more about the links?
            1. The Data Extractor page allows to perform extraction from Phonepe github clone json fies to MySQL.
            2. The Data explorer page provides option to view the various data insights.
            
        """)


# Run the Streamlit app
if __name__ == '__main__':
    main()