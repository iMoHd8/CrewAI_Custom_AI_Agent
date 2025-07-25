import requests, os
import streamlit as st


def save_uploaded_file(uploaded_file, save_dir="data"):
    os.makedirs(save_dir, exist_ok=True)
    file_path = f"{save_dir}/{uploaded_file.name}"
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

def send_file_to_api(file_path):
    response = requests.post("http://localhost:5678/webhook/get_crew", json={"doc_path": file_path})

    return response.json().get("response")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


uploaded_file = st.file_uploader(
    "Upload a file",
    type=["pdf", "docx"],
    help="Upload a file to extract information."
)

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)

    with st.chat_message("assistant"):
        with st.spinner("Please wait..."):
            result = send_file_to_api(file_path)
            st.markdown(result)
            delete_file(file_path)
