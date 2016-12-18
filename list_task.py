def average(lst):
    avg = sum(lst) / len(lst)
    return avg


def averages_row(mat):
    avg_lst = []
    for _, lst in enumerate(mat):
        avg_lst.append(average(lst))
    return avg_lst


def pair_min(lst):
    return min(lst), lst.index(min(lst))


def find_min_pos(mat):
    lst_min = list(map(pair_min, mat))
    return lst_min.index(min(lst_min)), min(lst_min)[1]


def unique(lst):
    hash_table = {}
    ans = []
    for _, item in enumerate(lst):
        if (hash_table.get(item) != 1):
            ans.append(item)
            hash_table.update({item: 1})
    return ans
