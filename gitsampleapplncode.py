import streamlit as st
import pandas as pd

st.set_page_config(
   page_title="Snow-Amazing Badge Mgmt",
   page_icon= "🏆"
)

cnx=st.connection("snowflake")
session = cnx.session()
if 'auth_status' not in st.session_state:
    st.session_state['auth_status'] = 'not_authed'
   
def initialize_user_info():
   # session is open but not authed
   st.session_state['auth_status'] = 'not_authed'
   # all profile fields get set back to nothing
   st.session_state['given_name'] = ''
   st.session_state['middle_name'] = ''
   st.session_state['family_name'] = ''
   st.session_state['badge_email'] = ''
   st.session_state['display_name'] = ''
   # workshop/account fields are set back to nothing 
   st.session_state['workshop_choice'] = '' 
   st.session_state['account_locator'] = ''
   st.session_state['account_identifier'] = ''
   st.session_state['submit_new_account_info'] = False

def get_user_profile_info():
   #start over with authentication and populating vars
   this_user_sql =  (f"select badge_given_name, badge_middle_name, badge_family_name, display_name, badge_email "
                     f"from UNI_USER_BADGENAME_BADGEEMAIL where UNI_ID=trim('{st.session_state.uni_id}') "
                     f"and UNI_UUID=trim('{st.session_state.uni_uuid}')")
   this_user_df = session.sql(this_user_sql)
   user_results_pd_df = this_user_df.to_pandas()                          
   user_rows = user_results_pd_df.shape[0]

   if user_rows>=1:
      # if at least one row was found then the key must have been correct so we consider the user authorized
      st.session_state['auth_status'] = 'authed'
       
      # 1 row found means the UNI_ID is legit and can be used to look up other information
      # all user vars need to be checked to make sure they aren't empty before we set session vars
      
      if user_results_pd_df['BADGE_GIVEN_NAME'].iloc[0] is not None:
         st.session_state['given_name'] = user_results_pd_df['BADGE_GIVEN_NAME'].iloc[0]
      if user_results_pd_df['BADGE_MIDDLE_NAME'].iloc[0] is not None:    
         st.session_state['middle_name'] = user_results_pd_df['BADGE_MIDDLE_NAME'].iloc[0]
      if user_results_pd_df['BADGE_FAMILY_NAME'].iloc[0] is not None:    
         st.session_state['family_name'] = user_results_pd_df['BADGE_FAMILY_NAME'].iloc[0]
      if user_results_pd_df['BADGE_EMAIL'].iloc[0] is not None:
         st.session_state['badge_email'] = user_results_pd_df['BADGE_EMAIL'].iloc[0]  
      if user_results_pd_df['DISPLAY_NAME'].iloc[0] is not None:
         st.session_state['display_name'] = user_results_pd_df['DISPLAY_NAME'].iloc[0]
      else:
         st.session_state['display_name'] = "PLEASE GO TO THE DISPLAY NAME TAB TO GENERATE A DISPLAY NAME FOR YOUR BADGE"
      st.dataframe(user_results_pd_df)
   else: # no rows returned
        st.markdown(":red[There is no record of the UNI_ID/UUID combination you entered. Please double-check the info you entered, check the FAQs tab below for tips on FINDING YOUR INFO, and try again]") 

with st.sidebar:
   st.sidebar.header("User")
   uni_id = st.text_input('Enter your learn.snowflake.com UNI ID:')
   uni_uuid = st.text_input('Enter the secret UUID displayed on the DORA is Listening Page of any Workshop:')
   find_my_uni_record = st.button("Find my UNI User Info")
   st.session_state

# Page Header
st.header('Are You Snow-A-Mazing?')
st.write('Welcome to the learn.snowflake.com Workshop Badge Management app!')
st.write('Using this app you can manage your badge name and email and you can view your results.')

if find_my_uni_record:
   # reset all session vars
   initialize_user_info()

   # Set uni_id and key to entries on form
   st.session_state['uni_id'] = uni_id
   st.session_state['uni_uuid'] = uni_uuid

   # this will query the db and if finds a match will populate profile vars
   get_user_profile_info()
   

if st.session_state.auth_status == 'authed':
   st.subheader("We Found You!")
   st.markdown("**GIVEN NAME:** " + st.session_state.given_name)
   st.markdown("**MIDDLE/ALTERNATE NAME:** "+ st.session_state.middle_name) 
   st.markdown("**FAMILY NAME:** " + st.session_state.family_name)
   st.markdown("**EMAIL:** " + st.session_state.badge_email)
   if st.session_state.display_name != "PLEASE GO TO THE DISPLAY NAME TAB TO GENERATE A DISPLAY NAME FOR YOUR BADGE":
      st.markdown("**Name Will Display on Badge As:** " + st.session_state.display_name)
   else:
      md_str =  "**Name Will Display on Badge As:** :red[" + st.session_state.display_name + "]"       
      st.markdown(md_str)
      st.write("-----")
      st.markdown("*If your display name has not been generated, or you would like to make changes to information, go to the Your Display Name page.*")
else:
   st.markdown(":red[Please sign in using your UNI_ID and UUID in the section above.]")
