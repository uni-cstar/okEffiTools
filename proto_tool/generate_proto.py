#!/usr/bin/env python3
import os
import subprocess
import argparse

# 默认配置
DEFAULT_PROTO_DIR = "source"
DEFAULT_JAVA_OUT = "out"
# 改为动态获取绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROTOC_PATH = os.path.join(BASE_DIR, "tools", "protoc", "bin", "protoc")

print(f"完整protoc路径：{os.path.abspath(PROTOC_PATH)}")

def check_and_create_dir(path):
    """强制创建缺失目录并打印提示"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"⚠️ 自动创建缺失目录: {os.path.abspath(path)}")
    elif not os.path.isdir(path):
        print(f"❌ 路径 {path} 是文件而非目录！")
        exit(1)

def is_proto_file(path):
    return os.path.isfile(path) and path.endswith(".proto")

def generate_proto(input_path, java_out):
    # 检查protoc
    if not os.path.exists(PROTOC_PATH):
        print(f"错误: protoc未找到，请确认已放置到 {PROTOC_PATH}")
        return False

    # 处理输入路径为绝对路径
    input_path = os.path.abspath(input_path)
    print(f"输入路径绝对地址: {input_path}")
    # 输入路径校验
    if not os.path.exists(input_path):
        print(f"错误: 输入路径不存在 - {input_path}")
        return False

    # 处理输出路径为绝对路径
    java_out = os.path.abspath(java_out)
    print(f"输出路径绝对地址: {java_out}")
    # 强制创建目录
    check_and_create_dir(java_out)

    # 处理单个文件
    if is_proto_file(input_path):
        proto_dir = os.path.dirname(input_path)
        proto_file = os.path.basename(input_path)
        return process_proto_file(proto_dir, proto_file, java_out)

    # 处理目录
    generated_count = 0
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.endswith(".proto"):
                success = process_proto_file(root, file, java_out)
                if not success:
                    return False
                generated_count += 1

    print(f"生成完成！共处理 {generated_count} 个文件")
    return True

def process_proto_file(proto_dir, proto_file, java_out):
    """处理单个proto文件"""
    proto_path = os.path.join(proto_dir, proto_file)
    cmd = [
        PROTOC_PATH,
        f"--proto_path={proto_dir}",
        f"--java_out={java_out}",
        proto_file  # 使用相对路径避免绝对路径问题
    ]
    try:
        result = subprocess.run(
            cmd,
            cwd=proto_dir,  # 关键：在proto所在目录执行命令
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"[✅] 成功生成: {proto_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[❌] 失败: {proto_file}\n错误信息:\n{e.stderr.strip()}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Protobuf编译工具 - 支持文件/目录输入")
    parser.add_argument("-i", "--input",
                        default=DEFAULT_PROTO_DIR,
                        help="输入路径（.proto文件或目录）")
    parser.add_argument("-o", "--output",
                        default=DEFAULT_JAVA_OUT,
                        help="Java输出目录")
    args = parser.parse_args()

    check_and_create_dir(args.output)
    print(f"输入路径: {args.input}")
    print(f"输出目录: {args.output}")
    print("=" * 50)

    success = generate_proto(args.input, args.output)
    if success:
        print("\n操作成功！")
    else:
        print("\n操作失败，请检查错误信息！")
        exit(1)