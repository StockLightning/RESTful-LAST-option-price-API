## What is This?

A small web server that grabs option prices for you

## How do I use it?

Simply access it by a GET request for `/getlastprice` with the following parameters: `symbol`,`strike`,`expiration`,`call_or_put`

format for expiration date: `mm-dd-yyyy`

example: `/getlastprice?symbol=NOK&strike=6&expiration=01-19-2018&call_or_put=CALL`

## That's cool can I use this for Google Sheets?

Yeah and that's why I made this project:

    `=IMPORTHTML("http(s)://<domain>/getlastprice?symbol="&B1&"&strike="&F1&"&expiration="&E1&"&call_or_put="&D1&"&A1="&$A$2, "list", 1)`

#### Why do you have the A1 parameter there?

Google Sheets doesnt have a reliable way to reload the cells that use the IMPORTHTML function, so instead I force it to reload by changing the value of the cell indirectly by changing the value of the A2 cell (frozen first 2 rows so it's easily accessible).

The server safely ignores this parameter.

## How do I run it?

* Setup Tradier:
    * Signup and get an Authorization token from [Tradier](https://developer.tradier.com/documentation)
    * put your authorization token in `app/views.py`
* Setup project:
    * clone the repo
    * run `pip install -r requirements.txt`
    * run `python manage.py runserver 0.0.0.0:<port>`