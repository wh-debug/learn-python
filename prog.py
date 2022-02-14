import argparse

# 什么是位置参数
# 什么是可选参数
parser = argparse.ArgumentParser()

# 位置参数
parser.add_argument("echo", help="echo the string you are here")
# 如果是输入的是整型数字，那么需要指定type为int型或者其他类型参数，因为type默认是字符型参数
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.echo)
print(args.square**2)
