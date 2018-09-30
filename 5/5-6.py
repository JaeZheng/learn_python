def if_age(age):
    if age < 2:
        print("他是个婴儿")
    elif age < 4:
        print("他正蹒跚学步")
    elif age < 13:
        print("他是儿童")
    elif age < 20:
        print("他是青少年")
    elif age < 65:
        print("他是成年人")
    else:
        print("他是老年人")


if_age(1)
if_age(3)
if_age(11)
if_age(18)
if_age(45)
if_age(67)