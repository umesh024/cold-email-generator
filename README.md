# 📨 cold-email-generator

A smart cold email generator for services companies, built using **GROQ**, **LangChain**, and **Streamlit**. This tool allows users to input a company’s careers page URL, extract job listings from it, and generate personalized cold outreach emails with relevant portfolio links — all tailored to each job description.

---

## How It Works

1. **Input:** Careers page URL (e.g., Nike’s job listing page)
2. **Processing:** Extracts job descriptions using LLM
3. **Vector Search:** Finds relevant portfolio links from a ChromaDB vector store
4. **Generation:** Crafts a personalized cold email using GROQ and LangChain
5. **Output:** A compelling outreach email with links to similar work

## Set-up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```
