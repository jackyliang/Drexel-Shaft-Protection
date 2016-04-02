# Drexel Shaft Protection

### What on earth is Drexel Shaft Protection?

Have you ever forgot to wake up in the morning of your 7:30 AM Drexel class registration? Have you ever been Shafted™ by Drexel because someone registered for you 30 seconds earlier and
now all the classes are full? Have you ever..

Oh of course you have! You've always been Drexel Shafted™!

Drexel Shaft Protection allows you to automatically register for classes!

### How to use Drexel Shaft Protection

1. Create an `info.json` file within the same directory as the `add.py` and use the following template:

	***Note:*** *You can only add maximum 10 CRNs at a time and you MUST follow this exact template*

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

2. `./add.py`

### What custom Python libraries I used

1. `lxml` for HTML/XML parsing and scraping

    `pip install lxml`

2. `fake_useragent` to generate randomized fake user agents 

    `pip install fake_useragent`

### Common errors and fixes

    Traceback (most recent call last):
	    File "./add.py", line 69, in <module>
	    	br.select_form(nr=1)
	  	File "/usr/local/lib/python2.7/site-packages/mechanize/_mechanize.py", line 524, in select_form
	    	raise FormNotFoundError("no form matching "+description)
	mechanize._mechanize.FormNotFoundError: no form matching nr 1

This means your username/password is incorrect.

TODO: Catch this exception and return a better error message

### What I used to develop Drexel Shaft Protection

1. Python 2.7.8

2. OS X Yosemite 10.10.5 (14F27)

3. Sublime Text 3 with Vintage Plugin

### I got questions!

If you have any questions, please feel free to submit an [issue](https://github.com/jackyliang/Drexel-Shaft-Protection/issues).
