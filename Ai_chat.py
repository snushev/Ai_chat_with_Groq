import tkinter as tk
from groq import Groq

# Initialize Groq API client
client = Groq(api_key='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')  # Replace with your actual API key

# Function to get chat completion from Groq API
def get_ai_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Function to handle user input and display AI response
def send_message():
    user_input = user_input_entry.get()  # Get user input from the entry widget
    if user_input.strip() == "":
        return  # Do nothing if input is empty

    chat_history.config(state="normal")  # Enable editing
    chat_history.insert(tk.END, f"You: {user_input}\n")
    user_input_entry.delete(0, tk.END)  # Clear entry widget

    response = get_ai_response(user_input)
    chat_history.insert(tk.END, f"AI: {response}\n")
    chat_history.config(state="disabled")  # Disable editing

    chat_history.yview(tk.END)  # Scroll to the bottom


# Initialize tkinter window
root = tk.Tk()
root.title("AI Chat Application")

# Configure window layout
root.geometry("400x500")
root.resizable(width=False, height=False)

# Chat history display
chat_history = tk.Text(root, wrap="word", state="disabled", bg="lightgrey", font=("Arial", 12))
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# User input field
user_input_entry = tk.Entry(root, font=("Arial", 14))
user_input_entry.pack(padx=10, pady=10, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12), bg="blue", fg="white")
send_button.pack(pady=5)

# Bind the Enter key to send message
root.bind('<Return>', lambda event: send_message())

# Run the application
root.mainloop()
