# 校园卡系统
powered by [Django](https://www.djangoproject.com/) and [Bootstrap](https://getbootstrap.com/)

## 模块功能：
- 登录注册、修改密码
- 账户管理、充值、消费

## 部署说明

**1. 下载本仓库，需[Git](https://git-scm.com/)**
```shell
git clone https://github.com/WIndki/CampusCardMgrSys.git
cd CampusCardMgrSys
```
**2. 创建虚拟环境（建议）**
- 使用 venv 创建虚拟环境，这将创建一个名为 CampusCardMgrSys 的虚拟环境目录。
```shell
python -m venv CampusCardMgrSys
```
- 激活虚拟环境： 在Windows上运行以下命令：
```shell
CampusCardMgrSys\Scripts\activate
```
- 在macOS和Linux上运行以下命令：
```shell
source CampusCardMgrSys/bin/activate
```
- 安装依赖： 激活虚拟环境后，运行以下命令安装 requirements.txt 文件中的依赖：
```shell
pip install -r requirements.txt
```
**使用 conda 创建虚拟环境（可选）**
- 安装 [Anaconda](https://www.anaconda.com/products/individual) 或 [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- 创建虚拟环境：
```shell
conda create --name CampusCardMgrSys python=3.8
```
- 激活虚拟环境：
```shell
conda activate CampusCardMgrSys
```
- 安装依赖：
```shell
pip install -r requirements.txt
```
**3. 数据库迁移**
- 运行以下命令进行数据库迁移：
```shell
python manage.py makemigrations
python manage.py migrate
```

**4. 创建超级用户**
- 创建超级用户以访问 Django 管理界面：
```shell
python manage.py createsuperuser
```
- 按照提示输入用户名、电子邮件和密码。

**5. 运行开发服务器**
- 启动 Django 开发服务器：
```shell
python manage.py runserver
```
- 打开浏览器并访问 `http://127.0.0.1:8000` 查看项目。

**6. 访问管理界面**
- 访问 `http://127.0.0.1:8000/admin` 并使用超级用户凭据登录。

**7. 部署到生产环境**
- 使用 [Gunicorn](https://gunicorn.org/) 和 [Nginx](https://www.nginx.com/) 部署到生产环境。
- 安装 Gunicorn：
```shell
pip install gunicorn
```
- 使用 Gunicorn 运行项目：
```shell
gunicorn --bind 0.0.0.0:8000 main.wsgi:application
```
- 配置 Nginx 以反向代理到 Gunicorn。

**8. 静态文件**
- 收集静态文件：
```shell
python manage.py collectstatic
```
- 确保 Nginx 配置正确以提供静态文件。

**9. 环境变量**
- 使用 `.env` 文件或其他方式设置环境变量，如数据库配置、密钥等。

**10. 备份和恢复**
- 定期备份数据库和重要文件。
- 测试恢复过程以确保备份有效。
### 目录结构
```
CampusCardMgrSys
├─ .git
│  ├─ config
│  ├─ description
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  ├─ sendemail-validate.sample
│  │  └─ update.sample
│  ├─ info
│  │  └─ exclude
│  ├─ objects
│  │  ├─ info
│  │  └─ pack
│  └─ refs
│     ├─ heads
│     └─ tags
├─ .gitignore
├─ main
│  ├─ main
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  └─ __init__.py
│  ├─ mainsys
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ form.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_alter_user_lastlogin_alter_user_username.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ templates
│  │  │  ├─ account.html
│  │  │  ├─ add.html
│  │  │  ├─ changepassword.html
│  │  │  ├─ index.html
│  │  │  ├─ layout.html
│  │  │  ├─ login.html
│  │  │  ├─ register.html
│  │  │  └─ shop.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  └─ manage.py
├─ readme
└─ requirements.txt
```

## 许可证

本项目采用BSD许可证，详情如下：

```
BSD 3-Clause License

Copyright (c) 2023, CampusCardMgrSys
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

### 第三方库版权声明

- Django 是由 Django Software Foundation 开发和维护的开源项目，遵循 BSD 许可证。
- Bootstrap 是由 Twitter, Inc. 开发和维护的开源项目，遵循 MIT 许可证。