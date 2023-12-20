def list_to_dict():
    keys = ["Apple", "Mango", "Orange"]
    nums = [1,2,3]
    values = ["one", "two", "three"]
    result = dict(zip(keys, values))
    result2 = dict(zip(nums, values))
    print(result)
    print(result2)

list_to_dict()
