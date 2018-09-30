cities = {}
cities["Kabul"] = {
    "CountryCode": "AFG",
    "District": "Kabol",
    "Population": "1780000"
}
cities["Groningen"] = {
    "CountryCode": "NLD",
    "District": "Groningen",
    "Population": "172701"
}
cities["Biskra"] = {
    "CountryCode": "DZA",
    "District": "Biskra",
    "Population": "128281"
}
for cityname, city in cities.items():
    print("\ncity name:"+cityname)
    print("\tCountryCode:"+city["CountryCode"])
    print("\tDistrict:" + city["District"])
    print("\tPopulation:" + city["Population"])