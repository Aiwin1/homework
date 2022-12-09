# Linux----作业过程简介



# 一、Socket
1.通过dockerfile创建两个Docker容器

```
FROM ubuntu:latest
RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' /etc/apt/sources.list;
RUN apt-get update --fix-missing &&apt-get install -y python3
RUN apt-get install -y vim
RUN apt-get install -y wget
CMD /bin/bash
```

> 利用from定制ubuntu镜像，然后更换镜像的源(主要是源镜像好像安装python环境报错)，通过RUN安装Python环境和一些命令。

2.运行命令docker bulid -f dockerfile -t name . 生成Ubuntu镜像容器
3.docker images查看镜像
4.docker run -p 40:40 -v /data:/data -d  IMAGE_NAME 运行容器并映射目录
5.docker exec -it images_id  /bin/bash进入容器
6.进入Ubuntu命令行后运行py文件即可

![在这里插入图片描述](https://img-blog.csdnimg.cn/fbc7f5d7c5904b059f8e8b05f2103922.png)

# 二、Hugo
1.sudo apt-get install git	下载git
2.git config --global user.name/user.email	配置昵称和邮箱
3.wget https://github.com/spf13/hugo/releases/download/v0.14/hugo_0.14_amd64.deb	下载Hugo包
4.sudo dpkg -i hugo*.deb 安装dpgk包
5.hugo new site /path 生成站点
6.可以使用模板，git clone url拉取模板，放在themes目录，修改config.toml文件修改成自己想要的
7.hugo new post/first.md 生成文章，文章至于content/posts目录
8. hugo Server 运行Hugo站点即可
9. 将Hugo搞好文章，目录等后，使用Hugo -D建立public文件
10.将public文件放至apache或者nginx的/var/www/html目录即可 
![在这里插入图片描述](https://img-blog.csdnimg.cn/479e46f02daf427d9f98fb89bc981457.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/91c50ba90a0b4257a5ed641f5d4fe83d.png)
# 三、Git
1. 先在github中注册token
![在这里插入图片描述](https://img-blog.csdnimg.cn/1683cb3231c34ecca8239ecc5514d3c1.png)
2.git add添加需要的到缓存区
3.git commit提交到将暂存区文件交到仓库区
4.git remote add 别名 url 创建远程仓库
5.git push -u 别名 分直 提交到github仓库中
6.输入用户名和Token即可
![在这里插入图片描述](https://img-blog.csdnimg.cn/01a892a4c7e24f689038a14316fb7276.png)

