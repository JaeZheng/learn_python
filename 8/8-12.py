def add_sandwich(*topping):
    print("我的三明治里要加：")
    for top in topping:
        print("- " + top)


add_sandwich("奶油")
add_sandwich("奶油", "火腿")
add_sandwich("奶油", "火腿", "肉松")

