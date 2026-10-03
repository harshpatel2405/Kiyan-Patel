
# nested if_else 
# if condition :
#     if condition :
#         logic 

power =int(input("IS power there?\t1.Yes\t2. NO "))

if(power == 1):
    charger = int(input("Do you have charger ? \t1.yes \n2. no"))
    if(charger == 1):
        print("You can charge")
    else:
        print("You cannot charge as you dont have charger")
else :
    print("No power")
