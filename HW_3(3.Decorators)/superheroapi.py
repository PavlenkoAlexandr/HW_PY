import requests


def find_hero(name, search):
    try:
        response = requests.get('https://www.superheroapi.com/api/2619421814940190/search/' + search)
        for data in (response.json()['results']):
            if data['name'] == name:
                return [name, data['powerstats']]
            else:
                return f'oops! {name} not found!'
    except KeyError:
        return 'Неверный поисковый запрос!'


def max_stats(*args, stat):
    compair_dict = dict()
    for arg in args:
        if type(arg) == list:
            compair_dict[arg[0]] = arg[1][stat]
    max_stat = sorted(compair_dict.items(), key=lambda x: x[1])[0]
    return max_stat


if __name__ == '__main__':
    captain_america = find_hero('Captain America', 'america')
    hulk = find_hero('Hulk', 'hulk')
    thanos = find_hero('Thanos', 'thanos')
    max_intelligence = max_stats(hulk, thanos, captain_america, stat='intelligence')
    print(max_intelligence)
