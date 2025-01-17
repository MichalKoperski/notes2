import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffe():
    time.sleep(4)
    print("You drank coffee")
def study():
    time.sleep(5)
    print("You finish studying")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffe, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()    #łączy thready i są uruchamiane jednocześnie jako jeden thread
y.join()    #bez tych join() każdy thread będzie uruchominy symultanicznie jako oddzielny thread
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())