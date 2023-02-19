import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title = 'Data',
    page_icon = '✅',
    layout = 'wide'
)


if "photo" not in st.session_state:
    st.session_state["photo"]="not done"

col1, col2, col3 = st.columns([1,2,1])

col1.markdown(" # Upload data")

def change_photo_state():
    st.session_state["photo"]="done"

uploaded_file = col2.file_uploader("Choose a CSV file", on_change=change_photo_state)
file_images = []
url_column_name = "change to the name of the column with url listing"

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    url_list = df[url_column_name]
    for url in url_list:
        file_images.append(url)

uploaded_photo = col2.file_uploader("Upload a photo", accept_multiple_files=True, on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

if st.session_state["photo"] == "done":
    bar = col2.progress(0)
    for x in range(100):
        time.sleep(0.05)
        bar.progress(x+1)

    col2.success("Photo uploaded successfully")

    col3.metric(label="Temperature", value="-25℃ ", delta="3℃ ")

    with st.expander("Click to read more"):
        st.write("Please complete this data acqusition feature")
        i = 0
        if camera_photo:
            for each in camera_photo:
                st.image(each)
                st.checkbox("choose image", key=i)
                i += 1

        if uploaded_photo:
            for each in uploaded_photo:
                st.image(each)
                st.checkbox("choose image", key=i)
                i += 1

        if uploaded_file:
            for each in file_images:
                st.image(each)
                st.checkbox("choose image", key=i)
                i += 1
