def soustableau(Tab,i1,i2):
    st=[]
    i=i1
    while i<i2:
        st.append(Tab[i])
        i=i+1
    
    return   st
while True:
    T=[]
    for i in range(5):
        N=int(input("enter a number: "))
        T.append(N)

    i=int(input("enter the first index:  "))
    while i<0 or i>5:
        print("this index is out of range")
        i=int(input("please enter the first index again: "))
    
    j=int(input("enter the second index:  "))
    while j<0 or j>5:
        print("this index is out of range")
        j=int(input("please enter the first index again:"))

    while j<=i:
        print("the second index musst be superior than the first one.")
        i=int(input("please enter the first index again: "))
        j=int(input("please enter the second index again:  "))
       
    print(soustableau(T,i,j))
    
    R=str(input("if you want to enter a new list print Yes,  if not print  No:"))
    if R=="no":
        break





