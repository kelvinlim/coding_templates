#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import glob
import sys
import json
from pathlib import Path
import textwrap

from dotenv import dotenv_values  # pip install python-dotenv
import yaml # pip install pyyaml

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
        self.config.update(dotenv_values(self.config['env']))
        
        if 'config' in self.config:
            # Open and read the YAML file
            with open(self.config['config'], 'r') as file:
                data = yaml.safe_load(file)
                self.config.update(data)
                    
        pass

    
if __name__ == "__main__":
    
    # provide a description of the program with format control
    description = textwrap.dedent('''\
    A description of the program goes here.
    
    Account information is read from a .env file which contains the 
    APITOKEN, DATACENTER and DIRECTORYID.
    
    Here are some examples of using the command. Text following the $ is
    the command that is entered at the command line in a terminal window.
    
    $ LNPIQualtrics
    Without any arguments, the mailingLists are listed with their index. 
    ''')
    
    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--env", type = str,
                     help="name of env file in the current directory, default .env",
                      default=".env") 

    parser.add_argument("--config", type = str,
                     help="name of yaml config file in the current directory, default config.yaml",
                      default="config.yaml") 
        
    parser.add_argument("--cmd", type = str,
                    help="cmd - [list, summarize], default list",
                    default = 'list')

    parser.add_argument("--format", type = str,
                    help="format to use, default json",
                    default = 'json')
    
    parser.add_argument("-H", "--history", action="store_true", help="Show program history")
     
    # parser.add_argument("--quiet", help="Don't output results to console, default false",
    #                     default=False, action = "store_true")  
    
    parser.add_argument("--verbose", type=int, help="verbose level default 2",
                         default=2) 
        
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()

    if args.history:
        print(f"{os.path.basename(__file__) } Version: {__version__}")
        print(version_history)
        exit(0)

    obj = YourClass(    cmd=args.cmd, 
                        env=args.env, 
                        verbose=args.verbose, 
                        config=args.config,
                        format=args.format,
                    )

