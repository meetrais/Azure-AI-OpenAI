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

# For one time embedding & FAISS vector store creation for your PDF file saved in data folder.
def emb_option_change(emb_option_sel):
    if(emb_option_sel=='Langchain'):
        print(emb_option_sel)
        #embeddings_langchain.CreateVectorDBAndSaveEmbeddings()
    elif(emb_option_sel=='Llama Index'):
        print(emb_option_sel)
        #embeddings_llama_index.CreateVectorDBAndSaveEmbeddings()

# Function to run the text generation process
def run_generation(user_text, top_p, temperature, top_k, max_new_tokens):
    embeddings=AzureOpenAIEmbeddings(deployment=AZURE_OPENAI_ADA_DEPLOYMENT,
                model="text-embedding-ada-002",
                azure_endpoint=AZURE_OPENAI_SERVICE,
                api_key=AZURE_OPENAI_KEY,
                chunk_size=1)
    model_output = ""
    db = FAISS.load_local(folder_path=DB_FAISS_PATH,embeddings=embeddings,index_name="index",allow_dangerous_deserialization=True)
    simmila_docs = db.similarity_search(user_text)
    print(simmila_docs[0].page_content)
    model_output = simmila_docs[0].page_content
    return model_output


# Gradio UI setup
embedding_option = ['Langchain', 'Llama Index'] #How do you want to create embeddings for your PDF file?
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=2):
            emb_option = gr.Dropdown(choices=embedding_option, label="How do you want to create embeddings for your PDF file?(Only run this once for PDF file.)")
            emb_option.input(emb_option_change, emb_option)
    with gr.Row():
        with gr.Column(scale=2):
            user_text = gr.Textbox(placeholder="Write your question here", label="User input")
            model_output = gr.Textbox(label="Model output", lines=10, interactive=False)
            button_submit = gr.Button(value="Submit")

        with gr.Column(scale=1):
            max_new_tokens = gr.Slider(minimum=1, maximum=1000, value=250, step=1, label="Max New Tokens")
            top_p = gr.Slider(minimum=0.05, maximum=1.0, value=0.95, step=0.05, label="Top-p (nucleus sampling)")
            top_k = gr.Slider(minimum=1, maximum=50, value=50, step=1, label="Top-k")
            temperature = gr.Slider(minimum=0.1, maximum=5.0, value=0.8, step=0.1, label="Temperature")

    user_text.submit(run_generation, [user_text, top_p, temperature, top_k, max_new_tokens], model_output)
    button_submit.click(run_generation, [user_text, top_p, temperature, top_k, max_new_tokens], model_output)

demo.queue(max_size=32).launch(server_port=8082)

# Gradion Setup Ends




  
    
