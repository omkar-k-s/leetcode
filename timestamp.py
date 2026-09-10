def timestamp(start,end):
    count=0

    sh,sm,ss=map(int,start.split(":"))
    eh,em,es=map(int,end.split(":"))

    start_seconds=sh*3600+sm*60+ss
    end_seconds=eh*3600+em*60+es

    for t in range(start_seconds,end_seconds+1):

        h=t//3600
        m=(t%3600)//60
        s=t%60

        timestamp=f"{h:02d}:{m:02d}:{s:02d}"

        digits=set(timestamp)

        if len(digits)<=2:
            count+=1
    return count