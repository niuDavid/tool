import cv2
import os

# 视频文件路径
#video_file = 'D:\\BaiduSyncdisk\\video\\traffic_net\\project\\test_code\\results\\Video\\testvideo_11_13\\new_map.avi'
video_file = '7_3.mp4'
# 新文件夹路径用于保存生成的帧图片
output_folder = 'frame_image_7_3'

# 创建新文件夹
os.makedirs(output_folder, exist_ok=True)


# 打开视频文件
cap = cv2.VideoCapture(video_file)

# 检查视频文件是否成功打开
if not cap.isOpened():
    print("无法打开视频文件")
    exit()

# 初始化帧计数器
frame_count = 0
save_count  = 0
while True:
    # 读取视频的每一帧
    ret, frame = cap.read()

    # 检查帧是否读取成功
    if not ret:
        print("无法读取帧")
        break

    #每隔5帧保存一次帧图片
    if frame_count % 5 == 0:

        # 生成帧文件名
        frame_filename = f'frame_{save_count}_7_3.png'
        # 保存帧为图片
        frame_path = os.path.join(output_folder, frame_filename)
        cv2.imwrite(frame_path, frame)

        # 打印当前帧的信息
        print(f"保存帧: {frame_filename}")

        # 增加保存计数器
        save_count += 1
    # 增加帧计数器
    frame_count += 1

# 释放资源
cap.release()
