# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2

# URL
URL = "http://www.tecoplaza.com/newlink/tabijyoho/kion.htm"

html = urllib2.urlopen(URL).read()
soup = BeautifulSoup(html)


class favplace():

	def scrape_temperature(self, color):
		"""
		scraping columns by bgcolor
		"""
		array = []
		_val = (soup("td", {"bgcolor": color}))
		for tag in _val:
			for fonttag in tag.findAll("font", {"size": "-1"}):
				array.append(fonttag.renderContents())

		return array
	
	def disp(self, temp1, temp2, temp3):
		months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
		count = 0
		n = 1
		print(cnames[0])
		print('-'*60)
		print("\t\t" + "High" + "\t\t" + "Low" + "\t\t" + "Precipitation")
		for i in range(len(temp1)):
			print(months[count] + "\t\t" + temp1[i] + "\t\t" + temp2[i] + "\t\t" + temp3[i])
			count = count + 1
			if count == 12:
				if not n >= len(cnames):
					print('-'*60)
					print(cnames[n])
					n = n + 1
				else:
					break
				print('-'*60)
				print("\t\t" + "High" + "\t\t" + "Low" + "\t\t" + "Precipitation")
				count = 0


if __name__ == "__main__":
	size = {"asia": "71", "america": "81", "oceania": "66", "euro": "64"}
	def city_name(width_val):
		cities = (soup("td", {"width": width_val}))
		city_group = []

		for tag in cities:
			for city in tag.findAll("font"):
				if city.renderContents() == "国" or \
					city.renderContents() == "都市":
					continue
				city_group.append(city.renderContents().replace("<br />", ""))

		return city_group
	
	cnames = city_name(size["asia"]) + city_name(size["america"]) \
		+ city_name(size["oceania"]) + city_name(size["euro"])
	
	bgcolor = {"hightemp": "#ffeeff", "lowtemp": "#e8f3ff", "rain": "#ffffdf"}

	climate = favplace()
	highest = climate.scrape_temperature(bgcolor["hightemp"])
	lowest = climate.scrape_temperature(bgcolor["lowtemp"])
	precipitation = climate.scrape_temperature(bgcolor["rain"])
	climate.disp(highest, lowest, precipitation)
