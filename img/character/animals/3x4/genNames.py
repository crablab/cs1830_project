import os

def gen1(start, stop, str1, str2, padNum):
    for i in range(start,stop +1):
        s = str(i)
        while len(s) < padNum:
            s = "0" + s
        
        print(str1 + "_" + s + " = SpriteAnimator(cwd + '/img/" + str2 + s + ".jpg')" )

def gen2(start, stop, str1, str2, padNum):
    for i in range(start,stop +1):
        s = str(i)
        while len(s) < padNum:
            s = "0" + s
        
        print("'" + str1 + "_" + s + "':" + str2 + "_" + s + ",")

def rename():
    cwd = os.getcwd()

    i = 0
    for file in os.listdir(cwd):
        if file[-3:] != "zip":
            s = pad(str(i), 3)

            if file != "genNames.py":
                print(file + " -> " + s + ".jpg")
                old_file = os.path.join(cwd, file)
                new_file = os.path.join(cwd, s + ".jpg")
                if old_file != new_file:
                    os.rename(old_file, new_file)
                i+=1

def pad(string, num):
    while len(string) < num:
        string = "0" + string
    return string
        
    
# = SpriteAnimator(cwd + '/img/Magic/magic07.jpg')
