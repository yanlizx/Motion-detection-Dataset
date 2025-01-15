# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:43:21 2024

@author: 35042
"""

import csv

# 读取txt文件内容，并将逗号分隔的第二、四、五、六列写入csv文件的1、2、3、4列
def txt_to_csv(input_txt_path, output_csv_path):
    with open(input_txt_path, 'r') as txt_file, open(output_csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        for line in txt_file:
            # 将每行按照逗号分隔
            columns = line.strip().split(',')
            
            # 提取第二、第四、五、六列并写入到csv文件的1、2、3、4列
            csv_writer.writerow([columns[1], columns[3], columns[4], columns[5]])

# 调用函数，指定输入txt文件路径和输出csv文件路径
txt_to_csv('WISDM.txt', 'WISDM.csv')
