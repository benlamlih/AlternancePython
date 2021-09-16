import requests 


#Apple emoji unicode
apple = "\U0001F34E"

#Windows emoji unicode (This emoji is not available in browser/windows)
windows = "\U0001FA9F"

#linux emoji unicode
linux = "\U0001F427"

#Android emoji unicode 
android = "\U0001F916"


url = "https://random-data-api.com/api/internet_stuff/random_internet_stuff"
#url = "http://10.255.255.1"

#api request
try:
    response = requests.get(url, timeout=10.0)
except requests.exceptions.Timeout:
    # Set up for a retry
    print("Timeout. We will try again")
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        # Exit
        raise SystemExit(e)
except requests.exceptions.TooManyRedirects:
    # Bad url
    print("Please try with another URL!")
except requests.exceptions.RequestException as e:
    # Exit
    raise SystemExit(e)

assert(response.status_code == 200)
res = response.json()

username = (res['username'])
email = (res['email'])
#User-Agent: Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>
user_agent = (res['user_agent'])
upper_user_agent = user_agent.upper()


if ("WINDOWS" in upper_user_agent or "WIN" in upper_user_agent):
    emoji = windows
elif ("APPLE" in upper_user_agent or "IOS" in upper_user_agent):
    emoji = apple
elif ("LINUX" in upper_user_agent):
    emoji = linux
else:
    emoji = android
    
print("L'adresse email de l'utilisateur " + username + " est " + email + ". Il utilise le système d'exploitation " + emoji + ".")

