# Azure-AI ~ OpenAI

## Introduction
This GitHub repo is for code samples of Microsoft Azure-AI Search(Cognitive) & Azure OpenAI services. It demonstrates how to develop Retrieval Augmented Generation(RAG) based chat-bot by consuming Azure-AI services like OpenAI and Azure-Search(Cognitive). You can refer to code folder of your choice of programming language - Java, Python or Dot Net(TBD). Please feel free to reach out to me if you find any bugs or have suggestions for improvement. I strongly recommend to read this documentation before you dive into the code. Happy Azure-AI programming.

## Setup Azure AI Services

### Request for Azure OpenAI Service access
First thing first, request for Azure Open-AI service access. Don't worry, initially I had a doubt if my request will be approved? however my request got approved in 24 hours.

[Request Access to Azure OpenAI Service
](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUNTZBNzRKNlVQSFhZMU9aV09EVzYxWFdORCQlQCN0PWcu)

### Azure Open-AI Service setup
1. In your Azure Portal account search for Azure OpenAI and then select "Azure OpenAI" service.
   ![image](https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/f9ca7994-b570-46a4-b515-b7f3671dfe49)

2. After following step#1 you will see below page. Select "Create Azure OpenAI" button and follow remaining steps.
   ![image](https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/3ebc7772-a747-49c5-a296-0e298872c1f8)

3. Once you created Azure OpenAI service you go to your Azure OpenAI service resource and then select "Go to Azure OpenAI Studio" link.
   <img width="934" alt="image" src="https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/cf7f70d2-bc4c-4fce-ab57-be26b29ded08">

4. Following above link you should bring you to this beautiful page.
   <img width="928" alt="image" src="https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/5b317379-80f3-43f8-a6d8-ab4f662240ca">

5. Now select "Deployments" option from left-menu and that should bring to this page.
   <img width="954" alt="image" src="https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/12618250-ed45-4af6-a8c5-ac6c351e7046">

6. Now create deployments by selecting "Create new Deployment" button. If you notice in below image, I created two deployments. First deployment for text-embeddings using OpenAI "text-embedding-ada-002" model and second deployment for chat/chat-completion using "gpt-35-turbo" model.
  <img width="776" alt="image" src="https://github.com/meetrais/Azure-AI-Search-OpenAI/assets/17907862/c4e5eb0c-06dc-46ea-a361-e708db73410f">

## Deep-Dive into Code
Assuming by this time you have your Azure-AI services setup complete and you created model deployments in Azure-OpenAI, lets deep-dive into the code. Please refer to code folder of programming language of your choice above or you can use below link.

[Java](https://github.com/meetrais/Azure-AI-Search-OpenAI/tree/main/Java)


