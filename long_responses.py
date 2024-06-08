import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
# Example of what could be in long_responses.py
def generate_long_response(input_text):
    # Placeholder for a function that generates a long response from input text
    response = f"This is a long response based on the input: {input_text}"
    return response
