# meiduo
首先进入虚拟环境:  py3_django_pro
	1. 静态目录: live-server
		a. cd /home/python/Desktop/Progect/Django/meiduo/front_end_pc
		b. 控制台输入live-server
		
	2. 后端: manage runserver
		a. 通过pycharm打开meiduo
		b. 启动 manage
		
	3. 图片资源: docker container start 容器名
		a. 启动容器 docker container start tracker
		b. 启动容器 docker container start storage
		c. 启动容器 docker container start elasticsearch
		d. 启动容器 docker container start mysql-slave
	4. 临时数据: redis-server ./redis.conf
		a. 进入redis-server配置文件目录: /etc/redis
终端输入: redis-server ./redis.conf
