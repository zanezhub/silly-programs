import requests, shutil, os

count = 1
num = 25

while num < 66:
    if num <= 9:
        dir = "0" + str(num)
    else:
        dir = str(num)

    os.chdir(dir)
    file1 = open('urls.txt', 'r')

    for line in file1:
        url = line.strip()
        if count <= 9:
            filename = str("0" + f"{count}.jpeg")
        else:
            filename = str(count) + ".jpeg"
        res = requests.get(url, stream=True)
        with open(filename, 'wb') as f:
            shutil.copyfileobj(res.raw, f)

        count = count + 1

    count = 1
    file1.close()
    os.chdir("..")
    num = num + 1