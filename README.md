# Daily Behavioral Question Generator

This project is a Python script that generates a daily behavioral interview question using the OpenAI API and sends it to your email. It’s designed to help you practice interview skills consistently.

## Features
- Generates a random behavioral question based on topics like leadership, teamwork, problem-solving, communication, and adaptability.
- Sends the question to your specified email address daily.
- Logs each question to a local file (`question_log.txt`) for review.

## Prerequisites
Before running the script, ensure you have:
- **Python 3.7 or higher** installed on your system.
- An **OpenAI API key** (get it from [OpenAI](https://platform.openai.com/account/api-keys)).
- A **Email account** with an app-specific password (if using Gmail; see [Google Account Help](https://support.google.com/accounts/answer/185833)).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/0KeirLi0/Daily_Interview_Question.git
   cd daily-question-question
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Copy the sample `.env` file:
     ```bash
     cp env.example .env
     ```
   - Open `.env` in a text editor and fill in your values:
     ```
     OPENAI_API_KEY="your_openai_api_key_here"
     OPENAI_BASE_URL=""  # Leave empty for default
     SENDER="your_email@gmail.com"
     PASSWORD="your_email_app_password_here"
     RECEIVER="email1@gmail.com, email2@gmail.com, email3@gmail.com"
     ```

## Usage
1. **Run the Script Manually**:
   ```bash
   python main.py
   ```
   - This generates a question and sends it to the specified email, also logging it to `question_log.txt`.

2. **Schedule Daily Execution** (Optional):
   - Use a scheduler like `cron` (Linux/macOS) or Task Scheduler (Windows) to run the script daily.
   - Example `cron` command (edit with `crontab -e`):
     ```bash
     0 8 * * * /path/to/.venv/bin/python /path/to/main.py
     ```
   - Replace paths with your actual locations; this runs at 8 AM daily.

## File Structure
- `main.py`: The main Python script.
- `action_daily_question.py`: The Python script for github actions.
- `env.example`: Sample environment variable file (fill your own in `.env`).
- `requirements.txt`: List of Python dependencies.
- `.gitignores`: Excludes sensitive or unnecessary files from Git.
- `question_log.txt`: Generated log file for tracking questions (created after running).
- `LICENSE`: MIT License file (or your chosen license).

## Dependencies
Listed in `requirements.txt`:
```
openai==1.60.1
pydantic==2.10.3
python-dotenv==1.0.1
```

## Contributing
Feel free to fork this repository, submit pull requests, or open issues for suggestions or bug reports.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, reach out to lihk0852@gmail.com.
