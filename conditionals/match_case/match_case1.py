choice = int(
    input("1. Spring\n2. Summer\n3. Monsoon\n4. Winter\nSelect your choice : "))

match choice:
    case 1:
        print("You Selected Spring")
    case 2:
        print("You Selected Summer")
    case 3:
        print("You Selected Monsoon")
    case 4:
        print("You Selected Winter")
    case _ :
        print("Select Season between 1 to 4 only")
