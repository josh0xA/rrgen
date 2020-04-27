'''
Copyright (C) 2020 Josh Schiavone - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license, which unfortunately won't be
written for another century.

You should have received a copy of the MIT license with
this file. If not, visit : https://opensource.org/licenses/MIT

'''
import random
from termcolor import colored, cprint

def LoadScyllaBanner():
    bannerA = colored('''

███████  ██████ ██    ██ ██      ██       █████  
██      ██       ██  ██  ██      ██      ██   ██ 
███████ ██        ████   ██      ██      ███████ 
     ██ ██         ██    ██      ██      ██   ██ 
███████  ██████    ██    ███████ ███████ ██   ██ 
   ''', 'red')
    subBanner = colored('''
        The Information Gathering Engine
          Developed By: Josh Schiavone
           https://github.com/josh0xA                                                                                                                                                          
    
    ''', 'green', attrs=['bold'])
    print(bannerA + subBanner)

def ScyllaBreaker():
  breaker = colored('''
  ====================================================================================
  ''', 'grey', attrs=['bold'])
  print(breaker)