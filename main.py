import requests
import random

#7438
page = random.randint(1, 7438)
#page = 2
pageSize = 1
url = f'https://api.disneyapi.dev/character?pageSize={pageSize}&page={page}'
response = requests.get(url)
# response = requests.get("https://api.disneyapi.dev/character")

#print(response)
#print('\n')

if response.ok:
    character = response.json()['data']

    print(f'Персонаж: {character["name"]}')

    s = character['films']
    if len(s) > 0 :
        print('Фільми:')
    for film in s:
        print(f'     {film}')

    s = character['shortFilms']
    if len(s) > 0:
        print('Короткометражки:')
    for film in s:
        print(f'     {film}')

    s = character['tvShows']
    if len(s) > 0:
        print('ТВ шоу:')
    for film in s:
        print(f'     {film}')

    s = character['videoGames']
    if len(s) > 0:
        print('Відеоігри:')
    for film in s:
        print(f'     {film}')

    s = character['parkAttractions']
    if len(s) > 0:
        print('Атракціони:')
    for film in s:
        print(f'     {film}')

else:
    print('Щось пішло не так...')
    print(f'{response.status.code}')

'''коротометражок, серіалів та ігор,'''
'''
shortFilms
tvShows
videoGames
parkAttractions
'''


