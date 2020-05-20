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

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
BOLD = '\033[1m'
END = '\033[0m'

def LoadScyllaBanner():
    print(W + BOLD + "\n    --------------+--------------      ")
    print(G + "            ___ /^^[___              _ ")
    print(G + "           /|^+----+   |#___________// ")
    print(G + "         ( -+ |____|    ______-----+/  ")
    print(G + "          ==_________--'            \  ")
    print(G + "            ~_|___|__                  \n" + END)
    print(B + BOLD + "_____________________________________" + END)
    print(R + BOLD + "               [Scylla]                  " + END)        
    print(W + "-==[ " + BOLD + "The Information Gathering Engine" + END)
    print(W + "-==[ " + BOLD + "Developed By: Josh Schiavone    " + END)                                                                                                                                                             
    print(B + BOLD + "_____________________________________\n" + END)                                                                                                                                                             

    bannerB = colored(r"""
                 ./~
        (=@@@@@@@=[}=================--
                 `\_ ... I <3 Scylla
    """, 'cyan', attrs=['bold'])   

def ScyllaBreaker():
  breaker = colored('''
  ====================================================================================
  ''', 'grey', attrs=['bold'])
  print(breaker)
