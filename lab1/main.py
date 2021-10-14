# print("Hello world!")
#
# #zadanie1
# a =input("Podaj pierwszą litere imienia: ")
# b =input("Podaj Nazwisko: ")
#
# def foo1(a,b):
#     return a+"."+b
# print(foo1(a,b))
#
# #zadanie2
# a =input("Podaj imie: ")
# b =input("Podaj Nazwisko: ")
#
# def foo2(a,b):
#     return a[0]+"."+b
# print(foo2(a,b))
#
# #zadanie3
# a=input("Podaj 2 pierwsze cyfry aktualnego roku: ")
# b=input("Podaj 2 ostatnie cyfry aktualnego roku: ")
# c=input("Podaj wiek użytkownika: ")
# def foo3(a,b,c):
#     wynik=a+b
#     return int(wynik)-int(c)
# print(foo3(a,b,c))
#
# #zadanie4
# a = input("Podaj imie: ")
# b = input("Podaj nazwisko: ")
# def foo4(a,b,foo2):
#     return foo2(a,b)
# print(foo4(a,b,foo2))
#
# #zadanie5
# a=int(input("Podaj liczbe a: "))
# b=int(input("Podaj liczbe b: "))
# def foo5(a,b):
#     if(a>0 and b>0 and b!=0):
#         return a/b
# print(foo5(a,b))

# #zadanie6
#
# for x in range(100):
#     x = int(input("Podaj liczbe: "))
#     x +=x
#     if(x>=100):
#         print("Osiągnięto sumę 100!")
#         break

# #zadanie7
# lista =['mleko','kasza','makaron','wino']
# print(lista)
# def foo7(lista):
#         return tuple(lista)
# print(foo7(lista))

# #zadanie8
# def foo8():
#     lista = []
#     liczba = None
#     n = int(input("Podaj ilość wartości do wprowadzenia: "))
#     for x in range(n):
#         liczba = int(input("Wprowadz wartosc: "))
#         lista.append(liczba)
#     return tuple(lista)
# print(foo8())

# #zadanie9
# def foo9(numer_dnia):
#     dzien={1: "poniedziałek",
#            2: "wtorek",
#            3: "sroda",
#            4: "czwartek",
#            5: "piatek",
#            6: "sobota",
#            7: "niedziela"}
#     return dzien[numer_dnia]
#
# print(foo9(2))

# #zadanie10
# def foo10(slowo):
#     odwroconeSlowo = slowo[::-1]
#     if(slowo==odwroconeSlowo):
#         return ("Jest to palindrom!")
#     else:
#         return ("Nie jes to palindrom!")
#
# print(foo10("ala"))
# print(foo10("kot"))