import argparse

# 创建解析器
parser = argparse.ArgumentParser()
# 添加参数
parser.add_argument('--file', type=str, help='转换文件')
# 解析参数
args = parser.parse_args()
# 输出参数
print(f'{args.file}')

