def get_image_path(num):

    image_paths = []
    for i in range(11):
        image_paths.append("./images/" + str(i) + ".jpeg")

    return image_paths[num]