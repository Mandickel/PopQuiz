import random

african_capitals = {
    "Algeria": "Algiers",
    "Angola": "Luanda",
    "Benin": "Porto-Novo",
    "Botswana": "Gaborone",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Cabo Verde": "Praia",
    "Cameroon": "Yaoundé",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Comoros": "Moroni",
    "Democratic Republic of the Congo": "Kinshasa",
    "Republic of the Congo": "Brazzaville",
    "Djibouti": "Djibouti",
    "Egypt": "Cairo",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Eswatini": "Mbabane",
    "Ethiopia": "Addis Ababa",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Ghana": "Accra",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Côte d'Ivoire": "Yamoussoukro",
    "Kenya": "Nairobi",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Mali": "Bamako",
    "Mauritania": "Nouakchott",
    "Mauritius": "Port Louis",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Namibia": "Windhoek",
    "Niger": "Niamey",
    "Nigeria": "Abuja",
    "Rwanda": "Kigali",
    "Sao Tome and Principe": "São Tomé",
    "Senegal": "Dakar",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Somalia": "Mogadishu",
    "South Africa": "Pretoria",
    "South Sudan": "Juba",
    "Sudan": "Khartoum",
    "Tanzania": "Dodoma",
    "Togo": "Lomé",
    "Tunisia": "Tunis",
    "Uganda": "Kampala",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"
}
countries = list(african_capitals.keys())
Score = 0
for i in [1,2,3,4,5]:
    country = random.choice(countries)
    city = african_capitals[country]

    Answer = input("What is the capital city of " + country + "?")

    if city == Answer:
        Score = Score + 1
        print("That is correct! the capital city of " + country + " is " + city)
    else:
        Score = Score + 0
        print("That is wrong! the capital city of " + country + " is not " + Answer + ",please try again!")

print("Game Over! Your Score is:" + str(Score) + "/5")  

