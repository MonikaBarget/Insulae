General island information on all islands / archipelagoes known in the early modern period are collected in a CSV table with the following columns:

|GeoNamesID|WikipediaID|IslandName|WikipediaLabel|LatGeonames|LongGeonames|GeodataWiki|ArchipelagoID|ArchipelagoName|Events|PubNumDE|PubNumEN|PubNumFR|PubNumLAT|etc.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|extracted via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|added manually as pseudo-XML|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|

The number of publications per language were extracted from Worldcat with Python Selenium to get a general overview of the importance of specific islands across space and time. For each search, HathiTrust displays the number of publications per language in filters on the first result page. Those filters could be used to create the various "PubNum" columns in the CSV table. Both mentions of an individual island and its archipelago were counted. All languages identified by HathiTrust were included in the statistics.

Problems to consider:

a) possible dublicates of entries
b) misattribution of publication languages

In order to identify the best query structure, the following manual searches were carried out in Worldcat:

|Query|Number of all results between 1600 and 1800|Number of German results|Oldest result|
|---|---|---|---|
|kw: island OR insula |52722|1123|Riddarholmskyrkan från nordost, by Erik Dahlbergh, ca. 1600|
|kw: island|49237|982|Portraits of Juan Rodriguez Cabrillo and Sebastian Viscaino, ca.1540 & ca.1600|   
|su: island|15103|405|Samling af Kort af forskellige kartografer fra det 16. århundrede, 22: Saxonum regionis quatenus eius gentis ... [Danmark, syd], by Christian Sgorothenus et al., ca. 1600|   
|su: islands|15103|405|Samling af Kort af forskellige kartografer fra det 16. århundrede, 22: Saxonum regionis quatenus eius gentis ... [Danmark, syd], by Christian Sgorothenus et al., ca. 1600|
|su: island OR insula|15107|405|Samling af Kort af forskellige kartografer fra det 16. århundrede, 22: Saxonum regionis quatenus eius gentis ... [Danmark, syd], by Christian Sgorothenus et al., ca. 1600|
|su: insel|440|52|Polvs arcticvs siue tract[us] septentrionalis, by Matthias Quad and Johannes Bussemacher, Coloniæ/Köln: Ex officina typographica Jani Bussemechers, 1600|
|su: insel OR island|15522|455|Samling af Kort af forskellige kartografer fra det 16. århundrede, 22: Saxonum regionis quatenus eius gentis ... [Danmark, syd], by Christian Sgorothenus et al., ca. 1600|
|su: Zypern|5483|1044||
|su: Cyprus|47103|850||
|su: Crete|745|21|Candie. Par Beaulieu (Map, ca. 1600)|
|su: Creta|40|1|Candia, by Philippe Galle and Abraham Ortelius and Jan Baptista Vrients, Antuerpiae, apud Ioannem Bapt. Urientium, 1601|
|su: Candia|83|1|Spaggia della città di Candia (1612)|
|su: Islands Maps Early Works to 1800|2159|||
|su: insul OR insula OR isle OR insel OR island OR inseln OR insuln OR isola OR ilha|17554|538|Samling af Kort af forskellige kartografer fra det 16. århundrede, 22: Saxonum regionis quatenus eius gentis ... [Danmark, syd], by Christian Sgorothenus et al., ca. 1600|
|kw: insul OR insula OR isle OR insel OR island OR inseln OR insuln OR isola OR ilha|95376|7696|Riddarholmskyrkan från nordost, by Erik Dahlbergh, ca. 1600|
|ti: insul OR insula OR isle OR insel OR island OR inseln OR insuln OR isola OR ilha|59923|6598|Riddarholmskyrkan från nordost, by Erik Dahlbergh, ca. 1600|
|ti:/su: insul OR insula OR isle OR insel OR island OR inseln OR insuln OR isola OR ilha|58567|5391|Riddarholmskyrkan från nordost, by Erik Dahlbergh, ca. 1600|

Using island terms in different languages or island names as "subjects" (su:) retrieves lower and vastly different results.
"Keyword" searches (kw:) retrieve three times as many results, but here, too, the search language makes a difference.
Also, "keyword" searches in all fields including publication places:

> The charter granted by his Majesty, King Charles II, to the governor and company of the English colony of Rhode Island and Providence Plantations in New England in America.
Autor: Rhode Island.
Sprache: Englisch  
Verlag: Newport : Printed by S. Hall, 1767.

Books entitled "de insulis" can only be found via a direct title search.

The problem is that Latin titles do not have any keywords or tags at all. Missing metadata in the catalogues of the owning libraries also influence the search results.

This is why the "title" search (ti:) is the most reliable option of island terms from all relevant languages are included. If (ti:) is combined with (su:) through "OR", the results are again improved. As the statistics would be distorted if languages are counted although their island terms are NOT part of the (ti:) search, the analysis has to be limited to Germanic and Romanesque languages. 

Searches in German and English, however, retrieve more similar numbers.
