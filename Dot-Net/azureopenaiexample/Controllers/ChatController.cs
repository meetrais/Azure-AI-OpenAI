using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using azureopenaiexample.Models;
using Azure.AI.OpenAI;
using Azure;
using DotNetEnv;
using static System.Environment;
using iText.Kernel.Pdf;
using System.Text;
using iText.Kernel.Pdf.Canvas.Parser.Listener;
using iText.Kernel.Pdf.Canvas.Parser;


namespace azureopenaiexample.Controllers;

public class ChatController : Controller
{
    private readonly ILogger<HomeController> _logger;

    public ChatController(ILogger<HomeController> logger)
    {
        Env.Load();
        _logger = logger;

    }

    public IActionResult Index()
    {
        return View();
    }

    [HttpGet]
    public async Task<IActionResult> GetChatResponse(string userQuestion)
    {
        try
        {
            string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
            string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY");
            string model = Environment.GetEnvironmentVariable("AZURE_OPENAI_MODEL");
            OpenAIClient client = new OpenAIClient(new Uri(endpoint), new Azure.AzureKeyCredential(key));

            var chatCompletionOptions = new ChatCompletionsOptions(){
                DeploymentName=model,
                Messages={
                    new ChatRequestSystemMessage("You are a helpful AI assistant."),
                    /// Single-shot Prompt
                    new ChatRequestUserMessage("Is Washington DC Capital of USA?"),
                    new ChatRequestAssistantMessage("Yes, Washington DC is the Capital of USA"),
                    /////////////
                    new ChatRequestUserMessage(userQuestion)
            },
            MaxTokens=500,
            Temperature=2 //Max Creativity
            };

            Response<ChatCompletions> response = await client.GetChatCompletionsAsync(chatCompletionOptions);

            var result = response.Value.Choices.First().Message.Content;

            return Json(new {Response=result});
        }
        catch(Exception ex){
            return Json(new {Response=ex.Message});
        }
    }

    [HttpGet]
    public async Task<IActionResult> GetChatWithYourDataResponse(string userQuestion)
    {
        try
        {
            string endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
            string key = Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY");
            string model = Environment.GetEnvironmentVariable("AZURE_OPENAI_MODEL");

            OpenAIClient client = new OpenAIClient(new Uri(endpoint), new Azure.AzureKeyCredential(key));
            string pdfText = GetTextFromPDF(@"YOUR_PDF_FILE_PATH");
            if(pdfText.Length>8192)
                pdfText = pdfText.Substring(0,8192);//I am using gpt-35-turbo which has max context length of 8192.
            var chatCompletionOptions = new ChatCompletionsOptions(){
                DeploymentName=model,
                Messages={
                    new ChatRequestSystemMessage("You are a helpful AI assistant."),
                    new ChatRequestUserMessage("Information from your PDF: " + pdfText),
                    new ChatRequestUserMessage(userQuestion)
            },
            MaxTokens=500,
            Temperature=0//No Creativity, more grounded response
            };

            Response<ChatCompletions> response = await client.GetChatCompletionsAsync(chatCompletionOptions);

            var result = response.Value.Choices.First().Message.Content;

            return Json(new {Response=result});
        }
        catch(Exception ex){
            return Json(new {Response=ex.Message});
        }
    }

    private  string GetTextFromPDF(string filePath)
    {
        try
        {
            PdfDocument pdfDocument = new PdfDocument(new PdfReader(filePath));
            StringBuilder text = new StringBuilder();

            for(int i=1; i<=pdfDocument.GetNumberOfPages(); i++)
            {
                PdfPage pdfPage= pdfDocument.GetPage(i);
                ITextExtractionStrategy strategy = new SimpleTextExtractionStrategy();
                string currentPageText = PdfTextExtractor.GetTextFromPage(pdfPage, strategy);
                text.Append(currentPageText);
            }

            pdfDocument.Close();
            return text.ToString();

        }
        catch(Exception ex)
        {
        return ex.Message;
        }
     }



}
