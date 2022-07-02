# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def remove_with_sets(some_list):
    list = set(some_list)
    return list

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list)) # with for cycle
    print(remove_with_sets(random_list)) # with sets

if __name__ == "__main__":
    run()
