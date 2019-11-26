import os
import json

# print(os.listdir("C:\\Users\\chase\\Desktop\\test"))
# # print(json.loads("C:\\Users\\chase\\Desktop\\test\\1.json"))
# with open("C:\\Users\\chase\\Desktop\\test\\1.json", 'r+') as f1:
#     content = json.load(f1)
#     # print(content['res'])
#     each_line = ""
#     for i in range(0, len(content['res'])):
#         each_res = list(content['res'][i])
#
#         for j in range(0, len(each_res)):
#
#             if j < len(each_res)-1:
#                 each_line += str(each_res[j]) + ","
#             else:
#                 each_line += str(each_res[j]) + "\n"
#
#     with open("test.txt","w+") as t:
#         t.write(each_line)
#
#     print(each_line)


#dirPath是存放json文件的文件夹,saveTxtPath是保存txt的文件夹
def json2txt(dirPath,saveTxtPath):
    jsonList = os.listdir(dirPath)
    for jsonName in jsonList:
        jsonFilePath = dirPath+"/"+jsonName
        with open(jsonFilePath, 'r+') as f:
            content = json.load(f)
            # print(content['res'])
            each_line = ""
            for i in range(0, len(content['res'])):
                each_res = list(content['res'][i])

                for j in range(0, len(each_res)):

                    if j < len(each_res) - 1:
                        each_line += str(each_res[j]) + ","
                    else:
                        each_line += str(each_res[j]) + "\n"
            txtName = jsonName.split(".")[0]+".txt"
            with open(txtName, "w+") as t:
                t.write(each_line)
                t.close()
            f.close()

json2txt("C:/Users/chase/Desktop/test","E:/pycharm/myTest")