import argparse

parser = argparse.ArgumentParser()
parser.add_argument('range_start', type=int)
parser.add_argument('range_end',  type=int)
args = parser.parse_args()

#for i in range(1,6):
for i in range(args.range_start,args.range_end):
    print(i, end=" ")
    for j in range(4):
        
        print(i ** j, end=" ")
    print()

