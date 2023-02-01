import streamlit as st
#import sqlite3
from database import *

import viewer as vw


def get_response(username):
    #conn = sqlite3.connect('users.db')
    #cursor = conn.cursor()
    #cursor.execute("SELECT response FROM users WHERE username=?", (username,))
    #result = cursor.fetchone()
    #conn.close()

    sql_code2 = f"SELECT response  \
        FROM users \
        WHERE (username = '{username}');"
    userfound = engine.execute(sql_code2)
    
    #st.success('User Updated')  
    

    if userfound is not None:
        #st.success(userfound)
        try:
            userans = userfound.fetchone()[0]   
            userfound.close() 
            return userans #[0]
        except:
            userfound.close() 
            return None #userans #[0]
    else:
        userfound.close()
        return None

def set_access(username):

    sql_code3 = f"UPDATE users  \
        SET accessed =1 \
        WHERE (username = '{username}');"
    UserUpdated = engine.execute(sql_code3)
    UserUpdated.close()
    #st.success('User Updated') 

    if UserUpdated:
        return "User Updated"
    else:
        return None
    


def main():
    st.title("Response Retriever")
    username = st.text_input("Enter your screen username").lower()
    if st.button("Submit"):
        response = get_response(username)
        if response:
            st.success(f"Response for {username}: {response}")
            acc = set_access(username) 

            st.success(f"acc : {acc}")
        else:
            st.error("Sorry, no response was left for you.")

if __name__ == '__main__':
    main()
