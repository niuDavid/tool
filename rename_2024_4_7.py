#
# import os
# import json
#
# path = "E:\\ai_project\\greatwall_data\\data_4_26\\fenghuotai"
#
# # 获取该目录下所有文件，存入列表中
# fileList = os.listdir(path)
#
# # 为不同类型文件定义计数器
# counters = {'txt': 0, 'png': 0, 'jpg': 0, 'json': 0}
#
# for filename in fileList:
#     # 获取文件扩展名
#     name, ext = os.path.splitext(filename)
#     ext = ext.lower()[1:]  # 去除扩展名前的点号，并转换为小写
#
#     # 检查文件类型
#     if ext in counters:
#         # 设置旧文件名（就是路径+文件名）
#         oldname = os.path.join(path, filename)
#
#         # 设置新文件名，格式化字符串确保文件名数字部分长度为6
#         newname = os.path.join(path, f'{int(counters[ext]) + 1:05d}.{ext}')
#
#         # 重命名文件
#         os.rename(oldname, newname)
#
#         # 如果文件类型是 JSON
#         if ext == 'json':
#             # 读取 JSON 文件内容
#             with open(newname, 'r') as json_file:
#                 data = json.load(json_file)
#
#             # 替换 JSON 内容中的 imagePath 字段
#             image_name = f'{int(counters["png"]) + 1:05d}.png'
#             data['imagePath'] = image_name
#
#             # 写回 JSON 文件
#             with open(newname, 'w') as json_file:
#                 json.dump(data, json_file, indent=4)
#
#             print(f'Renamed and updated JSON file: {oldname} ==> {newname}')
#
#         print(oldname, '======>', newname)
#
#         counters[ext] += 1


import os
import json

path = "D:\\BaiduNetdiskDownload\\监狱-2025-1-19\\alone_images_enhance\\labels"
start_num = 1000 # 自定义起始计数器值

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

# 为不同类型文件定义计数器，从start_num开始
counters = {'txt': start_num, 'png': start_num, 'jpg': start_num, 'json': start_num}

for filename in fileList:
    # 获取文件扩展名
    name, ext = os.path.splitext(filename)
    ext = ext.lower()[1:]  # 去除扩展名前的点号，并转换为小写

    # 检查文件类型
    if ext in counters:
        # 根据自定义起始值和当前计数器设置新文件名
        new_count = counters[ext]
        newname = os.path.join(path, f'{new_count:05d}.{ext}')
        oldname = os.path.join(path, filename)

        # 重命名文件
        os.rename(oldname, newname)

        # 如果文件类型是 JSON
        if ext == 'json':
            # 读取 JSON 文件内容
            with open(newname, 'r') as json_file:
                data = json.load(json_file)

            # 构建新的imagePath，基于png计数器（假设图片与json一一对应，且以png格式为例）
            image_name = f'{counters["png"]:05d}.png'
            data['imagePath'] = image_name

            # 写回 JSON 文件
            with open(newname, 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print(f'Renamed and updated JSON file: {oldname} ==> {newname}')

        print(oldname, '======>', newname)

        # 更新计数器
        counters[ext] += 1