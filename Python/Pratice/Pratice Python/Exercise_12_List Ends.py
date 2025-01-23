list = [5, 10, 15, 20, 25]
def list_end(list):
    start = list[0]
    end = list[len(list) - 1]
    return start, end
print(list_end(list))
