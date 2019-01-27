def alternatingSums(a):
    t=sum([e for i,e in enumerate(a) if i % 2 ==0])
    return [t,sum(a)-t]

print(alternatingSums([10,20,30,40,50]))
