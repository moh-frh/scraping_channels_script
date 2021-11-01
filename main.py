# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_bein_sport_low():
    channels_list = []
    channels_object = {}
    file_channels = open("channels.txt", "r", encoding="utf8")
    beinsport_low = open("beinsport_low.txt", "w", encoding="utf8")

    for i, line in enumerate(file_channels):
        if i%2 == 0:
            if line[0:11] == 'beIN_SPORTS' and 'Low' in line :
                string = '{name: \''+line+'\','
                print(line)
                category = '1'
        if i%2 != 0:
            string += ' url: \''+line+'\'' + ", categories: ["+category+"], image: \'' },"
            str = string.replace('\n', '')
            beinsport_low.write(str)
            string = ''

def get_bein_sport_1080():
    channels_list = []
    channels_object = {}
    file_channels = open("channels.txt", "r", encoding="utf8")
    beinsport_1080 = open("beinsport_1080.txt", "w", encoding="utf8")

    for i, line in enumerate(file_channels):
        category = '2'
        if i%2 == 0:
            string = '{name: \''+line+'\','
            if line[0:11] == 'beIN_SPORTS' and '1080' in line :
                print(line)
        if i%2 != 0:
            string += ' url: \''+line+'\'' + ", categories: ["+category+"], image: \'' },"
            str = string.replace('\n', '')
            beinsport_1080.write(str)
            string = ''

get_bein_sport_low()
# get_bein_sport_1080()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
