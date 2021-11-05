#zadanie1
def numbers(n: int):
    if n < 0:
        return
    print(n)
    numbers(n - 1)

numbers(5)

print("\n")
#zadanie2
def fib(n: int):
    if n < 0:
        print("n>=0")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(0))
print(fib(2))
print(fib(3))
print(fib(13))

print("\n")
#zadanie3
def power(number: int, n: int):
    wynik = 1
    for i in range(n):
        wynik = wynik * number
    return wynik

print(power(2,3))
print(power(6,2))
print(power(2,10))

print("\n")
#zadanie4
def reverse(txt: str):
    if txt == "":
        return txt
    else:
        return reverse(txt[1:]) + txt[0]

txt = "python"
print(reverse(txt))
txt = "nohtyp"
print(reverse(txt))

print("\n")
#zadanie5
def factorial(n: int):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(4))
print(factorial(10))

print("\n")
#zadanie6
def prime(n: int):
    if n/factorial(n)!=0:
        return True
    else:
        return False

print(prime(6))