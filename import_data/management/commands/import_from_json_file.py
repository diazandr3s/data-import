"""
Import json data from JSON file to Datababse
"""
import os
import json
from import_data.models import Movie
from django.core.management.base import BaseCommand
from datetime import datetime
from data_import.settings import BASE_DIR


class Command(BaseCommand):
    def import_movie_from_file(self):
        data_folder = os.path.join(BASE_DIR, 'import_data', 'resources/json_file')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    title = data_object.get('title', None)
                    url = data_object.get('url', None)
                    release_year = datetime.now()

                    try:
                        movie, created = Movie.objects.get_or_create(
                            title=title,
                            url=url,
                            release_year=release_year
                        )
                        if created:
                            movie.save()
                            display_format = "\nMovie, {}, has been saved."
                            print(display_format.format(movie))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this movie: {}\n{}".format(title, str(ex))
                        print(msg)


    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.import_movie_from_file()

