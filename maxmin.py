# define function which returns the min and max values in list format
def min_max(array: list):
    # initialising lowest and highest value will be replaced with higher and lower values
    lowest = array[0]
    highest = array[0]

    for num in array:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    return [lowest, highest]


print(min_max([2, 4, 1, 0, 2, -1]))
print(min_max([20, 50, 12, 6, 14]))
print(min_max([100, -100]))
