import os.path

import openai
from dotenv import load_dotenv
from openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, load_index_from_storage, StorageContext

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def custom_chat(prompt):
    data_path = "chatgpt/data"
    PERSIST_DIR = "chatgpt/storage"
    if not os.path.exists(PERSIST_DIR):
        try:
            documents = SimpleDirectoryReader("chatgpt/data").load_data()
        except Exception as e:
            print(f"Error loading data from '{data_path}': {e}")
            raise
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(prompt)
    print(response)
    return response
