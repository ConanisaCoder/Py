import random
int_a = int(input("Enter smallest vaule: "))
int_b = int(input("Enter largest vaule: "))
vaule_len = int(input("Enter total length of list: "))
list_a = []
list_b = []
list_both = []
index = 0
soultion =[]
for i in range(0,vaule_len,1):
    list_a.append(random.randrange(int_a,int_b))
    list_b.append(random.randrange(int_a,int_b))
print(list_a)
print(list_b)
for i in range(0,vaule_len,1):
    char_a = list_a[index]
    if char_a in list_b:
        list_both.append(char_a)
        index += 1
    else:
        index += 1
for i in list_both:
    if i not in soultion:
        soultion.append(i)
print("Items in both list: "+ str(list_both)) 
print("Solution: " + str(soultion))