from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
import applicationKeys as ApplicationKeys


DATA_PATH = 'Python/data/USA.pdf'
DB_FAISS_PATH = 'Python/vectorstore/db_faiss'

# Set up OpenAI client based on environment variables
AZURE_OPENAI_SERVICE = ApplicationKeys.AZURE_OPENAI_SERVICES
AZURE_OPENAI_ADA_DEPLOYMENT = ApplicationKeys.AZURE_OPENAI_ADA_DEPLOYMENT
AZURE_OPENAI_KEY= ApplicationKeys.AZURE_OPENAI_KEY

#Create Embeddings using langchain and store to FAISS Vector store
def CreateVectorDBAndSaveEmbeddings():
    loader = PyPDFLoader(file_path=DATA_PATH)
    pages = loader.load_and_split()

    embeddings=AzureOpenAIEmbeddings(deployment=AZURE_OPENAI_ADA_DEPLOYMENT,
                model="text-embedding-ada-002",
                azure_endpoint=AZURE_OPENAI_SERVICE,
                api_key=AZURE_OPENAI_KEY,
                chunk_size=1)
    db = FAISS.from_documents(documents=pages, embedding=embeddings)
    db.save_local(DB_FAISS_PATH)
