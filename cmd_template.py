#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import glob
import sys
import json
from pathlib import Path
import textwrap
from glob import glob

# from dotenv import dotenv_values  # pip install python-dotenv
# import yaml # pip install pyyaml

"""



"""

__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)

version_history = \
"""
0.1.0 - initial version  
"""
    


class YourClass:
    
    def __init__(self, **kwargs):
        
        # load self.config
        self.config = {}
        for key, value in kwargs.items():
            self.config[key] = value

        # read in .env file
        if 'env' in self.config:
            self.config.update(dotenv_values(self.config['env']))
        
                    
        pass

    
if __name__ == "__main__":
    
    # provide a description of the program with format control
    description = textwrap.dedent('''\
    Compute idea density of provided text files.
    
 
    ''')
    
    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.RawTextHelpFormatter)

    # handle a single file on command line argument
    parser.add_argument('csvfile',  type=str,  help='csv input file')
    
    # handle multiple files
    parser.add_argument("file_names", nargs='*')  # nargs='*' to combine all positional arguments into a single list

    parser.add_argument("--env", type = str,
                     help="name of env file in the current directory, default .env",
                      default=".env") 

    parser.add_argument("--config", type = str,
                     help="name of yaml config file in the current directory, default config.yaml",
                      default="config.yaml") 
        
    parser.add_argument("--cmd", type = str,
                    help="cmd - [list, summarize], default list",
                    default = 'list')
    
    parser.add_argument("-H", "--history", action="store_true", help="Show program history")
     
    # parser.add_argument("--quiet", help="Don't output results to console, default false",
    #                     default=False, action = "store_true")  
    
    parser.add_argument("--verbose", type=int, help="verbose level default 2",
                         default=2) 
        
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {__version__}')

    parser.add_argument("file_names", nargs='*')  # nargs='*' to combine all positional arguments into a single list
    args = parser.parse_args()

    # Use glob to find files matching wildcards
    file_names = []
        # Use glob to find files matching wildcards
        # If a string does not contain a wildcard, glob will return it as is.
    for arg in args.file_names:
            file_names += glob(arg)
            
    if args.history:
        print(f"{os.path.basename(__file__) } Version: {__version__}")
        print(version_history)
        exit(0)

    obj = YourClass(    file_names =file_names, 

                    )

