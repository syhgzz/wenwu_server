import shutil

def img_process(input_file_path,output_file_path):
    print("处理图像中")
    shutil.copy(input_file_path,output_file_path)
    print("处理图像完成")
