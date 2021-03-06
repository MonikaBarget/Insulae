**Why select this database?**

    *Contains all the records cataloged by OCLC member libraries.
    *Offers millions of bibliographic records.
    *Includes records representing 400 languages.
   
**Collecting search results**   
   
General island information on all islands / archipelagoes known in the early modern period are collected in a CSV table with the following columns:

|GeoNamesID|WikipediaID|IslandName|WikipediaLabel|LatGeonames|LongGeonames|GeodataWiki|ArchipelagoID|ArchipelagoName|Events|PubNumDE|PubNumEN|PubNumFR|PubNumLAT|etc.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|extracted via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|via webautomation|added manually as pseudo-XML|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|extracted from Worldcat result page|

The number of publications per language were extracted from Worldcat with Python Selenium to get a general overview of the importance of specific islands across space and time. For each search, HathiTrust displays the number of publications per language in filters on the first result page. Those filters could be used to create the various "PubNum" columns in the CSV table. Both mentions of an individual island and its archipelago were counted. All languages identified by HathiTrust were included in the statistics.

**Problems to consider:**

a) possible dublicates of entries
b) misattribution of publication languages

**HTML structure of language information on result list:**

```
<div id="SpracheRefinement">
<div class="head"><strong>Sprache</strong></div>
<ul class="refinement">

<li>
	    <a rel="nofollow" title="Englisch" href="/search?q=su%3AGreece+Crete.&dblist=638&fq=ln%3Aeng&qt=facet_ln%3A">Englisch</a> (4261)
	</li>

<li>
	    <a rel="nofollow" title="Neugriechisch [1453- ]" href="/search?q=su%3AGreece+Crete.&dblist=638&fq=ln%3Agre&qt=facet_ln%3A">Neugriechisch [1453- ]</a> (2183)
	</li>

<li>
	    <a rel="nofollow" title="Deutsch" href="/search?q=su%3AGreece+Crete.&dblist=638&fq=ln%3Ager&qt=facet_ln%3A">Deutsch</a> (877)
	</li>

<li>
```
**LINK TO MORE RESULTS IN DIFFERENT LANGUAGES:**

view-source:https://www.worldcat.org/search?q=su%3AGreece+Crete.&fq=&dblist=638&fc=ln:_50&qt=show_more_ln%3A&cookie

*ln:_150 shows all languages including Welsh and Church Slawonik!*

**URL structure of WorldCat query with several keywords:**

https://www.worldcat.org/search?q=kw%3Ainsul+OR+insula+OR+isle+OR+insel+OR+island+OR+inseln+OR+insuln+OR+isola&fq=yr%3A1600..1800+%3E&qt=advanced&dblist=638

**URL structure of WorldCat query with "subject" and "title" words:**

https://www.worldcat.org/search?q=su%3Aislands+OR+ti%3Ainsula&qt=advanced&dblist=638

**URLs of consecutive WorldCat result pages:**

https://www.worldcat.org/search?q=kw%3Ainsul+OR+insula+OR+isle+OR+insel+OR+island+OR+inseln+OR+insuln+OR+isola&fq=yr%3A1600..1800+%3E&dblist=638&start=01&qt=page_number_link

https://www.worldcat.org/search?q=kw%3Ainsul+OR+insula+OR+isle+OR+insel+OR+island+OR+inseln+OR+insuln+OR+isola&fq=yr%3A1600..1800+%3E&dblist=638&start=11&qt=page_number_link

https://www.worldcat.org/search?q=kw%3Ainsul+OR+insula+OR+isle+OR+insel+OR+island+OR+inseln+OR+insuln+OR+isola&fq=yr%3A1600..1800+%3E&dblist=638&start=21&qt=page_number_link

https://www.worldcat.org/search?q=kw%3Ainsul+OR+insula+OR+isle+OR+insel+OR+island+OR+inseln+OR+insuln+OR+isola&fq=yr%3A1600..1800+%3E&dblist=638&start=31&qt=page_number_link

etc. 

https://www.worldcat.org/search?q=kw%3Ainsul+OR+insula+OR+isle+OR+insel+OR+island+OR+inseln+OR+insuln+OR+isola&fq=yr%3A1600..1800+%3E&dblist=638&start=111&qt=page_number_link

etc.

https://www.worldcat.org/search?q=kw%3Ainsul+OR+insula+OR+isle+OR+insel+OR+island+OR+inseln+OR+insuln+OR+isola&fq=yr%3A1600..1800+%3E&dblist=638&start=231&qt=page_number_link

etc.

https://www.worldcat.org/search?q=kw%3Ainsul+OR+insula+OR+isle+OR+insel+OR+island+OR+inseln+OR+insuln+OR+isola&fq=yr%3A1600..1800+%3E&dblist=638&start=4991&qt=page_number_link

etc.

**5000 results max.**

**HTML structure of WorldCat result page:**

```<tr  class="menuElem">

<td class="num"><input type="checkbox" name="itemid" id="itemid_52654697" value="52654697"><label for="itemid_52654697" style="display:none">2. Die wüste Insel.</label></td>
   <td class="num">2.</td>

<td class="coverart">
<a href="/title/wuste-insel/oclc/52654697&referer=brief_results"> <img width="70" src="//coverart.oclc.org/ImageWebSvc/oclc/+-+24190170_70.jpg?SearchOrder=+-+OT,OS,TN,GO,FA"
     
                              title='Die wüste Insel. Autor: August Gottlieb Meissner'
                              alt='Die wüste Insel. Autor: August Gottlieb Meissner'
                          

       /></a>

  </td>
<td class="result details">
    <div class="oclc_number" data-source-collection="/XWC/">52654697</div>
    <div class="item_number">2</div>
<div class="name">
   <a id="result-2" href="/title/wuste-insel/oclc/52654697&referer=brief_results"><strong>Die wüste Insel.</strong></a>
     </div>

<div class="author">Autor: August Gottlieb Meissner</div><div class="type">
            <img class='icn' src='/wcpa/rel20200313/images/icon-bks.gif' alt=' ' height='16' width='16' >&nbsp;<span class='itemType'>Buch</span>&nbsp;<img class='icn' src='/wcpa/rel20200313/images/icon-mic.gif' alt=' ' height='16' width='16' >&nbsp;<span class='itemType'>Mikrofiche</span> : Mikrofiche<a href="/title/wuste-insel/oclc/52654697/editions?editionsView=true&referer=br"
                       title="Alle Ausgaben und Medienarten:"> Alle Medienarten und Sprachen anzeigen &raquo;</a>
                </div>
<div class="type language">Sprache: <span class="itemLanguage">Deutsch</span> &nbsp;</div><div class="publisher">Verlag: <span class="itemPublisher">Leipzig : [Verlag nicht ermittelbar], 1778.</span></div><!-- collection: /z-wcorg/ -->
<ul class="options">
  <li> <a href="/title/wuste-insel/oclc/52654697/editions?editionsView=true&referer=br" title="Alle Ausgaben und Medienarten:"> Alle Ausgaben anzeigen &raquo;</a></li>
        </ul>

	<div class="panel hidepanel" id="elpanel2"><p class="closepanel"><a href="javascript:void(0);" title="Close">Close</a></p></div>
 <div id="slice">
        <span class="Z3988" title="url_ver=Z39.88-2004&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&rft.genre=book&req_dat=%3Csessionid%3E&rfe_dat=%3Caccessionnumber%3E52654697%3C%2Faccessionnumber%3E&rft_id=info%3Aoclcnum%2F52654697&rft_id=urn%3AISBN%3A9783598518522&rft.aulast=Meissner&rft.aufirst=August&rft.btitle=Die+wu%C3%8C%C2%88ste+Insel.&rft.date=1778&rft.isbn=9783598518522&rft.place=Leipzig&rft.pub=%5BVerlag+nicht+ermittelbar%5D&rft.genre=book&rft_dat=%7B%22stdrt1%22%3A%22Book%22%2C%22stdrt2%22%3A%22Mic%22%7D"></span>
</div>
    <!-- Add "opacSaveMode" and "opacBypassMode" opts to Debug urls on the Brief
        results page.
    This helps with finding test records in WCLocal: Click on a lot of Debug
        links then grep the DR logs for your magic string in the saved opac
        response files.
 -->
</td>
</tr>```



