def solution(s):
    arr = []
    num_str = ""
    for i in range(len(s)):
        if s[i] == " ":
            arr.append(num_str)
            num_str = ""
        else:
            num_str += s[i]
    arr.append(num_str)
    
    min_num, max_num = int(arr[0]), int(arr[0])
    for num in arr[0:]:
        if int(num) < min_num:
            min_num = int(num)
        if int(num) > max_num:
            max_num = int(num)

    return str(min_num) + " " + str(max_num)