import requests, json

def api_request(filename, apikey, language='eng'):
    url = 'https://api.ocr.space/parse/image'
    params = { 'isOverlayRequired' : False
             , 'apikey'            : apikey
             , 'language'          : language
             }
    with open(filename, 'rb') as f:
        r = requests.post(url, files={filename: f}, data=params)
        return r.content.decode()

def parse_response(raw):
    text = json.loads(raw)["ParsedResults"][0]["ParsedText"]
    print(text)
    return 0

filename = "/home/patsonical/Documents/DoYouHaveTheGUTS2019/ocrTesting/imgs/expiry02_mini.jpg"
parse_response(api_request(filename, apikey='bf9a07b67388957'))
