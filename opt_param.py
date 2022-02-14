import argparse

parser = argparse.ArgumentParser()
# 不添加这一选项时程序没有提示任何错误而退出，表明这一选项确实是可选的。
# parser.add_argument("--verbosity", help="increase output verbosity")

# 注意我们现在指定了一个新的关键词 action，并赋值为 "store_true"。这意味着，当这一选项存在时，为 args.verbose 赋值为 True。没有指定时则隐含地赋值为 False。
# parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")

parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()

if args.verbosity:
    print("verbosity turned on")