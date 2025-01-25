import random
total_num = int(input("Enter num: "))
start = int(input("Enter start int: "))
end = int(input("Enter end int: "))
list_globe_var = [random.randrange(start,end) for i in range (total_num)]
def list_compare():
    start_var = int(input("Enter start intger(list compreasion): "))
    end_var = int(input("Enter end intger( list_compressaion): "))
    total_list = int(input("Enter total vaules: "))
    list_a = [random.randrange(start_var,end_var) for a in range(total_list)]
    list_b = [random.randrange(start_var,end_var) for b in range (total_list)]
    list_c = [a for a in list_a for b in list_b if a==b]
    list_soultion = list(set(list_c))
    return list_soultion
def list_set_remove_dup(list_var):
    x = list(set(list_var))
    return x 
def list_remove_dup(x):
    new_list = []
    for i in x:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(list_compare())
print(list_set_remove_dup(list_globe_var ))
print(list_remove_dup(list_globe_var ))
