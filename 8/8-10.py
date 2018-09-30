def make_great(singers):
    length = len(singers)
    for index in range(0, length):
        singer = singers.pop(0)
        singer = "the Great " + singer
        singers.append(singer)


def show_singers(singers):
    for singer in singers:
        print(singer)


singers = ['五月天', '周杰伦', '王力宏']
make_great(singers)
show_singers(singers)