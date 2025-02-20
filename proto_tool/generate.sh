#!/bin/bash
# 确保脚本具有执行权限（若没有，执行: chmod +x generate.sh）
# 用法: ./generate.sh -i [文件或目录] -o [输出目录]
# -i 参数可选，默认source目录， -o 参数可选，默认out目录
DIR=$(cd "$(dirname "$0")" && pwd)
cd "$DIR" || exit
python3 generate_proto.py "$@"