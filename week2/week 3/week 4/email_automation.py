import csv

# Email settings
SENDER_EMAIL = "harsh49saini@gmail.com"
CSV_FILE = "students.csv"

# Keep True to preview emails without sending them
TEST_MODE = True


def create_email(name):
    """Create a personalized email message."""
    subject = "Internship Project Update"

    message = f"""Hello {name},

I hope you are doing well.

This is a personalized sample email created using Python.
It demonstrates how email messages can be prepared automatically.

Regards,
Python Email Automation Tool
"""
    return subject, message


def is_valid_email(email):
    """Perform a basic email-format check."""
    if not email or " " in email:
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    if ".." in email:
        return False

    return True


def preview_emails():
    """Read recipients and display email previews."""

    if not TEST_MODE:
        print("Safety check: sending is not implemented.")
        print("No emails will be sent.")
        return

    print("TEST MODE IS ON - NO EMAILS WILL BE SENT")
    print("Sender:", SENDER_EMAIL)
    print()

    valid_count = 0
    skipped_count = 0

    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            # Check the CSV headers
            if not reader.fieldnames:
                print("Error: The CSV file is empty.")
                return

            # Allow headers with accidental surrounding spaces
            reader.fieldnames = [
                field.strip() for field in reader.fieldnames
            ]

            if "name" not in reader.fieldnames:
                print("Error: CSV must contain a 'name' column.")
                return

            if "email" not in reader.fieldnames:
                print("Error: CSV must contain an 'email' column.")
                return

            for row_number, student in enumerate(reader, start=2):
                name = (student.get("name") or "").strip()
                email = (student.get("email") or "").strip()

                # Skip missing information
                if not name or not email:
                    print(
                        f"Skipping row {row_number}: "
                        "name or email is missing."
                    )
                    skipped_count += 1
                    continue

                # Skip invalid email formats
                if not is_valid_email(email):
                    print(
                        f"Skipping row {row_number}: "
                        "invalid email format."
                    )
                    skipped_count += 1
                    continue

                subject, message = create_email(name)

                print("=" * 45)
                print("EMAIL PREVIEW - NOT SENT")
                print("From:", SENDER_EMAIL)
                print("To:", email)
                print("Subject:", subject)
                print()
                print(message)

                valid_count += 1

    except FileNotFoundError:
        print(f"Error: '{CSV_FILE}' was not found.")
        print("Keep it in the same folder as this Python file.")

    except PermissionError:
        print("Error: Permission denied while reading the CSV file.")

    except OSError as error:
        print("Could not read the CSV file:", error)

    else:
        print("=" * 45)
        print("Preview completed.")
        print("Valid recipients:", valid_count)
        print("Skipped rows:", skipped_count)
        print()
        print("Reminder: No emails were sent.")


if __name__ == "__main__":
    preview_emails()
