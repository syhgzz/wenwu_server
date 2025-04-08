# 文物服务器服务
## 运行方式
```
mkdir ./media/upload
mkdir ./media/processed
conda env create -n wenwu -f env.yml
conda activate wenwu
cd ~/repos/wenwu
./manage.py makemigration
./manage.py migrate
./manage.py createsuperuser
```
## 运行服务器
1. `./manage.py runserver 0.0.0.0:8000`
2. 如有端口映射, 请修改 ./frontend_app/templates/frontend.html 中
```
function processImage()  
const apiUrl = 'http://10.61.84.84:38000/process_file/';
```

## 管理页面
1. 路由为 /admin

## 外调程序
1. core.py 文件中的函数 img_process
2. 调用C++ openCV程序可能会遇到报错. 这是因为编译被调用程序的C++标准库版本高于conda自带的库. 
```
OSError: /home/zhouzhuo/miniconda3/envs/wenwu/lib/python3.13/site-packages/../../libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /lib/x86_64-linux-gnu/libopencv_core.so.406)

执行  conda install -c conda-forge libstdcxx-ng 升级conda内部的c++标准库版本
```

## 制作自启动服务
```
sudo cp ./wenwu.service /etc/systemd/system/wenwu.service
sudo systemctl daemon-reload
sudo systemctl enable wenwu
sudo systemctl start wenwu
sudo systemctl status wenwu
```