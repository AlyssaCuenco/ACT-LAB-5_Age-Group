def classify_age(age):
    if age > 0:
        if age >= 65:
            print("You are a Senior.")
        elif age >= 20:
            print("You are an Adult.")
        elif age >= 13:
            print("You are a Teen.")
        elif age1 >= 0:
            print("You are a Child.")
    elif age < 0:
        print("Please input an appropriate number.")
  
try:
    age = int(input("Please enter your age: "))
    classify_age(age)
except: 
    print("Please input an appropriate number.")    
        