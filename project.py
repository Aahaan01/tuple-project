tuple1=(1,2,3)

tuple2=()

for i in range(len(tuple1)):
    x=tuple1[i]*5
    tuple2=tuple2+(x,)
    
print(tuple2)