# flight_destination = []
registeredflights = ["Abuja", "Lagos","Ogun","Abia"]



print("Welcome to Riyadh Airways: What do you want to do today")
options = int(input("1. Add a destination \n2. Delete Destination\n3. Update Destination\n4. Read Destination\nYour Input: "))


if options == 1:
    destination = input("Enter the preferred state: ")
    registeredflights.append(destination)
    print(registeredflights)
          
elif options == 2:
    delle = input("Enter the destination you want to delete: ")
    registeredflights.remove(delle)
    print(f"{delle} was deleted from the options")

elif options == 3:
      update = input("Enter the destination you want to update: ")
      registeredflights.insert(0,update)
      print(f"{update} has been added to the list.List Updated")
elif options == 4:
     print(destination)

# flight_destination.insert(0, input("First Destination : "))
# flight_destination
# print(flight_destination)

"""registeredflights.append(destination)
    print(registeredflights)
    print( destination)
    if destination in registeredflights:
    
            print(
              "Your flight is successful"
          )
    else:
            print("Canceled")"""