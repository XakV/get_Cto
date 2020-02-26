#!/bin/python3

import requests
import hashlib
import pathlib

def get_corretto(version = 'latest', jdk = '8'):
    get_jdk = requests.get('https://corretto.aws/downloads/latest/amazon-corretto-8-x64-linux-jdk.tar.gz')
    with open('corretto.tar.gz', 'wb') as ctar:
        ctar.write(get_jdk.content)
    cor_path = pathlib.PosixPath.joinpath(pathlib.PosixPath.cwd(), 'corretto.tar.gz')
    return cor_path

def get_corretto_checksum(version = 'latest', jdk = '8'):
    get_jdk_cksum = requests.get('https://corretto.aws/downloads/latest_checksum/amazon-corretto-8-x64-linux-jdk.tar.gz')
    with open('jdk_8.md5', 'w') as cksum:
        cksum.write(get_jdk_cksum.text)
    cksum_path = pathlib.PosixPath.joinpath(pathlib.PosixPath.cwd(), 'jdk_8.md5')
    print(f"{cksum_path}")
    print(f"{ get_jdk_cksum.text }")
    return cksum_path

def hash_corretto(jdk_file):
    cor_md5 = hashlib.md5()
    with open(jdk_file, 'rb') as jdkbytes:
        cor_md5.update(jdkbytes.read())
    cor_md5_sum = cor_md5.digest()
    return cor_md5_sum

new_corretto = get_corretto()
new_co_cksum = get_corretto_checksum()
hashed_dl = hash_corretto(new_corretto)
with open(new_co_cksum, 'r') as dl_cksum:
    checksum_dl = dl_cksum.readlines()
if checksum_dl == hashed_dl:
    print(f"file ok")
else:
    print(f"Downloaded checksum is { dl_cksum }")
    print(f"Hashed value is { hashed_dl }")