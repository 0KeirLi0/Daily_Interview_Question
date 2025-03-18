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
    try:
        MODEL = os.getenv("MODEL")
    except:
        MODEL = ""
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

def generate_behavioral_question(background: str, model:str ="gpt-4o-mini"):
    """
    Generates a behavioral interview question based on a random topic, provides a suggested framework for answering the question, 
    and gives a sample answer based on the user's background information.

    This function selects a random topic from a predefined list of behavioral topics, constructs a prompt for the OpenAI model,
    and parses the response to extract the behavioral question, suggested framework, and sample answer. The response is tailored
    based on the user's background information provided as input.

    Args:
        background (str): The user's background information to tailor the sample answer. This can include details about their 
                          work experience, skills, achievements, and other relevant information.
        model (str, optional): The model to use for generating the question and answer. Defaults to "gpt-4o-mini".

    Returns:
        dict: A JSON object containing the following keys:
            - behavioral_question (str): The generated behavioral interview question.
            - suggested_framework (str): The suggested framework for answering the behavioral question.
            - sample_answer (str): A sample answer to the behavioral question, tailored to the user's background.
            - topic (str): The topic of the behavioral question.
    """
    
    topic = random.choice(topics)
    prompt = f'''
    1. Please generate 1 behavioral question related to the topic: {topic}.\n\n 
    2. Provide suggested frammework for answering the question you asked\n\n
    3. Provide sample answer based on user's background information(if any):\n\n{background}\n\n 
    output in JSON format: behavioral_question, suggested_framework, sample_answer, topic
    '''
    try:
        response = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": dedent(prompt)}
            ],
            temperature=0.9,
            response_format= AnsFormmat,
        )
        return response.choices[0].message.parsed
    except Exception as e:
        return f"Error when generating question：{str(e)}"


def send_email(question, suggested_framework, answer, topic):
    """
    Sends an email with the daily behavioral question, suggested framework, and sample answer.

    This function constructs an email message with the provided question, suggested framework, and sample answer.
    It then sends the email to the specified receiver using the SMTP protocol.

    Args:
        question (str): The daily behavioral question to be sent.
        suggested_framework (str): The suggested framework for answering the question.
        answer (str): A sample answer to the question.
        topic (str): The topic of the question.

    Raises:
        Exception: If there is an error sending the email.

    Returns:
        None
    """

    sender_email = SENDER
    receiver_email = RECEIVER
    password = PASSWORD
    
    msg = EmailMessage()
    msg["Subject"] = f"Daily Behavioral Questions:[{topic}]"
    msg["From"] = sender_email
    msg["To"] = receiver_email.split(",")
    msg.set_content(f"""Today's Question：{question} 
                    \n******************* \n
                    Suggested Framework: {suggested_framework}
                    \n******************* 
                    \n*\n*\n*\n*\n*\nSample Answer：{answer}
                    """)
    
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
        print("Background file does not exist.")
        background = "NULL"


    response = generate_behavioral_question(background, MODEL)
    
    question = str(response.behavioral_question)
    suggested_framework = str(response.suggested_framework)
    sample_answer = str(response.sample_answer)
    topic = str(response.topic)
    
    send_email(question, suggested_framework, sample_answer, topic)
    
    with open("question_log.txt", "a", encoding="utf-8") as f:
        f.write(f"********************************\n\nTopic: {topic}\nQuestion: {question}\nAnswer: {sample_answer}\n\n")

if __name__ == "__main__":
    main()
