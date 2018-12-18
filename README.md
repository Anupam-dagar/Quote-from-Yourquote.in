# Quote from Yourquote.in

## Usage
1. Import `Yquote` in your python file using `from Yquote import Yquote`.
2. Create a `Yquote` object. For example `yourquote = Yquote()`.
3. To get a quote, call the `get_quote(str: tag)` function with tag as the argument.  
For example: `quote = yourquote.get_quote('2019')`

## Requirements
1. BeautifulSoup4
2. Requests

Install requirements using pip install -r requirements.txt

## Limitation
Currently it can get a quote only from the limited number of quotes fetched for a provided tag.

## LICENSE
MIT