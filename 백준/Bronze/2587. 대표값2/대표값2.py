li = []
for _ in range(5):
    li.append(int(input()))
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]>li[j]: 
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
print(int(sum(li)/5))
print(li[2])

# sort()로 풀면 쉽다.
# x = []
# for i in range(5):
#     x.append(int(input()))
# x.sort()
# print(int(sum(x)/5))
# print(x[2])
