from django.shortcuts import render

# Create your views here.

#views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.http import HttpResponse

from line_app.serializers import *
from line_app.models import *

import time
from datetime import datetime
import os

# 自遍函数
from core import *

# Create your views here.
class movieViews(APIView):
    def get(self, request):
        movies = Film.objects.all()
        serializer = FilmSerializer(movies, many=True)
        data = {'message': 'This is a sample response'}
        return Response(serializer.data)

def process_file(request):
    if request.method != "POST":
        return HttpResponse('只支持 POST 请求', status=405)

    else:
        file_obj = request.FILES.get('filename') # 获取前台传来的文件对象
        upload_file_name = file_obj.name

        # 检测文件类型
        r_content_type, r_check_file_type = check_file_type(upload_file_name)
        if r_check_file_type != 0 :
            return HttpResponse('不支持的文件类型', status=400)

        # 生成输入输出文件路径
        upload_subpath, upload_file_path, processed_subpath, processed_file_path = gen_paths(upload_file_name)
        
        # 保存输入文件
        with open(upload_file_path, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        
        
        # 处理图片
        result = img_process(upload_file_path,processed_file_path)


        # 返回处理后的图片
        image_path = processed_file_path  
        if os.path.exists(image_path) and result == 0:

            # 以二进制模式打开图片文件
            with open(image_path, 'rb') as image_file:
                # 创建 HttpResponse 对象，并将图片内容作为响应体
                response = HttpResponse(image_file.read(), content_type=r_content_type)
                # 设置 Content-Disposition 头，指定文件名
                filename = os.path.basename(image_path)
                response['Content-Disposition'] = f'attachment; filename="{filename}"'

        else:
            return HttpResponse('图片文件未找到', status=404)


        # 创建新的 File 对象 记录到数据库
        File.objects.create(upload_file=upload_subpath,processed_file=processed_subpath)
        return response

# 检查文件类型是否支持
def check_file_type(upload_file_name):
    r = 0
    file_extension = os.path.splitext(upload_file_name)[1].lower()
    if file_extension == '.jpg':
        r_content_type = 'image/jpeg'
    elif file_extension == '.png':
        r_content_type = 'image/png'
    else:
        r = 1 #不支持类型
    return r_content_type,r

# 生成输入输出文件路径

def gen_paths(upload_file_name):
    timestamp = datetime.now()
    time_str = timestamp.strftime("%Y%m%d%H%M%S%f")
    upload_file_name = f"{os.path.splitext(upload_file_name)[0]}_{time_str}{os.path.splitext(upload_file_name)[1]}"

    upload_subpath = os.path.join('upload',upload_file_name)
    upload_file_path = os.path.join(settings.MEDIA_ROOT, upload_subpath)
    processed_subpath = os.path.join('processed',upload_file_name)
    processed_file_path = os.path.join(settings.MEDIA_ROOT, processed_subpath)
    return upload_subpath,upload_file_path,processed_subpath,processed_file_path


