# Overview

## Prerequisites
### Knowledge
Basic knowledge of .Net, HTML, JavaScript, Microsoft Azure and Generative-AI concepts like LLM, Vector data, Embeddings, Semantic/Vector search.
### Setup
. Dot Net Framework  
. IDE like VS-Code/Visual-Studio  
. Microsoft Azure Subscription

## High Level Diagram
### Chat Flow
<img width="472" alt="image" src="https://github.com/meetrais/Azure-AI-OpenAI/assets/17907862/f8675a4b-a086-4eae-85ee-37ee0f596a82">

## Overview of Code
### Technologies Used
. Dot Net, MVC  
. HTML  
. Azure OpenAI SDK

### Project Structure
<img width="194" alt="image" src="https://github.com/meetrais/Azure-AI-OpenAI/assets/17907862/7ed0805a-c579-41d8-9b08-43221bd6aeb6">

### .Net/Backend  
ChatController.cs - This .Net MVC controller class has two HTTPGet methods/services.  
1. GetChatResponse - To return response from Azure-OpenAI service by using gpt-35-turbo model.  
2. GetChatWithYourDataResponse - To return response from Azure-OpenAI service by using gpt-35-turbo model and your PDF data. 
  

### UI
1. Chat/index.cshtml  - Has UI for ChatBots using gpt-35-turbo model and chat with your data.
