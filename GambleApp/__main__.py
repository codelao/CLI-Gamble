#	 .=============-\  .=============-\ 
#	 |             ||  |             || 
#	 |  ●          ||  |   ●     ●   || 
#	 |             ||  |             || 
#	 |      ●      ||  |   ●     ●   || 
#	 |             ||  |             || 
#	 |          ●  ||  |   ●     ●   || 
#	 |_____________#/  |_____________#/ 
#	       CLI              GAMBLE      
#	~[$$$__________by Lao__________$$$]~

#!/usr/bin/env python3

import sys
from .gamble import main
from .deposit import setDeposit

def check_int(s: str) -> bool:
    return s.isdigit() or (s.startswith("-") and s[1:].isdigit())

def entry_point():
	if len(sys.argv)>1:
		if sys.argv[1] in ["--dep","-x","-e","-m","-h"]:	
			if "--dep" in sys.argv:
				deposit_pos = sys.argv.index("--dep")+1
				deposit = int(sys.argv[deposit_pos])
				try:
					setDeposit(deposit)
					print("New deposit:",deposit,
						"\nYou can continue playing now.")
				except:
					print("Something went wrong.",
						"\nMake sure that the amount you enter is an integer.")
					sys.exit(1)
			if "-x" in sys.argv:
				multiplier_pos = sys.argv.index("-x")+1
		else:
			print("Unknown argument(s).")
			sys.exit(1)
	else:
		sys.exit(0 if main() else 1)


if __name__ == '__main__':
	entry_point()
