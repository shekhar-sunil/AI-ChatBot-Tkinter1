import tkinter as tk
from tkinter import scrolledtext
import random
from datetime import datetime

# Create main window
window = tk.Tk()
window.title("AI ChatBot")
window.geometry("500x600")

# Chat display area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled', bg="#6e55aa", fg="white", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# User input field
user_input = tk.Entry(window, font=("Arial", 14),bg="#6e55aa", fg="white", insertbackground="white")
user_input.pack(padx=10, pady=10, fill=tk.X)

# Chatbot memory
name = ""

# Responses
greetings = ["hello", "hi", "hey"]
greeting_responses = ["I'm fine, thanks! 😊",
    "Doing great! 😎",
    "All good here! 👍"]

how_are_you_responses = [
    "I'm fine, thanks! 😊",
    "Doing great! 😎",
    "All good here! 👍"
]

# Function to display message
def display_message(message):
    chat_area.config(state='normal')
    chat_area.insert(tk.END, message + "\n")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)

# Chatbot logic
def chatbot_response(user_text):
    global name
    user_text = user_text.lower()

    if user_text in ["bye", "exit", "quit"]:
        display_message("🤖 Bot: Goodbye! 👋")
        window.quit()

    elif user_text in greetings:
        display_message("🤖 Bot: " + random.choice(greeting_responses))

    elif "name" in user_text:
        if name == "":
            name = user_input.get()
            display_message(f"🤖 Bot: Nice to meet you, {name}!")
        else:
            display_message(f"🤖 Bot: Your name is {name}")

    elif "how are you" in user_text:
        display_message("🤖 Bot: " + random.choice(how_are_you_responses))

    elif "time" in user_text:
        now = datetime.now()
        display_message("🤖 Bot: Current time is " + now.strftime("%H:%M:%S"))

    elif "joke" in user_text:
        display_message("🤖 Bot: Why do programmers prefer dark mode? Because light attracts bugs 😄")
    elif "sad" in user_text:
        display_message("🤖 Bot: Don't worry, things will get better 💙")
    elif "happy" in user_text:
        display_message("🤖 Bot: That's awesome! Keep smiling 😄✨")
    else:
        display_message("🤖 Bot: Sorry, I don't understand 😅")
    
# Send button function
def send_message():
    text = user_input.get()
    if text.strip() == "":
        return

    display_message("You: " + text)
    chatbot_response(text)
    user_input.delete(0, tk.END)

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

# Enter key binding
window.bind('<Return>', lambda event: send_message())

# Welcome message
display_message("🤖 Bot: Hello! I am your chatbot.")

# Run app
window.mainloop()