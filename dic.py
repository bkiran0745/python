lis={1:"kiran ",2:" venu ",3:" pavan ",4:" work "}
class stake():
    
    def ins(self,lis):
        a=[]
        i="kiran"
        for key,value in lis.items():
            a.append(value)
        
        lis[i]=a
        a1,a2,a3,a4=lis["kiran"]
        lis["kiran1"]=a1,a2,a3,a4,"try"
        lis["kiran1"]="kirannn"
        print("KIRAN values:",a1,a2,a3,a4)
        print(a[0])
        print(lis)
ob=stake()
print(type(lis))
ob.ins(lis)
#ob.display()
