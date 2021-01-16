**DNB (German National Library) norm data** are used to identify and compare the biographies and output of geographers, cartographers, printers, editors, and booksellers who contributed to printed works on European islands published in the Holy Roman Empire.

The relevant **search terms** for the "island" project are:

* Geograf
* Geograph
* Kartograf
* Kartograph
* Drucker
* Buchdrucker
* Verleger
* Buchhändler

The search is complicated by the fact that these tags or keywords are not used consistently throughout the datasets:

a) *Geograf* (modernised German spelling) and *Geograph* (traditional German spelling) are not synonymous but retrieve different results.

b) The hierarchy of search terms such as *Drucker* and *Buchdrucker* is not clear. While one would expect *Drucker* to be a broader category than *Buchdrucker*, not all items tagged *Buchdrucker* include *Drucker*. 

Metadata inconsistencies often reflect the acquisition process and can hardly be avoided in organically grown, large collections.

This is why as many variants as possible were used to find entries for early modern media entrepreneurs and do download the corresponding TTL files via web-automation.
The TTL files contain some explicit information (e.g. the names of people), whereas the majority of information is linked data that must be retrieved via DNB's URIs. A workflow to first select the prefixes of interest and to then access the URIs had to be developed: cf. [discussion on Stackoverflow](https://stackoverflow.com/questions/65748870/workflow-for-interpreting-linked-data-in-ttl-files-with-python-rdflib).

The **biographical information needed for the project** is:

* gndo:preferredNameForThePerson
* gndo:professionOrOccupation (linking to several URIs per person)
* gndo:geographicAreaCode
* gndo:biographicalOrHistoricalInformation (often overlaps with "occupation")
* gndo:placeOfBirth (e.g. <https://d-nb.info/gnd/4639387-0>)
* gndo:placeOfDeath (e.g. <https://d-nb.info/gnd/4267026-3>)
* gndo:gender (e.g. <https://d-nb.info/standards/vocab/gnd/gender#male>)
* gndo:dateOfBirth
* gndo:dateOfDeath





