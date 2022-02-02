import re

def solution(user_id, banned_id):
    answer = 0
    blist=[]
    dict_banned = {}
    for i in banned_id:
        dict_banned[i]=0
        for j in user_id:
            if len(i)==len(j):
                check_i = "".join(re.findall("[a-zA-Z0-9]+", i))
                check_i_len = len(check_i)
                if check_i=="":
                    dict_banned[i]=1
                    user_id.remove(j)
                    break
                check_cnt = 0
                for k in range(len(i)):
                    if j[k]==i[k]:
                        check_cnt+=1
                if check_cnt==check_i_len:
                    dict_banned[i]=1
                    user_id.remove(j)
                    break

    for i in dict_banned.values():
        answer+=i
    return answer