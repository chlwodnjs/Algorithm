def solution(numbers, hand):
    answer = ''
    L_list = [1,4,7]
    R_list = [3,6,9]
    check_L = 10
    check_R = 12
    check = {1:(0,0),2:(0,1),3:(0,2),
            4:(1,0),5:(1,1),6:(1,2),
            7:(2,0),8:(2,1),9:(2,2),
            10:(3,0),0:(3,1),12:(3,2)}
    for i in range(len(numbers)):
        if numbers[i] in L_list:
            check_L = numbers[i]
            answer+="L"
        elif numbers[i] in R_list:
            check_R = numbers[i]
            answer+="R"
        else:
            LL=abs(check[numbers[i]][0]-check[check_L][0])+abs(check[numbers[i]][1]-check[check_L][1])
            RR=abs(check[numbers[i]][0]-check[check_R][0])+abs(check[numbers[i]][1]-check[check_R][1])
            if LL==RR:
                if hand=="right":
                    answer+="R"
                    check_R=numbers[i]
                else:
                    answer+="L"
                    check_L=numbers[i]
            elif LL<RR:
                answer+="L"
                check_L=numbers[i]
            else:
                answer+="R"
                check_R=numbers[i]
    return answer