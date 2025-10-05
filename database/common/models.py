from datetime import datetime

from peewee import *

db = SqliteDatabase('database.db')


class ModelBase(Model):
    created_at = DateField(default=datetime.now())

    class Meta:
        database = db


class SearchHistory(ModelBase):
    movie_name = CharField()
    description = TextField()
    rating = FloatField()
    year = IntegerField()
    genres = CharField()
    age_rating = IntegerField()
    poster_url = TextField()

    class Meta:
        db_table = 'search_history'


class FavoriteList(ModelBase):
    movie_name = CharField()
    description = TextField()
    rating = FloatField()
    year = IntegerField()
    genres = CharField()
    age_rating = IntegerField()
    poster_url = TextField()

    class Meta:
        db_table = 'favorite_films'


class WatchLater(ModelBase):
    movie_name = CharField()
    description = TextField()
    rating = FloatField()
    year = IntegerField()
    genres = CharField()
    age_rating = IntegerField()
    poster_url = TextField()

    class Meta:
        db_table = 'watch_later_list'