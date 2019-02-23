import time
import threading
import random
import os
import sys


# Name: Harriet Haisty
# Instructor: Ji Li
# Class: Internet Programming

def customer_checkout(t, T1):
    while T1 > 0:
        T1 -= 1
        if len(t) > 0:
            t[0] -= 1
            if t[0] == 0:
                t.pop(0)

        display = 'Checkout: '
        for customer in t:
            display += str(customer) + ' '

        os.system('cls')
        print(display)

        time.sleep(1)


def new_customer(t, checkout_line_thread, T2, R, Tmin, Tmax):
    while checkout_line_thread.is_alive():
        if len(t) < R:
            t.append(random.randint(Tmin, Tmax))

        time.sleep(T2)


if __name__ == '__main__':
    if len(sys.argv) != 6:
        raise Exception('Incorrect number of arguments.')

    t = []
    T1, T2, R, Tmin, Tmax = list(map(lambda x: int(x), sys.argv[1:]))

    checkout_line_thread = threading.Thread(target=customer_checkout, args=[t, T1])
    new_customer_thread = threading.Thread(target=new_customer, args=[t, checkout_line_thread, T2, R, Tmin, Tmax])

    checkout_line_thread.start()
    new_customer_thread.start()
