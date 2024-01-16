# ***************************  Match Case Statements in Python  ***************************

num = 1

match num:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3: 
        print("three")
    case _:
        print("something else")