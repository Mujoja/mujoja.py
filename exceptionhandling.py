try:
    x = 5
    print(x)

except:
    print("An error occurred")
finally:
    print("Success")

num = 67
num2 = 0

try:
    print(num / num2)
except:
    print("ZeroDivisionError Occurred")