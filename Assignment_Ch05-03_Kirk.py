## Loop determines if the user will repeat
repeatProgram = True
while repeatProgram == True:
    ## Loop determines the validity of the values entered
    checkInput = True
    while checkInput  == True:
        print("Enter two positive integer numbers.")
        print("First number must be less than the second number:")
        print("Enter numbers:", end = ' ')
        userInput = input()
        print('\n')
        nums1And2 = userInput.split()
    ## Not sure if using try/except bad form, but couldn't get it to work with if/else
        try:
            firstNum = int(nums1And2[0])
            secondNum = int(nums1And2[1])
            if firstNum < 0 or secondNum < 0:
                print("No negative numbers!\nPlease try again.\n")
            elif firstNum > secondNum:
                print("First number must be less than the second number!\nPlease try again.\n")
            else:
                checkInput = False
        except:
            print("Incorrect Input.\nPlease try again.\n")
    ## Resuts for the values below
    count = firstNum
    print("Odd integers between", firstNum, "and", secondNum, "are:")
    while count <= secondNum:
        if count % 2 == 1:
            print(count, end = ' ')
        count += 1
    print('\n')

    count = firstNum
    sumEven = 0
    while count <= secondNum:
        if count % 2 == 0:
            sumEven += count
        count += 1
    print("Sum of even integers between", firstNum, "and", secondNum, "=", sumEven, '\n') 


    count = firstNum
    sumOddSqrt = 0
    while count <= secondNum:
        if count % 2 == 1:
            sumOddSqrt += count * count
        count += 1
    print("Sum of the squares of odd integers between", firstNum, "and", secondNum, "=", sumOddSqrt, '\n\n')
    ## User decides to repeat program or not
    print("Do you want to repeat this program?\ny/n")
    userChoice = input()
    if userChoice == 'n' or userChoice == 'N':
        repeatProgram = False
        print("\nBye!")
