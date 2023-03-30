# :)
# :(
# :()
# :/\
# :|
from random import randrange

MOOD_NUMBER = 5

VERY_HAPPY_MOOD = ":D"
HAPPY_MOOD = ":)"
NORMAL_MOOD = ":|"
BAD_MOOD = ":("
ANGRY_MOOD = ">:("


def detect_mood():
    m = randrange(MOOD_NUMBER)
    if m == 1:
        mood = VERY_HAPPY_MOOD
    elif m == 2:
        mood = HAPPY_MOOD
    elif m == 3:
        mood = NORMAL_MOOD
    elif m == 4:
        mood = BAD_MOOD
    else:
        mood = ANGRY_MOOD

    return mood


def main():
    mood = detect_mood()
    print("I feel your mood is", mood, "!")


# main()
