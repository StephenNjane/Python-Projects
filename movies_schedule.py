current_movies = {'nice guy': '2023-10-01',
                   'bad guy': '2023-10-02',
                   'good guy': '2023-10-03',
                    'evil guy': '2023-10-04',
                    'hero': '2023-10-05',
                   'villain': '2023-10-06',}

print('These are the movies currently showing:')

for key in current_movies:
    print(key)

movies = input('Enter the movie you want to see the release date: ')

release_date = current_movies.get(movies)

if release_date == None:
    print('Sorry, that movie is not currently showing.')
else:
    print(f'The movie {movies} is showing on {release_date}.')
