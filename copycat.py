#!/usr/bin/env python3

import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("output_filename", help="Specify the file name to output the result")
parser.add_argument("-u", "--unique", help="Removes duplicate lines", action="store_true")
parser.add_argument("-a", "--append", help="Appends to the file without overwriting previous content", action="store_true")
parser.add_argument("-s", "--sort", help="Sort the file alphabetically", action="store_true")
parser.add_argument("-r", "--remove-duplicates", help="Remove all duplicates", action="store_true")
args = parser.parse_args()




if __name__ == '__main__':
    ex_content = []
    new_content = []
    
    if args.append:
        try :
            with open(args.output_filename, 'r') as f:
                ex_content = f.readlines()
                ex_content[-1] = ex_content[-1]+'\n' 
        except FileNotFoundError:
            sys.stdout.write(f"{args.output_filename} does not exist. Creating new file.\n")
        f = open(args.output_filename, 'a')
        f.write("\n")

    else:
        f =  open(args.output_filename, 'w')



    for line in sys.stdin:
        if (args.unique and line not in ex_content and line not in new_content) or not args.unique:
            new_content.append(line)
            f.writelines(line)
            sys.stdout.write(line)
    sys.stdout.write("\n")

    
    if args.remove_duplicates:
        with open(args.output_filename, 'w') as f:
            f.writelines(set(ex_content + new_content))

    if args.sort:
        with open(args.output_filename, 'r') as f:
            cont = f.readlines()
        with open(args.output_filename, 'w') as f:
            f.writelines(sorted(cont))
    f.close()
