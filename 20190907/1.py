s = 'aabbaccc'

def solution(s):
    # print(len(s))
    cnt = 0
    new_str = ""
    # while cnt < len(s) :
    while cnt == 0 :
        cnt += 1
        keyword = s[0:cnt]
        temp = s
        find_cnt = 0
        while temp.find(keyword) > -1 :
            # print('temp====', temp)
            idx = temp.find(keyword)
            # print("idx=====", idx)
            temp = temp[(idx + 1):]
            if idx != 0 :
                find_cnt += 1
                new_str += s[0:cnt] + str(find_cnt)  
            else :
                find_cnt = 0
                # new_str + temp[]
        
        print("new_str======" + new_str)

    answer = 0
    return answer

solution(s)