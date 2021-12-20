from time import sleep

is_man = input("are you a man? (Y/N) : ")
is_arab = input("are you from Arabic contre? (Y/N) : ")
yas = "y"  and "Y"
no = "n" and "N"


if is_man == yas and is_arab == yas :
   print("your are a Arab man")
elif is_man == yas and not is_arab == no :
   print("you are a man but not Arab")
elif is_man == no and is_arab == yas :
    print("your are and Arab woman")
else:
    sleep(0.4)
    print("what ??")
    sleep(1.2)
    print("Rally?!!")
    sleep(2.1)
    print(input("why are you here then??? -_-? :"))
    sleep(5)
    print("oooh,OK Nice to meet you ^_^")
