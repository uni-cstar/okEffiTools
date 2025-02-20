该工具用于将整个目录下或单个proto文件生成对应的Java类，而无需借助其他插件---提效。

注意：提示没有权限则先执行命令`chmod +x generate.sh`赋予执行权限再执行命令
注意：脚本会使用protoc脚本，系统会禁止运行，在第一次运行脚本时会弹出阻止运行对话框，需要通过系统设置->安全性设置中点击仍要打开protoc（跟系统运行其他未知程序一样的流程）

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



protobuf工具获取地址： https://github.com/protocolbuffers/protobuf/releases