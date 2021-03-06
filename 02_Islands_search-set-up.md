General island information on all islands / archipelagoes known in the early modern period are collected in a CSV table with the following columns:

|GeoNamesID|WikipediaID|IslandName|WikipediaLabel|LatGeonames|LongGeonames|GeodataWiki|ArchipelagoID|ArchipelagoName|Events|PubNumDE|PubNumEN|PubNumFR|PubNumLAT|etc.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|extracted via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|added manually as pseudo-XML|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|

The number of publications per language were extracted from Worldcat with Python Selenium to get a general overview of the importance of specific islands across space and time. For each search, HathiTrust displays the number of publications per language in filters on the first result page. Those filters could be used to create the various "PubNum" columns in the CSV table. Both mentions of an individual island and its archipelago were counted. All languages identified by HathiTrust were included in the statistics.

Problems to consider:

a) possible dublicates of entries
b) misattribution of publication languages


