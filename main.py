import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from openai import OpenAI
import random
from pydantic import BaseModel
from textwrap import dedent

if load_dotenv():
    # Set up environment variables
    KEY = os.getenv("OPENAI_API_KEY")
    URL = os.getenv("OPENAI_BASE_URL")
    SENDER = os.getenv("SENDER")
    RECEIVER = os.getenv("RECEIVER")
    PASSWORD = os.getenv("PASSWORD")
else:
    raise ValueError("Environment variables are not set")

# Create OpenAI client
client = OpenAI(
    api_key=KEY,
    base_url=URL
)

# Define the format of the response
class AnsFormmat(BaseModel):
    behavioral_question: str  
    suggested_framework: str
    sample_answer: str
    topic: str

# Behavioral topics
topics = ["Motivation and Fit for Finance",
            "Teamwork and Collaboration",
            "Problem-Solving and Analytical Thinking",
            "Handling Pressure and Time Management",
            "Leadership and Initiative",
            "Adaptability and Learning from Feedback",
            "Ethical Judgment and Integrity",]

def generate_behavioral_question(background: str):
    topic = random.choice(topics)
    prompt = f'''
    1. Please generate 1 behavioral question related to the topic: {topic}.\n\n 
    2. Provide suggested frammework for answering the question you asked\n\n
    3. Provide sample answer based on user's background information(if any):\n\n{background}\n\n 
    output in JSON format: behavioral_question, suggested_framework, sample_answer, topic
    '''
    try:
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": dedent(prompt)}
            ],
            temperature=0.7,
            response_format= AnsFormmat,
        )
        return response.choices[0].message.parsed
    except Exception as e:
        return f"Error when generating question：{str(e)}"

def send_email(question, suggested_framework, answer, topic):
    sender_email = SENDER
    receiver_email = RECEIVER
    password = PASSWORD
    
    msg = EmailMessage()
    msg["Subject"] = f"Daily Behavioral Questions:[{topic}]"
    msg["From"] = sender_email
    msg["To"] = receiver_email.split(",")
    msg.set_content(f"Today's Question：{question} \n******************* \n\n Suggested Framework: {suggested_framework}\n******************* \n*\n*\n*\n*\n*\n\n Sample Answer：{answer}")
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Email sent failed：{str(e)}")

def main():
    try:
        with open('background.txt', 'r', encoding='utf-8') as file:
            background = file.read()
    except FileNotFoundError:
        print("Background does not exist.")
        background = "NULL"
    response = generate_behavioral_question(background)
    question = str(response.behavioral_question)
    suggested_framework = str(response.suggested_framework)
    sample_answer = str(response.sample_answer)
    topic = str(response.topic)
    send_email(question, suggested_framework, sample_answer, topic)
    with open("question_log.txt", "a", encoding="utf-8") as f:
        f.write(f"********************************\n\nTopic: {topic}\nQuestion: {question}\nAnswer: {sample_answer}\n\n \n\n")

if __name__ == "__main__":
    main()
