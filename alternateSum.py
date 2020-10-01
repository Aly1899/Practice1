def alternatingSums(a):
    t=sum([e for i,e in enumerate(a) if i % 2 ==0])
    return [t,sum(a)-t]

num=input("enter the list")) #here you can take a input from user with his choose
alternatingSums(num) #here you are calling a function to do that work 
