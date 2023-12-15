from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()

    if session_date:
        movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(movies_session_id: int) -> None:
    return MovieSession.objects.get(id=movies_session_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie = movie_id

    if cinema_hall_id:
        movie_session.cinema_hall = cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
