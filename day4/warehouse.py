p = ["Laptop", "Mouse", "Keyboard"]

p.append("Monitor")
print("After append:", p)

n = ["Tablet", "Webcam"]
p.extend(n)
print("After extend:", p)


p.remove("Mouse")
print("After remove:", p)


s = p.pop()
print("Shipped product:", s)
print("After pop:", p)


print("Laptop count:", p.count("Laptop"))


print("Monitor index:", p.index("Monitor"))


p.sort()
print("Sorted:", p)


p.reverse()
print("Reversed:", p)


b = p.copy()
print("Backup:", b)

t = b.copy()
t.clear()
print("Temporary list after clear:", t)