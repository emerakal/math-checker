import requests
import json
import os


File = 'MathData.txt'
if os.path.getsize(File) != 0:
    ffl = open(File, 'w')
    ffl.truncate()
    ffl.close()


data = {
    "src": "https://mathpix-ocr-examples.s3.amazonaws.com/limit.jpg",
    "formats": [
        "latex_simplified",
        "asciimath",
        "mathml"
    ]
}

r = requests.get("https://api.mathpix.com/v3/latex",
        json= data, 
        headers={
            "app_id": "ed_strok_17_gmail_com_f758da_ee81be",
            "app_key": "ca0766ae6ded2bce61706b7282dc156c2e10ac800bd8328ecdf8e18204588941",
            "Content-type": "application/json"
        }
    )

with open(File, 'w') as f:
    data = json.dumps(r.json(), indent = 0, sort_keys=True)
    f.write(data)

