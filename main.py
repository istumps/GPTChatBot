#run with python main.py
import openai

openai.api_key = "YOUR OPEN AI API KEY!"

def chat_with_GPT(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].messaage.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_GPT(user_input)
        print ("Chatbot: ", response)

