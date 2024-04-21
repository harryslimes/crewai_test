from crew import EmailResponderCrew

email_spam = "Good day to you fine sir, I am a prince from the country of Nigeria and I am looking for help moving gold into your country. I need person to keep gold and I will pay 10 million dollars in bullion. Please reply quickly as time is a running out."
email_important = "Hello son, it's your father. Your mother died last night. Can you come to the funeral?"
emails = [email_spam, email_important]
for email in emails:
    inputs = {"email": email}
    output = EmailResponderCrew(default_model="llama3-8B-instruct-q8-quantfactory").crew().kickoff(inputs=inputs)
    print(output)