nestup=(("arav","betech",94),
        ("neha","bcom",96),
        ("rohit","bsc",90))
newtup=()
for i in nestup:
        print(i)
ch=raw_input("do u want to continue")
if ch== 'y':
        name=raw_input("enter name of student")
        new_n=raw_input("enter new name")
        new_c=raw_input("enter new course")
        new_m=int(input("enter new marks"))
for i in range(len(nestup)):
        if nestup[i][0]==name:
            newtup+=(new_n,new_c,new_m)
        else:
            newtup+=nestup[i]
print(newtup)
        
