import random

stages = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

word_list = [
    "apple", "banana", "orange", "grape", "peach", "cherry", "mango", "lemon", "lime", "pear",
    "car", "train", "plane", "bicycle", "motorcycle", "boat", "submarine", "rocket", "truck", "bus",
    "computer", "keyboard", "mouse", "monitor", "printer", "laptop", "tablet", "phone", "camera", "speaker",
    "python", "java", "swift", "kotlin", "ruby", "javascript", "variable", "function", "loop", "condition",
    "river", "mountain", "ocean", "desert", "forest", "island", "valley", "waterfall", "volcano", "glacier",
    "tiger", "lion", "elephant", "giraffe", "zebra", "panda", "kangaroo", "dolphin", "shark", "whale",
    "table", "chair", "window", "door", "ceiling", "floor", "couch", "bed", "pillow", "blanket",
    "school", "teacher", "student", "library", "notebook", "pencil", "eraser", "backpack", "lesson", "homework",
    "music", "guitar", "piano", "drums", "violin", "trumpet", "microphone", "concert", "album", "melody",
    "happy", "sad", "angry", "excited", "nervous", "brave", "calm", "proud", "shy", "curious",
    "castle", "dragon", "wizard", "knight", "princess", "king", "queen", "battle", "sword", "shield",
    "galaxy", "planet", "asteroid", "comet", "satellite", "telescope", "astronaut", "spaceship", "orbit", "gravity"
]

chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []
lives = 6


while not game_over:
    guess = input("**⭐Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over = True
            print("********************YOU lOST THE GAME !💔********************")
            print(chosen_word)



    if "_" not in display :
        game_over=True
        print("********************YOU'VE WONT THE GAME !💯********************")

    print(stages[lives])

