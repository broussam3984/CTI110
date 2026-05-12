run_again = "yes"

while run_again == "yes":
    num = int(input("Enter an integer: "))

    if num < 0:
        print("This program does not handle negative number!")

    else:
        for i in range(1, 13):
            print(num, "*", i, "=", num * i)

    run_again = input("\nWould you like to run the program again? ")

print("\nExiting program...")