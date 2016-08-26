
import math

h = 6.626e-34
G = 6.67e-11
c = 3*10e+8 		
epsilon = 0.1
kappa = .665e-26 / 1.6726219e-27 #what

print " "
print "Hello this program finds various things related to Schwarzchild's radius"
print " "
print "For example, mass of sun is 1.989E30, mass of earth is 5.972E24."
print "Sagittarius A* is 7.956e+36."
print " "
print "To find radius (meters) from given mass (kg), enter 'mass_to_radius_schwarz(input)'"
print " "
print "To find mass (kg) from given radius (meters), enter 'radius_to_mass(input)'"
print " "
print "To find maximum rate of schwarzchild radius growth from given mass enter... "
print " 'mass_to_edd_schwar_rad(input)'"
print " "
print "To find de Broglie wavelength, enter, deBroglie(input)"
print " "


def mass_to_radius_schwarz(mass):
	radius = (2*G*(mass))/(c**2)
	#return str(radius) + " meters"
	return "{0:g} meters".format(radius)

def radius_to_mass(radius):
	mass_2 = ((radius)*(c**2))/(2*G)
	return str(mass_2) + " kilograms"

#calculate the max schwarz rad from max...
#Eddington accretion rate from a given mass
def mass_to_edd_schwar_rad(mass):
	radius = ((2*G)/(c**2)) * (math.pi * 4 * G * mass)/(epsilon * kappa * c)
	return str(radius) + " meters/second"
	
def deBroglie(x):
    Lambda = (h / x)
    return Lambda

