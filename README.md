# Drexel Shaft Protection

### What on earth is Drexel Shaft Protection?

Have you ever forgot to wake up in the morning of your 7:30 AM Drexel class registration? Have you ever been Shafted™ by Drexel because someone registered for you 30 seconds earlier and
now all the classes are full? Have you ever..

Oh of course you have! You've always been Drexel Shafted™!

Drexel Shaft Protection allows you to automatically register for classes!

### How to use Drexel Shaft Protection

1. Create an `info.json` file within the same directory as the `add.py` and use the following template:

***Note:*** You can only add maximum 10 CRNs at a time and you MUST follow this exact template

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

    pip install lxml

2. `fake_useragent` to generate randomized fake user agents 

    pip install fake_useragent

### Common errors and fixes

    print page.cookies['IDMSESSID'] KeyError

This means your username/password is incorrect.

TODO: Catch this exception and return a better error message

### What I used to develop Drexel Shaft Protection

1. Python 2.7.9

2. Debian 8.0 (jessie)

3. VIM - Vi IMproved 7.4 (2013 Aug 10)

### I got questions!

If you have any questions, please feel free to submit an [issue](https://github.com/jackyliang/Drexel-Shaft-Protection/issues).
