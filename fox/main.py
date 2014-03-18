# Mike Taatgen
# DPW 2 
# What does the fox say?
# 03 - 18 - 14

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()

		# redPanda class that gets all the attributes from the AbstractAnimals class
		redPanda = Sound()
		redPanda.name = "Red Panda"
		redPanda.phylum = "Chordata"
		redPanda.cclass = "Mammalia"
		redPanda.order = "Carnivora"
		redPanda.family = "Ailuridae"
		redPanda.genus = "Ailurus"
		redPanda.url = "http://animaldiversity.ummz.umich.edu/accounts/Ailurus_fulgens/pictures/collections/contributors/Kjeldsen_Per/Red_Panda7208/"
		redPanda.alifespan = "The maximum lifespan of the red panda is 14 years, but the average is eight to ten."
		redPanda.habitat = "Red pandas live in temperate climates in deciduous and coniferous forests. There is usually an understory of bamboo and hollow trees. The average temperature is 10 to 25 degrees Celsius, and the average annual rainfall is 350 centimeters."
		redPanda.geolocation = "Red pandas are found throughout the Himalayan mountains between 2,200 and 4,800 meters in elevation in northern Burma, Nepal, Sikkim region of India, and the districts of western Sichuan and Yunnan in China. Their geographic range is bounded in the north by the Namlung Valley in the Mugo District and the Lake Rara region of northern Nepal, in the south by the Liakiang Range of western Yunnan, and the northern and eastern boundary is the upper Min Valley of western Sichuan."
		redPanda.sound = "Wieuw Wieuw"
		redPanda.update()

		# LeopardShark class that gets all the attributes from the AbstractAnimals class
		leopardShark = Sound();
		leopardShark.name = "Leopard Shark"
		leopardShark.phylum = "Chordata"
		leopardShark.cclass = "Chondrichthyes"
		leopardShark.order = "Carcharhiniformes"
		leopardShark.family = "Carcharhinidae"
		leopardShark.genus = "Galeocerdo"
		leopardShark.url = "http://www.elasmodiver.com/Sharkive%20images/Leopard_Shark224.jpg"
		leopardShark.alifespan = "The average lifespan of tiger sharks in the wild is 27 years, though some may live to 50 years of age. "
		leopardShark.habitat = "Tiger sharks are a saltwater species. Although they prefer the sea grass ecosystems of the costal areas, they occasionally inhabit other areas due to prey availability. Tiger sharks spend approximately 36&#37; of their time in shallow coastlne habitats (Heithaus et al., 2002), generally at depths of 2.5 to 145 m. This species, however, has been documented several kilometers from the shallow areas and at depths up to 350 m. Females are observed in shallow areas more often than males. Tiger sharks have also been documented in river estuaries and harbors"
		leopardShark.geolocation = "Tiger sharks are found in many subtropical and tropical waters, primarily from 45&deg;N to 32&deg;S. Tiger sharks have been sighted from the eastern coast of North America to the eastern coast of Brazil. This includes the coasts of southern North America, Mexico, and Latin America along the Gulf of Mexico. Tiger sharks also populate the coasts of China, India, Africa, Japan, and many islands of the Pacific Ocean."
		leopardShark.sound = "Wrah Wrah"
		leopardShark.update()

		# Blue Marlin class that gets all the attributes from the AbstractAnimals class
		blueMarlin = Sound()
		blueMarlin.name = "Blue Marlin"
		blueMarlin.phylum = "Chordata"
		blueMarlin.cclass = "Actinopterygii"
		blueMarlin.order = "Perciformes"
		blueMarlin.family = "Istiophoridae"
		blueMarlin.genus = "Makaira"
		blueMarlin.url = "http://animaldiversity.ummz.umich.edu/collections/contributors/Grzimek_fish/Scombroidei/Makaira_nigricans/button.jpg"
		blueMarlin.alifespan = "The maximum lifespan of females is estimated to be at least 27 years, while males are estimated to live a maximum of 18 years."
		blueMarlin.habitat = "Makaira nigricans is an epipelagic and oceanic species. It is the most oceanic of all istiophorids, usually remaining far from land except where the continental shelf is narrow. It can be found in waters with surface temperatures of 22-31C, but it prefers the warm mixed layer above the thermocline, and spends the majority of its time in the uniformly warm near-surface waters from 25-27C. It shows preference for blue waters, at least in the northern Gulf of Mexico."
		blueMarlin.geolocation = "<p>Makaira nigricans is distributed mainly in the tropical and temperate waters of the Atlantic, Pacific, and Indian Oceans. It is the most tropical of all billfishes.</p> <p>In the Atlantic Ocean, its range extends to around 40-45N in the North Atlantic and to 40S in the western Atlantic, 30S in the central South Atlantic and 35S in the eastern south Atlantic, but is absent from the Mediterranean Sea. In the Pacific, its range extends to about 45N in the western North Pacific, 35N in the eastern North Pacific, 35S in the western South Pacific, and 25S in the eastern South Pacific. </p> <p> In the Indian Ocean, its range extends to 45S in the southwestern Indian Ocean and 35S in the southeastern Indian Ocean. Larvae are found extensively in the tropical and subtropical waters of the western and central Pacific Ocean, south of Maldives Islands, around the Mascalene Islands, and off the south coasts of Java and Sumatra in the Indian Ocean. In the western central Atlantic, larvae are found off Georgia, North Carolina, Florida, Jamaica, Bahamas, Arecibo, and also off Brazil in the southwest Atlantic. </p>"	
		blueMarlin.sound = "Whish Whish"
		blueMarlin.update()
		
		#Array with all the animals in it
		animals = [blackDolphins,leopardShark,blueMarlin]

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
