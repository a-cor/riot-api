import creds
import constants
import json
import requests

# HELPER FUNCTIONS

def buildURL(url):
	return constants.NA_URL_PREFIX + url + "?api_key=" + creds.apiKey

def printJSON(jsonObject):
	jsonFormattedString = json.dumps(jsonObject, indent=2)
	print(jsonFormattedString)

# REQUEST FUNCTIONS

def requestSummonerData(summonerName):
	URL = buildURL(constants.REQUEST_SUMMONER_BY_NAME + summonerName)
	response = requests.get(URL)
	return response.json()	

def requestMatchList(encryptedAccountId):
	URL = buildURL(constants.REQUEST_MATCH_LIST + encryptedAccountId)
	response = requests.get(URL)
	return response.json()	

def requestMatch(matchId):
	URL = buildURL(constants.REQUEST_MATCH + str(matchId))
	response = requests.get(URL)
	return response.json()	



def main():

	summonerName = input("Summoner Name: ")
	summonerDataJSON = requestSummonerData(summonerName)
	printJSON(summonerDataJSON)

	accountId = summonerDataJSON['accountId']
	matchListJSON = requestMatchList(accountId)
	printJSON(matchListJSON['matches'][0])

	matchId = matchListJSON['matches'][0]['gameId']
	matchJSON = requestMatch(matchId)
	# printJSON(matchJSON) # prints a lot!

if __name__ == "__main__":
	main()