def modify_list(l1: list, l2: list) -> list:
        l_ret = l1 + l2
        l_ret = list(dict.fromkeys(l_ret))
        l_ret = [item ** 3 for item in l_ret]
        return l_ret

l1 = [9, 8, 17]
l2 = [9, 5, 2]

l3 = modify_list(l1, l2)
for item in l3:
    print(item)