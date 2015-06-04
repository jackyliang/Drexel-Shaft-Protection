# Drexel Shaft Protection

Have you ever forgot to wake up in the morning of your 7:30 AM Drexel class registration? Have you ever been Shafted™ by Drexel because someone registered for you 30 seconds earlier and
now all the classes are full? Have you ever..

Oh of course you have! You've always been Drexel Shafted™!

Drexel Shaft Protection allows you to automatically register for classes!

### Usage

1. Create an `info.json` file within the same directory as the `add.py`. 

        {   
            "username":"Your Drexel username",
            "password":"Your Drexel password",
            "term_in":"The term you're trying to register for i.e. 201445"
        }   
    
    This serves as the file in which this script will read your Drexel username, password, and 
    the term you want to register classes for. 

2. `./add.py`

### Custom Libraries Used

1. `lxml` for HTML/XML parsing and scraping

2. `fake_useragent` to generate randomized fake user agents 

### Development Information

1. Python 2.7.9

2. Debian 8.0 (jessie)
