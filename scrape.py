import firebase_admin
from bs4 import BeautifulSoup
from firebase_admin import credentials, db
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_Pok%C3%A9mon_names")


def bulbapedia_pokemon_names_en():
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Specify the target column index you want to retrieve
    english_col_index = 2

    # Return values from the specified column for all rows
    data = [
        row.find_all('td')[english_col_index].text.strip().replace('\n', '')
        if len(row.find_all('td')) > english_col_index
        else '' # Replace None with an empty string for missing values
        for row in soup.find_all('tr')
    ]

    # Remove empty strings and last table from the list
    data = list(filter(None, data))
    data = data[:-4]
    return data


def bulbapedia_pokemon_names_ja():
    # Scrape kana by using the lang attribute for japanese 'ja'
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    response = soup.find_all("td", {"lang": "ja"})
    data = []

    for item in response:
        data.append((item.text.strip('\n')))

    return data


extracted_english = bulbapedia_pokemon_names_en()
extracted_kana = bulbapedia_pokemon_names_ja()

extracted_english = tuple(key.encode('ascii', 'ignore').decode('ascii').replace("'", '').replace('.', '')
                          .replace(' ', '_') for key in extracted_english)

print(extracted_english)
print(extracted_kana)

combined_names = dict(zip(extracted_english, extracted_kana))

print(combined_names)

cred = credentials.Certificate('monkana_secret_key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://monkana-7420d-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')

ref.set(combined_names)