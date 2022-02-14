import argparse
"""
    结果：
        (pytorch) wh@wh-ASUS-TUF-Gaming-F15-FX506HCB:~/python$ python3 opt_location_param.py 4 
        16
        (pytorch) wh@wh-ASUS-TUF-Gaming-F15-FX506HCB:~/python$ python3 opt_location_param.py 4 -v
        the square of 4 equals 16
        (pytorch) wh@wh-ASUS-TUF-Gaming-F15-FX506HCB:~/python$ python3 opt_location_param.py -v 5
        the square of 5 equals 25
"""
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
# 注意--而不是-
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)