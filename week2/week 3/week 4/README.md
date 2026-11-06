# Email Automation Tool

## Project Overview
This project is a beginner-friendly Python email automation tool developed as part of the Skill Nexis Python Developer Internship.

It reads recipient details from a CSV file, validates the provided information, and creates personalized email messages in preview mode.

## Features
- Reads recipient names and email addresses from a CSV file.
- Creates personalized email messages.
- Checks for missing names and email addresses.
- Performs basic email-format validation.
- Skips invalid records and displays a summary.
- Supports preview-only test mode.
- Does not send real emails in the current version.

## Technologies Used
- Python
- CSV file handling
- Functions
- Exception handling
- String formatting

## Project Files
- `email_automation.py` — Main Python program.
- `students.csv` — Sample recipient data for testing.
- `README.md` — Project documentation.

## Requirements
- Python 3
- Visual Studio Code or another Python editor

No external Python packages are required for the current version.

## How to Run
1. Download or clone this project.
2. Open the project folder in VS Code.
3. Make sure `students.csv` is in the same folder as `email_automation.py`.
4. Open the terminal in that folder.
5. Run:

   ```bash
   python email_automation.py
   ```

6. Review the personalized email previews and validation summary.

## CSV Format
The CSV file must contain `name` and `email` columns.

Example:

```csv
name,email
harsh,harsh@example.com
mithlesh,mithlesh@example.com
vansh,vansh@example.com
```

These example addresses are placeholders for testing and are not intended for real email delivery.

## Safety Note
The current version runs in test mode. It displays email previews but does not connect to Gmail or send messages. Basic email-format validation does not confirm that an address exists.

The sender address configured for preview is `harsh49saini@gmail.com`. No password or App Password is stored in the project.

## Learning Outcomes
- Reading structured data from CSV files.
- Writing reusable Python functions.
- Validating user data.
- Handling file-related errors.
- Generating personalized messages.
- Testing automation workflows safely.

## Future Improvements
- Add secure Gmail SMTP integration.
- Load credentials from environment variables.
- Add email sending logs and delivery error handling.
- Add automated tests for validation functions.

## Internship
**Program:** Skill Nexis Python Developer Internship  
**Project:** Email Automation Tool  
**Language:** Python