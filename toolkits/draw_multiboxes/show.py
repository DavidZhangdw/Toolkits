import cv2
from otb import OTB
import os
import numpy as np
import json
'''
 运行说明：
 record=True 时会存储多跟踪框的结果图
 >>输入文件
 1、data:OTB2015数据集   结构为：data/Basketball/img/*.jpg   data/Basketball/groundtruth_rect.txt
 2、results:输出文件  可为got10k工具的结果(txt文件)，也可为vot-toolkit工具的结果(json文件)
 >>输出文件
 1、output_mutibox    图片命名：{序列名}_{下标}.jpg
 '''


def view_result(record):
    src="data"
    box_dir="results"
    dataset = OTB(src,version=2015,download=False)

    for s,(images,anno) in enumerate(dataset):
        seq_name =dataset.seq_names[s]
        record_file1=os.path.join(box_dir,'DCANet','%s.txt'%seq_name)
        record_file2 = os.path.join(box_dir, 'SiamFC', '%s.txt' % seq_name)
        record_file3 = os.path.join(box_dir, 'MUSTer', '%s.json' % seq_name)
        if not os.path.exists(record_file3) :
            continue
        box1=np.loadtxt(record_file1,delimiter=',')
        box2 = np.loadtxt(record_file2, delimiter=',')

        #对json形式文件的读取部分
        resultFile = open(record_file3)
        string = resultFile.read()
        jsonList = json.loads(string)
        box3 =jsonList[0]["res"]


        for i,image in enumerate(images):
            image=cv2.imread(image)

            x1, y1, w1, h1 = anno[i]  # gt
            x2, y2, w2, h2 = box1[i]  # dcanet
            x3, y3, w3, h3 = box2[i]  # siamfc
            if i == len(box3):
                break
            #说明：因为MUSTer跟踪器结果和OTB2015不完全一致，加了个判断
            x4, y4, w4, h4 = box3[i]  # muster

            color1 = (0, 255, 0)  #绿色：groundtruth
            color2 = (255, 0, 0)  #红色：dcanet
            color3 = (255, 255, 0)  #黄色：siamfc
            color4 = (0,0,255)  #蓝色：muster
            # Line thickness of 2 px
            thickness = 2
            out = cv2.rectangle(image, (int(x1), int(y1)), (int(x1 + w1), int(y1 + h1)), color1, thickness)
            out = cv2.rectangle(out, (int(x2), int(y2)), (int(x2 + w2), int(y2 + h2)), color2, thickness)
            out = cv2.rectangle(out, (int(x3), int(y3)), (int(x3 + w3), int(y3 + h3)), color3, thickness)
            out = cv2.rectangle(out, (int(x4), int(y4)), (int(x4 + w4), int(y4 + h4)), color4, thickness)
            print("{sequence}{id}".format(sequence=seq_name, id=i))



            #cv2.imshow("draw_0", out)  # 显示画过矩形框的图片
            if record:
                cv2.imwrite("output_mutibox/{seq_name}_{id}.jpg".format(seq_name=seq_name, id=i), out)
            #cv2.waitKey(0)

if __name__ == '__main__':
    view_result(record=True)
