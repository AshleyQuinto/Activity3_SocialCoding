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
        
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Distance (in Kilometers): " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6)))
        print("Time Restriction? " + str(format(json_data["route"]["hasTimedRestriction"]))) #added info
        print("Fuel Usage (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]* 3.78)))

        if ((str(json_data["route"]["legs"][0]["hasFerry"])) != "true"): #check if there is ferry
            print("Route does not have ferry trip")
        else:
            print("Route offers ferry trip")

        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    elif json_status == 612:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; There are no routes available for this location") #added status code
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")