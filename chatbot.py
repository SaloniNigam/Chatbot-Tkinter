import tkinter as tk
from tkinter import scrolledtext
import random


# ---------------- Chatbot Logic ----------------
def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    greetings = [
        "hello", "hi", "hey", "hola", "namaste",
        "good morning", "good evening", "what's up"
    ]

    farewells = [
        "bye", "goodbye", "byee", "see you later",
        "see ya", "take care", "later"
    ]

    thanks = [
        "thanks", "thank you", "thank you soo much",
        "thanks a lot", "appreciate it", "many thanks"
    ]

    how_are_you = [
        "how are you", "how are you doing"
    ]

    project_topics = {
        "project": "This chatbot is my project. It uses Python and Tkinter for the GUI.",
        "tkinter": "Tkinter is Python's standard library for creating GUIs.",
        "chatbot": "A chatbot is software that can talk with users and answer questions.",
        "pydroid": "This project can also run on Pydroid 3.",
        "python": "Python is a simple and powerful programming language created by Guido van Rossum.",
        "creator": "My creator is a B.Tech student learning Python.",
        "gui": "The user interface was built using Tkinter.",
        "who are you": "I am a mini chatbot."
    }

    if user_input in greetings:
        return random.choice([
            "Hello! How can I help you today?",
            "Hi there!",
            "Hey! Nice to meet you."
        ])

    elif user_input in farewells:
        return random.choice([
            "Goodbye! Have a great day!",
            "See you later!",
            "Take care!"
        ])

    elif any(text in user_input for text in how_are_you):
        return "I'm doing great! Thanks for asking."

    elif any(text in user_input for text in thanks):
        return "You're welcome!"

    else:
        for keyword, response in project_topics.items():
            if keyword in user_input:
                return response

        return random.choice([
            "Sorry, I don't understand.",
            "Please rephrase your question.",
            "I'm only programmed for limited responses.",
            "Can you ask something related to this project?"
        ])


# ---------------- GUI ----------------
class ChatbotGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot Project")
        self.master.geometry("450x550")
        self.master.configure(bg="plum")

        # Chat Area
        self.chat_history = scrolledtext.ScrolledText(
            master,
            wrap=tk.WORD,
            state='disabled',
            font=("Arial", 10),
            bg="white",
            fg="black"
        )
        self.chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input Frame
        self.input_frame = tk.Frame(master, bg="plum")
        self.input_frame.pack(fill=tk.X, padx=10, pady=10)

        # Entry Box
        self.user_entry = tk.Entry(
            self.input_frame,
            font=("Arial", 11)
        )
        self.user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        self.user_entry.bind("<Return>", self.send_message)

        # Send Button
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            command=self.send_message,
            bg="orchid",
            fg="white",
            font=("Arial", 10, "bold")
        )
        self.send_button.pack(side=tk.RIGHT, padx=5)

        # Welcome Message
        self.display_message(
            "Chatbot",
            "Hello! I am your chatbot. Ask me something."
        )

    def display_message(self, sender, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_history.config(state='disabled')
        self.chat_history.see(tk.END)

    def send_message(self, event=None):
        user_message = self.user_entry.get().strip()

        if user_message:
            self.display_message("You", user_message)
            self.user_entry.delete(0, tk.END)

            bot_response = get_bot_response(user_message)
            self.master.after(
                500,
                lambda: self.display_message("Chatbot", bot_response)
            )


# ---------------- Main Program ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()