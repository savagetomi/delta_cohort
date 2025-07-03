# data structures

# dictionary

person = {

    "name" : "OluwaTomi",
    "nationality" : "Nigerian",
    "age" : 30,
    "religion" : "Christianity",
    "gender" : "Male",
    "extra_details" : {
        "nin" : 463284932626,
        "DOB" : "15 November",
        "BVN" : 2243758464830,
    }
}

person["name"] = "Segun"
person["extra_details"]["nin"] = 57363747392928

print(person)

a = {}

a["key"] = 1
a["name"] = "BigTee"
a["age"] = 32

print(a)

#list

collection = ["Abel","Kane",12,114.3,True,[1, "tame", 14, ["Tomi",42]]]

collection.insert(0,"Arsenal")
collection.pop()
collection.remove(True),
collection[0] = input("Enter your First Value: ")
print(collection)


# slicing
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
numbers.append(16)

print(numbers)