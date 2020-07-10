# 小根堆, 大数下潜
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
        if j + 1 <= high and li[j+1] < li[j]:
            j += 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp

def top_k(li, k):
    heap = li[0: k]
    # 建堆
    for i in range((k-2) // 2, -1, -1):
        sift(heap, 0, k-1)
    # 筛选top_k
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # 依次弹出最小值, 排序top_k
    for i in range(k-1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap


import random
li = list(range(1000))
random.shuffle(li)

print(top_k(li, 10))
