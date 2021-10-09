import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "uzk5yMc9thiFlYRBQJLOUhwtZ7pCvwGC"

while True:
    orig = input("Source City: ")

    if orig == "quit" or orig == "q":
        break

    dest = input("Dest City: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL ", (url))
    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]


    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")