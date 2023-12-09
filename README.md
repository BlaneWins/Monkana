# Monkana

A useful tool for translating Pokémon, aka Mons, or Pocket Monsters names in English to Japanese (Kana) for searching Japanese marketplaces for Pokémon related products!

This is done via webscraping the [Bulbapedia List of Pokémon Names](https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_Pokémon_names) page for names in both languages.

## Why is this necessary?

Pokémon is a Japanese franchise, and as such, the names of Pokémon first originate in Japanese. As a result, when 
searching for Pokémon related products on Japanese [marketplaces](https://buyee.jp/), it is often necessary to search for the Japanese 
name of the Pokémon because the English translations are not the same as their Japanese counterpart.

As of this moment Buyee JP supports auto translation of Pokémon names, but through testing, it is still no different 
from Google Translate which is not accurate.


## How does it work?

A list of Pokémon names in English and Japanese are scraped from the Bulbapedia page and stored in a dictionary. 
Logic is then used to input a Pokémon name in English and output the Japanese name.

## Roadmap

- [x] Create a scraped dictionary of Pokémon names in English and Japanese
- [ ] Persist the dictionary to a database
- [ ] Create a function that takes in a Pokémon name in English and outputs the Japanese name
- [ ] Automatically copy the Japanese name to the clipboard
- [ ] Package the function into a Google Chrome extension
- [ ] Add support for sealed Japanese products (i.e. booster packs, booster boxes, etc.)
- [ ] Add Pokemon sprites from the same Bulbapedia page to the dictionary and display them in the extension