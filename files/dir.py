import os
import random
import shutil

folder_path = "/root/temp"
shutil.rmtree(folder_path)

if os.path.exists(folder_path):
    print("exists")
else:
    os.makedirs("/root/temp")

counter = {}


def get_count(ext):
    if ext not in counter:
        counter[ext] = 1
    else:
        counter[ext] += 1
    return f"{ext[1:]}_{counter.get(ext, 0)}"


def random_name():
    name_arr = ["Assignment", "Photo", "File", "Project", "Image"]
    ext_arr = ["gif", "png", "txt", "dat", "jpg", "docx"]
    name = random.choice(name_arr)
    ext = random.choice(ext_arr)
    num = random.randint(100, 200)
    return f"{name}{num}.{ext}"


item_list = os.listdir(folder_path)

if len(item_list) < 10:
    item_list = os.listdir(folder_path)
    for _ in range(10):
        file = random_name()
        dst = os.path.join(folder_path, file)
        with open(dst, "w") as f:
            f.write("this is some random value")
    item_list = os.listdir(folder_path)

for item in item_list:
    src = os.path.join(folder_path, item)
    name, ext = os.path.splitext(item)
    new_name = f"{get_count(ext)}{ext}"
    dst = os.path.join(folder_path, new_name)
    print(f"Renaming {src} -> {dst} ")
    os.rename(src, dst)

print(os.listdir(folder_path))
