import requests
response = requests.get("https://whenisthenextmcufilm.com/api")
print(response)
print('\n')
if response.ok:
    # print(response.text)
    print('\n\n')
    film = response.json()
    print('When is the next MCU film?')
    print('\n')
    print(film['title'] + ' releases in')
    print(str(film['days_until']) + ' days!')
    print('Release Date: ' + film['release_date'])
    print('Production Type: ' + film['type'])
    print('What\'s afterwards? ' + film['following_production']['title'])

    print('\n\n')
    print(film['overview'])

else:
    print(f'{response.status.code}')

'''

'''
