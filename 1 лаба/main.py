from random import randint

def input_func(lst,q):
    for x in range(q):
        string = "Введите " + str(x + 1) + " элемент списка: "
        lst.append(input(string))
    return lst

def input_random(lst,q):
    lst = [randint(0, 10) for i in range(q)]
    return lst

def check_input(proverka,lst):
    for x in lst:
        if not x.isnumeric():
            proverka = False
            print("В списке могут быть только числа")
            break
    return proverka

def sort_method(nums):
    t = 0
    n = 0
    while t < len(nums):
        if t + 1 == len(nums) and nums[t] % 2 == 0:
            if n == 2:
                break
            while n > -1:
                nums.pop(t)
                t -= 1
                n -= 1
        elif nums[t] % 2 == 0:
            n += 1
        elif nums[t] % 2 == 1 and n < 3:
            while n != 0:
                nums.pop(t - 1)
                t -= 1
                n -= 1
        else:
            n = 0
        t += 1
    return nums

def sort_no_method(nums, res):
    n = 0
    t = 0
    while t < len(nums):
        if nums[t] % 2 == 1 and n < 3:
            res.append(nums[t])
            n = 0
        elif nums[t] % 2 == 1 and n >= 3:
            while n != 0:
                res.append(nums[t - n])
                n -= 1
            res.append(nums[t])
        elif nums[t] % 2 == 1:
            res.append(nums[t])
        elif t + 1 == len(nums) and nums[t] % 2 == 0:
            if n >= 2:
                while n != 0:
                    res.append(nums[t - n])
                    n -= 1
                res.append(nums[t])
        elif nums[t] % 2 == 0:
            n += 1
        elif nums[t] % 2 == 1:
            res.append(nums[t])
        t += 1
    return res

lst = []
vld = True
nums = []
res = []
q = 0
print('Количество элементов списка: ')
q_str = input()
q = int(q_str)
print('Создание списка: \n1.С помощью ввода клавиатуры\n2.Рандом')
j_str = input()
j = int(j_str)
if j == 1:
    lst = input_func(lst,q)
    nums = [int(x) for x in lst]
else:
    nums = input_random(lst,q)
vld = check_input(vld, lst)
if vld:
    print('Необработанный список:')
    print(nums)
    print('Обработка массива: \n1.С помощью метода\n2.Без методов')
    h_str = input()
    h = int(h_str)
    if h == 1:
        res = sort_method(nums)
    else:
        res = sort_no_method(nums, res)
    print(res)
