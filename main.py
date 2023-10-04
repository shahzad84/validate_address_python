import requests
def validate_address(address, pin_code):
    api_url = f"https://api.postalpincode.in/pincode/{pin_code}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if data and data[0]["Status"] == "Success":
            post_offices = data[0]["PostOffice"]
            for post_office in post_offices:
                if post_office["Name"].lower() in address.lower():
                    return True

    return False
addresses = [
    "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050",
    "2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050",
    "374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050",
    "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095",
    "Colony, Bengaluru, Karnataka 560050",
]
pin_codes = [
    "560050",
    "560050",
    "560050",
    "560095",
    "560050",
]
for address, pin_code in zip(addresses, pin_codes):
    if validate_address(address, pin_code):
        print(f"'{address}' valid address")
    else:
        print(f"'{address}' not valid address")
