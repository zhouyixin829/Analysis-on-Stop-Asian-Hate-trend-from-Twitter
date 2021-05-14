import twitter
import json
import datetime

username = 'yuxinli121@gmail.com'
password = '784951lyx'
CONSUMER_KEY = 'xNr1WbSrqZO5U4qWu2y5MiyX7'
CONSUMER_SECRET = 'u7IN0Zx0IL0zegwQwxXMEGmySdW0fRjQij9bf1Ap9MZeUE6qjB'
OAUTH_TOKEN = '1310683540678414336-zUz6tFUqGtnEQGxnDVjhyECVJMdQV8'
OAUTH_TOKEN_SECRET = 'rKZ6YHZ3zN0aN5g8Fqugr62x2GuRCcQYUGtJcyrqxpipM'


def oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET):
    # XXX: Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://developer.twitter.com/en/docs/basics/authentication/overview/oauth
    # for more information on Twitter's OAuth implementation.
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


def twitter_search(twitter_api, q, max_results, **kw):
    # See https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
    # and https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators
    # for details on advanced search criteria that may be useful for
    # keyword arguments

    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
    search_results = twitter_api.search.tweets(q=q, count=100, **kw)
    # print(search_results)
    statuses = search_results['statuses']

    # Enforce a reasonable limit
    max_results = min(1000, max_results)

    for _ in range(30):  # 10*100 = 1000
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e:  # No more results when next_results doesn't exist
            break

        # Create a dictionary from next_results, which has the following form:
        # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs = dict([kv.split('=')
                       for kv in next_results[1:].split("&")])

        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']

        if len(statuses) > max_results:
            break

    return statuses


def main(twitter_api, location, keywords, max_results=10):
    result = []
    for keyword in keywords:
        q = f"({keyword}) lang:en"  # place_country:23424977
        try:
            results = twitter_search(twitter_api, q, max_results=max_results, geocode=f'{location},100mi')
        except Exception as e:
            continue
        result += [{'text': x['text'], 'username': x['user']['name'], 'user_id': x['user']['id'],
                  'created_at': x.get('created_at')} for x in results]
    return result


twitter_api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
keywords = {
    'positive': ['MyAsianAmericanStory', 'StopAAPIHate', 'StopAsianHate', 'StopAsianHateCrimes', 'AsianLivesMatter', 'AsiansAreHuman', 'EndAsianHate', 'protectasianlives', 'IAmNotAVirus', 'WashTheHate', 'RacismIsAVirus', 'IAmNotCovid19', 'BeCool2Asians', 'ActToChange', 'HateIsAVirus'],
    'objective': ['AAPIwomen', 'AAPIMonth', 'aapihm', 'AAPIHeritageMonth', 'JusticeForYao', 'jarrodpowell', 'YaoPanMa', 'asianhate', 'antiasian', 'AsianVoices', 'Asiansolidarity'],
    'negative': ['CCPVirus', 'chinaVirus', 'ChinaVirus', 'ChineseVirus', 'WuhanVirus', 'communistVirus', 'Chinese virus', 'ChineseBioterrorism', 'slant eye', 'slopehead', 'ting tong', 'wuhan virus', 'wuhanflu', 'wuhanvirus', 'dog eater', 'gook eyed', 'chink', 'rice nigger', 'ching chong', 'Chonky', 'Kung-fu virus', 'Chinaman', 'Ching-Chong', 'Dog-Eater', 'chinavirusoutbreak', 'wuhancoronavirus', 'Wuhanlabs']
}

max_results = 100
locations = {'Santa_Fe': '35.67,-105.97',
             'Little_Rock': '34.7361,-92.3311',
             'Raleigh': '35.818889,-78.644722',
             'Bismarck': '46.8133, -100.7789',
             'Columbus': '39.983333,-82.983333',
             'Oklahoma_City': '35.4823,-97.5352',
             'Salem': '44.930833,-123.028889',
             'Philadephia': '39.9528,-75.1636',
             'Providence': '41.8,-71.4',
             'Columbia': '34.0006,-81.0442'
             }
for city, location in locations.items():
    for _type, keys in keywords.items():
        result = main(twitter_api, location, keys, max_results)
        print(len(result))
        for one in result:
            print(one)
        with open(f'{city}_{_type}.json', 'w+', encoding='utf-8')as f:
            f.write('{"data":[' + ",".join([json.dumps(x) for x in result]) + ']}')
