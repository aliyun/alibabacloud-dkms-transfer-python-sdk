# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

"""
setup module for dkms-transfer-python.

Created on 05/23/2022

@author: Alibaba Cloud SDK
"""

packages = find_packages()
NAME = "alibabacloud-dkms-transfer-python"
DESCRIPTION = "Alibaba Cloud Dedicated KMS Transfer SDK for Python"
AUTHOR = "Alibaba Cloud SDK"
AUTHOR_EMAIL = "sdk-team@alibabacloud.com"
URL = "https://github.com/aliyun/alibabacloud-dkms-transfer-python-sdk"
VERSION = "0.0.3"
REQUIRES = [
    "alibabacloud_dkms_gcs>=0.0.3",
    'aliyun_python_sdk_core>=2.13.30',
    'aliyun_python_sdk_kms>=2.14.0',
]

LONG_DESCRIPTION = ''
if os.path.exists('./README.rst'):
    with open("./README.rst", encoding='utf-8') as fp:
        LONG_DESCRIPTION = fp.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License 2.0",
    url=URL,
    keywords=["alibabacloud", "dkms-transfer-sdk"],
    packages=find_packages(exclude=["example*"]),
    include_package_data=True,
    platforms="any",
    install_requires=REQUIRES,
    python_requires=">=3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development"
    ],
)
