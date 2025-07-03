store = [" "]


for object in store:
    print(len(store))
    if len(store) == 0:
        object = input("What objects do you want to store: ")
        store.append(object)
        print(store)
        # continue
    else :
        print(f"Exceeded length : Your list contains {store}")
        break

     
# while
# num = 0
# while num < 10:
#     num = num + 1
#     print("keep running ", num) 

num = 20

while True:
    guess = int(input("Guess the number: "))
    if guess > num and guess <= 25:
        print("You're too close")
    elif guess > num:
        print("Number is greater than the guess number")
    elif guess > num and guess >= 25:
        print("Almost there, Don't give up")
    elif guess == num:
        print(f"Hurray you've found the number.The number is {num}")
        break
    else:
        print("Number is lesser than the guess number")