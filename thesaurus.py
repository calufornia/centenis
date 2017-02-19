from urllib2 import Request, urlopen

api_key = 'ad74d3ccf397694429ae145c20db06cc'  # DO NOT CHANGE
version = '2'  # DO NOT CHANGE
base_url = 'http://words.bighugelabs.com/api/{}/{}/{}/'

syn = 'syn'  # Hardcoded in due to output format from API


def is_synonym(nym):
    return nym == syn


def get_synonyms(word):
    synonym_list = [word]
    url = base_url.format(version, api_key, word)
    request = Request(url)
    response = urlopen(request)
    result = response.read()
    nyms = result.split('\n')
    for line in range(len(nyms) - 1):
        nym = nyms[line].split('|')
        print(nym)
        if is_synonym(nym[1]):
            synonym_list += [nym[2]]
    return synonym_list
