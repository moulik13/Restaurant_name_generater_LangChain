import streamlit as st
import LangChain_helper
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine", ("indian", "italian", "mexican", "chinese", "korean", "american"))

if cuisine:
    response = LangChain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu items**")
    for item in menu_items:
        st.write("-", item)
