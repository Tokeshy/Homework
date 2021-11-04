'''
Custom functions container
'''

no_such_info = 'Information not presented by this portal.'
verbose = False

def LineCleaner(line :str, property_id :int) -> str:
   '''
   clearing parameters depending on the scaned type and also from non-printable characters

   description for Dict id params (property_dict dict):
      general id section:
         1 - RSS page feed
         2 - RSS page link
         3 - RSS page description (optional)
         4 - RSS language (optional)
         5 - RSS logo image link (optional)
      news id section:
         11 - title of the news
         12 - link of the news
         13 - publication date of the news
         14 - source url, used if news page locate on remote (not RSS) server - optional parameter 
         15 - news category - opttional parameter
         16 - description  - opttional parameter of news category
         17 - media:content - link to media content - opttional parameter
   '''

   VerbosePrint('Loading ID codes....')

   property_dict = {1 : '<title>', 2 : '<link>', 3 : '<description>', 4: '<language>', 5 : '<url>',
               11 : '<title>', 12 : '<link>', 13 : '<pubDate>', 14 : '<source', 15 : '<category>',
               16 : '<description>',}

   VerbosePrint('....Done')  
   VerbosePrint('Loading non-printable characters....')          

   substitution_dict = {'&quot;' : '"', '&#34;' : '"', '&amp;' : '&', '&#38;' : '&', '&lt;' : '<', 
                       '&#60;' : '<', '&gt;' : '>', '&#62;' : '>', '&hellip;' : '…', '&#8230;' : '…',
                       '&prime;' : '′', '&#8242;' : '′', '&Prime;' : '″', '&#8243;' : '″', '&ndash;' : '–',
                       '&#8211;' : '–', '&mdash;' : '—', '&#8212;' : '—', '&lsquo;' : '‘', '&#8216;' : '‘',
                       '&rsquo;' : '’', '&#8217;' : '’', '&sbquo;' : '‚', '&#8218;' : '‚', '&ldquo;' : '“',
                       '&#8220;' : '“', '&rdquo;' : '”', '&#8221;' : '”', '&bdquo;' : '„', '&#8222;' : '„',
                       '&laquo;' : '«', '&#171;' : '«', '&raquo;' : '»', '&#187;' : '»', '&nbsp;' : ' ',
                       '&#160;' : ' ', '&pound;' : '£', '&#163;' : '£', '&euro;' : '€', '&#8364;' : '€',
                       '&para;' : '¶', '&#182;' : '¶', '&sect;' : '§', '&#167;' : '§', '&copy;' : '©',
                       '&#169;' : '©', '&reg;' : '®', '&#174;' : '®', '&trade;' : '™', '&#8482;' : '™',
                       '&deg;' : '°', '&#176;' : '°', '&plusmn;' : '±', '&#177;' : '±', '&frac14;' : '¼',
                       '&#188;' : '¼', '&frac12;' : '½', '&#189;' : '½', '&frac34;' : '¾', '&#190;' : '¾',
                       '&times;' : '×', '&#215;' : '×', '&divide;' : '÷', '&#247;' : '÷', '&fnof;' : 'ƒ',
                       '&#402;' : 'ƒ', '&#39;':"'"}

   VerbosePrint('....Done')  
   VerbosePrint(f'Scaning & replacing non-printable characters of id_{property_id}....')  

   for key, value in substitution_dict.items():  # Cleaning of non-printable characters - it's not a BS4 just cause don't sure that it's really need to import it
      line = line.replace(key, substitution_dict[key])

   VerbosePrint('....Done') 
   VerbosePrint(f'Parcing id_{property_id} info....')  

   if property_id != 17:  # wrapper of media link is different that other ones
      try:
         value = line[(line.index(property_dict[property_id]) + len(property_dict[property_id])) : (line.index(property_dict[property_id].replace('<', '</')))]
         if len(value) <= 1:
            value = no_such_info
      except:
         value = no_such_info
      finally:
         VerbosePrint('....Done') 
         return value
   else:  # reading media content
      try:
         value = (line[(line.index('<media:content height="') + 23) : (line.index('width="'))])
         value = value[(value.index('" url="') + 7) : -2]
         if len(value) <= 1:
            value = no_such_info
      except:
         value = no_such_info
      finally:
         VerbosePrint('....Done') 
         return value


def BlockParser(Page:str, limit:int = -1) -> dict:
   '''
   receiving the page as str and news limit as int, after which we form the heading part and the news list
   Using '<item>' as item separator and if there no limit (limit == -1) - reading all of the news 
   '''

   VerbosePrint('Setting splitter....')  

   divided_page = Page.split('<item>')  
   if limit == -1: 
      limit = Page.count('<item>')
   elif limit > Page.count('<item>'):
      limit = Page.count('<item>')
   
   VerbosePrint('....Done')
   VerbosePrint('Mutate "Head"....')  

   news_storage = {}  # grabbing general "head" info
   news_storage['capacity'] = limit
   news_storage['RSSFeed'] = LineCleaner(divided_page[0], 1)
   news_storage['RssLink'] = LineCleaner(divided_page[0], 2)
   news_storage['RssDescription'] = LineCleaner(divided_page[0], 3)
   news_storage['RssLang'] = LineCleaner(divided_page[0], 4)
   news_storage['RssLogoUrl'] = LineCleaner(divided_page[0], 5)  
   
   VerbosePrint('....Done')
   VerbosePrint('Mutate news section....')    

   for id in range(1, limit+1):  # parsing news
      news_storage['title_' + str(id)] = LineCleaner(divided_page[id], 11)
      news_storage['link_' + str(id)] = LineCleaner(divided_page[id], 12)
      news_storage['pubDate_' + str(id)] = LineCleaner(divided_page[id], 13)
      news_storage['source_' + str(id)] = LineCleaner(divided_page[id], 14)
      news_storage['category_' + str(id)] =LineCleaner(divided_page[id], 15)
      news_storage['description_' + str(id)] =LineCleaner (divided_page[id], 16)
      news_storage['media_' + str(id)] = LineCleaner(divided_page[id], 17)

   VerbosePrint('....Done')

   return news_storage


def Printer(news_storage: dict, is_json = False):
   '''
   print news depending on what print parameters we need.
   in this part it's possible to understand wat happens
   by reading VerbosePrint's texts, first comes "head" of 
   output and in "for lines in range" fill news container
   '''
   limit = news_storage['capacity']

   VerbosePrint('Spelling into readable....')
   VerbosePrint('....Forming news separator....')

   if news_storage['capacity'] <= 1:
      news_separator = ''
   elif not is_json:
      news_separator = '******************' + '\n'
   elif is_json:
      news_separator = ',\n    {'
   
   VerbosePrint('....Done')

   if not is_json:  # if it's not a Json
      VerbosePrint("Well..json wasn't selected, start printing head....")

      print('\n' + 'Feed: ' + news_storage['RSSFeed'] + '\n')
      VerbosePrint('....Done')
      for lines in range(1, news_storage['capacity'] + 1):
         VerbosePrint(f'Printing news - {lines} of {limit} ....')  

         print('Title: ' + news_storage['title_' + str(lines)])
         print('Date: ' + news_storage['pubDate_' + str(lines)])
         print('Link: ' + news_storage['link_' + str(lines)])
         additional_links = '\n' +'Links:' + '\n' + '  [1] ' + news_storage['link_' + str(lines)] + ' (link)' + '\n'

         if no_such_info not in news_storage['source_' + str(lines)]:
            source_link = news_storage['source_' + str(lines)]
            link_it_selfs = source_link[source_link.index('"') + 1 : source_link.index('">')]  # Cleaning to Link itselfs
            source_description = source_link[source_link.index('">') +2 : ]  # Getting source description
            additional_links += '  [2] ' + link_it_selfs + ' (Source - ' + source_description +')' + '\n'

         if no_such_info not in news_storage['media_' + str(lines)]:
            additional_links += '  [3] ' + news_storage['media_' + str(lines)] + ' (Media content)' + '\n'
         
         VerbosePrint('....Done\nAdditional links section....')
         print(additional_links)
         print(news_separator)
         VerbosePrint('....Done\n')

   if is_json:  # if json was selected 
      VerbosePrint('Well..forming json....')
      json = ('{\n  "Page feed": "' + news_storage['RSSFeed'] + '",\n' + '  "Page link": "' + news_storage['RssLink'] + 
               '",\n  "Page description (optional)": "' + news_storage['RssDescription'] + '",\n  "Language (optional)": "' + 
               news_storage['RssLang'] + '",\n  "Logo image link (optional)": "' + news_storage['RssLogoUrl'] + '",\n ' +
               ' "News": [ \n   {\n')
      VerbosePrint('...."Head" done')

      for lines in range(1, news_storage['capacity'] + 1):
         VerbosePrint(f'Printing news - {lines} of {limit} ....')  
         if no_such_info not in news_storage['source_' + str(lines)]:
            source_link = news_storage['source_' + str(lines)]
            link_it_selfs = source_link[source_link.index('"') + 1 : source_link.index('">')] 
         else:
            link_it_selfs = no_such_info 

         json += ('    "Title": "' + news_storage['title_' + str(lines)] + '",\n    "Date": "' + news_storage['pubDate_' + str(lines)] +
                 '",\n    "Link": "' + news_storage['link_' + str(lines)] + '",\n    "All links" : {\n      "News link": "' + 
                 news_storage['link_' + str(lines)] + '",\n      "Source link": "' + link_it_selfs + '",\n      "Media content": "'+
                 news_storage['media_' + str(lines)] + '"\n'+ '    }\n    }')

         if lines < int(news_storage['capacity']) :
            json += news_separator
         elif lines == int(news_storage['capacity']):
            json += '\n]\n}'
         
         VerbosePrint('....Done')

      VerbosePrint('So here is your json....')
      print(json)  # outputed form of json was checked on "http://jsonviewer.stack.hu/", description is in "Json description.txt"


def VerbosePrint(message):
   if verbose:
      print(message)