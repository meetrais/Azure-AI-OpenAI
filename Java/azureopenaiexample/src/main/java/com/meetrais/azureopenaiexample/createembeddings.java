package com.meetrais.azureopenaiexample;
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  

@RestController  
public class createembeddings {
    @RequestMapping("api/createembeddings")  
    public String createandSaveEmbeddings()   
    {  
        
        
        
        return "true";  
        
    }  
}
