import streamlit as st
import phone_pe_mysql as mysql
import phone_pe_transformer as transform
import plotly.express as px



# Streamlit app code
def main():
    st.set_page_config(
        page_title="Home",
        page_icon="👋",
    )

   
   

    st.markdown(
        """
        #### select an option from the dropdown
        """)
    st.write("All India")

    series= mysql.fetch_years()
    tuple_of_strings = transform.convert_to_str_tuple(series)

    # Create the selectboxes side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_option1=st.selectbox("Type",("Transactions","Users" ),index=None,placeholder="Select an option ")
    with col2:
        selected_year=st.selectbox("Year",tuple_of_strings,index=None,placeholder="Select an option ")
    with col3:
        selected_quarter=st.selectbox("Quarter",(1,2,3,4),index=None,placeholder="Select an option ")
    final_df=[]
    if(selected_option1=="Transactions"):
        df = mysql.fetch_aggregate_transactions(selected_year,selected_quarter)
        df['State']=df['State'].apply(lambda a: " ".join([k.capitalize() if k.lower() != 'and' else k for k in a.split('-')]))
        df['State']=df['State'].apply(lambda a: " ".join([k.replace('-',' ') for k in a.split()]))

        mask=(df['Year']==2018)
        df2=df[mask]
        mask1=df2['Quarter']==1
        df2=df2[mask1]
        mask2=df2['Transaction_type'].isin(['Peer-to-peer payments']) 
        final_df=df2[mask2]

    elif(selected_option1=="Users"):
        df = mysql.fetch_aggregate_users(selected_year,selected_quarter)
        df['State']=df['State'].apply(lambda a: " ".join([k.capitalize() if k.lower() != 'and' else k for k in a.split('-')]))
        df['State']=df['State'].apply(lambda a: " ".join([k.replace('-',' ') for k in a.split()]))

        mask=(df['Year']==2018)
        df2=df[mask]
        mask1=df2['Quarter']==1
        final_df=df2[mask1]
        
    if final_df:
        fig = px.choropleth(
        final_df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_amount',
        )
        fig.update_geos(fitbounds="locations", visible=False)

        fig.show()
    


# Run the Streamlit app
if __name__ == '__main__':
    main()