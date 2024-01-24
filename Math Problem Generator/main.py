import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Please press Enter to start!")
totalProblems = int(input("Please input how many problems to generate: "))
print("----------------------")

start_time = time.time()

for i in range(totalProblems):

    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")

if wrong == 1:
    print("You had", wrong, "incorrect answer. Keep it up!")
elif wrong == 0:
    print("Good job! You answered it perfectly!")
else:
    print("You had", wrong, "incorrect answers. Keep it up!") 

print("You finished in", total_time, "seconds.")

