# 文物服务器服务
## 运行方式
```
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