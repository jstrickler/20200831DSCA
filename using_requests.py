import requests

DSCA_HOME_URL = "https://www.dsca.mil"

try:
    response = requests.get(DSCA_HOME_URL)
except requests.ConnectionError as err:
    print(err)
else:
    if response.status_code == requests.codes.OK:
        contents = response.content.decode()
        print(contents)  # search with regex  or BeautifulSoup ??

DSCA_PDF_URL = "https://www.dsca.mil/sites/default/files/NVDGuideFiles/2014%20DoD%20Transfer%20of%20Night%20Vision%20Devices%20Handbook.pdf"

response = requests.get(DSCA_PDF_URL)
if response.status_code == requests.codes.OK:
    with open('dsca.pdf', 'wb') as pdf_out:
        pdf_out.write(response.content)
else:
    print("Invalid request")