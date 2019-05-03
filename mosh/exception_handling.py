try:
    file = open("file.txt")
    age = int(input("Age: "))
    #xfactor = age / 0
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
finally:
    file.close()
