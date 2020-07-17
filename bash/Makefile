# Makefiles provide locally accessible bash commands
# Can be a pain to read
# Not great support on Windows
# Good for making project installation easy (often just 'make install')
# TABS must be used NOT spaces
# wrap lines with \
# Much more functionality is excluded, often used to do conditional compilation of C files

# Define default shell (will use bash by default):
SHELL=/bin/bash

# Define files/dirs with which commands should run EVEN IF they already exist:
# Inbuilt assumption that if a file/folder referred to exists then the command will not execute
# Instead it will say "..." is up to date.
.PHONY: docs

#Define Variables:
named_variable = "This is the text here"
dependencies = test.py
listy = file1 file2 file3

# Define commands:
help:                       # Handy to explain Makefile content and uses (not required)
    @echo "-install     : installs shizzle"
    @echo "-test"       : test shizzle"

use_variable:
    echo $(named_variable)

test: $(dependencies)       # REQUIREMENTS (files/folders and other functions can be placed here)
    pytest test.py
    touch some_file         # This will only run once as once some_file is created Makefile won't let this run again
                            # unless some_file is listed in .PHONY

clean: test                 # This depends on 'test' having run first
    rm -rd __pycache__ .pytest_cache

check:
    test clean              # Can use previously defined commands

docs:
    pdoc --html --force --output-dir docs common