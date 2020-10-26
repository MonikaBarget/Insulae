# taken from https://pypi.org/project/wikimapper/

from wikimapper import WikiMapper

# Map Wikipedia page title to Wikidata id

mapper = WikiMapper("index_enwiki-latest.db")
wikidata_id = mapper.title_to_id("Python_(programming_language)")
print(wikidata_id) # Q28865

# Map Wikipedia URL to Wikidata id

mapper = WikiMapper("index_enwiki-latest.db")
wikidata_id = mapper.url_to_id("https://en.wikipedia.org/wiki/Python_(programming_language)")
print(wikidata_id) # Q28865

# Map Wikidata id to Wikipedia page title

mapper = WikiMapper("index_enwiki-latest.db")
titles = mapper.id_to_titles("Q183")
print(titles) # Germany, Deutschland, ...
