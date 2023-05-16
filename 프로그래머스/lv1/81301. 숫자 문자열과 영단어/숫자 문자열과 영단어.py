def solution(s):
    num_list = [ ["zero","0"], ["one","1"], ["two", "2"], ["three","3"], ["four","4"], ["five","5"], ["six", "6"], ["seven","7"], ["eight", "8"], ["nine","9"]]
    for num in num_list:
        if num[0] in s:
            s = s.replace(num[0], num[1])
            
    return int(s)