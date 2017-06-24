try:
	from setuptools import setup #setuptools工具针对Python官方的distutils做了很多针对性的功能增强，比如依赖检查，动态扩展等.
except ImportError:
	from distutils.core import setup #The distutils.core module is the only module that needs to be installed to use the Distutils. It provides the setup() (which is called from the setup script). Indirectly provides the distutils.dist.Distribution and distutils.cmd.Command class.

config={
	'description':'My Project', #项目描述
	'author':'My Name',#作者
	'url':'URL to get it at.',#网址
	'download_url':'Where to download it.',#下载安装包的网址
	'author_email':'My email.',#作者的邮箱
	'version':'1.0',#安装包的发行版本
	'install_requires': ['nose'],#代替require函数。表示当前包的安装依赖于哪些分发包，这些信息会写入egg的元信息中，这些包在安装时会自动（从PyPI）下载并安装。如果包在PyPI中找不到，则会从dependency_links标识的URL中获取。
	'packages': ['NAME'],#告诉Distutils需要处理那些包（包含__init__.py的文件夹）（when you say packages = ['foo'] in your setup script, you are promising that the Distutils will find a file foo/__init__.py）
	'scripts': [],#脚本名称
	'name':'ex48a.py' #项目名称
}

setup(**config)
