customer ={
    "name" : "John",
    "age" : 30,
    "is_verified": True
}

print(customer["age"])
#print(customer["birthday"]) #error
print(customer.get("birthday")) #None
print(customer.get("birthday", "Sep 1")) #Sep 1, if present get value , else get value specified in 2nd arg