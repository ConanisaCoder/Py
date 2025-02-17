writelocation1 = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #61; Writing Files - Splitting the sentence /file.txt","w")
writelocation2 = open("/home/omega01/MyDrive/Zebra Robotics/Zebra_Robtoics_Challenges/Challenge #61; Writing Files - Splitting the sentence /file1.txt","w")
inputval = "Hello World I am Greeting You From a File"
words = inputval.split(" ")
count = len(words)
for i in range(0,count,1):
    if i % 2 == 0:
        writelocation1.write(words[i] +"\n")
    else: 
        writelocation2.write(words[i] + "\n")
writelocation1.close()
writelocation2.close()