# Overview of Java Code base.

## Prerequisites
### Knowledge
Basic knowledge of Java, Spring-Boot, HTML, JavaScript and Microsoft Azure and Generative-AI concepts like LLM, Vector data, Embeddings, Semantic/Vector search.
### Setup
On your maching you have JAva 17 or higher, IDE like VS-Code/IntelliJ/STS

## Project Structure
<img width="185" alt="image" src="https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/873a7202-6cb4-4c4d-8502-d8e99c6f0b4b">

Lets deep dive into the code.  

### Java/Backend  
1. Embeddings.java - This file/class has a method/rest-endpoint - "createandSaveEmbeddings". This GET method reads PDF file from "resources/data" folder. Performs tokenization/chunking on PDF file and then creates embeddings or vector-Data. Then it saves embeddings/vector-data to Pinecone Vector Database. If you dont know about Pinecone Database or Vector databases then dont worry. We will see how to setup Pinecone database down below. In this class, object of org.springframework.ai.vectorstore.VectorStore is Autowired which gets initialized with class and refers to properties defined in application.properties file, which we will see below.  
2. ChatWithData.java - This file/class has a method/rest-endpoint - "getChatResponse". This GET method accepts user input in request-parameter-"message"
