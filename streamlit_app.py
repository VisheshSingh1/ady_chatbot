import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

def main():
    st.title("Farming Chatbot")
    
    # User input field
    user_input = st.text_input("Enter your question:")
    
    # Button to submit user input
    if st.button("Submit"):
        # Call function to generate chatbot response
        bot_response = generate_response(user_input)
        
        # Display chatbot's response
        st.write("Chatbot:", bot_response)

def generate_response(user_input):
    # Call OpenAI API to generate response
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the engine according to your preference
        prompt=user_input,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    main()
