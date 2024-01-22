# ***************************  Exception Handling in Python  ***************************

a = input("Enter number: ")  # gives a in form of string

try:
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a) * i}")
        # arr = [2, 6, 4, 3]
        # print(arr[int(a)])
        
# except Exception as e:
#     print(e)

# except:
#     print("Invalid Input")

except IndexError:
    print("Index Error Occurred")

except ValueError:
    print("Value Error Occurred")

print("Bye")
