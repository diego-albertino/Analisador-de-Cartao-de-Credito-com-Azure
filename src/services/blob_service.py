import os
import streamlit as st
from utils.Config import Config
from azure.storage.blob import BlobServiceClient


def upload_blob(file, filename):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)

        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=filename)
        
        blob_client.upload_blob(file, overwrite=True)
        
        return blob_client.url
        
    except Exception as e:
        st.error(f"Erro ao enviar arquivo para o Azure Blob Storage: {e}")
        return None