# Overview

## Prerequisites
### Knowledge
Basic knowledge of Java, Spring-Boot, HTML, JavaScript, Microsoft Azure and Generative-AI concepts like LLM, Vector data, Embeddings, Semantic/Vector search.
### Setup
. Java 17 or higher  
. IDE like VS-Code/IntelliJ/STS  
. Microsoft Azure Subscription

## High Level Diagram
### Create and Save Embeddings Flow
<img width="530" alt="image" src="https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/f8467415-743d-45e2-b4a7-d514d7d6ea26">

### Chat Flow
<img width="470" alt="image" src="https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/2d464dc1-a3d7-452c-a920-e770f6497193">

## Overview of Code
### Technologies Used
. Java, Spring-Boot  
. HTML  
. Spring-AI  
. Pinecone Vector Database

### Project Structure
<img width="185" alt="image" src="https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/873a7202-6cb4-4c4d-8502-d8e99c6f0b4b">

### Java/Backend  
1. Embeddings.java - To tokenize/chunking og PDF file and create embeddings/vector-data. Then it saves vector-data to Pinecone Vector Database.  
2. ChatWithData.java - To perform semantic search for user's input on vecror-data.  
### UI
1. index.html  
2. creatembeddings.html  
3. chat.html  
### Resources
1. application.properties - This is where initialization of Azure OpenAI and Pinecone properties done.  
2. data - This contains PDF file.  

## Spring AI
In this Project, I used below dependencies/libraries from Spring AI.  
1. spring-ai-azure-openai-spring-boot-starter  
2. spring-ai-pdf-document-reader  
3. spring-ai-pinecone  

Please refer below link to explore and learn more about Spring AI.  
[Spring AI](https://docs.spring.io/spring-ai/reference/index.html)

## Pinecone Vector Database
Please refer below link to register and create vector database on Pinecone.  
[Pinecone Vector Database](https://www.pinecone.io/)

Please refer below Spring AI documentation links to integrate different vector databases in your Retrieval Augmented Generation(RAG) application.  
[Spring AI - Vector Databases Integration](https://docs.spring.io/spring-ai/reference/api/vectordbs.html)



