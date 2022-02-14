import argparse
"""
(pytorch) wh@wh-ASUS-TUF-Gaming-F15-FX506HCB:~/python$ python3 opt_action_test.py 4 -v
4^2 == 16
(pytorch) wh@wh-ASUS-TUF-Gaming-F15-FX506HCB:~/python$ python3 opt_action_test.py 4 -vv
the square of 4 equals 16
(pytorch) wh@wh-ASUS-TUF-Gaming-F15-FX506HCB:~/python$ python3 opt_action_test.py 4 -vvv
16

"""

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
# 动作 "count"，来统计特定选项出现的次数。
parser.add_argument("-v", "--verbosity", action="count", help="increase output verbosity", default=0)
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)
print(__file__) # 显示正在运行的当前文件的名字
