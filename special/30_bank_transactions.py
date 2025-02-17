#Challenge: 30-bank_transactions
#Difficulty:  Intermediate
#Prompt:
#- Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three methods to perform these calculations and output the result to the user. 

#Gather user input using the `input` function. Note that input always returns user input as a string. You have to manually convert it to an int or a float to make it behave like number. Also, end the input prompt with a \n newline character if you want the user to type in on the next line.

#```
#age = input("How old are you?\n")
#age = int(age)
#```

#Here is a sample output:

#```
#Your current balance is
#4000
#What would you like to do? (deposit, withdraw, check_balance)
#deposit
#How much would you like to deposit?
#1000
#Your current balance is 5000
#Are you done?
#yes
#Thank you!
#```

# Your solution for 30-bank_transactions here:

print("Hello! Welcome to Ciaran's bank.")

should_run = True
balance = 1000000

while should_run:
    print("What can I help you with? (deposit, withdraw, check_balance)")
    prompt = '> '
    action = input(prompt)

    if action == "deposit":
        print("Please enter an amount")
        amount = int(input(prompt))
        balance += amount
    elif action == "withdraw":
        print("Please enter an amount")
        amount = int(input(prompt))
        balance -= amount
    elif action == "check_balance":
        print(f"Your current account balance is : {balance}")
    else:
        print("invalid input")

    print("Are you done? ('y/n')")
    done = input(prompt)
    if done == "y":
        print("Have a nice day!")
        should_run = False