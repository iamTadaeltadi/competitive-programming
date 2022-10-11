           
x=[]
        for i in tokens:
            if i=="/":
                z=int(int(x[-2])/int(x[-1]))
                x.pop()
                x[-1]=z
            elif i=="+":
                z=int(x[-2])+int(x[-1])
                x.pop()
                x[-1]=z
            elif i=="*":
                z=int(x[-2])*int(x[-1])
                x.pop()
                x[-1]=z
            elif i=="-":
                z=int(x[-2])-int(x[-1])
                x.pop()
                x[-1]=z
            else:x.append(i)
        return x[-1]
