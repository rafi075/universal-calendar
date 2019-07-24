
def leap(l):
    if l%400==0:
        return 1
    elif l%100==0:
        return 0
    elif l%4==0:
        return 1
    else:
        return 0


def firstday(y):
    count=0
    refy=2000
    if y==refy:
        return 0
    elif y>refy:
        while refy<y:
            count=(count+1+leap(refy))%7
    
            refy+=1

        return count
    elif y<refy:
        while y<refy:
            refy-=1
            count=count+1+leap(refy)
        count=(7-count)%7   
        return count
    
        


def month(p,r):

    month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    q=month[:p]
    
    if p>2:
        count=firstday(r)+leap(r)
    else:
        count=firstday(r)
    

    for i in q:
        
        count=count+i
    count=count%7
    return count 
    
def date(d,m,y):
    count=month(m,y)
    count=(d+count)%7
    return count

def day():
    bar=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    print(bar[date(d-1,m,y)])
def monthlist(monthnum):
    count=month(monthnum,y)
    mon=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    enddate=mon[monthnum]
    
    months=[0,"January","February","March","April","May","June","July","August","September","October","November","December"]
    bar=['sat','sun','mon','tue','wed','thu','fri']
    str1="{0:^30}"
    str2="{0:6}"
    print(str1.format(months[monthnum]))
    for i in range(7):
        print str2.format(bar[i]),
    print("\n")
    j=0
    k=1
    week=1
    while week<=6:
        print("\n")

        for b in bar:
        
            if j<count:
                print(str2.format(" "))
                j+=1
            else:
                if monthnum==2:
                
                    if k<=enddate+leap(y):
                        print str2.format(str(k)),
                        k+=1
                else:
                    if k<=enddate:
                        print str2.format(str(k)),
                        k+=1
                    
        
        week+=1
def fullyear():
    monthnum=1
    while monthnum<=12:
        monthlist(monthnum)
        monthnum+=1
        print("\n")
def onemonth(m):
    monthlist(m)
    

        
a=input("Enter a d-m-y or a m-y or a year:")
x=a.split("-")

if len(x)==3:
    d=int(x[0])
    m=int(x[1])
    y=int(x[2])
    if d>31 or m>12:
        print("invalid")
    else:
        day()
elif len(x)==2:
    m=int(x[0])
    y=int(x[1])
    if m>12:
        print("invalid")
    else:
        onemonth(m)
elif len(x)==1:
    y=int(x[0])
    fullyear()
    
    
    

    
    

    
    



        
        
    
         
        
        


        
