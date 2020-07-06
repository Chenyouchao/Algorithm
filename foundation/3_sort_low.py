def bubble_sort(li):
    for i in range(len(li) - 1):
        flag = False
        for j in range(len(li) - i - 1):    # range可将长度转换为角标
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                flag = True
        if not flag:
            return
        print(li)

def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]
        print(li)

def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)
        

li = [3,2,4,5,1,7,9,8,6]
print(li)
insert_sort(li)
        