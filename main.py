from deta import Deta
import streamlit as st


DETA_KEY = "d0yz71smpt6_DHwfWqpYu865GAhNXngRAMkvsK1XMnxr"


deta = Deta(DETA_KEY)
db = deta.Base("Workshop")
res = db.fetch(query={"category?contains": "south"})
data=res.items
# print(data)


st.title("NEWSIFY")
st.header("Explore the World")

select = st.text_input("Enter the Word")
submit = st.button("Search")

if submit:
    DETA_KEY = st.secrets["data_key"]


    deta = Deta(DETA_KEY)
    db = deta.Base("Workshop")
    res = db.fetch(query={"headlines?contains": select})
    data=res.items
    for news in data:
        st.header(news["headlines"])
        with st.container():
            left,right = st.columns(2)
            with left:
                st.image(news["images"])
            with right:
                st.write(news["news"])
                st.write(news["authors"])
                st.write(news["Date"])
                st.write(news["country"])

















        

        