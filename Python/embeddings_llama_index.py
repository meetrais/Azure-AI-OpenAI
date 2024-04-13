import llama_index.vector_stores.faiss as FAISS
from llama_index.core import (
    SimpleDirectoryReader,
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
)
from llama_index.vector_stores.faiss import FaissVectorStore
from IPython.display import Markdown, display

DATA_PATH = 'Python/data/'
DB_FAISS_PATH = 'Python/vectorstore/db_faiss'

def CreateVectorDBAndSaveEmbeddings():
    # dimensions of text-ada-embedding-002
    d = 1536
    faiss_index = FAISS.IndexFlatL2(d)
    # load documents
    documents = SimpleDirectoryReader(DATA_PATH).load_data()
    vector_store = FaissVectorStore(faiss_index=faiss_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context)
    # save index to disk
    index.storage_context.persist()
    
if __name__ == "__main__":
    CreateVectorDBAndSaveEmbeddings()
