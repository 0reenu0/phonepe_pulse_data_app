import streamlit as st
from phone_pe_etl import phonepe_etl


# Streamlit app code
def main():

    st.set_page_config(page_title="1. Data Extractor", page_icon=":globe_with_meridians:")

    st.sidebar.subheader("Phonepe Data Extraction")

    if st.sidebar.button("Extract Data to MySQL"):
         result_list=phonepe_etl()
         st.success(f"The data has been successfully extracted from json to MySQL!'")

# Run the Streamlit app
if __name__ == '__main__':
    main()