import embeddings_langchain

if __name__ == "__main__":
    #Set this flag to True during first time run to create FAISS vector-store 
    #to save embeddings of your PDF file saved in data folder.
    create_faiss_vector_store_using_langchain=False

    if(create_faiss_vector_store_using_langchain==True):
        embeddings_langchain.CreateVectorDBAndSaveEmbeddings()

    
