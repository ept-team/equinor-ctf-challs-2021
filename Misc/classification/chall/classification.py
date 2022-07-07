import numpy as np

def welcome():
    print("\nWelcome!")
    print("Please provide a valid input")

    print(" ") 
    data = input("> ").strip()

    if len(data) != 600:
        print("The input format is not correct, goodbye")
        exit()

    try:
        data = [int(x) for x in data]
        
        with open("solution.npy", "rb") as f:
            solution = np.load(f)

        correct = 0
        for x,y in zip(solution, data):
            if x == y:
                correct += 1
        if correct/600 >= 0.85:
            with open("flag.txt") as f:
                 print("Here is your flag: ", f.read())
        else:
            print(f"Your score was too low :( Better luck next time. Perhaps tune the model a bit")
    except Exception as e:
        print("The input format is not correct, goodbye ", e)
        exit()

welcome()
