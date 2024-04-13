using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using azureopenaiexample.Models;
using Azure.AI.OpenAI;
using Azure;


namespace azureopenaiexample.Controllers;

public class ChatController : Controller
{

    string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
    string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY");
    string model = Environment.GetEnvironmentVariable("AZURE_OPENAI_MODEL");

    private readonly ILogger<HomeController> _logger;

    public ChatController(ILogger<HomeController> logger)
    {
        _logger = logger;
    }

    public IActionResult Index()
    {
        return View();
    }

    [HttpPost]
    public async Task<IActionResult> GetResponse(string userQuestion)
    {
        OpenAIClient client = new OpenAIClient(new Uri(endpoint), new Azure.AzureKeyCredential(key));

        var chatCompletionOptions = new ChatCompletionsOptions(){
            DeploymentName=model,
            Messages={
                new ChatRequestSystemMessage("Helpful a helpful AI assistant."),
                /// Single-shot Prompt
                new ChatRequestUserMessage("Is Washington DC Capital of USA?"),
                new ChatRequestAssistantMessage("Yes, Washington DC is the Capital of USA"),
                /////////////
                new ChatRequestUserMessage(userQuestion)
           },
           MaxTokens=500
        };

        Response<ChatCompletions> response = await client.GetChatCompletionsAsync(chatCompletionOptions);

        var result = response.Value.Choices.First().Message.Content;

        return Json(new {Response=result});
    }

}
