import random
import time

def random_generator():
    low = 0
    high = 10

    return random.randint(low, high)


while True:
    time.sleep(.01)
    
    f = open('prng-service.txt', "r")
    if f.read() == 'run':
        f.close()
        f = open('prng-service.txt', "w")
        random_number = str(random_generator())
        print('Random number generated: ', random_number)
        f.write(random_number)
        f.close()
    else:
        f.close()