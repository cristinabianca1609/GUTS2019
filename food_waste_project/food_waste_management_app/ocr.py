import requests, json, re

def api_request(filename, apikey, language='eng'):
    url = 'https://api.ocr.space/parse/image'
    params = { 'isOverlayRequired' : False
             , 'apikey'            : apikey
             , 'language'          : language
             }
    with open(filename, 'rb') as f:
        r = requests.post(url, files={filename: f}, data=params)
        return r.content.decode()

def date_segment_valid(seg):
    seg = seg.upper()

def parse_response(raw):
    text  = json.loads(raw)["ParsedResults"][0]["ParsedText"]
    regex = re.findall(r'\b(0[1-9]|[1-2][0-9]|3[0-1]|[A-Za-z]{3,9}|20\d{2})\b', text)
    date  = dateparser.parse(" ".join(regex.split()))
    return date

filename = "../static/images/expiry02_mini.jpg"
print(parse_response(api_request(filename, apikey='bf9a07b67388957')))
