## [Iteration 1] One-shot command-line RSS reader.
# RSS reader should be a command-line utility which receives [RSS](wikipedia.org/wiki/RSS) URL and prints results in human-readable format.

# You are free to choose format of the news console output. The textbox below provides an example of how it can be implemented:

# ```shell
# $ rss_reader.py "https://news.yahoo.com/rss/" --limit 1

# Feed: Yahoo News - Latest News & Headlines

# Title: Nestor heads into Georgia after tornados damage Florida
# Date: Sun, 20 Oct 2019 04:21:44 +0300
# Link: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html

# [image 2: Nestor heads into Georgia after tornados damage Florida][2]Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged
# homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve
# off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its
# march across a swath of the U.S. Southeast.

# Links:
# [1]: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html (link)
# [2]: http://l2.yimg.com/uu/api/res/1.2/Liyq2kH4HqlYHaS5BmZWpw--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en/ap.org/5ecc06358726cabef94585f99050f4f0 (image)

# ```
# Utility should provide the following interface:
# ```shell
# usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
#                      source

# Pure Python command-line RSS reader.

# positional arguments:
#   source         RSS URL

# optional arguments:
#   -h, --help     show this help message and exit
#   --version      Print version info
#   --json         Print result as JSON in stdout
#   --verbose      Outputs verbose status messages
#   --limit LIMIT  Limit news topics if this parameter provided
# ```

# In case of using `--json` argument your utility should convert the news into [JSON](https://en.wikipedia.org/wiki/JSON) format.
# You should come up with the JSON structure on you own and describe it in the README.md file for your repository or in a separate documentation file.


# With the argument `--verbose` your program should print all logs in stdout.

### Task clarification (I)

# 1) If `--version` option is specified app should _just print its version_ and stop.
# 2) User should be able to use `--version` option without specifying RSS URL. For example:
# ```
# > python rss_reader.py --version
# "Version 1.4"
# ```
# 3) The version is supposed to change with every iteration.
# 4) If `--limit` is not specified, then user should get _all_ available feed.
# 5) If `--limit` is larger than feed size then user should get _all_ available news.
# 6) `--verbose` should print logs _in the process_ of application running, _not after everything is done_.
# 7) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout_.
# 8) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout in JSON format_.
# 9) It is preferrable to have different custom exceptions for different situations(If needed).
# 10) The `--limit` argument should also affect JSON generation.

##############################################################################################################

from argparse import ArgumentParser # for reading console params
from requests import get  # linking with web


'''
RSS urls for tests:
   https://news.yahoo.com/rss/
   https://www.space.com/feeds/all
   https://www.wired.com/category/science/feed
   https://www.liga.net/tech/technology/rss.xml
   https://news.yandex.ru/society.rss
   https://www.trend.az/rss/trend_all_ru.rss

'''

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


def printer(news_storage: dict, is_json = False):
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

      VerbosePrint('So here your json....')
      print(json)  # outputed form of json was checked on "http://jsonviewer.stack.hu/", description is in "Json description.txt"


def VerbosePrint(message):
   if args.verbose:
      print(message)

terminate = False  # app terminate flag

try:  # try to load arguments and if not sucseed change app terminate flag for app termination
   inp_loader = ArgumentParser(description='Pure Python command-line RSS reader.')
   inp_loader.add_argument('source', nargs='?', type = str, help = 'RSS URL')
   inp_loader.add_argument('--version', action="store_true", help = 'Print version info')
   inp_loader.add_argument('--json', action="store_true", help = 'Print result as JSON in stdout')
   inp_loader.add_argument('--verbose', action="store_true", help = 'Outputs verbose status messages')
   inp_loader.add_argument('--limit', nargs='?', type = int, help = 'Limit news topics if this parameter provided')
   args = inp_loader.parse_args()
   VerbosePrint('Loading arguments...Done')
   if args.source: 
      terminate = False
   else:
      terminate = True
 
except:
   terminate = True


if terminate == False:

   VerbosePrint('Loading constants...')
   current_version = 'Version 1.0'
   no_such_resource = 'The resource you trying to connect is not responding or does not exists.'
   no_such_info = 'Information not presented by this portal.'
   VerbosePrint('...Done')

   if args.version: # if version requested - have no needs to other actions
      print(current_version)
   else:
      arguments = inp_loader.parse_args()
      url = arguments.source
   
      VerbosePrint(f'Connecting attempt to {url}...')

      if get(url).status_code != 200:
         VerbosePrint('...Connection attempt failed')
         print(no_such_resource)
      else:
         VerbosePrint('...Connection attempt succeed')
         RssPage = get(url).text

         VerbosePrint("OK, let's parse it...")

         if not arguments.limit:
            Output = BlockParser(RssPage)
         else:
            Output = BlockParser(RssPage, arguments.limit)
            
         VerbosePrint('...Done')

      VerbosePrint('We start the printer, everything will be fine...')
      printer(Output, args.json)

elif terminate == True:
   print('Parameters reading failed... \nSee --help for input format')