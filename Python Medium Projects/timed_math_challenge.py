import random, time

OPERATORES = ["+", "-", "*"]
MIN_OPERAND = 3 
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORES)
    
    expr = str(left) +" " + operator + " " + str(right)
    answer = eval(expr) # evaluate a string as such it is a expression
    return expr, answer

wrong = 0
input("Press Enter to Start!")
print("-----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1 
end_time = time.time()
total_time = end_time - start_time

print("-----------------------")
print("Nice work! You finished in", total_time, "seconds!")

