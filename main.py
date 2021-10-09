import requests

data = requests.get("https://covid-api.mmediagroup.fr/v1/cases")

d = data.json()

#Ask for an input 
print("Enter a place")
country = input("What country are you looking for?")
#Capitalize the first letter of the country from input 


#Captialize only does first letter in string
#Title capitalizes each first letter in words in a string 
country = country.title()
print (country)
if country == "United States":
  country = "US"

if country == "South Korea":
  country = "Korea, South"
#Same thing for South Korea


print(country)
for x in d:
#Compare the input with x (which is list of countries )
  if country == x:

    print("Confirmed cases", x, ":",d.get(x).get("All").get("confirmed"))





#Get the percentage of confirmed cases with the population.
#confirmed cases
#population
#A fraction of total amount to determine 
#proportion = from fraction to decimal 
#percentage = from decimal(proportions) * 100 


#percentage  = confirmed / population * 100 
 
#*****per capita******

#Percentage by per capita 