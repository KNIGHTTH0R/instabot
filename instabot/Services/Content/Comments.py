import subprocess
import json

# import sys
# topic = sys.argv[1]
# maxpp = sys.argv[2]
# num = sys.argv[3]

def getComments(topic, maxpp, num):
    information = subprocess.check_output(["php", "phpapi/comments.php", str(topic), str(maxpp), str(num)])
    information_dict = str(information.decode('utf-8'))
    data = {}
    data['topic'] = topic
    data['maxpp'] = maxpp
    data['num'] = num
    data['comments'] = information_dict
    return data

def getCommentsSaveToFile(topic, maxapp, num):
    data = getComments(topic, maxapp, num)
    with open('savedStatus/comments.json', 'w') as f:
        json.dump(data, f)
    #open file
    # fh = open('phpapi/resources/comments.json', 'r')
    # # if file does not exist, create it
    # if not fh:
    #     fh = open('phpapi/resources/comments.json', "w")
    #
    # with open('phpapi/resources/comments.json', 'a') as f:
    #     f.write("\n")
    #     f.write("\n")
    #     f.write(json.dumps(data).decode('unicode-escape').encode('utf8'))
    #
    # print('..results added to phpapi/resources/comments.json file.')

    return data