import smtplib
from email.message import EmailMessage

def send_email(question, suggested_framework, answer, topic, sender_email, receiver_email, password):
    """
    Sends an email with the daily behavioral question, suggested framework, and sample answer.

    Args:
        question (str): The daily behavioral question to be sent.
        suggested_framework (str): The suggested framework for answering the question.
        answer (str): A sample answer to the question.
        topic (str): The topic of the question.
        sender_email (str): The email address of the sender.
        receiver_email (str): The email address(es) of the receiver(s), comma-separated if multiple.
        password (str): The password or app-specific password for the sender's email account.

    Returns:
        None
    """
    msg = EmailMessage()
    msg["Subject"] = f"Daily Behavioral Questions:[{topic}]"
    msg["From"] = sender_email
    msg["To"] = receiver_email.split(",")
    msg.set_content(f"""Today's Question: {question} 
                    \n******************* \n
                    Suggested Framework: {suggested_framework}
                    \n******************* 
                    \n*\n*\n*\n*\n*\nSample Answer: {answer}
                    """)
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Email sent failed: {str(e)}")