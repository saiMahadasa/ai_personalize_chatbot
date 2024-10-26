from flask import Flask, render_template, request, jsonify
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os


prompt = open('pdf_text', 'r').read()

hotel_assistant_template = prompt + """
You are "Sai Mahadasa", a professional assistant specialized in providing brief, clear responses to questions about my career background. 

- Only respond to questions directly related to my professional experience, skills, and projects. 
- Keep answers short and conversational, focusing on providing relevant insights about my background.
- If a question falls outside my professional scope, respond with, "I'm unable to assist with that, sorry!"

Question: {question} 
Answer:
"""

hotel_assistant_prompt_template = PromptTemplate( 
    input_variables=["question"], 
    template=hotel_assistant_template 
    ) 

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env
api_key = os.getenv("OPENAI_API_KEY")



llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0, openai_api_key = api_key) 


llm_chain = hotel_assistant_prompt_template | llm 

def query_llm(question): 
    response = llm_chain.invoke({'question': question}) 
    return response 

app = Flask(__name__) 

@app.route("/") 
def index(): 
    return render_template("index.html") 

@app.route("/chatbot", methods=["POST"]) 
def chatbot(): 
    data = request.get_json() 
    question = data["question"] 
    response = query_llm(question) 
    return jsonify({"response": response}) 

if __name__ == "__main__": 
    app.run(debug=True)