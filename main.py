from typing import Text
import requests
url = requests.get('https://www.mcexperienciasurvey.com')
print(url.encoding, url.text)