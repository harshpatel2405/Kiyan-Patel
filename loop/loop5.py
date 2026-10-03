# for i in range(1,6):
#     for j in range(6,9):
#         print(i,j)
        
for i in range(1, 6):
    for j in range(1,6):
        print("* ", end="")
    print()
    
    
for i in range(1,6): # row 
    for j in range(1,i+1): # column
        print("* ", end="")
    print()