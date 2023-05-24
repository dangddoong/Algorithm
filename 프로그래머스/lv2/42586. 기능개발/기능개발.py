

def solution(progresses, speeds):
    progresses.reverse(), speeds.reverse()
    answer = []
    
    while len(progresses) != 0:
        count = 0
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        if progresses[-1] >= 100:
            for i in range(len(progresses)):
                if progresses[-1] >= 100:
                    progresses.pop()
                    count += 1
                else:
                    break
        if count != 0:
            answer.append(count)
        
    return answer