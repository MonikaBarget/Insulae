All items analysed and mapped in this project were collected in a custom [ZOTERO](zotero.org) library.

1) IMPORTING ITEMS

The import of items was carried out via **web automation**. I have I have written a **Python script** that automates my ZOTERO browser add-on in a personalised Google Chrome profile and allows me to add search results from WORLDCAT and other digital archives to a group library. 

2) MANAGING DUPLICATES

As several queries needed to be run, a considerable number of duplicates were retrieved. The most efficient way to eliminate duplicates from the same source was to store results as RIS files first and delete those with the same IT before import into ZOTERO. In order to exclude duplicates from different sources, search results were first imported to separate ZOTERO folders and then dragged and dropped into the main folder. In this way, ZOTERO could already identify some of the duplicates. Remaining duplicates were merged with the in-built ZOTERO duplicate management.

3) TAGGING

Tagging was unified manually via the ZOTERO **tag selector** and **PyZotero** scripts.

4) LINKING OF RELATED ITEMS

Related items (e.g. reprints or translations) were marked with special tags, using the unique **ZOTERO URI** to identify each item. For data analysis, this information coded in the tags could either be accessed via the **ZOTERO API** or via data dumps in various file formats.

5) Comparing imported data from WorldCat (and national catalogues) to full-text items in featured HathiTrust collections

In order to carry out meaningful text analysis, items frequently re-printed or translated had to be identified in the collected metadata. Full-texts could then be retrieved from services like the Bavarian State Library in Munich or HathiTrust. It was first necessary to compare full-texts items collected in featured HathiTrust collections to the metadata in Zotero to make sure that no important items had been missed. For this purpose, exported JSON metadata from HathiTrust could be mapped to CSL-JSON exports from Zotero.

*Structure of HathiTrust JSON files (2 sample items)*:

![img1](/Screenshots_INSULAE_data-issues/JSONstructure_HathiTrust.png)

*Structure of HathiTrust JSON files with collection metadata on top*:

![img2](/Screenshots_INSULAE_data-issues/JSONstructure_HathiTrust_CollectionInfo.png)



