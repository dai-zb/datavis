# coding=utf-8

from setuptools import setup, find_packages
import os

author = 'dzb'
author_email = 'dai_zb@163.com'
description = "A library with some simple tool functions"
url = ""

name = os.path.split(os.getcwd())[1]  # 当前文件名作为工程名
name = name.split("-")[0]
src_lst = os.listdir("src")
assert (len(src_lst) == 1 and name in src_lst) or (
        len(src_lst) == 2 and name in src_lst and f"{name}.egg-info" in src_lst)

with open(f"src/{name}/__init__.py", "r", encoding="utf-8") as f:
    for line in f.readlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
            break
    else:
        print("Can't find version! Stop Here!")
        exit(1)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,

    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",

    url=url,

    # packages=find_packages(),  # 会把当前目录下所有 __init__.py 文件的目录都扫描出来
    packages=find_packages("src"),
    package_dir={"": "src"},

    classifiers=[  # 给包额外的元数据，比如 代码版本的兼容性、证书许可、操作系统相关
        # "Development Status :: 4 - Beta",
        # "Programming Language :: Python :: 3.6",
        # "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        # "Programming Language :: Python :: 3.9",
        # "Programming Language :: Python :: 3.10",
        # "Intended Audience :: Developers",
        # "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",

    # 安装依赖的包，如果环境中没有，则会从pypi中下载安装
    install_requires=["matplotlib", "numpy"],
    # install_requires=["matplotlib>=3.4"],

    # 这些包不会被自动安装
    setup_requires=["mypy", "coverage"],
)
# python 3.5  引入了asyncio
# python 3.6  引入了f-string


s = f"""
# 打包成为wheel
python setup.py bdist_wheel

# 本地安装
pip install dist/{name}*.whl

# 查看安装的结果
pip list

# 卸载
pip uninstall -y {name}

# 重新安装
pip uninstall -y {name} && python setup.py bdist_wheel && pip install dist/{name}*.whl
"""
print(s)
