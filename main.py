import os
from groq import Groq

# API Key 
API_KEY = "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"

def get_user_input():
    return input("You: ")

def run(question):
    client = Groq(api_key=API_KEY)  # 🔥 Using the hardcoded API key

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": question}],
        max_tokens=100
    )

    # Extract response correctly
    if hasattr(response, "choices") and response.choices:
        first_choice = response.choices[0]
        if hasattr(first_choice, "message") and hasattr(first_choice.message, "content"):
            print(f"Groq: {first_choice.message.content.strip()}")
        else:
            print("Error: Unexpected response format. No 'message.content' found.")
    else:
        print("Error: No valid response from API.")

if __name__ == "__main__":
    print("Welcome to Groq Chat! Type 'exit' to quit.")
    while True:
        user_input = get_user_input()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        run(user_input)
