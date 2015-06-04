#!/usr/bin/env python 

# Jacky Liang 2015

## OS and Python Version
# Python 2.7.9
# Debian 8.0 (jessie)

## Libraries:
# Uses the requests, lxml, and fake_useragent Python libraries
# pip install [library name]

import requests,json,os.path,sys
from lxml import html
from fake_useragent import UserAgent

info_db = './info.json'

# Parse info.json which contains our three input params
if os.path.exists(info_db):
    with open(info_db) as data_file:
        info = json.load(data_file)
else:
    print "Error - please create a info.json file!"
    sys.exit(0)

# Grab username, password, and term_in from info.json
username = info['username']
password = info['password']
term_in = info['term_in']

login_url="https://login.drexel.edu/cas/login?service=https%3A%2F%2Fone.drexel.edu%2Fc%2Fportal%2Flogin"

# Fake random user agent generator
ua = UserAgent()

# Persist a session
with requests.Session() as s:
    
    # Call this URL to get our initial hidden parameter variables
    # In particular, the `lt` variable changes every time [I'm not
    # sure how often, but it's necessary every time you login]
    page = s.get('https://one.drexel.edu/web/university')    

    # Convert page to string for easy scraping
    tree = html.fromstring(page.text)

    # Grab our unique variables from these particular XPaths
    # Yes, the XPaths are a MESS, but that's because Drexel's websites
    # are a mess. 
    lt = tree.xpath('//*[@id="fm1"]/div[4]/input[1]/@value')
    execution = tree.xpath('//*[@id="fm1"]/div[4]/input[2]/@value')
    eventId = tree.xpath('//*[@id="fm1"]/div[4]/input[3]/@value')
    submit = tree.xpath('//*[@id="fm1"]/div[4]/input[4]/@value')

    # Login page POST parameters
    l_payload = { 
        'username':username, 
        'password':password,
        'lt':lt,
        'execution':execution,
        '_eventId':eventId,
        'submit':submit
    }
   
    # Login page cookies 
    l_cookies = {
        'JSESSIONID':page.cookies['JSESSIONID'],
        'IDMSESSID':username
    }

    # Login page headers with a fake user-agent generator 
    l_headers = { 
        "Referer":"https://login.drexel.edu/cas/login?service=https%3A%2F%2Fone.drexel.edu%2Fc%2Fportal%2Flogin",
        "User-Agent":ua.random
    }   
    
    # Now we login to Drexel Connect, Drexel's single-sign-o
    # for all its web apps like Drexel Learn, Drexel One, etc
    # For more info in this: 
    # https://www.drexel.edu/irt/help/a-z/drexelConnect/
    s.post(
        login_url, 
        data = l_payload, 
        cookies = l_cookies, 
        headers = l_headers,
        allow_redirects = True
    )
    
    # Go to the "Add/Drop Class" link within Drexel One
    # to grab the SESSID cookie which will allow us to 
    # add and/or drop classes
    term = s.get('https://bannersso.drexel.edu/ssomanager/c/SSB?pkg=bwszkfrag.P_DisplayFinResponsibility%3Fi_url%3Dbwskfreg.P_AltPin')
    
    # Grab the Add/Drop Class page cookies
    vad_cookie = {
        'SESSID':term.cookies['SESSID'],
        'IDMSESSID':username
    }

    # Specify the term in which you want to add classes
    vad_payload = {
        'term_in':term_in
    }

    # The final add/drop class URL to POST to. This is where
    # we specify the term in which we want to add/drop classes 
    vad_url = "https://banner.drexel.edu/pls/duprod/bwskfreg.P_AltPin"

    # POST the data
    view = s.post(
        vad_url, 
        cookies = vad_cookie, 
        data = vad_payload
    )

    ad_url = "https://banner.drexel.edu/pls/duprod/bwckcoms.P_Regs"

    # print view.cookies['SESSID']

    foo = s.post(ad_url, cookies = {'SESSID':view.cookies['SESSID']}) 
    
    print foo.text

    # Grab the Add/Drop Class page cookies
    # ad_cookie = { 
    #     'SESSID':view.cookies['SESSID'],
    #     'IDMSESSID':username,
    #     '__utma':''
    # } 
    #  
    # ad_payload = {
    #     'CRN_IN':'40116',
    #     'RSTS_IN':'WR',
    #     'term_in':term_in,
    #     'REG_BTN':'Submit Changes'
    # } 

    # ad_headers = { 
    #     "Referer":"https://banner.drexel.edu/pls/duprod/bwskfreg.P_AltPin",
    #     "User-Agent":ua.random,
    #     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #     "Host":"banner.drexel.edu"
    # }   

    # classes = s.post(
    #     ad_url,
    #     cookies = ad_cookie,
    #     data = ad_payload,
    #     headers = ad_headers
    # )

    # # And we're in!
    # print classes.text
