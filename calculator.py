#Calculator without library on the terminal 
#for 4 number

while 1:  
#input calculator       
    data = input("")

#ok string for list 
    data =  data.replace("*",".*.")
    data =  data.replace("/","./.")
    data =  data.replace("+",".+.")
    data =  data.replace("-",".-.") 
    mylist = data.split(".")

#try for input
    try:
        x= int(mylist[0])
        y= int(mylist[2])
    except:
        print("please Enter number!")

#if list is big
    if len(mylist)> 7:
        print("Non programming(just 4 Number)")
        exit()
    else:
        pass
    
#try for calculate numbers
    try:
        if mylist[1] =="*":
            z = x*y
            if len(mylist) > 3 and mylist[3] in mylist:
                if mylist[3] =="*":
                    v= int(mylist[4])
                    z2 = z*v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = z2*f
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z2/f
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)

                    else:
                        print(z2)
                elif mylist[3] =="/":
                    v= int(mylist[4])
                    z2 = z/v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = (z*f)/v
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z2/f
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2)

                elif mylist[3] =="+":
                    v= int(mylist[4])
                    z2 = z+v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = (v*f)+z
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = (v/f)+z
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2)
                
                elif mylist[3] =="-":
                    v= int(mylist[4])
                    z2 = z-v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = z-(v*f)
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z-(v/f)
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2)
            else:
                print(z)


        elif mylist[1] =="/":
            z = x/y
            if len(mylist) > 3 and mylist[3] in mylist:
                if mylist[3] =="*":
                    v= int(mylist[4])
                    z2 = (x*v)/y
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = z2*f
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z2/f
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2)                    
                elif mylist[3] =="/":
                    v= int(mylist[4])
                    z2 = z/v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = (z*f)/v
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z2/f
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2)
                elif mylist[3] =="+":
                    v= int(mylist[4])
                    z2 = z+v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = z+(v*f)
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z+(v/f)
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2)                    
                elif mylist[3] =="-":
                    v= int(mylist[4])
                    z2 = z-v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = z-(v*f)
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z-(v/z)
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2)   
            else:
                print(z)

        elif mylist[1] =="+":
            z = x+y 
            if len(mylist) > 3 and mylist[3] in mylist:
                if mylist[3] =="*":
                    v= int(mylist[4])
                    z2 = x+(y*v)
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = x+(y*v)*f
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = x+(y*v)/f
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2)   
                elif mylist[3] =="/":
                    v= int(mylist[4])
                    z2 = x+(y/v)
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = x+(y/v)*f
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = x+(y/v)/f
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2) 
                elif mylist[3] =="+":
                    v= int(mylist[4])
                    z2 = z+v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = z+(v*f)
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z+(v/f)
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2) 
                elif mylist[3] =="-":
                    v= int(mylist[4])
                    z2 = z-v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = z-(v*f)
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z-(v/f)
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2) 
            else:
                print(z)
                
                
        elif mylist[1] =="-":
            z = x-y
            if len(mylist) > 3 and mylist[3] in mylist:
                if mylist[3] =="*":
                    v= int(mylist[4])
                    z2 = x-(y*v)
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = x-(y*v)*f
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = x-(y*v)/f
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2) 
                elif mylist[3] =="/":
                    v= int(mylist[4])
                    z2 = x-(y/v)
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = x-(y/v)*f
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = x-(y/v)/f
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2) 
                elif mylist[3] =="+":
                    v= int(mylist[4])
                    z2 = z+v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = z+(v*f)
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z+(v/f)
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2) 
                elif mylist[3] =="-":
                    v= int(mylist[4])
                    z2 = z-v
                    if len(mylist) > 5 and mylist[5] in mylist:
                        if mylist[5] =="*":
                            f = int(mylist[6])
                            z3 = z-(v*f)
                            print(z3)
                        elif mylist[5]=="/":
                            f = int(mylist[6])
                            z3 = z-(v/f)
                            print(z3)
                        elif mylist[5]=="+":
                            f = int(mylist[6])
                            z3 = z2+f
                            print(z3)
                        elif mylist[5]=="-":
                            f = int(mylist[6])
                            z3 = z2-f
                            print(z3)
                    else:
                        print(z2)    
            else:
                print(z)
        else:
            pass
    except:
        print("Error")    
        
