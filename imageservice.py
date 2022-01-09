import time

def create_image_paths():

    image_paths = []
    for i in range(11):
        image_paths.append("./images/" + str(i) + ".jpeg")
    return image_paths

def clear_service_file():
    f = open('image-service.txt', "w")
    f.write('')
    f.close()

def monitor_service_calls(image_paths):
    while True:
        time.sleep(.01)
        
        f = open('image-service.txt', "r")
        service_call = f.read()
        if service_call.isnumeric():
            service_call = int(service_call)
            f.close()
            photo_path = image_paths[service_call]
            print('Photo path generated: ', photo_path)
            f = open('image-service.txt', "w")
            f.write(str(photo_path))
            f.close()
        else:
            f.close()

if __name__ == '__main__':
    clear_service_file()
    image_paths = create_image_paths()
    monitor_service_calls(image_paths)