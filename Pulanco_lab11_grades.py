counter = 0
passed = 0
numlist = []
for x in range(5):
    num = int(input("Enter Your Grade:"))
    if num <= 39 or num >= 101:
        print("invalid Input. Number must be between 40 and 100")
        break
    else:
        numlist.append(num)
    if num >= 75:
        passed += 1
        counter += 1
        
    else:
        counter += 1
    if counter == 5:
        print()
        sumNums = sum(numlist)
        averagegrade = sumNums / 5
        averagegrade = round (averagegrade, 2)
        
        passpercent = (passed / len(numlist)) * 100
        passpercent = round(passpercent, 2)
        
        print("Grades inputted: " + str(numlist))
        print("Average grade: " + str(averagegrade))
        print("Number of students passed: " + str(passed))
        print("Percentage of student who passed: " + str(passpercent) + "%")
        