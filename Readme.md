# Python Start Project Template

![Tests](https://github.com/wangzhe3224/python_project_template/actions/workflows/test.yml/badge.svg)

: )

如何配置一个自动测试的Python项目?

前置知识：

- 如何配置虚拟环境
- github的基本使用

1. 项目结构
    1. 分离源代码和测试
    2. 配置项目本地安装
       1. `pyproject.toml`
       2. `setup.py/cfg`
       3. `requirements.txt`
       4. `pip install -e .`
2. 自动测试、类型检查、代码规范检查
   1. pytest/mypy/flake8
   2. `requirements_dev.txt`
   3. 配置`setup.cfg`，增加pytest,mypy,flake的相关配置
   4. 配置`pyproject.toml`，增加pytest，mypy的相关配置
3. 多环境测试
   1. 配置`tox.ini`
2. 自动测试，Github Action
   1. 配置 GH on commit 动作
   2. 增加 readme 的测是·标签
