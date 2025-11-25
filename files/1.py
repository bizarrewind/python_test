import os
import random

folder_path = "/root/temp"
extensions = ["png", "jpg", "txt", "log", "dat"]
names = ["picture", "assignment", "photo", "video"]


os.system(f"rm -r {folder_path}")


def random_filename():
    num = random.randint(1000, 9999)
    ext = random.choice(extensions)
    name = random.choice(names)
    return f"{name}{num}.{ext}"


if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Made a new directory at {folder_path}")


item_list = os.listdir(folder_path)

if len(item_list) < 30:
    random_items = [random_filename() for _ in range(30)]

    for item in random_items:
        file_path = os.path.join(folder_path, item)
        with open(file_path, "w") as f:
            f.write("this is dummy content")

    item_list = os.listdir(folder_path)


counter = {}


def count_num(ext):
    if ext not in counter:
        counter[ext] = 1
    else:
        counter[ext] += 1
    return counter.get(ext, 0)


for item in item_list:
    name = os.path.splitext(item)
    src = os.path.join(folder_path, item)
    new_name = f"item{count_num(name[1])}{name[1]}"
    dst = os.path.join(folder_path, new_name)

    print(f" Renaming {src} => {dst}")
    os.rename(src, dst)

print(os.listdir(folder_path))
