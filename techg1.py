def main():
    n=int(input())
    q=list(map(int,input().split()))
    t=list(map(int,input().split()))
    l=[]
    for i in range(0,len(t)):
        data=t[i]//q[i]
        l.append(data)
    print(min(l))