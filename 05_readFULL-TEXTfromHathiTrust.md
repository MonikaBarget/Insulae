## Advantages of full-text search in HathiTrust

HathiTrust does not only offer a catalogue search but full-text search which may be combined with searches in fields like title or subject. In this way, HathiTrust can retrieve a variety of relevant non-monograph publications that are generally not captured by searched in other bibliographic databases.

## Use / build featured collections

Furthermore, HathiTrust permits users (incl. guests) to build public and private collections of items. Subsequent queries can then be run within such collections, and it is also possible to download the collection metadata in two different file formats for data analysis.

For my research, I am building several collections on island publications:

1) [INSULAE (EUROPE)](https://babel.hathitrust.org/cgi/mb?a=listis;c=1751299776)

Description:

This collection contains European works on islands / insularity printed between 1600 & 1800. Works in Romanesque, Germanic & Celtic languages are added first. Greek, Slawonic, Turkish works etc. will follow in a 2nd step.

Query URL: 

https://babel.hathitrust.org/cgi/ls?a=srchls;q1=eil%C3%A2n%20eilannen%20eilean%20eileanan%20%C3%AEles%20%C3%AEles%20ilha%20ilhas%20isla%20islas%20insel%20insul%20inseln%20insuln%20insulen%20Insel%20Inselen%20insula%20insulae%20insul%C4%83%20insule%20isla%20ysla%20isle%20isles%20isola%20isole%20%22%C3%B6%22%20%C3%B6ar%20%22%C3%B8%22%20%C3%B8er%20oile%C3%A1n%20oile%C3%A1in%20%C3%B8y%20%C3%B8yer%20%20island%20isle%20%20eiland%20eilanden%20ynys%20ynysoedd;field1=ocronly;anyall1=any;q2=eil%C3%A2n%20eilannen%20eilean%20eileanan%20%C3%AEles%20%C3%AEles%20ilha%20ilhas%20isla%20islas%20insel%20insul%20inseln%20insuln%20insulen%20Insel%20Inselen%20insula%20insulae%20insul%C4%83%20insule%20isla%20ysla%20isle%20isles%20isola%20isole%20%22%C3%B6%22%20%C3%B6ar%20%22%C3%B8%22%20%C3%B8er%20oile%C3%A1n%20oile%C3%A1in%20%C3%B8y%20%C3%B8yer%20geography%20geographie%20geographia%20cartography%20cartographie%20cartographia%20%20island%20isle%20%20eiland%20eilanden%20ynys%20ynysoedd;field2=title;anyall2=any;op2=AND;q3=eil%C3%A2n%20eilannen%20eilean%20eileanan%20%C3%AEles%20%C3%AEles%20ilha%20ilhas%20isla%20islas%20insel%20insul%20inseln%20insuln%20insulen%20Insel%20Inselen%20insula%20insulae%20insul%C4%83%20insule%20isla%20ysla%20isle%20isles%20isola%20isole%20%22%C3%B6%22%20%C3%B6ar%20%22%C3%B8%22%20%C3%B8er%20oile%C3%A1n%20oile%C3%A1in%20%C3%B8y%20%C3%B8yer%20%20island%20isle%20%20eiland%20eilanden%20ynys%20ynysoedd;field3=ocronly;anyall3=any;q4=eil%C3%A2n%20eilannen%20eilean%20eileanan%20%C3%AEles%20%C3%AEles%20ilha%20ilhas%20isla%20islas%20insel%20insul%20inseln%20insuln%20insulen%20Insel%20Inselen%20insula%20insulae%20insul%C4%83%20insule%20isla%20ysla%20isle%20isles%20isola%20isole%20%22%C3%B6%22%20%C3%B6ar%20%22%C3%B8%22%20%C3%B8er%20oile%C3%A1n%20oile%C3%A1in%20%C3%B8y%20%C3%B8yer%20geography%20geographie%20geographia%20cartography%20cartographie%20cartographia%20%20island%20isle%20%20eiland%20eilanden%20ynys%20ynysoedd;field4=subject;anyall4=all;op4=AND;op3=OR;yop=between;pdate_start=1600;pdate_end=1800;pn=1"

## Extract full-text from HathiTrust

Full-text pages are stored in HTML tags that contain "ocr-word" as class value.

Cf. the sample page: (LINK)

Files can be downloaded as HTML, converted to XHTML and read with XQuery.

Alternatively, the HTML files can be analysed with BeautifulSoup in Python: plain text can be written to separate .txt files for further analysis.
