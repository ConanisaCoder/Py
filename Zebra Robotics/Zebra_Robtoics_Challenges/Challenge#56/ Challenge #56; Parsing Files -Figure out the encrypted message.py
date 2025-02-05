readObj = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge#56/text.txt","r")
file_list = readObj.readline()
file_list = file_list.strip()
val = int(file_list)
print(val)

readObj.close()