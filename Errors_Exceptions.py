
#Example 1
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Essa operação não é possível com os itens da lista")
finally:
    print("Operação terminou")    

#Example 2
x = 5
y = 0

try:
    z=x/y
except:
    print("Divisão por zero!")
finally:
    print("All Done")

#Example 3 
def ask():
    x = int(input("Please insert a number "))
    return x
while True:

    try:
        ask()
    except:
        print("The type insertes is not a number")
    else:
        break
    finally:
        print("Thanks")