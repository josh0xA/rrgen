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
be used in a way to harm, stalk or threaten others. Josh Schiavone is not responsible
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

try:
    from googlesearch import search 
except ImportError as ie:
    print(str(ie)) 
    sys.exit(1)


__version__ = "1.0"
__author__  = "Josh Schiavone 2020"

scyllaUrls = ["https://www.instagram.com/", "https://www.twitter.com/", "http://api.hackertarget.com/geoip/?q="]

useragent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7']

reqErrorCodes = [404, 400, 401, 320, 500, 501, 502, 503, 504]

keys = ['23f9cdfa535aa12cd21c844d552bfcb0']
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
                            s.print_scylla_valid(line + " ➞ profile FOUND!", color=True)
                        elif req.status_code == cfg.SCL_HTTP_GET_FATAL: 
                            s.print_scylla_invalid(line + " ➞ profile doesn't exist. continuing...", color=True)
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


class SMS(object):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def ReversePhoneNumberLookup(self):
        s = Scylla()
        api_url = 'http://apilayer.net/api/validate?number='+self.phone_number+'&country_code=&format=1&access_key=' + str(keys[0])
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
            cprint('Valid: '+ 'False', 'red', attr=['bold'])

    

'''
class Email(object):
    def __init__(self, address):
        self.address = address
'''
    
class Instagram(object):

    def __init__(self, username):
        self.username = username

    def RetrieveProfileInformation(self):
        web = Web()
        cfg = Config()
        scylla_profile = requests.get(str(scyllaUrls[0]) + str(self.username), headers={'User-Agent': random.choice(useragent)})

        if scylla_profile.status_code == cfg.SCL_HTTP_GET_FATAL:
            print("Instagram Username Is Invalid.")
            sys.exit(1)
        else:
            bsoup = BeautifulSoup(scylla_profile.text, 'html.parser')
            
            scylla_scripts = bsoup.find_all('script', attrs={'type': 'text/javascript'})
            tr=str(scylla_scripts[3])
            tr=tr[51:-10]
            self.t_data = json.loads(tr)
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

        return opt

class Twitter(object):
    def __init__(self, username):
        self.username = username

    def RetrieveAccountInformation(self):
        account_information = []
        dataopt = ""

        try:
            twitter_profile = urlopen(str(scyllaUrls[1]) + str(self.username)).read()
            decode = twitter_profile.decode('UTF-8')

            [account_information.append(value) for value in findall('data-is-compact="false">(.*?)<', decode)]

            picture_url = findall(b'href="https://pbs.twimg.com/profile_images(.*?)"', twitter_profile)[0].decode('utf-8')
            account_date = findall(b'<span class="ProfileHeaderCard-joinDateText js-tooltip u-dir" dir="ltr" title="(.*?)"', twitter_profile)[0].decode('utf-8')

            dataopt = '''
        > Name      :: {}
        > Tweets    :: {}
        > Likes     :: {}
        > Following :: {}
        > Followers :: {}
        > Account Created :: {}
        > Link To Profile Picture :: {}

            '''.format(str(findall(b'<title>(.*?) \(', twitter_profile)[0].decode('utf-8')), 
            account_information[0], account_information[3], account_information[1], account_information[2],
            account_date, picture_url)

        except Exception as ex:
            cprint("\tCannot Scrape Twitter Profile at This Time.", 'red', attrs=['bold'])
            pass
        return dataopt
        

def main():
    p = Platform()
    p.ScyllaClear()
    p.GetOperatingSystemDescriptor()

    LoadScyllaBanner()
    s = Scylla()
    w = Web()

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


    
if __name__ == "__main__":
    main() 



