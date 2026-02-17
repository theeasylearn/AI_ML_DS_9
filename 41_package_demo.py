#import module 
from world.africa import country as af 
from world.europe import country as eu 
from world.asia import country as ai 

#call getCountry function of africa subpackage
print(af.getCountries())
#call getCountry function of europe subpackge
print(eu.getCountries())
#call getCountry function of asia subpackge
print(ai.getCountries())