# Scylla - The Simplistic Information Gathering Engine
<p align="center">
  <img src="https://github.com/josh0xA/Scylla/blob/master/imgs/Screen%20Shot%202020-04-27%20at%2012.54.29%20AM.png?raw=true">
</p>

## About Scylla
Scylla is an OSINT tool developed in python 3.6. Scylla lets users perform advanced searches on Instagram & Twitter accounts, websites/webservers, phone numbers, names. Scylla also allows users to find all social media profiles (main platforms) assigned to a certain username. This is the first version of the tool and please contact the developer if you want to help contribute and add more to Scylla.

## Installation
1: ```git clone https://www.github.com/josh0xA/Scylla```<br/>
2: ```cd Scylla```<br/>
3: ```sudo python3 setup.py install```<br/>
4: ```python3 scylla.py --help```<br/>

## Usage
1. ```python3 scylla.py --instagram davesmith --twitter davesmith```<br/>
Command 1 will return account information of that specified Instagram & Twitter account.<br/>
2. ```python3 scylla.py --username johndoe```<br/>
Command 2 will return all the social media (main platforms) profiles associated with that username.<br/>
3. ```python3 scylla.py --username johndoe -l="john doe"```
Command 3 will repeat command 2 but instead it will also perform an in-depth google search for the "-l" argument. NOTE: When searching a query with spaces make sure you add the equal sign followed by the query in quotations. If your query does not have spaces, it will be as such: ```python3 scylla.py --username johndoe -l query```<br/>


