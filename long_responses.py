import random

R_EATING = "I can eat your brain up by not giving good replies obviously! hahahhah!)"
R_ADVICE = "I don't know, go to the internet see for yourself!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response