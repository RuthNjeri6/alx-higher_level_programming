def weight_average(my_list=[]):
    sum = 0
    total = 0
    if len(my_list) == 0:
        return 0
    for item in my_list:
        prod = 1
        for element in item:
            prod *= element
        sum += prod
        for i in range(len(item)):
            if (i == 1):
                print(item[-1])
                total += item[-1]

    return sum / total
