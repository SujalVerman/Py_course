import random

def game():
    print("You are in game...")
    score = random.randint(1, 100)

    # Open the file in read mode
    with open("hiscore.txt", "r") as f:
        hiscore = f.read().strip()  # Read and remove any extra whitespace or newlines

        if hiscore:  # Check if hiscore is not empty
            hiscore = int(hiscore)
        else:
            hiscore = 0  # If file is empty, set hiscore to 0

    print(f"Your previous high score: {hiscore}")
    print(f"Your current score: {score}")

    # Update high score if the current score is higher
    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        print(f"New high score: {score}")
    else:
        print(f"High score remains: {hiscore}")

    return score

game()
