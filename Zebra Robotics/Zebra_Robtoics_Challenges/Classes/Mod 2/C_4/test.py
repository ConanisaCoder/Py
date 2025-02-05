read_file = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Classes/Mod 2/C_4 /text.txt","r")
list_detials =[]
while True:
    readObj = read_file.readline()
    if not readObj:
        break
    name = readObj[0:readObj.index(" ")]
    age = readObj[readObj.index(" ")+1 : len(readObj)-1]
    age = int(age)
    list_detials.append([name, age])
print(list_detials)