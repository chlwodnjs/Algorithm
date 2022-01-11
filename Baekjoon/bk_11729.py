def hanoi(n,x,y):
    if n==1:
        print(x, y)
    else:
        hanoi(n-1,x,6-x-y)
        print(x,y)
        hanoi(n-1,6-x-y,y)

if __name__ =='__main__':
    N = int(input())

    print((2**N)-1)
    hanoi(N,1,3)
