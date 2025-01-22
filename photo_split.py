
import os
import shutil


def split_images(input_directory, output_directory, batch_size=40):
    # 创建输出目录
    os.makedirs(output_directory, exist_ok=True)

    # 初始化计数器
    image_count = 0
    batch_index = 1

    # 创建批次文件夹
    batch_directory = os.path.join(output_directory, f'batch_{batch_index}')
    os.makedirs(batch_directory, exist_ok=True)

    # 遍历输入目录中的所有文件
    for filename in sorted(os.listdir(input_directory)):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):  # 只处理图片文件
            image_count += 1
            image_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(batch_directory, filename)
            shutil.copyfile(image_path, output_file_path)

            # 如果达到了batch_size，则创建一个新文件夹
            if image_count % batch_size == 0:
                batch_index += 1
                batch_directory = os.path.join(output_directory, f'batch_{batch_index}')
                os.makedirs(batch_directory, exist_ok=True)

    # 如果最后一个文件夹没有图片，则删除该文件夹
    if image_count % batch_size == 0:
        os.rmdir(batch_directory)

    print(f"Splitting complete. Total number of images: {image_count}")



# 使用示例
input_directory_path = 'E:\\tools_data\\Great_wall_2024_3_27\\3.qiangtiliehen\\photo'

output_directory_path = './data_3_27/qiangtiliehen_2024_3_27'
split_images(input_directory_path, output_directory_path)



