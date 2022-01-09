import random
import time

def clear_service_file():
    f = open('prng-service.txt', "w")
    f.write('')
    f.close()

def random_generator():
    low = 0
    high = 10

    while True:
        time.sleep(3)
        
        f = open('prng-service.txt', "r")
        if f.read() == 'run':
            f.close()
            f = open('prng-service.txt', "w")
            random_number = str(random.randint(low, high))
            print('Random number generated: ', random_number)
            f.write(random_number)
            f.close()
        else:
            f.close()

if __name__ == '__main__':
    print('PRNG Service Running...')
    clear_service_file()
    random_generator()