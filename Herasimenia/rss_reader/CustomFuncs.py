'''
Custom functions container
'''

from argparse import ArgumentParser  # for reading console params
import os, sys  # some OS actions
import ast
import file_printer

try:
   import dateutil.parser  # some strange story - it's invisible for console start so will install it if needed
except:
   import subprocess
   subprocess.check_call([sys.executable, "-m", "pip", "install", 'python-dateutil'])


no_such_info = 'Information not presented by this portal.'
verbose = False
path = os.path.dirname(os.path.abspath(sys.argv[0]))
output_format = 0  # description of numbers in "LetItBe" func of "file_printer.py"
epub_name = pdf_name = html_name = ''
conv_needed = False  # if True will need conversion of news

def CanIRun():  # loading initial arguments
   '''
   Here loading initial arguments and seting runnign permissions & options
   '''
   terminate = False  # app terminate flag
   version_only = False  # version only flag
   date_param_set = False  # date param presented flag
   args = None
   global verbose, pdf_name, html_name, output_format, conv_needed

   try:  # try to load arguments and if not sucseed change app terminate flag for app termination
      inp_loader = ArgumentParser(description='Pure Python command-line RSS reader.')
      inp_loader.add_argument('source', nargs='?', type = str, help = 'RSS URL')
      inp_loader.add_argument('--version', action="store_true", help = 'Print version info')
      inp_loader.add_argument('--json', action="store_true", help = 'Print result as JSON in stdout')
      inp_loader.add_argument('--verbose', action="store_true", help = 'Outputs verbose status messages')
      inp_loader.add_argument('--limit', nargs='?', type = int, help = 'Limit news topics if this parameter provided')
      inp_loader.add_argument('--date', nargs='?', type = str, help = 'Date of publication of news in which you are interested')
      inp_loader.add_argument('--to-html', dest='html', nargs='?', type = str, help = 'Convertation to FileName.html - pls enter output file name w/o extention')
      inp_loader.add_argument('--to-pdf', dest='pdf', nargs='?', type = str, help = 'Convertation to FileName.pdf - pls enter output file name w/o extention')

      args = inp_loader.parse_args()
      verbose = args.verbose
      VerbosePrint('Loading arguments...Done')

      if args.source or args.version or args.date: 
         terminate = False
      else:
         terminate = True

      if args.html or args.pdf:
         conv_needed = True
         pdf_name = args.pdf
         html_name = args.html
         if args.html and args.pdf :
            output_format = 3
         elif args.html:
            output_format = 1
         elif args.pdf:
            output_format = 2

         
   except:
      terminate = True
   
   return (terminate, version_only, date_param_set, args)
   

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


def BlockParser(Page:str, source, limit:int = -1) -> dict:
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
   rss_feed = news_storage['RSSFeed'] = LineCleaner(divided_page[0], 1)
   rss_link = news_storage['RssLink'] = LineCleaner(divided_page[0], 2)
   rss_description = news_storage['RssDescription'] = LineCleaner(divided_page[0], 3)
   rss_lang = news_storage['RssLang'] = LineCleaner(divided_page[0], 4)
   rss_logo_url = news_storage['RssLogoUrl'] = LineCleaner(divided_page[0], 5)  
   
   VerbosePrint('....Done')
   VerbosePrint('Mutate news section....')    

   news_date_list = []  # list of already scaned dates
   news_cache_holder = []  # storage for cached b not saved news

   for id in range(1, limit+1):  # parsing news
      news_title = news_storage['title_' + str(id)] = LineCleaner(divided_page[id], 11)
      news_link = news_storage['link_' + str(id)] = LineCleaner(divided_page[id], 12)
      news_pubdate = news_storage['pubDate_' + str(id)] = dateutil.parser.parse(LineCleaner(divided_page[id], 13)).strftime('%Y%m%d')    
      news_source = news_storage['source_' + str(id)] = LineCleaner(divided_page[id], 14)
      news_category = news_storage['category_' + str(id)] =LineCleaner(divided_page[id], 15)
      news_description = news_storage['description_' + str(id)] =LineCleaner (divided_page[id], 16)
      news_media = news_storage['media_' + str(id)] = LineCleaner(divided_page[id], 17)

      VerbosePrint('Caching data....')

      if news_pubdate not in news_date_list:  # if it's a new date - we create it's storage
         InitialSubStorage(news_pubdate)
         news_date_list.append(news_pubdate)  # if current date not in already, add it there

         temp_news_holder = InitialTempNewsHolder(1, rss_feed, rss_link, rss_description, rss_lang, rss_logo_url)  # and initial new cache block
         temp_news_holder['title_1'] = news_title
         temp_news_holder['link_1'] = news_link
         temp_news_holder['pubDate_1'] = news_pubdate
         temp_news_holder['source_1'] = news_source
         temp_news_holder['category_1'] = news_category
         temp_news_holder['description_1'] = news_description
         temp_news_holder['media_1'] = news_media

         news_cache_holder.append({'date' : news_pubdate, 'rss_link' : LinkCleaener(source), 'data' : temp_news_holder})
         temp_news_holder.clear  

      elif news_pubdate in news_date_list:  # if date is already in list we reload it and update
         temp_news_holder = news_cache_holder[news_date_list.index(news_pubdate)]['data']
         current_id = str(int(temp_news_holder['capacity']) + 1) 

         temp_news_holder['title_' + current_id] = news_title
         temp_news_holder['link_' + current_id] = news_link
         temp_news_holder['pubDate_' + current_id] = news_pubdate
         temp_news_holder['source_' + current_id] = news_source
         temp_news_holder['category_' + current_id] = news_category
         temp_news_holder['description_' + current_id] = news_description
         temp_news_holder['media_' + current_id] = news_media   
         temp_news_holder['capacity'] = int(current_id)

         news_cache_holder[news_date_list.index(news_pubdate)]['data'] = temp_news_holder
         temp_news_holder.clear 

   VerbosePrint('....Done')

   for cache_frame in news_cache_holder:  # wen all scaned saving to files
      WritingCache(cache_frame['date'], cache_frame['rss_link'], cache_frame['data'])

   return news_storage  # cleaned dict w news


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
   
   if conv_needed:
      file_printer.LetItBe(output_format, news_storage, pdf_name, html_name, path)


def VerbosePrint(message):
   '''
   if Verbose param is set additional info prints
   '''
   if verbose:
      print(message)


def LinkCleaener(Link:str) -> str:
   '''
   no magic here just cleaning url
   '''
   if 'https://' in Link:
      return (Link[Link.index('https://') + 8 : -1][:Link[Link.index('https://') + 8 : -1].index('/')])
   elif 'http://' in Link:
      return (Link[Link.index('http://') + 7 : -1][:Link[Link.index('http://') + 7 : -1].index('/')])


def InitialStorage():  # used in rss_reader.py 
   '''
   Looking for local cache storage and create if didn't find it
   if not exests crate cache storage folder
   '''
   general_cache_dir = path + os.sep + 'CasheStorage'
   VerbosePrint("...let's check cache repo")     
   if not os.path.exists(general_cache_dir):
      try:
         VerbosePrint(f'...."{general_cache_dir}" never exists so was created')
         os.makedirs(general_cache_dir)
      except:
         VerbosePrint(f'...."{general_cache_dir}" never exists and wasn not created - so no cache')
         print('check util permissions!')
   else:
      VerbosePrint('....Done')  
       

def InitialSubStorage(subfolder:str):
   '''
   Looking for local cache subfolder and create if didn't find it
   if not exests crate cache storage subfolder
   '''
   VerbosePrint("...let's check cache repo subfolder")
   local_path = path + os.sep + 'CasheStorage' + os.sep + subfolder

   if not os.path.exists(local_path):
      try:
         VerbosePrint(f'...."{subfolder}" never exists so was created')
         os.makedirs(local_path)
      except:
         VerbosePrint(f'...."{subfolder}" never exists and wasn not created - so no cache')
         print('check util permissions!')
   else:
      VerbosePrint('....Done')  


def InitialTempNewsHolder(capacity, rss_feed, rss_link, rss_description, rss_lang, rss_logo_url) -> dict:
   '''
   creating empty dict w filled "head"
   '''
   temp_news_holder = {}
   temp_news_holder['capacity'] = capacity
   temp_news_holder['RSSFeed'] = rss_feed
   temp_news_holder['RssLink'] = rss_link
   temp_news_holder['RssDescription'] = rss_description
   temp_news_holder['RssLang'] = rss_lang 
   temp_news_holder['RssLogoUrl'] =  rss_logo_url
   return(temp_news_holder)


def WritingCache(news_pubdate: str, link: str, temp_news_holder: dict):  # saving loaded news to cache storage (limited by '--limit' param)
   '''
   Saving ours cache into files
   '''
   local_path = path + os.sep + 'CasheStorage' + os.sep 
   VerbosePrint("...let's save cache subfolder")

   try:
      cache_file = open((local_path + news_pubdate + os.sep + link + '.txt'), 'w', encoding = "utf-8")
      cache_file.write(str(temp_news_holder)) 
      cache_file.close
      VerbosePrint('....Caching data were saved')
   except:
      VerbosePrint(f'...."{news_pubdate}" never exists and wasn not created - so no cache')
      print('check util permissions!') 



def ScanForFiles(cache_path:str) -> list:
   file_list = []
   for root, dirs, files in os.walk(cache_path):  # looking for file list for specified date
      for filename in files:
         file_list.append(filename)
   return file_list


def LoadFromCache(cached_date: str, rss_url: str, as_json, limit):  # loading news from stored cache
   '''
   Here loading pre-cached data if user ask
   '''
   cache_path = path + os.sep + 'CasheStorage' + os.sep + cached_date

   if rss_url == 'no_url':  # w no_url we parse all urls stored in cache
      if not os.path.exists(cache_path):
         print('There is no such date in storage \nRe-check input or load w/o "--date" param first')
      else:
         temp_news_holder = {}
         file_list = ScanForFiles(cache_path)

         if len(file_list) == 1:
            cache_file = open(cache_path + os.sep + file_list[0], 'r', encoding = "utf-8")
            temp_news_holder = ast.literal_eval(cache_file.readline())
            cache_file.close
         
         else:
            cache_file = open(cache_path + os.sep + file_list[0], 'r', encoding = "utf-8")
            temp_news_holder = ast.literal_eval(cache_file.readline())  # it will be a main dict that holds loaded news
            cache_file.close

            temp_news_holder['RssLang'] = 'not applicable'
            temp_news_holder['RssLogoUrl'] = 'not applicable'

            for file_id in range(1, len(file_list)):
               news_counter = int(temp_news_holder['capacity'])  # also it will be a start point for new aded ids
               cache_file = open(cache_path + os.sep + file_list[file_id], 'r', encoding = "utf-8")
               fetched_news = (ast.literal_eval(cache_file.readline()))
               cache_file.close

               temp_news_id = news_counter + 1  # start id for aded news

               temp_news_holder['RSSFeed'] = temp_news_holder['RSSFeed'] + '\n' + fetched_news['RSSFeed']
               temp_news_holder['RssLink'] = temp_news_holder['RssLink'] + '\n' + fetched_news['RssLink']
               temp_news_holder['RssDescription'] = temp_news_holder['RssDescription'] + '\n' + fetched_news['RssDescription']

               for currend_id in range(1, int(fetched_news['capacity']) + 1):
                  temp_news_holder['title_' + str(temp_news_id)] = fetched_news['title_' + str(currend_id)]
                  temp_news_holder['link_' + str(temp_news_id)] = fetched_news['link_' + str(currend_id)]
                  temp_news_holder['pubDate_' + str(temp_news_id)] = fetched_news['pubDate_' + str(currend_id)]
                  temp_news_holder['source_' + str(temp_news_id)] = fetched_news['source_' + str(currend_id)]
                  temp_news_holder['category_' + str(temp_news_id)] = fetched_news['category_' + str(currend_id)]
                  temp_news_holder['description_' + str(temp_news_id)] = fetched_news['description_' + str(currend_id)]
                  temp_news_holder['media_' + str(temp_news_id)] = fetched_news['media_' + str(currend_id)]   
                  temp_news_id += 1
               
               temp_news_holder['capacity'] = news_counter + int(fetched_news['capacity'])
               
         if limit != None:  # checking "--limit" param
            if limit < temp_news_holder['capacity'] and limit > 0:
               temp_news_holder['capacity'] = limit
            elif limit > temp_news_holder['capacity']:
               print(f"Warning cached news count less that you request so we have only {temp_news_holder['capacity']} news for this time")

         Printer(temp_news_holder, as_json)

   else:
      url_cached = LinkCleaener(rss_url)
      file_list = ScanForFiles(cache_path)
      if (url_cached + '.txt') in file_list:
         cache_file = open(cache_path + os.sep + (url_cached + '.txt'), 'r', encoding = "utf-8")
         temp_news_holder = ast.literal_eval(cache_file.readline())
         cache_file.close
         if limit != None:  # checking "--limit" param
            if limit < temp_news_holder['capacity'] and limit > 0:
               temp_news_holder['capacity'] = limit
            elif limit > temp_news_holder['capacity']:
               print(f"Warning cached news count less that you request so we have only {temp_news_holder['capacity']} news for this time")

         Printer(temp_news_holder, as_json)
      else:
         print('There is no such cahce in storage \nRe-check input or load w/o "--date" param first')