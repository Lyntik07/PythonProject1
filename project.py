import string
import random

def F(key,text): #шифрование
    result=''
    for i in text:
        if i.isalpha():
            shift = key%26
            if i.islower():
                result+=chr((ord(i)-ord('a')+shift)%26 + ord('a'))
            else:
                result+=chr((ord(i) - ord("A") + shift) % 26 + ord("A"))
        else:
            result+=i
    return result
def M(key,text):
    return F(-key,text) # заканчивает процесс шифрования => происходит дешифрование
def menu():
    print("\n Выберите режим")
    print("1)Шифрование")
    print("2)Дешифрование")
    print("Вы выбираете 1 или 2?")
    choice=input("Ваш выбор:")
    if choice == "1":
        message = input("\nВведите что хотите зашифровать:")
        key = random.randint(-25,25)
        fm=F(key,message)
        print(f'\nВаше зашифрованое сообщение:{fm}')
        print(f"Используемый ключ:{key}")
    elif choice == "2":
        message = input("\nВведите сообщение для дешифрования:")
        print('\nВарианты дешифрования:')
        for key in range(-25,25):
            print(f'Ключ{key}:{M(key,message)}')
    else:
        print("\nОшибка запроса.Попробуйте заново")
        menu()
while True:
    menu()
    if input("\nХотите продолжить?(yes/no):").lower()!="yes":
        break