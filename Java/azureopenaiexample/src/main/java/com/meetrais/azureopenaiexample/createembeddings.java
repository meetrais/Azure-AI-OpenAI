package com.meetrais.azureopenaiexample;
import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.ArrayList;
import java.util.List;

import org.springframework.ai.document.Document;
import org.springframework.ai.embedding.EmbeddingClient;
import org.springframework.ai.reader.ExtractedTextFormatter;
import org.springframework.ai.reader.pdf.PagePdfDocumentReader;
import org.springframework.ai.reader.pdf.config.PdfDocumentReaderConfig;
import org.springframework.ai.transformer.splitter.TokenTextSplitter;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.PathResource;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

@Configuration
@RestController  
public class createembeddings {

    @Autowired
    private VectorStore vectorStore;

    @RequestMapping("api/createembeddings")  
    public String createandSaveEmbeddings()   
    {       
        try
        {
            List<Document> documents = new ArrayList<>();
            //Path filePath = Paths.get("/USA.PDF");
            File file = new File("src/main/resources/data/USA.PDF");
            String absolutePath = file.getAbsolutePath();
                PagePdfDocumentReader pdfReader = new PagePdfDocumentReader(
                        "file:" + absolutePath,
                        PdfDocumentReaderConfig.builder()
                                .withPageTopMargin(0)
                                .withPageBottomMargin(0)
                                .withPageExtractedTextFormatter(ExtractedTextFormatter.builder()
                                        .withNumberOfTopTextLinesToDelete(0)
                                        .withNumberOfBottomTextLinesToDelete(3)
                                        .withNumberOfTopPagesToSkipBeforeDelete(0)
                                        .build())
                                .withPagesPerDocument(1)
                                .build());
                documents = pdfReader.get();
            TokenTextSplitter tokenTextSplitter = new TokenTextSplitter();
            documents = tokenTextSplitter.apply(documents);
            vectorStore.add(documents);

            return "true";  
        }
        catch(Exception ex)
        {
            return "false";
        }
        
    }  

}
