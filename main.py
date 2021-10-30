# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def clean_channels():
    channels_list = []
    channels_object = {}
    
    file_channels = open("channels.txt", "r")
    output = open("output.txt", "w")

    for i, line in enumerate(file_channels):
        if i%2 == 0:
            string = '{name: \''+line+'\','
            if line[0:11] == 'beIN_SPORTS':
                print(line[0:11])
                category = '1'
        if i%2 != 0:
            string += ' url: \''+line+'\'' + ", categories: ["+category+"], image: \'' },"
            str = string.replace('\n', '')
            output.write(str)
            string = ''



        # if line.startswith("METAR") and line[-2] != "=":
        #     print(line[-2])
        #     line += line + "####"
        #     output.write(line)

clean_channels()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
