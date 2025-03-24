import os
from openai import OpenAI
from src.utils.question_generator import generate_behavioral_question
from src.utils.email_sender import send_email

# Directly use environment variables from GitHub Secrets
KEY = os.getenv("OPENAI_API_KEY")
URL = os.getenv("OPENAI_BASE_URL")
SENDER = os.getenv("SENDER")
RECEIVER = os.getenv("RECEIVER")
PASSWORD = os.getenv("PASSWORD")
BACKGROUND = os.getenv("BACKGROUND")

# Check if required variables are set
if not all([KEY, URL, SENDER, RECEIVER, PASSWORD]):
    raise ValueError("One or more required environment variables are not set")

# Create OpenAI client
client = OpenAI(
    api_key=KEY,
    base_url=URL
)

def main():
    # Use background from environment variable, default to "NULL" if not set
    background = BACKGROUND if BACKGROUND else "NULL"

    # Generate question
    response = generate_behavioral_question(background, client, model="gpt-4o-mini")
    
    if isinstance(response, str):
        print(response)
        return
    
    question = str(response.behavioral_question)
    suggested_framework = str(response.suggested_framework)
    sample_answer = str(response.sample_answer)
    topic = str(response.topic)
    
    # Send email
    send_email(question, suggested_framework, sample_answer, topic, SENDER, RECEIVER, PASSWORD)
    
    # Log the question
    with open("question_log.txt", "a", encoding="utf-8") as f:
        f.write(f"********************************\n\nTopic: {topic}\nQuestion: {question}\nAnswer: {sample_answer}\n\n")

if __name__ == "__main__":
    main()