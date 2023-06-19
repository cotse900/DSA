# DSA456V1A
# Lab 1
# Student: Chungon Tse
# ID: 154928188
# Date: 8 Feb 2023

# wins_rock_scissors_paper
def wins_rock_scissors_paper(player, opponent):
    p1 = player.lower()
    p2 = opponent.lower()
    if p1 == "rock" and p2 == "scissors":
        return True
    elif p1 == "paper" and p2 == "rock":
        return True
    elif p1 == "scissors" and p2 == "paper":
        return True
    else:
        return False


print(wins_rock_scissors_paper("scissors", "rock"))
# prints False
print(wins_rock_scissors_paper("sCiSsOrS", "PAPER"))
# prints True
print(wins_rock_scissors_paper("paper", "I don't play"))


# prints False

# factorial
def factorial(n):
    if n < 0 or n % 1 != 0:
        raise Exception("Error")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1);


# ANumber = int(input("Enter an integer: "))
# print("The factorial of", ANumber, "is", factorial(ANumber))

print("Testing factorial")
print(factorial(1))
print(factorial(2))


# print(factorial(-1))

# fibonacci
def fibonacci(n):
    if n < 0 or n % 1 != 0:
        raise Exception("Error")
    elif n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Testing fibonacci")
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(9))
