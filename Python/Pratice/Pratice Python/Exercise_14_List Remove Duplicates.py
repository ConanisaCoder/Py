import random
start = int(input("Enter start intger: "))
end = int(input("Enter end intger: "))
total_list = int(input("Enter total vaules: "))
list_a = [random.randrange(start,end) for a in range(total_list)]
list_b = [random.randrange(start,end) for b in range (total_list)]
list_c = [a for a in list_a for b in list_b if a==b]
list_soultion = list(set(list_c))
print(list_c)
print(list_soultion)
