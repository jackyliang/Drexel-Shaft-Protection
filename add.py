#!/usr/bin/env python

import mechanize, os, json, sys

info_db = './info.json'                                                 
                                                                          
# Parse info.json which contains our three input params                   
if os.path.exists(info_db):                                               
    with open(info_db) as data_file:                                      
        info = json.load(data_file)                                       
else:                                                                     
    print "Error - please create a info.json file!"                       
    sys.exit(0)                                                           
                                                                          
# Grab username, password, and classes from info.json                     
username = info['username']                                               
password = info['password']
classes = info['classes']

# Create a new Mechanize browser
br = mechanize.Browser()

# Allow redirection as Drexel One has a ton of redirections
br.set_handle_redirect(True)

# Drexel One login URL
url = 'https://login.drexel.edu/cas/login?service=https%3A%2F%2Fone.drexel.edu%2Fc%2Fportal%2Flogin'

response = br.open(url)

# Select the first form element where the username and
# password is
br.select_form(nr = 0)
br.form['username'] = username
br.form['password'] = password

br.submit()

# Navigate to the "Academics" page
academics = br.open('https://one.drexel.edu/web/university/academics?gpi=10230')

# Navigate to the "Add/Drop Classes" page
add_drop = br.open('https://bannersso.drexel.edu/ssomanager/c/SSB?pkg=bwszkfrag.P_DisplayFinResponsibility%3Fi_url%3Dbwskfreg.P_AltPin')

# Select the second form in the page
br.select_form(nr=1)
form=br.form

# Select the academic year term
# TODO: select the first item instead of hardcoding
form['term_in'] = ['201535',]
response = br.submit()

br.select_form(nr=1)

for id_tag, crn in classes.items():
	if(crn != ''):
		add_control = br.form.find_control(name='CRN_IN', id='crn_id' + id_tag)
		add_control.value = crn

response = br.submit()
print response.get_data()

for control in br.form.controls:
    print control