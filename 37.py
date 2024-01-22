# ***************************  Finally keyword in Python  ***************************

def func1(num):
    try:
        arr = [10, 20, 30, 40]
        return arr[num]
    except:
        return -1
    
    # It will always execute in every case, whether try or except or whether function has returned or not
    finally:  
        print("Finally executed")  

print(func1(4))
