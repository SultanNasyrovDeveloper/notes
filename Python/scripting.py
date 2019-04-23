Python shell scripting
---------------------------------
common kinds of OS-level resource manipulations in it:

    Reading configuration files
    Killing (and creating) processes
    Doing date arithmetic
    Creating (and deleting) directories
    Running applications
    Managing files

There are also some higher-level considerations than managing OS resources. These considerations include conditional processing and iterating over objects. I’ll show an example of iterating over files, but scripts also iterate over processes or even lines in a file.

There are parameters you need to pass to the script depending how they are developed and they can either be:

    Arguments: This is a required parameter that’s passed to the script. If you don’t provide it, the CLI will run into an error. For instance, django is the argument in this command: pip install django.

    Options: As the name implies, its is an optional parameter which usually comes in a name and a value pair such as pip install django --cache-dir ./my-cache-dir. The --cache-dir is an option param and the value ./my-cache-dir should be uses as the cache directory.

    Flags: This is special option parameter that tells the script to enable or disable a certain behaviour. The most common one is probably --help.

-----------
CLint
-----------
from clint.argument import Args
from clint.textui import puts, indent, prompt, validators, colored

project structure
clint
---> packages
---> textui
	---> colored  
		- black, green, yellow, blue, magenta, cyan, white
	---> cols  # column formatting
		- console_width()
		- columns()
	---> core
		- puts()  # text output function
		- puts_err()
		- indent()  # 
		- dedent()
		
	---> formatters
	---> progress  # creating and managing progress bar tools
		- Bar()
	---> promt
	---> validators  # input validation
		regex, path, file, integer
- arguements # parse given arguements

Examples:

parsing arguements

#!/usr/bin/env python
# -*- coding: utf

from clint.arguements import Args

args = A
arg = args.get(1)

str(args.all)
str(args.flags)
str(args.files)
str(args.not_files)
str(args.grouped)
---------------------------------------------------------
from clint.textui import prompt, validators

path = prompt.query('Installation Path', default='/usr/local/bin/', validators=[validators.PathValidator()])
-----------------------------------------------------------
input with options:

inst_options = [{'selector': '1', 'prompt': 'Full', 'return': 'full'},
                        {'selector': '2', 'prompt': 'Partial', 'return': 'partial'},
