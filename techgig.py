def main(): 
    x=int(input())
    while x>0:
        Ad=0
        a=int(input())
        powerg=list(map(int,input().split()))
        powero=list(map(int,input().split()))
        powerg.sort(reverse =True)
        powero.sort(reverse = True)
        p=0
        for i in range(a):
            for j in range(p,a):
                if powerg[i]>powero[j]:
                    p=j+1
                    Ad +=1
                    break
        print(Ad)
        x -=0
main()