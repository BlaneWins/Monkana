from bs4 import BeautifulSoup, NavigableString, Tag
from selenium import webdriver
import statistics


def bulbapedia_pokemon_names_en():
    driver = webdriver.Chrome()
    driver.get("https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_Pok%C3%A9mon_names")

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Specify the target column index you want to retrieve (0-based index)
    target_column_index = 2  # Get values from the second column

    # Return values from the specified column for all rows
    data = [
        row.find_all('td')[target_column_index].text.strip().replace('\n', '')
        if len(row.find_all('td')) > target_column_index
        else '' # Replace None with an empty string for missing values
        for row in soup.find_all('tr')
    ]

    # Remove empty strings from the list
    data = list(filter(None, data))
    data = data[:-4]
    return data


def bulbapedia_pokemon_names_ja():
    driver = webdriver.Chrome()
    driver.get("https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_Pok%C3%A9mon_names")

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    response = soup.find_all("td", {"lang": "ja"})
    data = []

    for item in response:
        data.append((item.text.strip('\n')))

    return data


extracted_english = bulbapedia_pokemon_names_en()
# extracted_kana = bulbapedia_pokemon_names_ja()

print(extracted_english)
# print(extracted_kana)
