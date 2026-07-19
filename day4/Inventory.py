c=3
p=4

inv=[]

for i in range(c):
    print("category",i+1)
    t=[]
    for j in range(p):
        q=int(input(f"Product{j+1}"))
        t.append(q)
    inv.append(t)

print("\inventory")

for i in range(c):
    print("Category",i+1)
    for j in range(p):
        print("Product",j+1,":",inv[i][j])