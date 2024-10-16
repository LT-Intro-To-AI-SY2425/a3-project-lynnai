from games import game_db
from match import match
from typing import List, Tuple

# projection functions

def get_title(game: Tuple[str, str, str, int]) -> str:
    return game[0]

def get_developer(game: Tuple[str, str, str, int]) -> str:
    return game[1]

def get_genre(game: Tuple[str, str, str, int]) -> str:
    return game[2]

def get_year(game: Tuple[str, str, str, int]) -> int:
    return game[3]

#action functions

def title_by_year(matches: List[str]) -> List[str]:
    """ Returns titles of games made in the passed-in year """
    year = int(matches[0])
    result = []
    for game in game_db:
        if get_year(game) == year:
            result.append(get_title(game))
    return result

def title_by_year_range(matches: List[str]) -> List[str]:
    """ Returns titles of games made in-between passed-in years"""
    start_year = int(matches[0])
    end_year = int(matches[1])
    result = []
    for game in game_db:
        if start_year <= get_year(game) <= end_year:
            result.append(get_title(game))
    return result

def title_before_year(matches: List[str]) -> List[str]:
    """ Returns titles of games made before the passed-in year"""
    year = int(matches[0])
    result = []
    for game in game_db:
        if get_year(game) > year:
            result.append(get_title(game))
    return result

def title_by_genre(matches: List[str]) -> List[str]:
    """ Returns titles of games that match the passed-in genre"""
    genre = matches[0]
    result = []
    for game in game_db:
        if get_genre(game) == genre:
            result.append(get_title(game))
    return result

def title_by_developer(matches: List[str]) -> List[str]:
    """ Returns titles of games made by passed-in developer"""
    developer = matches[0]
    result = []
    for game in game_db:
        if get_developer(game) == developer:
            result.append(get_title(game))
    return result

def developer_by_year(matches: List[str]) -> List[str]:
    """Returns developers that created games in passed-in year"""
    year = int(matches[0])
    result = []
    for game in game_db:
        if get_year(game) == year:
            result.append(get_developer(game))
    return result

def developer_by_genre(matches: List[str]) -> List[str]:
    """Returns developers that created games of passed-in genre"""
    genre = matches[0]
    result = []
    for game in game_db:
        if get_genre(game) == genre:
            result.append(get_developer(game))
    return result

def developer_by_title(matches: List[str]) -> List[str]:
    """Returns developers that created game named by the passed-in title """
    title = matches[0]
    result = []
    for game in game_db:
        if get_title(game) == title:
            result.append(get_developer(game))
    return result

def genre_by_year(matches: List[str]) -> List[str]:
    """Returns genre of games made in the passed-in year"""
    year = int(matches[0])
    result = []
    for game in game_db:
        if get_year(game) == year:
            result.append(get_genre(game))
    return result

def genre_by_developer(matches: List[str]) -> List[str]:
    """Returns genre of game made by the passed-in developer"""
    developer = matches[0]
    result = []
    for game in game_db:
        if get_developer(game) == developer:
            result.append(get_genre(game))
    return result

def genre_by_title(matches: List[str]) -> List[str]:
    """Returns genre of the game with a passed-in title"""
    title = matches[0]
    result = []
    for game in game_db:
        if get_title(game) == title:
            result.append(get_genre(game))
    return result