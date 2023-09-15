notSelfNumberSet = set()  
for num in range(1, 10000) :
    for n in str(num):
        num += int(n)
    notSelfNumberSet.add(num)  

selfNumberSet = set(range(1,10000)) - notSelfNumberSet  
for self_num in sorted(selfNumberSet):  # sorted 함수로 정렬
    print(self_num)