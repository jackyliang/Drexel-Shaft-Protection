# Drexel Shaft Protection

*"I wish I'd had this in undergrad. LOL."*   -actual Drexel student comment

<img src="http://i.imgur.com/60DCbzR.gif">

### What on earth is Drexel Shaft Protection?

Have you ever forgot to wake up in the morning of your 7:30 AM Drexel class registration? Have you ever been Shafted™ by Drexel because someone registered for you 30 seconds earlier and
now all the classes are full? Have you ever..

Oh of course you have! You've always been Drexel Shafted™!

Drexel Shaft Protection was created to help fellow Drexel students to automatically register for classes! Well, at least those that are willing to get their hands a little dirty and know a little code :).

### How to use Drexel Shaft Protection

1. Install the Mechanize and lxml library

		pip install mechanize
		pip install lxml

2. Change name of `change_me_to_info.json` to `info.json`. Alternatively, download it [here](https://github.com/jackyliang/Drexel-Shaft-Protection/blob/master/change_me_to_info.json) and change the name to `info.json`. Template of `info.json` is below. 

	***Note:*** *You can only add maximum 10 CRNs at a time and you MUST follow this exact template*. The value `33587` is a sample CRN and can be removed.

		{   
		    "username":"Your Drexel username",
		    "password":"Your Drexel password",
		    "classes": {
		    	"1": "33587",
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
	
	*Note*: I do not save or harvest your Drexel usernames or password. 

2. Execute using `./add.py`

3. Alternatively, use the "[at](http://www.computerhope.com/unix/uat.htm)" command (thanks [Tomer](https://github.com/eclair4151) for the suggestion) and set a time that's one second after your registration time (i.e. execute at `7:30:01`.. `7:30:02`.. `7:30:3`..) for 4 - 5 time per second. That'll likely better handle your system clock not matching Drexel One's clock. 

### Really important information you should read

1. Registering for a class in a new quarter

	If this is a new quarter, you ***MUST*** manually update your registration information within the Drexel One "Add/Drop Class" page. Fortunately, you can access this page even before your registration ticket. This application WILL NOT WORK if you do not do that first.

2. Running the script before your class registration time slot:

	If you try to run the script before your class registration time slot, you will receive the following error.  

        ERROR: It seems like it's not your registration time yet. If it is, then try again in a few seconds.
	    	
	This is normal as the script cannot find the dropdown that selects your term. It will work when you execute the script on the registration time.
	
### People love the Drexel Shaft Protection

*"Drexel-shaft-protection is an amazing script to avoid those days where you waste time manually looking up and entering classes during registration day only to find you took too long and the class is full. It's convenient and it works!"*

*"I wish I'd had this in undergrad. LOL."*

*"Drexel-shaft-protection" I think we could all use a bit more of that"*

*"Why do you come up with all this shit AFTER we're getting ready to graduate? I could've used this so many times, instead of having to wake up early and register for classes."*

### What custom Python libraries I used

1. `mechanize` for browser emulation
	
		pip install mechanize

2. `lxml` for HTML/XML parsing and scraping

    	pip install lxml

### TODO

- *Important*: Error message for telling the user they need to fill the pre-registration form
- *Important*: Error message for telling the user that the script failed because it is not their class registration time slot
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

### What I used to develop Drexel Shaft Protection

1. Python 2.7.8

2. OS X Yosemite 10.10.5 (14F27)

3. Sublime Text 3 with Vintage Plugin

### I got questions!

If you have any questions, please feel free to submit an [issue](https://github.com/jackyliang/Drexel-Shaft-Protection/issues).
