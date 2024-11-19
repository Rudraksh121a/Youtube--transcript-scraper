import streamlit as st
from ccextracter import ccextract
import time

def main():
    st.title('YT CC Extractor')

   
    user_input = st.text_input("Enter your Url:")

    if st.button('Submit'):
        with st.spinner('Processing your request...'):
            time.sleep(8)
            if user_input:
                result=ccextract(user_input)
                result_in_str=str(result)
                st.write(len(result_in_str))
                # st.write(result_in_str)
                for i in result:
                    st.write(i)

if __name__=="__main__":
    main()