import requests
import sys

HEADERS = {"X-API-Key":'83bdaf66edb2466fa4ec180b164668ae'}
xur_url = "https://www.bungie.net/Platform/Destiny/Advisors/Xur/"
print ("\n\n\nConnecting to Bungie: " + xur_url + "\n")
print ("Fetching data for: Xur's Inventory!")
res = requests.get(xur_url, headers=HEADERS)

error_stat = res.json()['ErrorStatus']
if error_stat == "DestinyVendorNotFound":
    print("Xur is not currently available!")
else:
    print ("Error status: " + error_stat + "\n")

input("Press Enter to quit.")

sys.exit()    
