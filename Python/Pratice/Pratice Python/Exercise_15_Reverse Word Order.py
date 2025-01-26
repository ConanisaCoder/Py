def Rev_Word_Order(string):
    list_string = string.split()
    rev_word_order = " ".join(list_string[::-1])
    return rev_word_order
string = input("Enter string: ")
print(Rev_Word_Order(string))
