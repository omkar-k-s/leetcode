def minimum_diff(a,b):
    n=len(a)
    ans=float('inf')

    def solve(i,x,y):
        nonlocal ans

        if i==n:
            diff=abs(int(x)-int(y))
            ans=min(ans,diff)
        return

    solve (i+1,x+a[i],y+b[i])
    solve (i+1,x+b[i],y+a[i])

    solve(0,"","")
    return ans