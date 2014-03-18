# Mike Taatgen
# DPW 2 
# What does the fox say?
# 03 - 18 - 14

import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
		page = Page()

		# redPanda class that gets all the attributes from the AbstractAnimals class
		red_panda = Sound()
		red_panda.name = "Red Panda"
		red_panda.phylum = "Chordata"
		red_panda.cclass = "Mammalia"
		red_panda.order = "Carnivora"
		red_panda.family = "Ailuridae"
		red_panda.genus = "Ailurus"
		red_panda.url = "http://animaldiversity.ummz.umich.edu/collections/contributors/Kjeldsen_Per/Red_Panda7208/large.jpg"
		red_panda.alifespan = "The maximum lifespan of the red panda is 14 years, but the average is eight to ten."
		red_panda.habitat = "Red pandas live in temperate climates in deciduous and coniferous forests. There is usually an understory of bamboo and hollow trees. The average temperature is 10 to 25 degrees Celsius, and the average annual rainfall is 350 centimeters."
		red_panda.geolocation = "Red pandas are found throughout the Himalayan mountains between 2,200 and 4,800 meters in elevation in northern Burma, Nepal, Sikkim region of India, and the districts of western Sichuan and Yunnan in China. Their geographic range is bounded in the north by the Namlung Valley in the Mugo District and the Lake Rara region of northern Nepal, in the south by the Liakiang Range of western Yunnan, and the northern and eastern boundary is the upper Min Valley of western Sichuan."
		red_panda.sound = "Wieuw Wieuw"
		red_panda.update()

		# great_auk class that gets all the attributes from the AbstractAnimals class
		great_auk = Sound();
		great_auk.name = "Great Auk"
		great_auk.phylum = "Chordata"
		great_auk.cclass = "Aves"
		great_auk.order = "Charadriiformes"
		great_auk.family = "Alcidae"
		great_auk.genus = "Pinguinus"
		great_auk.url = "http://animaldiversity.ummz.umich.edu/collections/contributors/grzimek_birds/Alcidae/pinguinus_impennis/medium.jpg"
		great_auk.alifespan = "As in other large seabirds, annual survival is thought to have been relatively high. Estimated lifespan was from 20 to 25 years."
		great_auk.habitat = "In recorded history, great auks were found breeding only on isolated, rocky islands in the North Atlantic. They foraged in the open ocean when not breeding."
		great_auk.geolocation = "The last great auk was seen in 1852 off the Newfoundland Banks. They were extinct in the western Atlantic before 1800 and persisted a bit longer in some parts of the eastern Atlantic and off the coast of Iceland. They lived and bred on scattered, offshore islands in the northern Atlantic in recorded history, although it is possible they once occurred on continental coastlines but were extirpated from those areas earlier. They were found from Canada, Greenland, and Iceland to the British Isles and Scandinavia. Colonies in the western Atlantic may have been less numerous than in the eastern Atlantic. Archeological records indicate they once occurred as far south as southern Spain and New England in the United States, Pleistocene records indicate great auks occurred as far south as Italy and other parts of the Mediterranean. Great auks became extinct before any natural history studies were conducted, so little is known about their lives except for a few studies of lone, captive birds and the casual records of mariners."
		great_auk.sound = "Wrah Wrah"
		great_auk.update()

		# Leopard Cat class that gets all the attributes from the AbstractAnimals class
		leopard_cat = Sound()
		leopard_cat.name = "Blue Marlin"
		leopard_cat.phylum = "Chordata"
		leopard_cat.cclass = "Mammalia"
		leopard_cat.order = "Carnivora"
		leopard_cat.family = "Felidae"
		leopard_cat.genus = "Prionailurus"
		leopard_cat.url = "http://animaldiversity.ummz.umich.edu/collections/contributors/tanya_dewey/leopardcat/large.jpg"
		leopard_cat.alifespan = "In the wild, leopard cats have an average lifespan of about 4 years, and have been known to live up to 20 years in captivity. The lifespan of captive individuals varies greatly as individuals may die from the stress of transport. When leopard cats are released into non-native environments by breeders, they usually die not long after."
		leopard_cat.habitat = "Prionailurus bengalensis is found in tropical and temperate forests, coniferous forests, shrub land habitat, and grasslands. Its distribution is limited to areas with less than 10 cm of snow annually, and it is not found in steppe or arid climates. Prionailurus bengalensis has a fairly diverse diet and is able to find food in most habitats. It seems relatively impervious to human disturbance as populations in secondary growth and disturbed areas are stable and it is often found near agricultural fields and rural settlements. Prionailurus bengalensis is an exceptional swimmer, possibly explaining its distribution on islands, and is intolerant of temperatures above 35 C, possibly explaining its absence from central India. It is capable of living at higher elevations (i.e., 3000 m) with minimal snow fall."
		leopard_cat.geolocation = "Prionailurus bengalensis is one of the most widespread carnivore species in Asia, and can be found throughout most of southern Asia. Prionailurus bengalensis occupies eastern Afghanistan and northern Pakistan, northern and coastal India, Myanmar, Laos, Thailand, Indonesia, Malaysia, Vietnam, Taiwan, Sumatra, Java, Bali, Borneo, Nepal, Korea, Cambodia, parts of the Philippines, and Eastern China. Prionailurus bengalensis has been divided into a number of subspecies over its range that differ in coloration, pelage, body length, and reproductive cycles."	
		leopard_cat.sound = "Whish Whish"
		leopard_cat	.update()

		#Array with all the animals in it
		animals = [red_panda,great_auk,leopard_cat]
		
		self.response.write(page.head())
		if self.request.GET:
			indexAnimal = int(self.request.GET['animal']) #Grabs the index number out of the URL on the top of the browser
			self.response.write(page.content(animals[indexAnimal])) #fills the templating in with the index number 
		self.response.write(page.nav()) #Buttons on the page
		self.response.write(page.foot()) # Footer of the page. Currently blank		
class AbstractAnimals(object): #Sets the orginal class where the smaller classes take note from
    def __init__(self):
        self.name = ''
        self.phylum = ''
        self.cclass = ''
        self.order = ''
        self.family = ''
        self.genus = ''
        self.url = ''
        self.alifespan = ''
        self.habitat = ''
        self.geolocation = ''
        self.sound = ''
                
class Sound(AbstractAnimals): # makes a class Sound that is part of the Abstract Animal class
    def __init__(self):
		super(Sound, self).__init__()
		self.__soundText = self.sound
        
    @property #GETTER for the sound
    def soundGet(self):
		return self.__soundText

    def update(self): #Update function
		self.__soundText = self.__soundText.format(**locals())  

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
