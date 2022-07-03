import re
import sys
def str_int(onestring):
    num = re.findall('[\d]',onestring)
    c = ''
    d = int(c.join(num))
    return d

if __name__ =="__main__":
    if len(sys.argv) == 1:
        print(str_int('$1,234'))#This is a sample
else:
    print(f'...Importing module {__name__}...')
        

    
    

    
