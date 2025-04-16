import random

# 🟢 Easy mode function (10 attempts)
def easy(num):
    print("🧠 I'm thinking of a number between 1 and 100... Try to guess it!")
    attempt = 10
    while attempt > 0:
        guess = int(input("🔢 Try to guess the number: "))
        
        if guess == num:
            print("🎉 Congratulations! You guessed the number!")
            break
        
        elif guess < num:
            print("⬇️ Your guess is too low. Try again!")
            attempt -= 1
            
        elif guess > num:
            print("⬆️ Your guess is too high. Try again!")
            attempt -= 1

        print(f"🧮 Remaining attempts: {attempt}\n")
        
    else:
        print("❌ You ran out of attempts. You lose!")
        print("💥" * 30)

# 🔴 Hard mode function (5 attempts)
def hard(num):
    print("🧠 I'm thinking of a number between 1 and 100... Try to guess it!")
    attempt = 5
    while attempt > 0:
        guess = int(input("🔢 Try to guess the number: "))
        
        if guess == num:
            print("🎉 Congratulations! You guessed the number!")
            break
        
        elif guess < num:
            print("⬇️ Your guess is too low. Try again!")
            attempt -= 1
            
        elif guess > num:
            print("⬆️ Your guess is too high. Try again!")
            attempt -= 1

        print(f"🧮 Remaining attempts: {attempt}\n")
        
    else:
        print("❌ You ran out of attempts. You lose!")
        print("*" * 90)

# 🔁 Main game loop
ch = "Y"
while ch.upper() == "Y":
    num = random.randint(1, 100)  # 🎲 Generate a new number every game
    
    print("\n🎮 Welcome to the Guess the Number Game!")
    print("🚀 Let's gooo!\n")
    
    diff = int(input("📊 Select difficulty: Easy (1) or Hard (2): "))
    
    if diff == 1:
        easy(num)
    elif diff == 2:
        hard(num)
    else:
        print("⚠️ Invalid input! Please choose 1 or 2.")

    ch = input("🔁 Want to play again? (Y/N): ")

print("\n👋 Thanks for playing! See you next time!")
