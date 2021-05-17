# Scylla - The Simplistic Information Gathering Engine
<p align="center">
  <img src="https://github.com/josh0xA/Scylla/blob/master/imgs/Screen%20Shot%202020-05-10%20at%206.43.35%20AM.png?raw=true">
</p>

# Notice For Deprecation
This project is no longer being worked on by the developer. As of today, the program has many flaws and is not up to modern OSINT standards. A lot of APIs utilized within Scylla are no longer working as they did when the project was first released. The developer wrote Scylla out of boredom and as a side project therefore he is no longer working on it. The community is more than welcome to use Scylla's source as a base to improve on it's original capabilities to keep the tool alive. Please do not contact the developer to fix issues as he will not be replying as the project is deprecated. 

## About Scylla
Scylla is an OSINT tool developed in Python 3.6. Scylla lets users perform advanced searches on Instagram & Twitter accounts, websites/webservers, phone numbers, and names. Scylla also allows users to find all social media profiles (main platforms) assigned to a certain username. In continuation, Scylla has shodan support so you can search for devices all over the internet, it also has in-depth geolocation capabilities. Lastly, Scylla has a finance section which allows users to check if a credit/debit card number has been leaked/pasted in a breach and returns information on the cards IIN/BIN. This is the first version of the tool so please contact the developer if you want to help contribute and add more to Scylla.

## Installation
1: ```git clone https://www.github.com/DoubleThreatSecurity/Scylla```<br/>
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
9. ```python3 scylla.py -c 123456789123456```<br/>
Command 9 will retrieve information on the IIN of the credit/debit card number entered. It will also check if the card number has been leaked/pasted in a breach. Scylla will return the card brand, card scheme, card type, currency, country, and information on the bank of that IIN. NOTE: Enter the full card number if you will like to see if it was leaked. If you just want to check data on the first 6-8 digits (a.k.a the BIN/IIN number) just input the first 6,7 or 8 digits of the credit/debit card number. Lastly, all this information generated is public because this is an OSINT tool, and no revealing details can be generated. This prevents malicous use of this option. 

## Menu
```
usage: scylla.py [-h] [-v] [-ig INSTAGRAM] [-tw TWITTER] [-u USERNAME]
                 [--info INFO] [-r REVERSE_PHONE_LOOKUP] [-l LOOKUP]
                 [-s SHODAN_QUERY] [-g GEO] [-c CARD_INFO]

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
  -c CARD_INFO, --card_info CARD_INFO
                        check if the credit/debit card number has been pasted
                        in a breach...dumps sites. Also returns bank
                        information on the IIN
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
