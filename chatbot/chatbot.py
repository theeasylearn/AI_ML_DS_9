import knowledge_base as k 
import spacy 
import random as rd 
import re
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
nlp = spacy.load('en_core_web_sm')
agent = "Skisha: "
subjects = k.knowledge.get('knowledge_base') #return list 
def preprocess(question, print_func=print):
    isFound = False
    for item in k.greetings:
        if question == item.get('message'):
            print_func(agent,item.get('reply'))
            return
    global subjects
    doc = nlp(question)
    tokens_lower = [t.text.lower() for t in doc]
    question_lower = question.lower()
    
    if "mobile" in tokens_lower or "whatsapp" in tokens_lower or "contact no" in question_lower:
        for subject in subjects:
            if subject.get('id') == 'contact_01':
                print_func(subject.get('contact_no'))
                return

    if "email" in tokens_lower or "mail" in tokens_lower:
        for subject in subjects:
            if subject.get('id') == 'contact_01':
                print_func(subject.get('email'))
                return

    if "location" in tokens_lower or "address" in tokens_lower or "situated at" in question_lower:
        for subject in subjects:
            if subject.get('id') == 'location_01':
                print_func(subject.get('address'))
                return
    for subject in subjects:
        if question in subject.get('utterances'):
            if subject.get('answer_variations') != None:
                if rd.randint(1,2) == 1: #return answer
                    print_func(subject.get('answer'))
                else:
                    size = len(subject.get('answer_variations'))
                    print_func(subject.get('answer_variations')[rd.randint(0,size-1)])
            else:
                print_func(subject.get('answer'))
            return
    metadata_key_map = {
        'fees': 'fees',
        'fee': 'fees',
        'duration': 'duration',
        'durations': 'duration',
        'level': 'level',
        'levels': 'level',
        'category': 'category',
        'categories': 'category'
    }
    for token in doc:
        for subject in subjects[:8]:
            if subject.get('type') == 'Course' and token.text.lower() in [k.lower() for k in subject.get('keywords', [])]:
                metadata = subject.get('metadata', {})
                for m_token in doc:
                    m_text_lower = m_token.text.lower()
                    if m_text_lower in metadata_key_map:
                        m_key = metadata_key_map[m_text_lower]
                        if m_key in metadata:
                            val = metadata[m_key]
                            if m_key == 'fees' and isinstance(val, str):
                                val = val.replace('₹', '').replace(',', '').strip()
                            verb = 'are' if m_text_lower == 'fees' else 'is'
                            clean_question = question.rstrip('?.! ')
                            print_func(f"{clean_question} {verb} {val}")
                            return

    for token in doc:
        for subject in subjects:
            if token.text.lower() in [k.lower() for k in subject.get('keywords', [])]:
                #print(token,subject.get('keywords'))
                if subject.get('answer_variations') != None:
                    if rd.randint(1,2) == 1: #return answer
                        print_func(subject.get('answer'))
                    else:
                        size = len(subject.get('answer_variations'))
                        print_func(subject.get('answer_variations')[rd.randint(0,size-1)])
                else:
                    print_func(subject.get('answer'))
                isFound = True
                return

    if isFound == False:
        print_func(agent,"sorry i dont have answer of your question")
def get_user_info():
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    mobile_regex = r'^\+?[0-9]{10,12}$'
    
    print("Welcome! Please provide your details before starting.")
    name = input("Enter your name: ")
    
    while True:
        email = input("Enter your email: ")
        if re.match(email_regex, email):
            break
        print("Invalid email. Please try again.")
        
    while True:
        mobile = input("Enter your mobile number: ")
        if re.match(mobile_regex, mobile):
            break
        print("Invalid mobile number. Please try again.")
        
    return name, email, mobile

def load_env():
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip()

def send_chat_log_email(filepath, sender_name):
    load_env()
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    try:
        smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    except ValueError:
        smtp_port = 587
    sender_email = "karan.bhatt.bhavnagar@gmail.com"
    sender_password = "yjbi tmwf onch ufcy"
    recipient_email = "theeasylearn@gmail.com"
    
    if not sender_email or not sender_password:
        print("\n[Warning] Chat log saved locally. Email sending skipped because SENDER_EMAIL or SENDER_PASSWORD environment variables are not set.")
        return False
        
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            log_content = f.read()
            
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"Chat Log - {sender_name}"
        
        msg.attach(MIMEText(log_content, 'plain', 'utf-8'))
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print(f"\nChat log successfully emailed to {recipient_email}.")
        return True
    except Exception as e:
        print(f"\nFailed to send chat log email: {e}")
        return False

if __name__ == '__main__':
    name, email, mobile = get_user_info()
    start_time = datetime.now()

    log_dir = "log"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    clean_name = re.sub(r'[^a-zA-Z0-9]', '_', name)
    timestamp = start_time.strftime("%Y-%m-%d_%H-%M-%S")
    log_filepath = os.path.join(log_dir, f"{clean_name}_{timestamp}.txt")

    log_file = open(log_filepath, "w", encoding="utf-8")
    log_file.write(f"Name: {name}\n")
    log_file.write(f"Email: {email}\n")
    log_file.write(f"Mobile: {mobile}\n")
    log_file.write("-" * 40 + "\n")
    log_file.flush()

    _original_print = print
    def print(*args, **kwargs):
        msg = " ".join(str(arg) for arg in args)
        if not log_file.closed:
            log_file.write(msg + "\n")
            log_file.flush()
        _original_print(*args, **kwargs)

    while True:
        question = input("You : ")
        log_file.write(f"You : {question}\n")
        log_file.flush()
        if question == "bye" or question == "exit":
            print(agent, " Good bye see you again,")
            break 
        else:    
            preprocess(question)

    end_time = datetime.now()
    duration = end_time - start_time
    duration_str = f"{duration.seconds // 60} minutes, {duration.seconds % 60} seconds"
    log_file.write("-" * 40 + "\n")
    log_file.write(f"Conversation duration: {duration_str}\n")
    log_file.close()

    send_chat_log_email(log_filepath, name)