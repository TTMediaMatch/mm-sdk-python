# coding:utf-8

from setuptools import setup, find_packages

setup(
    name="mediamatch_sdk",
    version="1.0.1",
    keywords=("pip", "ttmediamatch", "mm-sdk-python"),
    description="The Python SDK for Mediamatch",
    license="MIT Licence",

    url="https://github.com/TTMediaMatch/mm-sdk-python",
    author="TTMediamatch SDK",
    author_email="shengyang.wang@bytedance.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests"]
)
