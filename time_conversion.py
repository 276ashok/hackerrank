def timeConversion(s):
    time = s.split(":")
    if s[-2:]=="PM":
        if time[0]!="12":
            time[0]=str(int(time[0])+12)

    else:
        if time[0]=="12":
            time[0]="00"
    
    ntime=":".join(time)
    print(ntime)
    
    return str(ntime[:-2])

s = input()
result = timeConversion(s)
print(result)

"""
sample input
07:05:45PM

sample output
19:05:45
"""