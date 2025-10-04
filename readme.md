## CV Savvy (AI-powered Resume Review)

CV Savvy is a Streamlit app that analyzes PDF resumes using generative AI (Google’s Gemini model via the `google.generativeai` client). It provides actionable feedback focused on clarity, impact, structure (including STAR-style examples), and overall professionalism.

### Key Goals

* Provide clear, actionable improvements for work experience bullets using the STAR (Situation, Task, Action, Result) method  
* Highlight formatting and length issues that affect recruiter readability  

### Features

* Upload PDF resumes for automated analysis  
* AI-powered feedback on content, STAR-style bullet improvements, structure, and length  
* Resume scoring (1–10) with a category breakdown  
* Simple Streamlit UI for fast reviews  

### Quickstart

1. Clone the repository and navigate into the folder
```Bash
git clone https://github.com/DavidMajomi/cv-savvy.git
cd cv-savvy
```

2. Create and activate a virtual environment  
```Bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies  
```Bash
pip install -r requirements.txt
```

4. Configure environment variables (see Configuration below)

5. Launch the app  
```Bash
streamlit run app.py
```

### Configuration

The app uses Google's Gemini model via the `google.generativeai` package (`genai.GenerativeModel('gemini-pro')`). Environment variables must be set to enable AI and email functionality.

Environment variables used in `app.py`:

* `GOOGLE_API_KEY` — your Google API key used to authenticate with Gemini  
* `SENDER_EMAIL` — email address used by `redmail.gmail` to send review emails  
* `EMAIL_key` — the SMTP/app password used by `redmail.gmail` (referred to as `EMAIL_key` in the code)  

### Usage

* After starting the app, open the local Streamlit URL in your browser  
* Upload a PDF resume and wait for analysis  
* View the score and improvement suggestions  
* If email is configured, enter a recipient address to send the full report  

### Development Notes

* Main entry point: `app.py`  
* Dependencies managed via `requirements.txt`  

### Future Improvements

* Add unit and integration tests for PDF parsing and AI interaction  
* Implement CI checks for linting and formatting  
* Include a toggle to redact or anonymize personal data before sending to external APIs  

### License and Contact

This project is provided as-is. To contribute or ask questions, open an issue or pull request on the repository.
