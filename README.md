# Scylla - The Simplistic Information Gathering Engine
<p align="center">
  <img src="https://github.com/josh0xA/Scylla/blob/master/imgs/Screen%20Shot%202020-04-27%20at%2012.54.29%20AM.png?raw=true">
</p>

## About Scylla
Scylla is an OSINT tool developed in python 3.6. Scylla lets users perform advanced searches on Instagram & Twitter accounts, websites/webservers, phone numbers, names. Scylla also allows users to find all social media profiles (main platforms) assigned to a certain username. This is the first version of the tool and please contact the developer if you want to help contribute and add more to Scylla.

## Installation
1: ```git clone https://www.github.com/josh0xA/Scylla```<br/>
2: ```cd Scylla```<br/>
3: ```sudo python3 -m pip install -r requirments.txt```<br/>
4: ```python3 scylla.py --help```<br/>

## Usage
1. ```python3 scylla.py --instagram davesmith --twitter davesmith```<br/>
Command 1 will return account information of that specified Instagram & Twitter account.<br/>
2. ```python3 scylla.py --username johndoe```<br/>
Command 2 will return all the social media (main platforms) profiles associated with that username.<br/>
3. ```python3 scylla.py --username johndoe -l="john doe"```<br/>
Command 3 will repeat command 2 but instead it will also perform an in-depth google search for the "-l" argument. NOTE: When searching a query with spaces make sure you add the equal sign followed by the query in quotations. If your query does not have spaces, it will be as such: ```python3 scylla.py --username johndoe -l query```<br/>
4. ```python3 scylla.py --info google.com```<br/>
Command 4 will return crucial WHOIS information about the webserver/website.
5. ```python3 scylla.py -r +14167777777```<br/>
Command 5 will dump information on that phone number (Carrier, Location, etc.)<br/>
6. ```python3 scylla.py -s apache```<br/>
Command 6 will dump all the IP address of apache servers that shodan can grab based on your API key. The query can be anything that shodan can validate.<br/>
A Sample API key is given. I will recommend reading API NOTICE below, for more information.<br/>
7. ```python3 scylla.py -s webcamxp```<br/>
Command 7 will dump all the IP addresses and ports of open webcams on the internet that shodan can grab based on your API key. You can also just use the ``webcam`` query but ``webcamxp`` returns better results.<br/>
A Sample API key is given. I will recommend reading API NOTICE below, for more information.<br/>
8. ```python3 scylla.py -g 1.1.1.1```<br/>
Command 8 will geolocate the specified IP address. It will return the longitude & latitude, city, state/province, country, zip/postal code region and the district.<br/>

## Menu
```
usage: scylla.py [-h] [-v] [-ig INSTAGRAM] [-tw TWITTER] [-u USERNAME]
                 [--info INFO] [-r REVERSE_PHONE_LOOKUP] [-l LOOKUP]
                 [-s SHODAN_QUERY] [-g GEO]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         returns scyla's version
  -ig INSTAGRAM, --instagram INSTAGRAM
                        return the information associated with specified
                        instagram account
  -tw TWITTER, --twitter TWITTER
                        return the information associated with specified
                        twitter account
  -u USERNAME, --username USERNAME
                        find social media profiles (main platforms) associated
                        with given username
  --info INFO           return information about the specified website(WHOIS)
                        w/ geolocation
  -r REVERSE_PHONE_LOOKUP, --reverse_phone_lookup REVERSE_PHONE_LOOKUP
                        return information about the specified phone number
                        (reverse lookup)
  -l LOOKUP, --lookup LOOKUP
                        performs a google search of the 35 top items for the
                        argument given
  -s SHODAN_QUERY, --shodan_query SHODAN_QUERY
                        performs a an in-depth shodan search on any simple
                        query (i.e, 'webcamxp', 'voip', 'printer', 'apache')
  -g GEO, --geo GEO     geolocates a given IP address. provides: longitude,
                        latitude, city, country, zipcode, district, etc.
```
## API NOTICE
The API used for the reverse phone number lookup (free package) has maximum 250 requests. The one used in the program right now will most definetely run out of uses in the near future. If you want to keep generating API keys, go to https://www.numverify.com, and select the free plan after creating an account. Then simply go scylla.py and replace the original API key with your new API key found in your account dashboard. Insert your new key into the keys[] array (at the top of the source). For the Shodan API key, it is just a sample key given to the program. The developer recommends creating a shodan account and adding your own API key to the shodan_api[] array at the top of the source (scylla.py). 

## Discord Server
https://discord.gg/jtZeWek

## Ethical Notice
The developer of this program, Josh Schiavone, written the following code for educational and OSINT purposes only. The information generated is not to be used in a way to harm, stalk or threaten others. Josh Schiavone is not responsible for misuse of this program. May God bless you all.

### License
MIT License<br/>
Copyright (c) 2020 Josh Schiavone
