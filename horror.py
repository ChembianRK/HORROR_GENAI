import os
import google.generativeai as genai
import streamlit as st


api_key = "AIzaSyAgy30p0Aba9V1zWnxVAFwmwLQzagC7Ing"
genai.configure(api_key=api_key)


generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)


def generate_horror_story(character_name, situation, no_of_lines):
    prompt = (
        f"Write me a horror story with the character name \"{character_name}\" "
        f"and situation \"{situation}\" in {no_of_lines} lines."
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    return response.text


def main():
    st.title("🧟‍♂️ Horror Story Generator")
    st.write("Enter the details below to generate your custom horror story:")

    character_name = st.text_input("Character Name")
    situation = st.text_input("Situation")
    no_of_lines = st.number_input("Number of Lines", min_value=1, value=5)

    if st.button("Generate Story"):
        with st.spinner("Generating your horror story..."):
            try:
                story = generate_horror_story(character_name, situation, no_of_lines)
                st.subheader("Your Horror Story:")
                st.write(story)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    main()
