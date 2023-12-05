import random
print("Hi class!")
print("This is fun?, what a great second day")

def print_hello():
    languages = ["English", "Spanish", "French", "German", "Italian"]
    hello_messages = {
        "English": "Hello",
        "Spanish": "Hola",
        "French": "Bonjour",
        "German": "Guten Tag",
        "Italian": "Ciao"
    }
    
    random_language = random.choice(languages)
    hello_message = hello_messages[random_language]
    
    print(f"{hello_message}, {random_language}!")

print_hello()