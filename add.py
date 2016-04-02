#!/usr/bin/env python

# Jacky Liang 2016
                                                                          
## OS and Python Version                                                  
# Python 2.7.8                                                         
# OS X Yosemite 10.10.5 (14F27)
                                                                          
## Libraries:                                                             
# Uses the mechanize library
# 	pip install mechanize 

## TODO:
# 1. Drop classes
# 2. Better/more error handling
# 3. Not hardcoding the term selection
# 4. Show each submission error
# 5. Show total credit hours

import mechanize, os, json, sys
from lxml import html

# Path and name to info.json which is where we store
# our credentials and classes to add
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

# Open the Drexel One URL
response = br.open(url)

# Select the first form element where the username and
# password is
br.select_form(nr = 0)
br.form['username'] = username
br.form['password'] = password

# Login by submitting the form
br.submit()

# Navigate to the "Academics" page
academics = br.open('https://one.drexel.edu/web/university/academics?gpi=10230')

# Navigate to the "Add/Drop Classes" page
add_drop = br.open('https://bannersso.drexel.edu/ssomanager/c/SSB?pkg=bwszkfrag.P_DisplayFinResponsibility%3Fi_url%3Dbwskfreg.P_AltPin')

# Select the second form in the page which is the select
# for the academic year
br.select_form(nr=1)

# Select the academic year term
form = br.form
# TODO: select the first item instead of hardcoding
form['term_in'] = ['201535',]

# Submit the form
response = br.submit()

# Select the second form in the add/remove class page
br.select_form(nr=1)

# Iterate through our 'classes' object from info.json
# which contains the ID tag and CRN
for id_tag, crn in classes.items():
	# Convert ID tags to integers
	id_tag_int = int(id_tag)
	# Only valid ID tags and non-spaces will be submitted
	# to the form
	if(id_tag_int >= 1 and id_tag_int <= 10):
		# Ignore if input is empty
		if(crn != ''):
			print 'Adding your class with CRN ' + crn + "..."
			# Assign the CRN as the value based on the form name
			# and crn_id form ID tag
			add_control = br.form.find_control(name='CRN_IN', id='crn_id' + id_tag)
			add_control.value = crn
			print 'Successfully added your class with CRN ' + crn + "!"

# Submit the form after all textboxes filled in
response = br.submit()

# Convert all forms to a list to access its key-value pairs
f = list(br.forms())

# Generate a string for each class
test = ''

# Print out all added classes
print '== All your added classes =='

for k,v in f[1]._pairs():
	# Ignore dummy values
	if v == 'DUMMY':
		continue
	if k == 'CRN_IN':
		test += '[' + v + '] '
	if k == 'SUBJ':
		test += v
	if k == 'CRSE':
		test += '-' + v
	if k == 'SEC':
		test += ' ' + v
	if k == 'TITLE':
		test += ' ' + v
		print test
		test = ''
