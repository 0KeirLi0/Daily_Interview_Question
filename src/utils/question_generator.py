import random
from openai import OpenAI
from pydantic import BaseModel
from textwrap import dedent

# Define the format of the response
class AnsFormmat(BaseModel):
    behavioral_question: str  
    suggested_framework: str
    sample_answer: str
    topic: str

# Behavioral topics
topics = ["Motivation - What drives you to Financial Industry? Ideal candidates are self-motivated, passionate about technologies and products that have a real impact.",
          "Ability to be Proactive - Are you able to take initiative? Given a difficult problem, are you able to figure out how to get it done and execute on it?",
          "Ability to work in an unstructured environment - How well are you able to take ownership in ambiguous situations? Or do you rely on others to be told what to do?",
          "Perseverance - Are you able to push through difficult problems or blockers?",
          "Conflict Resolution - How well are you able to handle and work through challenging relationships?",
          "Empathy - How well are you able to see things from the perspective of others and understand your motivations?",
          "Growth - How well do you understand your strengths, weaknesses and growth areas? Are you making a continued effort to grow?",
          "Communication - Are you able to clearly communicate your stories during the interview?"]

def generate_behavioral_question(background: str, client: OpenAI, model: str = "gpt-4o-mini"):
    """
    Generates a behavioral interview question based on a random topic, provides a suggested framework for answering the question, 
    and gives a sample answer based on the user's background information.

    Args:
        background (str): The user's background information to tailor the sample answer.
        client (OpenAI): Initialized OpenAI client with API key and base URL.
        model (str, optional): The model to use for generating the question and answer. Defaults to "gpt-4o-mini".

    Returns:
        AnsFormmat: A parsed object containing behavioral_question, suggested_framework, sample_answer, and topic.
        str: Error message if generation fails.
    """
    topic = random.choice(topics)
    prompt = f'''
    1. Please generate 1 behavioral question related to the topic: {topic}.\n\n 
    2. Provide suggested framework for answering the question you asked\n\n
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
            response_format=AnsFormmat,
        )
        return response.choices[0].message.parsed
    except Exception as e:
        return f"Error when generating question: {str(e)}"