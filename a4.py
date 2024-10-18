from games import game_db
from match import match
from typing import List, Tuple, Callable, Any

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
        if get_year(game) < year:
            result.append(get_title(game))
    return result

def title_after_year(matches: List[str]) -> List[str]:
    """Returns titles of games made after the passed-in year"""
    year = int(matches[0])
    result = []
    for game in game_db:
        if get_year(game) > year:
            result.append(get_title(game))
    return result

def year_by_title(matches: List[str]) -> List[str]:
    """Returns year of passed-in title of a game"""
    title = matches[0]
    result = []
    for game in game_db:
        if get_title(game) == title:
            result.append(get_year(game))
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

def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what games were made in _"), title_by_year),
    (str.split("what games were made between _ and _"), title_by_year_range),
    (str.split("what games were made before _"), title_before_year),
    (str.split("what games were made after _"), title_after_year),
    (str.split("when was % made"), year_by_title),
    (str.split("what games fall under %"), title_by_genre),
    (str.split("what games are developed by %"), title_by_developer),
    (str.split("who developed a game in _"), developer_by_year),
    (str.split("who developed a game under %"), developer_by_genre),
    (str.split("who developed %"), developer_by_title),
    (str.split("who was the developer of %"), developer_by_title),
    (str.split("what genres of games were developed in _"), genre_by_year),
    (str.split("what genre of game was developed by %"), genre_by_developer),
    (str.split("what is the genre of %"), genre_by_title),
    (["bye"], bye_action),
]

def search_pa_list(src: List[str]) -> List[str]:
    for pattern, action in pa_list:
        mat = match(pattern, src)
        # print(mat)
        if mat != None:
            result = action(mat)
            # print(result)
            if result == []:
                return ["No answers"]
            return result
    return ["I don't understand"]

def query_loop() -> None:
    print("Welcome to the video game database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)
        except(KeyboardInterrupt, EOFError):
            break
    print("\nGoodbye!\n")

query_loop()

