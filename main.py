import creds
import constants
import requests

def buildURL(url):
	return constants.NA_URL_PREFIX + url + "?api_key=" + creds.apiKey

def requestSummonerData(summonerName):
	URL = buildURL(constants.REQUEST_SUMMONER_BY_NAME + summonerName)
	response = requests.get(URL)
	return response.json()	

def requestMatchList(encryptedAccountId):
	URL = buildURL(constants.REQUEST_MATCH_LIST + encryptedAccountId)
	response = requests.get(URL)
	return response.json()	

def main():
	summonerName = input("Summoner Name: ")
	summonerDataJSON = requestSummonerData(summonerName)
	print(summonerDataJSON)

if __name__ == "__main__":
	main()