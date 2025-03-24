
# Daily Behavioral Question Generator

![GitHub Workflow Status](https://github.com/0KeirLi0/Daily_Interview_Question/actions/workflows/main.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Daily Behavioral Question Generator** is a Python-based tool that generates a daily behavioral interview question using the OpenAI API and emails it to subscribers. Designed to help you practice interview skills consistently, it runs automatically via GitHub Actions.

## Features
- Generates random behavioral questions from topics like leadership, teamwork, problem-solving, and adaptability.
- Provides a suggested framework and sample answer tailored to a user-provided background.
- Sends questions daily to specified email addresses.
- Logs each question and answer to `question_log.txt` for review.

## Project Structure


```
Daily_Interview_Question/
├── .github/
│   ├── workflows/
│   │   └── main.yml          # GitHub Actions workflow
│   └── FUNDING.yml           
├── src/
│   ├── actions/
│   │   └── daily_question.py # Script for GitHub Actions automation
│   ├── utils/
│   │   ├── email_sender.py   # Email sending module
│   │   └── question_generator.py  # Question generation module
│   └── main.py               # Local execution script
├── .gitattributes            # Git attributes configuration
├── .gitignore                # Git ignore file
├── env.example               # Sample environment variables
├── LICENSE                   # MIT License
├── README.md                 # This file
└── requirements.txt          # Python dependencies
```

## Prerequisites
- Python 3.8 or higher
- An OpenAI API key ([Get it here](https://platform.openai.com/account/api-keys))
- A Gmail account with an app-specific password ([See Google Account Help](https://support.google.com/accounts/answer/185833))

## Setup for GitHub Actions
This project is optimized to run automatically via GitHub Actions.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/0KeirLi0/Daily_Interview_Question.git
   cd Daily_Interview_Question
   ```

2. **Configure GitHub Secrets**:
   - Go to `Settings > Secrets and variables > Actions > Secrets` in your repository.
   - Add the following:
     - `OPENAI_API_KEY`: Your OpenAI API key
     - `OPENAI_BASE_URL`: OpenAI API base URL (e.g., `https://api.openai.com/v1`)
     - `SENDER`: Your email address (e.g., `your_email@gmail.com`)
     - `RECEIVER`: Recipient email(s), comma-separated (e.g., `email1@gmail.com,email2@gmail.com`)
     - `PASSWORD`: App-specific password for your email
     - `BACKGROUND` (optional): Background info for personalized answers

3. **Push to GitHub**:
   - Commit and push changes. The workflow in `.github/workflows/main.yml` runs daily at UTC 00:00 (adjustable via `cron`).

## Usage Example
Once running:
- **Question**: "Describe a time you resolved a conflict in a team."
- **Framework**: STAR (Situation, Task, Action, Result)
- **Sample Answer**: Generated based on `BACKGROUND`.
- **Output**: Emailed to `RECEIVER` and logged in `question_log.txt`.

## Dependencies
See `requirements.txt`:
```
openai==1.60.1
pydantic==2.10.3
python-dotenv==1.0.1
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to your fork (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or feedback, email [lihk0852@gmail.com](mailto:lihk0852@gmail.com) or open an [Issue](https://github.com/0KeirLi0/Daily_Interview_Question/issues).

