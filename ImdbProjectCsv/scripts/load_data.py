from MovieDataApp.models import Genre, MovieData
import csv
from datetime import datetime

def run():
    with open('scripts/IMDb-movies.csv') as file:
        reader = csv.reader(file)
        next(reader)
        Genre.objects.all().delete()
        MovieData.objects.all().delete()
        for row in reader:
            print(row)
            if ',' in row[4]:
                genres = row[4].split(',')
                movieData = MovieData(
                    imdb_title_id = row[0],
                    original_title = row[1],
                    year = row[2],
                    date_published = datetime.strptime(row[3],'%Y-%m-%d').date(),
                    duration = row[5],
                    language = None if row[6] == None else row[6],
                    description = row[7],
                    reviews_from_user = row[8] if row[8] != '' else None,
                    reviews_from_critics = row[9] if row[9] != '' else None
                )
                movieData.save()
                for i in genres:
                    genre, _ = Genre.objects.get_or_create(genreName = i)
                    movieData.genre.add(genre)
                movieData.save()
            else:
                movieData = MovieData(
                    imdb_title_id = row[0],
                    original_title = row[1],
                    year = row[2],
                    date_published = datetime.strptime(row[3],'%Y-%m-%d').date(),
                    duration = row[5],
                    language = None if row[6] == None else row[6],
                    description = row[7],
                    reviews_from_user = row[8] if row[8] != '' else None,
                    reviews_from_critics = row[9] if row[9] != '' else None
                )
                movieData.save()
                genre, _ = Genre.objects.get_or_create(genreName = row[4])
                movieData.genre.add(genre)
                movieData.save()