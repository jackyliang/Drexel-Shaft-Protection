#!/usr/bin/env python

# Jacky Liang 2016
                                                                          
## OS and Python Version                                                  
# Python 2.7.8                                                         
# OS X Yosemite 10.10.5 (14F27)
                                                                          
## Libraries:                                                             
# Uses the mechanize + lxml library
# 	pip install mechanize
# 	pip install lxml

## TODO:
# 1. Drop classes
# 2. Better/more error handling
# 3. Not hardcoding the term selection
# 4. Prettify course submission errors

import mechanize, os, json, sys
import lxml.html

# Path and name to info.json which is where we store
# our credentials and classes to add
info_db = './info.json'                                                 
                                                                          
# Parse info.json which contains our three input params                   
if os.path.exists(info_db):                                               
    with open(info_db) as data_file:                                      
        info = json.load(data_file)                                       
else:                                                                     
    print "ERROR: download info.json here: https://github.com/jackyliang/Drexel-Shaft-Protection/blob/master/info.json"
    sys.exit(0)                                                           
                                                                          
# Grab username, password, and classes from info.json                     
try:
	username = info['username']                                               
	password = info['password']
	classes = info['classes']
except Exception as e:
	print 'ERROR: There is something wrong with your info.json file!'
	sys.exit(0)

# Create a new Mechanize browser
br = mechanize.Browser()
# Allow redirection as Drexel One has a ton of redirections
br.set_handle_redirect(True)
br.set_handle_refresh(True)
# Drexel One login URL
url = 'https://connect.drexel.edu'

# Open the Drexel One URL
response = br.open(url)

print 'Reading info.json'

# Select the first form element where the username and
# password is
br.select_form(nr = 0)
br.form['j_username'] = username
br.form['j_password'] = password

print '(OK)'
print 'Logging in for: ' + username

# Login by submitting the form
br.submit()

#Drexel broken? need to make 2 requests. the first one fails
try:
	br.open('https://one.drexel.edu/web/university/academics')
except:
	print ''
br.open('https://one.drexel.edu/web/university/academics')
# Navigate to the "Add/Drop Classes" page
add_drop = br.open('https://bannersso.drexel.edu/ssomanager/c/SSB?pkg=bwszkfrag.P_DisplayFinResponsibility%3Fi_url%3Dbwskfreg.P_AltPin')

# Select the second form in the page which is the select
# for the academic year
try:
	br.select_form(nr=1)
except Exception as e:
	print 'ERROR: Seems like your login credentials are wrong. Check info.json to make sure!'
	sys.exit(0)

print '(OK)'

# Select the academic year term
form = br.form
# TODO: select the first item instead of hardcoding
form['term_in'] = ['201635']

# Submit the form
response = br.submit()

# Select the second form in the add/remove class page
try:
	br.select_form(nr=1)
except Exception as e:
	print 'ERROR: It seems like it is not your registration time yet. If it is, then try again in a few seconds.'
        sys.exit(0)

print '*****************************************************************'
print '                  Submitting classes'
print '*****************************************************************'

# Iterate through our 'classes' object from info.json
# which contains the ID tag and CRN
for id_tag, crn in classes.items():
	# Convert ID tags to integers
	id_tag_int = int(id_tag)
	# Only valid ID tags and non-spaces will be submitted
	# to the form
	if(id_tag_int >= 1 and id_tag_int <= 10):
		# Ignore if input is empty
		if crn:
			print 'Attempting to add CRN ' + crn + "..."
			# Assign the CRN as the value based on the form name
			# and crn_id form ID tag
			add_control = br.form.find_control(name='CRN_IN', id='crn_id' + id_tag)
			add_control.value = crn
			# print 'Successfully added your class with CRN ' + crn + "!"

# Submit the form after all textboxes filled in
response = br.submit()

# Convert all forms to a list to access its key-value pairs
f = list(br.forms())

# Generate a string for each class
test = ''

# Read the HTML and convert it to XML for traversal
html = br.response().read()
root = lxml.html.fromstring(html)

# Get total credits
credits = root.xpath('/html/body/div[3]/form/table[2]/tr[1]/td[2]/text()')
try:
        credits = credits[0].strip(' ')
except Exception as e:
        credits = '0'

# Print out all added classes
print '*****************************************************************'
print '       All your added classes with total credits: ' + credits
print '*****************************************************************'

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
		print '    ' + test
		test = ''

# Print out all errors
print '*****************************************************************'
print '          All errors will be shown here (if any)'
print '*****************************************************************'

for i in range(10):
	# Print all errors
	errors = root.xpath('/html/body/div[3]/form/table[4]/tr[' + str(i) + ']/td/text()')

	# Join the list and print it if not empty
	if errors:
		print '    [x] ' + ' '.join(errors)
