import smtplib
from email.mime.text import MIMEText


class FairnessAgent:

    def evaluate(self, scores):

        avg = sum(scores) / len(scores)

        if avg < 0.3:
            return "⚠ Possible bias detected"

        return "Hiring process appears fair"



class EmailSender:

    def send_email(self, receiver_email, candidate_name):

        sender_email = "your_email@gmail.com"
        password = "your_app_password"

        message = f"""
        Hello {candidate_name},

        Congratulations!

        You have been shortlisted for the interview.

        Regards
        FairHire AI System
        """

        msg = MIMEText(message)

        msg["Subject"] = "Interview Shortlisted"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(sender_email,password)
            server.sendmail(sender_email,receiver_email,msg.as_string())