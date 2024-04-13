import embeddings_langchain
import embeddings_llama_index
from langchain_openai import AzureOpenAIEmbeddings
import gradio as gr
from langchain_community.vectorstores.faiss import FAISS
import applicationKeys as ApplicationKeys

DB_FAISS_PATH = 'Python/vectorstore/db_faiss'
# Set up OpenAI client based on environment variables
AZURE_OPENAI_SERVICE = ApplicationKeys.AZURE_OPENAI_SERVICES
AZURE_OPENAI_ADA_DEPLOYMENT = ApplicationKeys.AZURE_OPENAI_ADA_DEPLOYMENT
AZURE_OPENAI_KEY= ApplicationKeys.AZURE_OPENAI_KEY
FAISS_INDEX_NAME='faiss_langchain'
# For one time embedding & FAISS vector store creation for your PDF file saved in data folder.
"""def emb_option_change(emb_option_sel):
    global FAISS_INDEX_NAME
    if(emb_option_sel=='Langchain'):
        FAISS_INDEX_NAME="faiss_langchain"
    elif(emb_option_sel=='Llama Index'):
        FAISS_INDEX_NAME="faiss_llama_index"""

# Function to run the text generation process
def run_generation(user_text):
    embeddings=AzureOpenAIEmbeddings(deployment=AZURE_OPENAI_ADA_DEPLOYMENT,
                model="text-embedding-ada-002",
                azure_endpoint=AZURE_OPENAI_SERVICE,
                api_key=AZURE_OPENAI_KEY,
                chunk_size=1)
    model_output = ""
    db = FAISS.load_local(folder_path=DB_FAISS_PATH,embeddings=embeddings,index_name=FAISS_INDEX_NAME,allow_dangerous_deserialization=True)
    simmila_docs = db.similarity_search(user_text, fetch_k=1)
    print(simmila_docs[0].page_content)
    model_output = simmila_docs[0].page_content
    return model_output

def create_embedding():
    #if(FAISS_INDEX_NAME=='faiss_langchain'):
    embeddings_langchain.CreateVectorDBAndSaveEmbeddings()
    gr.Info("FAISS Vector Store Created Successfully.")
        #print('faiss_langchain')
    #elif(FAISS_INDEX_NAME=='faiss_llama_index'):
        #embeddings_llama_index.CreateVectorDBAndSaveEmbeddings()
        #print('faiss_llama_index')
    

# Gradio UI setup
embedding_option = ['Langchain', 'Llama Index'] #How do you want to create embeddings for your PDF file?
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):
            #emb_option = gr.Dropdown(choices=embedding_option, label="How do you want to create/use embeddings for your PDF file?")
            #emb_option.input(emb_option_change, emb_option)
            button_submit_emb = gr.Button(value="Create Embeddings(Only run this once to create FAISS vector-store for your PDF file.)")
    with gr.Row():
        with gr.Column(scale=2):
            user_text = gr.Textbox(placeholder="Write your question here", label="User input")
            model_output = gr.Textbox(label="Model output", lines=10, interactive=False)
            button_submit = gr.Button(value="Submit")
           

    button_submit_emb.click(create_embedding)
    
    user_text.submit(run_generation, [user_text], model_output)
    button_submit.click(run_generation, [user_text], model_output)

demo.queue(max_size=32).launch(server_port=8082)

# Gradion Setup Ends




  
    
