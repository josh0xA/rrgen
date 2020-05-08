'''
Copyright (C) 2020 Josh Schiavone - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license, which unfortunately won't be
written for another century.
You should have received a copy of the MIT license with
this file. If not, visit : https://opensource.org/licenses/MIT
'''

'''
Scylla - The Information Gathering Engine
    Developed By: Josh Schiavone
    https://www.profify.ca/josh
'''

'''
                                    NOTICE
The developer of this program, Josh Schiavone, written the following code
for educational and OSINT purposes only. The information generated is not to
be used in a way to harm, stalk or threaten others. The developer, is not responsible
for misuse of this program. May God bless you all.
'''


import os
import sys
import time
import requests
import argparse

from bs4 import BeautifulSoup

import random
import string
from external.ext import *

from re import findall
from urllib.request import urlopen

import json
import pythonwhois

from contextlib import suppress
import socket

import shodan

try:
    from googlesearch import search
except ImportError as ie:
    cprint(str(ie), 'red', attrs=['bold'])
    sys.exit(1)


__version__ = "1.1"
__author__  = "Josh Schiavone 2020"

scyllaUrls = ["https://www.instagram.com/", "https://www.twitter.com/", "http://api.hackertarget.com/geoip/?q="]
reqErrorCodes = [404, 400, 401, 320, 500, 501, 502, 503, 504]

'''
API Key Storage. Users can modify the these arrays in the source to fit there needs
and add their own API keys. 
'''
sms_api = ['23f9cdfa535aa12cd21c844d552bfcb0']
shodan_api = ['ouLQS2Obofjsb8eda7Fchq50AyNTCRPw']

useragent = [
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
    'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
    'Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; ja) Opera 11.00',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.56 Safari/1EA69',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
    'Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 1660.57.0) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.46 Safari/535.19',
    'Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
    'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)',
    'Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)',
    'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51',
    'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 5.1; U; MRA 5.5 (build 02842); ru) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
    'Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)',
    'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    'Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11',
    'Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10',
    'Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01',
    'Mozilla/4.0 (compatible; MSIE 8.0; X11; Linux x86_64; pl) Opera 11.00',
    'Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50',
    'Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.11 Safari/535.19',
    'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; fr) Opera 11.00',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    'Opera/9.80 (Windows NT 5.1; U; it) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
    'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; pl) Opera 11.00',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
    'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
    'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1',
    'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00',
    'Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; en) Opera 11.00',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
    'Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7',
    'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    'Mozilla/5.0 (Windows NT 6.0; U; ja; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)',
    'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/19.0.1047.0 Safari/535.22',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
    'Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11',
    'Mozilla/5.0 (Macintosh; AMD Mac OS X 10_8_2) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/18.6.872',
    'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221',
    'Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)',
    'Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1042.0 Safari/535.21',
    'Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19',
    'Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
    'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)',
    'Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
    'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00',
    'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
    'Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
    'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10',
    'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00',
    'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari',
    'Mozilla/5.0 (Windows NT 5.1; U; pl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11',
    'Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19',
    'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    'Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.142 Chrome/18.0.1025.142 Safari/535.19',
    'Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00'
    ]

class Config:
    # Program Handlers
    SCL_ERROR_CODE_STANDARD = -1
    SCL_SUCCESS_CODE_STANDARD = 0
    SCL_SCYLLA_PROCESS_ACTIVE = False

    # OS Handlers
    SCL_OSYSTEM_UNIX_LINUX = False
    SCL_OSYSTEM_DARWIN = False
    SCL_OSYSTEM_WIN32_64 = False

    # Status Codes
    SCL_HTTP_GET_SUCCESS = 200
    SCL_HTTP_GET_FATAL = 404

class Scylla(object):
    def print_scylla_message(self, msg, color=True):
        icon = '[*] '
        if color:
            cprint('\t' + icon + msg, 'blue', attrs=['bold'])
        else: print('\t' + icon + msg)

    def print_scylla_notab(self, msg, color=True):
        icon = '[*] '
        if color:
            cprint(icon + msg, 'blue', attrs=['bold'])
        else: print(icon + msg)

    def print_scylla_error(self, errortype, errormsg, color=True):
        if color:
            cprint(f"\t[-] {errortype}: {errormsg} ", 'red', attrs=['bold'])
        else:
            print(f"\t[-] {errortype}: {errormsg} ")

    def print_scylla_valid(self, msg, color=True):
        if color:
            cprint(f"\t[+] {msg}", 'green', attrs=['bold'])
        else:
            print(f"\t[+] {msg}")

    def print_scylla_invalid(self, msg, color=True):
        if color:
            cprint(f"\t[!] {msg}", 'grey', attrs=['bold'])
        else:
            print(f"\t[!] {msg}")

class Platform(object):
    def GetOperatingSystemDescriptor(self):
        s = Scylla()
        cfg = Config()
        if sys.platform == "win32" or sys.platform == "win64":
            cfg.SCL_OSYSTEM_WIN32_64 = True
            s.print_scylla_notab("OS: Windows", color=True)

        if sys.platform == "darwin":
            cfg.SCL_OSYSTEM_DARWIN = True
            s.print_scylla_notab("OS: OSX/Darwin", color=True)

        if sys.platform == "linux" or sys.platform == "linux2":
            cfg.SCL_OSYSTEM_UNIX_LINUX = True
            s.print_scylla_notab("OS: Unix/Linux", color=True)

    def ScyllaClear(self):
        time.sleep(0.7)
        if sys.platform == "win32" or sys.platform == "win64":
            os.system("cls")

        if sys.platform == "darwin" or sys.platform == "linux" or sys.platform == "linux2":
            os.system("clear")

class Web(object):

    def shorten_url(self, url):
        apiurl = "http://tinyurl.com/api-create.php?url="
        tinyurl = urlopen(apiurl + url).read()
        return tinyurl.decode("utf-8")

    def dump_user_data(self, username):
        s = Scylla()
        cfg = Config()
        with open('sites.txt', 'r') as istr:
            with open('sites_opt.txt', 'w') as ostr:
                try:
                    s.print_scylla_message("Searching Known Social Networks For: " + username, color=True)
                    for i, line in enumerate(istr):
                        # Get rid of the trailing newline (if any).
                        line = line.rstrip('\n') + str(username)
                        req = requests.get(line, headers={'User-Agent': random.choice(useragent)})
                        if req.status_code == cfg.SCL_HTTP_GET_SUCCESS:
                            s.print_scylla_valid(line + " => profile FOUND!", color=True)
                        elif req.status_code == cfg.SCL_HTTP_GET_FATAL:
                            s.print_scylla_invalid(line + " => profile doesn't exist. continuing...", color=True)
                            continue
                except Exception as ex:
                    pass

    def scylla_return_ip_address(self, target):
        s = Scylla()
        try:
            address = socket.gethostbyname(target)
        except socket.gaierror as sock_error:
            s.print_scylla_error("ScyllaError: ", str(sock_error), color=True)

        return address

    def scylla_geolocate_ip_address(self, ip_addr):
        s = Scylla()

        reverse_socket_dns = socket.getfqdn(ip_addr)
        geoip = requests.get(scyllaUrls[2] + str(ip_addr), headers={'User-Agent': random.choice(useragent)})
        bsoup = BeautifulSoup(geoip.text, 'html.parser')
        s.print_scylla_valid(str(bsoup), color=True)

    def scylla_whois(self, domain):
        w = Web()
        s = Scylla()
        ip_address = w.scylla_return_ip_address(domain)
        try:
            data = pythonwhois.get_whois(domain, normalized=True)
        except pythonwhois.shared.WhoisException:
            return "Invalid input."
        info = []
        s.print_scylla_message("Retrieving WHOIS Data From Server...", color=True)
        w.scylla_geolocate_ip_address(ip_address)

        with suppress(KeyError):
            info.append("Server: {}".format(data["emails"][0]))

        with suppress(KeyError):
            info.append("Registrar: {}".format(data["registrar"][0]))

        with suppress(KeyError):
            info.append("Registered: {}".format(data["creation_date"][0].strftime("%d-%m-%Y")))

        with suppress(KeyError):
            info.append("Expires: {}".format(data["expiration_date"][0].strftime("%d-%m-%Y")))

        with suppress(KeyError):
            info.append("Emails (if showable): {}".format(data["emails"][0]))

        with suppress(KeyError):
            info.append("Address: {}".format(data["address"][0]))

        with suppress(KeyError):
            info.append("City: {}".format(data["city"][0]))

        with suppress(KeyError):
            info.append("State: {}".format(data["state"][0]))

        with suppress(KeyError):
            info.append("Zipcode: {}".format(data["zipcode"][0]))

        with suppress(KeyError):
            info.append("Country: {}".format(data["country"][0]))

        info_text = ", ".join(info)
        return "{} - {}".format(domain, info_text)

    def search_google(self, query):
        s = Scylla()
        for j in search(query, tld="co.in", num=35, stop=35, pause=2):
            s.print_scylla_valid(j, color=True)

class Shodan(object):
   
    def shodan_lookup(self, query):
        s = Scylla()
        api = shodan.Shodan(str(shodan_api[0]))
        try:
            results = api.search(query)
            total_results = int(results['total'])

            s.print_scylla_message("Results Found: " + str(total_results), True)
            
            for result in results['matches']:
                s.print_scylla_valid("IP Address-> %s" % result['ip_str'], True)
                s.print_scylla_valid(result['data'], True)
        except shodan.APIError as se:
            s.print_scylla_error("ScyllaError", str(se), True)

        
class SMS(object):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def ReversePhoneNumberLookup(self):
        s = Scylla()
        api_url = 'http://apilayer.net/api/validate?number='+self.phone_number+'&country_code=&format=1&access_key=' + str(sms_api[0])
        api_request = requests.get(api_url)
        try:
            response = api_request.content.decode('UTF-8')
        except Exception as ex:
            s.print_scylla_error("ScyllaError: ", str(ex), color=True)
            pass

        responseObject = json.loads(response)
        if 'error' in responseObject:
            s.print_scylla_error("ScyllaError: ", 'error', color=True)

        elif 'True' in str(responseObject['valid']):
            s.print_scylla_valid('Valid: ' + 'True\n', color=True)
            array = ['local_format', 'international_format', 'country_name', 'location', 'carrier', 'line_type']
            for i in array:
                if i in responseObject:
                    s.print_scylla_message(i.replace('_', ' ').title() + ': ' + str(responseObject[i]).replace('_', ' ').title(), color=True)
        elif 'False' in str(responseObject['valid']):
            s.print_scylla_error('Valid', 'False', True)


# TODO: Add an email class

class Instagram(object):

    def __init__(self, username):
        self.username = username

    def RetrieveProfileInformation(self):
        web = Web()
        cfg = Config()
        scylla_profile = requests.get(str(scyllaUrls[0]) + str(self.username), headers={'User-Agent': random.choice(useragent)})

        if scylla_profile.status_code == cfg.SCL_HTTP_GET_SUCCESS:
            bsoup = BeautifulSoup(scylla_profile.text, 'html.parser')

            scylla_scripts = bsoup.find_all('script', attrs={'type': 'text/javascript'})
            scylla_strip_js = str(scylla_scripts[3])

            scylla_strip_js = scylla_strip_js[51:-10]
            self.t_data = json.loads(scylla_strip_js)
            self.bsoup_data = self.t_data['entry_data']['ProfilePage'][0]['graphql']['user']
            opt = '''
         > Username                :: {}
         > Name                    :: {}
         > Url                     :: {}
         > Followers               :: {}
         > Following               :: {}
         > # of posts              :: {}
         > Biography               :: {}
         > External url            :: {}
         > Private                 :: {}
         > Verified                :: {}
         > Business account        :: {}
         > Connected To Facebook   :: {}
         > Joined recently         :: {}
         > Business category       :: {}
         > Profile Picture         :: {}
             '''.format(str(self.bsoup_data['username']), str(self.bsoup_data['full_name']),
             str("instagram.com/%s" % self.username), str(self.bsoup_data['edge_followed_by']['count']),
             str(self.bsoup_data['edge_follow']['count']), str(self.bsoup_data['edge_owner_to_timeline_media']['count']),
             str(self.bsoup_data['biography']), str(self.bsoup_data['external_url']),
             str(self.bsoup_data['is_private']), str(self.bsoup_data['is_verified']), str(self.bsoup_data['is_business_account']),
             str(self.bsoup_data['connected_fb_page']), str(self.bsoup_data['is_joined_recently']),
             str(self.bsoup_data['business_category_name']), web.shorten_url(str(self.bsoup_data['profile_pic_url_hd'])))

        elif scylla_profile.status_code in reqErrorCodes:
            print("Instagram Username Is Invalid.")
            sys.exit(1)

        return opt

class Twitter(object):
    def __init__(self, username):
        self.username = username
 
    def RetrieveAccountInformation(self):
        web = Web()
        s = Scylla()
        account_information = []
        dataopt = ""

        url = str(scyllaUrls[1]) + self.username
        s.print_scylla_message("Gathers Details of " + self.username + " from Twitter", True)
        response = None
        try:
            response = requests.get(url)
        except Exception as e:
            print(repr(e))
            sys.exit(1)
   
        if response.status_code != 200:
            s.print_scylla_error("ScyllaError", "Invalid Username: " + str(response.status_code), True)
            sys.exit(1)
 
        soup = BeautifulSoup(response.text, 'lxml')
 
        '''
        if soup.find("div", {"class": "errorpage-topbar"}):
            s.print_scylla_error("ScyllaError", "Invalid username.")
            sys.exit(1)
        '''

        try:
            twname = soup.title.text.split("|")[0]
            twbio = soup.find("p", {"class": "ProfileHeaderCard-bio u-dir"}).text
        except AttributeError as y: pass
        try:
            join_date = soup.find("span", {"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"})
            twjoin = join_date['title']
        except AttributeError as y: pass
        try:
            followers = soup.find("li", {"class": "ProfileNav-item ProfileNav-item--followers"}).find('a')
            twfollowers = followers['title']
        except AttributeError as y: pass
        try:
            followers = soup.find("li", {"class": "ProfileNav-item ProfileNav-item--following"}).find('a')
            twfollowing = followers['title']
        except AttributeError as y: pass
        try:
            pictureURL = soup.find("a",{"class": "ProfileAvatar-container u-block js-tooltip profile-picture"})
            twdp = pictureURL['data-url']
        except AttributeError as y: pass
        try:
            filename = self.username+"_twitter.json"
            s.print_scylla_valid("Dumping data in file " + filename, True)
        except AttributeError as y: pass

        data = dict()
        data["Bio: "] = twbio
        data["Join date: "] = twjoin
        data["Followers: "] = twfollowers
        data["Following: "] = twfollowing
        data["Profile URL: "] = web.shorten_url(twdp)
 
        dataopt = '''
       > Name          :: {}
       > Bio           :: {}
       > Join date     :: {}
       > Followers     :: {}
       > Following     :: {}
       > Profile URL   :: {}
           '''.format(str(twname), str(data['Bio: ']),
            str(data['Join date: ']), str(data['Followers: ']),
            str(data['Following: ']), str(data['Profile URL: ']))
 
        with open(filename, 'w') as fh:
            fh.write(json.dumps(data))
 
        return dataopt


def main():
    p = Platform()
    p.ScyllaClear()
    p.GetOperatingSystemDescriptor()

    LoadScyllaBanner()
    s = Scylla()
    w = Web()
    sh = Shodan()

    parser = argparse.ArgumentParser()
    parser.add_argument("-v",
                        "--version",
                        help="returns skyla's version",
                        action="store_true")
    parser.add_argument("-ig",
                        "--instagram",
                        type=str,
                        help="return the information associated with specified instagram account",
                        )

    parser.add_argument("-tw",
                        "--twitter",
                        type=str,
                        help="return the information associated with specified twitter account",
                        )

    parser.add_argument("-u",
                        "--username",
                        type=str,
                        help="find social media profiles (main platforms) associated with given username",
                        )
    parser.add_argument("--info",
                        type=str,
                        help="return information about the specified website(WHOIS) w/ geolocation",
                        )
    parser.add_argument("-r",
                        "--reverse_phone_lookup",
                        type=str,
                        help="return information about the specified phone number (reverse lookup) ",
                        )
    parser.add_argument("-l",
                    "--lookup",
                    type=str,
                    help="performs a google search of the 35 top items for the argument given",
                    )
    parser.add_argument("-s",
                    "--shodan_query",
                    type=str,
                    help="performs a an in-depth shodan search on any simple query (i.e, 'webcamxp', 'voip', 'printer', 'apache')",
                    )                   
    args = parser.parse_args()

    if args.version:
        print("\t\tVersion: {}".format(__version__))

    if args.instagram:
        ScyllaBreaker()
        s.print_scylla_message("Attempting To Gather Account Information", color=True)
        time.sleep(1)
        try:
            cprint(Instagram(args.instagram).RetrieveProfileInformation(), 'yellow', attrs=['bold'])
        except KeyboardInterrupt as ki:
            cprint("\tExiting Scylla...", 'red', attrs=['bold'])
            sys.exit(1)
    if args.twitter:
        ScyllaBreaker()
        s.print_scylla_message("Attempting To Gather Account Information", color=True)
        time.sleep(1)
        try:
            cprint(Twitter(args.twitter).RetrieveAccountInformation(), 'green', attrs=['bold'])
        except KeyboardInterrupt as ki:
            cprint("\tExiting Scylla...", 'red', attrs=['bold'])
            sys.exit(1)

    if args.username:
        ScyllaBreaker()
        try:
            w.dump_user_data(args.username)
        except KeyboardInterrupt as ki:
            cprint("\tExiting Scylla...", 'red', attrs=['bold'])
            sys.exit(1)
    if args.info:
        ScyllaBreaker()
        try:
            s.print_scylla_valid(w.scylla_whois(args.info), color=True)
        except KeyboardInterrupt as ki:
            cprint("\tExiting Scylla...", 'red', attrs=['bold'])
            sys.exit(1)
    if args.reverse_phone_lookup:
        ScyllaBreaker()
        s.print_scylla_message("Fetching Phone Number Information", color=True)
        time.sleep(0.7)
        try:
            sms = SMS(args.reverse_phone_lookup)

            sms.ReversePhoneNumberLookup()
        except KeyboardInterrupt as ki:
            cprint("\tExiting Scylla...", 'red', attrs=['bold'])
            sys.exit(1)

    if args.lookup:
        ScyllaBreaker()
        s.print_scylla_message("Searching Possible Results For: " + args.lookup, color=True)
        try:
            w.search_google(args.lookup)
        except KeyboardInterrupt as ki:
            cprint("\tExiting Scylla...", 'red', attrs=['bold'])
            sys.exit(1)

    if args.shodan_query:
        ScyllaBreaker()
        s.print_scylla_message("Searching ShodanAPI For: " + args.shodan_query, color=True)
        try:
            sh.shodan_lookup(args.shodan_query)
        except KeyboardInterrupt as ki:
            cprint("\tExiting Scylla...", 'red', attrs=['bold'])
            sys.exit(1)        



if __name__ == "__main__":
    main()