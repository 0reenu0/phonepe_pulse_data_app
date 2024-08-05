import pandas as pd
import json
import os
from sqlalchemy import create_engine,text
from phone_pe_transformer import preprocess_state_name 
from phone_pe_mysql import ENGINE

def get_agg_state_transactions():
   path="D:/PD/Apps/streamlit/phonepe/pulse/data/aggregated/transaction/country/india/state/"
   agg_state_list=os.listdir(path)
   clm={'State':[], 'Year':[], 'Quarter':[], 'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
   for i in agg_state_list:
    p_i=path+i+"/"
    agg_yr=os.listdir(p_i)
    for j in agg_yr:
        p_j=p_i+j+"/"
        agg_yr_list=os.listdir(p_j)
        for k in agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
                Name=z['name']
                count=z['paymentInstruments'][0]['count']
                amount=z['paymentInstruments'][0]['amount']
                clm['Transaction_type'].append(Name)
                clm['Transaction_amount'].append(amount)
                clm['Transaction_count'].append(count)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))
   agg_trans=pd.DataFrame(clm)
    #agg_trans.to_csv('phone_pe_agg_transaction.csv',index=False)
   return agg_trans

def get_agg_state_users():
   path="D:/PD/Apps/streamlit/phonepe/pulse/data/aggregated/user/country/india/state/"
   agg_state_list=os.listdir(path)
   clm={'State':[], 'Year':[], 'Quarter':[], 'Brand':[], 'Count':[], 'Percentage':[]}
   for i in agg_state_list:
    p_i=path+i+"/"
    agg_yr=os.listdir(p_i)
    for j in agg_yr:
        p_j=p_i+j+"/"
        agg_yr_list=os.listdir(p_j)
        for k in agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            if D['data']['usersByDevice'] is not None:
                for z in D['data']['usersByDevice']:
                   brand=z['brand']
                   count=z['count']
                   percentage=z['percentage']
                   clm['Brand'].append(brand)
                   clm['Count'].append(count)
                   clm['Percentage'].append(percentage)
                   clm['State'].append(i)
                   clm['Year'].append(j)
                   clm['Quarter'].append(int(k.strip('.json')))
   agg_trans=pd.DataFrame(clm)
    #agg_trans.to_csv('phone_pe_agg_user.csv',index=False)
   return agg_trans

def get_top_state_transactions():
   path="D:/PD/Apps/streamlit/phonepe/pulse/data/top/transaction/country/india/state/"
   agg_state_list=os.listdir(path)
   clm={'State':[], 'District':[], 'Pincode':[], 'Year':[], 'Quarter':[], 'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
   for i in agg_state_list:
    p_i=path+i+"/"
    agg_yr=os.listdir(p_i)
    for j in agg_yr:
        p_j=p_i+j+"/"
        agg_yr_list=os.listdir(p_j)
        for k in agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['districts']:
                d_name=z['entityName']
                type=z['metric']['type']
                count=z['metric']['count']
                amount=z['metric']['amount']
                clm['District'].append(d_name)
                clm['Transaction_type'].append(type)
                clm['Transaction_amount'].append(amount)
                clm['Transaction_count'].append(count)
                clm['Pincode'].append(None)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))

            for z in D['data']['pincodes']:
                pincode=z['entityName']
                type=z['metric']['type']
                count=z['metric']['count']
                amount=z['metric']['amount']
                clm['Transaction_type'].append(type)
                clm['Transaction_amount'].append(amount)
                clm['Transaction_count'].append(count)
                clm['State'].append(i)
                clm['District'].append(None)
                clm['Pincode'].append(pincode)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))
   agg_trans=pd.DataFrame(clm)
    #agg_trans.to_csv('phone_pe_top_transaction.csv',index=False)
   return agg_trans

def get_top_state_users():
   path="D:/PD/Apps/streamlit/phonepe/pulse/data/top/user/country/india/state/"
   agg_state_list=os.listdir(path)
   clm={'State':[], 'Year':[], 'Quarter':[], 'District':[], 'Pincode':[],'Registered_Users':[]}
   for i in agg_state_list:
    p_i=path+i+"/"
    agg_yr=os.listdir(p_i)
    for j in agg_yr:
        p_j=p_i+j+"/"
        agg_yr_list=os.listdir(p_j)
        for k in agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['districts']:
                d_name=z['name']
                registered_user_count=z['registeredUsers']
                clm['District'].append(d_name)
                clm['Pincode'].append(None)
                clm['Registered_Users'].append(registered_user_count)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))
            for z in D['data']['pincodes']:
                pincode=z['name']
                registered_user_count=z['registeredUsers']
                clm['Pincode'].append(pincode)
                clm['District'].append(None)
                clm['Registered_Users'].append(registered_user_count)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))
   agg_trans=pd.DataFrame(clm)
    #agg_trans.to_csv('phone_pe_top_user.csv',index=False)
   return agg_trans
    


def get_map_state_transactions():
   path="D:/PD/Apps/streamlit/phonepe/pulse/data/map/transaction/hover/country/india/state/"
   agg_state_list=os.listdir(path)
   clm={'State':[], 'District':[], 'Year':[], 'Quarter':[], 'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
   for i in agg_state_list:
    p_i=path+i+"/"
    agg_yr=os.listdir(p_i)
    for j in agg_yr:
        p_j=p_i+j+"/"
        agg_yr_list=os.listdir(p_j)
        for k in agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverDataList']:
                district_name=z['name']
                transaction_type=z['metric'][0]['type']
                count=z['metric'][0]['count']
                amount=z['metric'][0]['amount']
                clm['District'].append(district_name)
                clm['Transaction_type'].append(transaction_type)
                clm['Transaction_amount'].append(amount)
                clm['Transaction_count'].append(count)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))
   agg_trans=pd.DataFrame(clm)
    #agg_trans.to_csv('phone_pe_map_transaction.csv',index=False)
   return agg_trans
    

def get_map_state_users():
   path="D:/PD/Apps/streamlit/phonepe/pulse/data/map/user/hover/country/india/state/"
   agg_state_list=os.listdir(path)
   clm={'State':[], 'Year':[], 'Quarter':[], 'District':[], 'Registered_Users':[], 'App_Opens':[]}
   for i in agg_state_list:
    p_i=path+i+"/"
    agg_yr=os.listdir(p_i)
    for j in agg_yr:
        p_j=p_i+j+"/"
        agg_yr_list=os.listdir(p_j)
        for k in agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for district,v in D['data']['hoverData'].items():
                district_name=district
                count=v['registeredUsers']
                amount=v['appOpens']
                clm['District'].append(district_name)
                clm['Registered_Users'].append(count)
                clm['App_Opens'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quarter'].append(int(k.strip('.json')))
   agg_trans=pd.DataFrame(clm)
    #agg_trans.to_csv('phone_pe_map_user.csv',index=False)
   return agg_trans

def phonepe_etl():

    with ENGINE.begin() as conn:
     agg_tr_df=preprocess_state_name(get_agg_state_transactions())
     agg_user_df=preprocess_state_name(get_agg_state_users())
     top_tr_df=preprocess_state_name(get_top_state_transactions())
     top_user_df=preprocess_state_name(get_top_state_users())
     map_tr_df=preprocess_state_name(get_map_state_transactions())
     map_user_df=preprocess_state_name(get_map_state_users())

     agg_tr_df.to_sql('aggregate_transactions', conn, if_exists='replace', index=False)
     agg_user_df.to_sql('aggregate_users',conn, if_exists='replace', index=False)
     top_tr_df.to_sql('top_transactions',conn, if_exists='replace', index=False)
     top_user_df.to_sql('top_users',conn, if_exists='replace', index=False)
     map_tr_df.to_sql('map_transactions',conn, if_exists='replace', index=False)
     map_user_df.to_sql('map_users',conn, if_exists='replace', index=False)

       # video_df2=video_df1.drop_duplicates(subset='video_id',keep='first')                                                               
       # comments_df2=comments_df.drop_duplicates(subset='comment_id',keep='first')


       
     return