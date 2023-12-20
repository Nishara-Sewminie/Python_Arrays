def list_to_dict():
    keys = ["Apple", "Mango", "Orange"]
    nums = [1,2,3]
    values = ["one", "two", "three"]
    result = dict(zip(keys, values))
    result2 = dict(zip(nums, values))
    print(result)
    print(result2)

list_to_dict()

def dict_to_tuple():
    x = {1:"one", 2:"two", 3:"three"}
    for i in x.items():
        print(i)

dict_to_tuple()
