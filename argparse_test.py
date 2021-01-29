import argparse


parser = argparse.ArgumentParser(description = 'input a digiter')
parser.add_argument('--name',type = str,default = '網頁',help = 'enter a name')
parser.add_argument('--num',type=str,default='535266',required=True,help = 'please input a digiter')
args = parser.parse_args()

print(args.name+args.num)








'''
	paramers:
	    1. type = str 
		input is a string type(int)
	    2. nargs = '+'
		you can input a continous num or letter
	    3. default = 'ww'
		dafault value, if you enter nothing ,output the default
	    4.required = True
		what you must enter paramer,whatever you have a default or not


'''
