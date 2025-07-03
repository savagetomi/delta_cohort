# sets

unordered_values = {"Lagos", "Rivers","Abuja","Kogi"}
unordered_values_1 = {"Delta", "Oyo","Lagos","Sokoto","Kogi"}

# Membership
check_value_in_set = "Rivers" in unordered_values
check_value_in_set_1 = "Rivers" in unordered_values_1


unordered_values.add("Zamfara") # add to the sets
unordered_values.remove("Abuja") #Remove values
unordered_values.update(["Adamawa","Gombe"])
print(unordered_values)

unordered_values_2 = unordered_values.difference(unordered_values_1)



print(unordered_values_2)

# Union of sets

merge = unordered_values.union(unordered_values_1)   # better way to go through -> unordered_values / unordered_values_1

# Intersection

intersect = unordered_values.intersection(unordered_values_1) # better way to go through -> unordered_values & unordered_values_1



print(check_value_in_set)
print(check_value_in_set_1)


# loops

""" list = [1,2,3,4,5,6,7,8,9,0]

    if number in list:
        print ("init")
    else:
        print(outit) """

menu = ["Beans", "Plantain", "Rice", "Pasta", "Macaroni", "Mashed Potatoes", "Afang Soup", "Salad"]

new_menu = [
    {
        "name" : "Beans",
        "price" : 2000
    },
    {
        "name" : "Rice",
        "price" : 5000
    },
    {
        "name" : "Pasta",
        "price" : 30000
    },
]

meal = input("We are here to take your order: ")

for dish in new_menu:
    if meal == dish["name"]:
        print(f"Here is your {dish["name"]}, that would be {dish["price"]}")
        break
else:
    print("You have not made an order.")
    
