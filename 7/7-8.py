sandwich_orders = ["茄汁三明治", "火腿三明治", "芥末三明治"]
finished_sandwiched = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("我已经做好了"+sandwich)
    finished_sandwiched.append(sandwich)

print("******已完成******")
for sand in finished_sandwiched:
    print(sand, end=" ")