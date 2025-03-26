import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
from src.utils.question_generator import generate_behavioral_question
from src.utils.email_sender import send_email

if load_dotenv():
    # Set up environment variables
    KEY = os.getenv("OPENAI_API_KEY")
    URL = os.getenv("OPENAI_BASE_URL")
    SENDER = os.getenv("SENDER")
    RECEIVER = os.getenv("RECEIVER")
    PASSWORD = os.getenv("PASSWORD")
    try:
        MODEL = os.getenv("MODEL")
    except:
        MODEL = ""
else:
    raise ValueError("Environment variables are not set")

client = OpenAI(
    api_key=KEY,
    base_url=URL
)

def main():
    try:
        with open('background.txt', 'r', encoding='utf-8') as file:
            background = file.read()
    except FileNotFoundError:
        print("Background file does not exist.")
        background = "NULL"

    response = generate_behavioral_question(background, client, MODEL)
    
    if isinstance(response, str):
        print(response)
        return
    
    question = str(response.behavioral_question)
    suggested_framework = str(response.suggested_framework)
    sample_answer = str(response.sample_answer)
    topic = str(response.topic)
    
    send_email(question, suggested_framework, sample_answer, topic, SENDER, RECEIVER, PASSWORD)
    
    with open("question_log.txt", "a", encoding="utf-8") as f:
        f.write(f"********************************\n\nTopic: {topic}\nQuestion: {question}\nAnswer: {sample_answer}\n\n")

if __name__ == "__main__":
    main()