from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 


def write_to_csv(fileName, names, prices):
	f = open(fileName, "w", encoding="utf-8")
	headers = "product_name, price\n"
	f.write(headers)
	for name, price in zip(names, prices):
		f.write(name.replace(",", " ") + "," + price.text + "\n")
	f.close()


def print_cards(names, prices):
	for name, price in zip(names, prices):
		print("Name : ", name)
		print("Price : ", price.text)
		print("\n")


def get_containers(url, tagName, toFind):
	uClient = uReq(url)
	pageHtml = uClient.read()
	uClient.close()
	pageSoup = soup(pageHtml, "html.parser")
	return pageSoup.findAll(tagName, toFind)


def get_info_from_containers(containers, tagName, attributeToLookFor, attributeToGet=0):
	result = list()
	if attributeToGet == 0:
		for item in containers:
			result.append(item.find(tagName, attrs=attributeToLookFor))
	else:	
		for item in containers:
			result.append(item.find(tagName, attrs=attributeToLookFor)[attributeToGet])
	return result


'''
containers = get_containers("https://hard.rozetka.com.ua/videocards/c80087/producer=asus/", "div", {"class":"goods-tile__inner"})
cardNames = get_info_from_containers(containers, "a", {"class":"goods-tile__heading"}, "title")
cardPrices = get_info_from_containers(containers, "span", {"class":"goods-tile__price-value"})
write_to_csv("data.csv", cardNames, cardPrices)
'''



