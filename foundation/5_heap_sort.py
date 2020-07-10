# 下潜性
def sift(li, low, high):
    '''
    :param li: 待调整列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个位置
    :return:
    '''
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        # 寻找i的位置 (待插入位置)
        if j + 1 <= high and li[j+1] > li[j]:
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp

def heap_sort(li):
    high = len(li) - 1
    # 建堆
    for i in range((high - 1) // 2, -1, -1):
        sift(li, i, high)
    # 取值
    for i in range(high, 0, -1):
        # i指向堆的最后一个元素
        li[i], li[0] = li[0], li[i]
        sift(li, 0, i-1)


li = [3,2,4,5,1,7,9,8,6]
print(li)
heap_sort(li)
print(li)