import argparse as arg
parser = arg.ArgumentParser(description='Calculate the exponent of given number, sample to practise argparse')
parser.add_argument("testflag", type=int, help="display the test")
parser.add_argument("-l", "--list", type=int, help="given number and power", required=True, nargs='+')
parser.add_argument("-v", "--verbosity", type=int, choices=[0,1], help="increate output verbosity", default=0)
args=parser.parse_args()

#answer=args.testflag**2
if args.testflag==1:
    print("test success")
list=args.list;
answer=list[0]**list[1]
if args.verbosity==1:
    print"the number {0} power {1} is {2}".format(list[0], list[1], answer)
else:
    print(answer) 
