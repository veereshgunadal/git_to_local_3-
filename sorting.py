def bubble(l):
    for i in range(len(l)-1, 0 , -1):
        for j in range(i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
l = [2,1,5,3,6,7]
bubble(l)
print(l)
