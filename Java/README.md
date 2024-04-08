# Overview of Java Code base.

## Prerequisites
### Knowledge
Basic knowledge of Java, Spring-Boot, HTML, JavaScript, Microsoft Azure and Generative-AI concepts like LLM, Vector data, Embeddings, Semantic/Vector search.
### Setup
On your maching you have JAva 17 or higher, IDE like VS-Code/IntelliJ/STS

## Project Structure
<img width="185" alt="image" src="https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/873a7202-6cb4-4c4d-8502-d8e99c6f0b4b">

### Java/Backend  
1. Embeddings.java  
2. ChatWithData.java  
### UI
1. index.html  
2. creatembeddings.html  
3. chat.html  
### Resources
1. application.properties - This is where initialization of Azure OpenAI and Pinecone properties done.  
2. data - This containes PDF file.  

## Spring AI
In this Project, I used below dependencies/libraries from Spring AI.  
1. spring-ai-azure-openai-spring-boot-starter  
2. spring-ai-pdf-document-reader  
3. spring-ai-pinecone

Please refer below link to explore and learn more about Spring AI.  
[Spring AI](https://docs.spring.io/spring-ai/reference/index.html)






