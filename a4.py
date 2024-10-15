from games import games_db
from match import match
from typing import List, Tuple

def get_title(game: Tuple[str, str, str, int]) -> str:
    return game[0]

def get_developer(game: Tuple[str, str, str, int]) -> str:
    return game[1]

def get_genre(game: Tuple[str, str, str, int]) -> str:
    return game[2]