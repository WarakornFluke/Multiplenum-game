import random
def main():
    correct = True
    score = 0
    print("Answers question")
    while correct:
        numberA = random.randrange(1,13)
        numberB = random.randrange(1,13)
        ans = int(input("%s * %s = " %(numberA,numberB)))
        if ans == numberA*numberB:
            score += 1
        else:
            print("Game Over")
            correct = False
    print("Score: %d" %score)
main()