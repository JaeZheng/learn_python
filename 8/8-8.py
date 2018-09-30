def make_album(singer, album_name, song_num=0):
    album = {}
    album['歌手'] = singer
    album['专辑名'] = album_name
    if song_num!=0:
        album['歌曲数'] = song_num
    return album


def print_dict(dict):
    print()
    for key in sorted(dict.keys()):
        print(key + ":" + str(dict[key]), end="  ")
    print()


while True:
    print("\n请输入专辑信息：")
    print("(任何时候输入'q'可以退出)")

    singer = input("歌手：")
    if singer == 'q':
        break
    album_name = input("专辑名：")
    if album_name == 'q':
        break
    song_num = input("歌曲数：")
    if song_num == 'q':
        break

    album = make_album(singer, album_name, song_num)
    print_dict(album)

