# How to get (non-English) Wikipedia page titles from Wikidata Id?
# script based on: https://stackoverflow.com/questions/37079989/how-to-get-wikipedia-page-from-wikidata-id

with open ("C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\9_INSULAE\\Entity_list.txt", "r", encoding="utf-8") as f:
    wikidata_ids=f.read().splitlines()
    print(wikidata_ids[:5])
    print(type(wikidata_ids))
    
def get_wikipedia_titles_from_wikidata_id(wikidata_id, lang='en', debug=False):
    import requests
    from requests import utils
    print(wikidata_id)
    url = (
        'https://www.wikidata.org/w/api.php'
        '?action=wbgetentities'
        '&props=sitelinks/urls'
        f'&ids={wikidata_id}'
        '&format=json')
    json_response = requests.get(url).json()
    if debug: print(wikidata_id, url, json_response) 

    entities = json_response.get('entities')    
    if entities:
        entity = entities.get(wikidata_id)
        if entity:
            sitelinks = entity.get('sitelinks')
            print(type(sitelinks)) # TYPE IS DICTIONARY
            print(sitelinks)
            for sitelink in sitelinks:
                for title, name in sitelink:  # for name, age in dictionary.iteritems():  (for Python 2.x)
                    if time == search_name:
                        print(name)
    return None   

for wikidata_id in wikidata_ids:
    get_wikipedia_titles_from_wikidata_id(wikidata_id, lang="en")