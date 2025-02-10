import shutil

import ctypes
import os





def img_process(input_file_path,output_file_path):
    print("处理图像中")
    # shutil.copy(input_file_path,output_file_path)

    lg = ctypes.CDLL("/usr/lib/libLineGenerator.so")

    # 定义函数参数和返回类型
    lg.go_py.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    lg.go_py.restype = ctypes.c_int


    input_cstr = input_file_path.encode()
    output_cstr = output_file_path.encode()

    # 调用函数
    result = lg.go_py(input_cstr, output_cstr)

    print("处理图像完成")
