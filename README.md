# Drexel Shaft Protection

### What on earth is Drexel Shaft Protection?

Have you ever forgot to wake up in the morning of your 7:30 AM Drexel class registration? Have you ever been Shafted™ by Drexel because someone registered for you 30 seconds earlier and
now all the classes are full? Have you ever..

Oh of course you have! You've always been Drexel Shafted™!

Drexel Shaft Protection allows you to automatically register for classes!

### How to use Drexel Shaft Protection

1. Create an `info.json` file within the same directory as the `add.py` and use the following template:

	***Note:*** *You can only add maximum 10 CRNs at a time and you MUST follow this exact template*

		# Template for info.json
		# Save this in the same directory as add.py
		{   
		    "username":"Your Drexel username",
		    "password":"Your Drexel password",
		    "classes": {
		    	"1": "33587", # this is an example CRN
		    	"2": "",
		    	"3": "",
		    	"4": "",
		    	"5": "",
		    	"6": "",
		    	"7": "",
		    	"8": "",
		    	"9": "",
		    	"10": ""
		    }
		}  
	    
	This serves as the file in which this script will read your Drexel username, password, and the classes you want to register classes for. 

2. Execute using `./add.py`

3. Alternatively, set up a scheduled task 5 ms after your time ticket i.e. `7:30:00:50 AM` on your favorite operating system

### What custom Python libraries I used

1. `mechanize` for browser emulation
	
		pip install mechanize

2. `lxml` for HTML/XML parsing and scraping

    	pip install lxml

### TODO

- Drop classes
	- add a new associative array for `drop` in `info.json`
	- remove classes by iterating through the CRNs
- ~~Better/more error handling~~
	- ~~handling the incorrect login credentials~~
	- ~~handling incorrect `info.json` file~~
	- ~~handling missing `info.json` file~~
- Not hardcoding the term selection
	- term selection is currently hardcoded for the specific term i.e. `201535`. See if a index be selected instead
- ~~Show each submission error~~
- ~~Show total credit hours~~
- Prettify the console outputs

### Common errors and fixes

1. ~~Incorrect login credentials will give the following error~~ Added exception handling for this

	    Traceback (most recent call last):
		    File "./add.py", line 69, in <module>
		    	br.select_form(nr=1)
		  	File "/usr/local/lib/python2.7/site-packages/mechanize/_mechanize.py", line 524, in select_form
		    	raise FormNotFoundError("no form matching "+description)
		mechanize._mechanize.FormNotFoundError: no form matching nr 1

### What I used to develop Drexel Shaft Protection

1. Python 2.7.8

2. OS X Yosemite 10.10.5 (14F27)

3. Sublime Text 3 with Vintage Plugin

### I got questions!

If you have any questions, please feel free to submit an [issue](https://github.com/jackyliang/Drexel-Shaft-Protection/issues).
