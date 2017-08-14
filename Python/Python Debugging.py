Python Debugging
#############################################
Author = "Gilad Amar"                       #
Email = "giladamar@gmail.com"               #
#############################################

''' A safety pig has been provided for your benefit:
 _._ _..._ .-',     _.._(`))
'-. `     '  /-._.-'    ',/
   )         \            '.
  / _    _    |             \
 |  a    a    /              |
 \   .-.                     ;  
  '-('' ).-'       ,'       ;
     '-;           |      .'
        \           \    /
        | 7  .__  _.-\   \
        | |  |  ``/  /`  /
       /,_|  |   /,_/   /
          /,_/      '`-'
'''
##### LAUNCH IPDB #####

	1) 	import ipdb; ipdb.set_trace(context=3) 
			Shows default 3 lines of code

	2)	from ipdb import launch_ipdb_on_exception
			with launch_ipdb_on_exception():
				<Try stuff here>

	3)	ipdb.pm()
			Launch ipdb after exception occured


##### HELP #####
	? - help

##### CONTEXT #####
	l [first, last] - List source code surrounding present location, 11 lies unless range specified
	w - Print stack trace with most recent frame at the bottom

##### NAVIGATION #####
	s - Step into (stop at first possible location)
	n - Step over to next line
	c - Continue to next breakpoint
	unt <line_no> - Continue until line <line_no>
	r - Continue function till return 

	d - Go down level in stack trace (i.e up to whatever called this function.)
	u - Go up level in stack trace (i.e. into called function.)

##### BREAKPOINTS #####
	b(reak) [ ([filename:]lineno | function) [, condition] ] - Create breakpoint at location
		Lists all breakpoints if no arguments are given
	tbreak  [ ([filename:]lineno | function) [, condition] ] - Create temporary breakpoint 
		Automatically removed after first being hit
	cl 1 3 4 - Remove breakpoints 1 3 and 5
	disable 1 3 4 - Disable breakpoints
	enable 1 3 4 - Deenable breakpoints

	ignore [bpnumber] [count] - Ignore breakpoint for <count> more times. Afterward it is enabled.
	condition [bpnumber] condition

##### SHOW #####
	a - print the current function arguments
	pp <var> - prettyprint variable
		* Helpful with pp locals() and pp globals()
	pinfo <var> - show var info.
	pinfo2 <var> - show extra var info.
	interact - starts an ipython like terminal
			   Exit with cntl + D 
	display <expression> - display value of expression if changed


q - quit debugging