该工具用于将整个目录下或单个proto文件生成对应的Java类，而无需借助其他插件---提效。

# 1. 处理整个目录
```Bash
#默认输入目录(source) → 默认输出目录(out)
./generate.sh

# 指定输入目录和输出目录
./generate.sh -i my_protos -o generated_code
```

# 2. 处理单个文件
```Bash
# 指定单个文件
./generate.sh -i source/user.proto -o out

# 指定绝对路径
./generate.sh -i /tmp/test.proto -o /tmp/out
```

注意：提示没有权限则先执行命令`chmod +x generate.sh`赋予执行权限再执行命令


protobuf工具获取地址： https://github.com/protocolbuffers/protobuf/releases