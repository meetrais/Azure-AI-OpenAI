package com.meetrais.azureopenaiexample;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.ai.azure.openai.AzureOpenAiChatClient;
import org.springframework.ai.chat.ChatResponse;
import org.springframework.ai.chat.messages.AssistantMessage;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.document.Document;
import org.springframework.ai.vectorstore.SearchRequest;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;


@RestController  
public class ChatWithData {

    @Autowired
    private VectorStore vectorStore;

    public ChatWithData(AzureOpenAiChatClient chatClient) {
        this.chatClient = chatClient;
    }

    private final AzureOpenAiChatClient chatClient;

    //private final Prompt systemPrompt = new Prompt(new SystemMessage("You are a helpful assistant. Only answer questions which you know."));

    private List<Message> messageList = new ArrayList<>();

    @GetMapping("/api/getChatResponse")
    public ChatResponse getChatResponse(@RequestParam(value = "message", defaultValue = "") String message) {
        List<Document> result = vectorStore.similaritySearch(SearchRequest.query(message).withTopK(1));
        String content = result.stream().map(document -> document.getContent()).collect(Collectors.joining("\n"));
        messageList.add(new SystemMessage("You are a helpful assistance. Only answer if you know about it."));
        messageList.add(new UserMessage(message));
        messageList.add(new UserMessage(content));
        Prompt prompt = new Prompt(messageList);
        ChatResponse response = chatClient.call(prompt);
        messageList.add(new AssistantMessage(response.getResult().getOutput().toString()));
        return response;
    }
    
}
