def make_album(singer, album_name, song_num=0):
    album = {}
    album['歌手'] = singer
    album['专辑名'] = album_name
    if song_num!=0:
        album['歌曲数'] = song_num
    return album


def print_dict(dict):
    for key in sorted(dict.keys()):
        print(key + ":" + str(dict[key]), end="  ")
    print()


album_1 = make_album("周杰伦", "七里香", 12)
album_2 = make_album("王力宏", "火力全开")
album_3 = make_album("五月天", "自传", 12)

print_dict(album_1)
print_dict(album_2)
print_dict(album_3)