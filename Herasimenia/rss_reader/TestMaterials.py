'''
test constants storage
this where ugly variables hides ))
'''

t_01_request = '<link>empty_sample_Link_&lt;_&lt;</link>'
t_01_responce = 'empty_sample_Link_<_<'

t_02_request = '<pubDate>some_random_pub_date_&pound;</pubDate>'
t_02_responce = 'some_random_pub_date_£'

t_03_request = 'some_random_value'
t_03_responce = 'Information not presented by this portal.'

t_04_request = '''<title>Yahoo News - Latest News & Headlines</title>
<link>https://www.yahoo.com/news</link>
<description>The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.</description>
<language>en-US</language>
<copyright>Copyright (c) 2021 Yahoo! Inc. All rights reserved</copyright>
<pubDate>Tue, 02 Nov 2021 11:56:11 -0400</pubDate>
<ttl>5</ttl>
<image>
<title>Yahoo News - Latest News & Headlines</title>
<link>https://www.yahoo.com/news</link>
<url>http://l.yimg.com/rz/d/yahoo_news_en-US_s_f_p_168x21_news.png</url>
</image>
<item>
<title>Judge starts Rittenhouse trial with trivia and lectures</title>
<link>https://news.yahoo.com/judge-starts-rittenhouse-trial-trivia-171749242.html</link>
<pubDate>2021-11-01T17:17:49Z</pubDate>
<source url="http://www.ap.org/">Associated Press</source>
<guid isPermaLink="false">judge-starts-rittenhouse-trial-trivia-171749242.html</guid>
<media:content height="86" url="https://s.yimg.com/uu/api/res/1.2/LgB3qIDbxCLhSDMya4_d5Q--~B/aD0zNDExO3c9NTExNjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/843cfc7e16b5c479a8cbd915c532218e" width="130"/>
<media:credit role="publishing company"/>
</item>
'''
t_04_responce = {'capacity': 1, 'RSSFeed': 'Yahoo News - Latest News & Headlines', 'RssLink': 'https://www.yahoo.com/news', 'RssDescription': 'The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.',
 'RssLang': 'en-US', 'RssLogoUrl': 'http://l.yimg.com/rz/d/yahoo_news_en-US_s_f_p_168x21_news.png', 'title_1': 'Judge starts Rittenhouse trial with trivia and lectures', 'link_1': 'https://news.yahoo.com/judge-starts-rittenhouse-trial-trivia-171749242.html',
 'pubDate_1': '2021-11-01T17:17:49Z', 'source_1': ' url="http://www.ap.org/">Associated Press', 'category_1': 'Information not presented by this portal.', 'description_1': 'Information not presented by this portal.',
 'media_1': 'https://s.yimg.com/uu/api/res/1.2/LgB3qIDbxCLhSDMya4_d5Q--~B/aD0zNDExO3c9NTExNjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/843cfc7e16b5c479a8cbd915c532218e'}


t_05_request = '''<title>Yahoo News - Latest News & Headlines</title>
<link>https://www.yahoo.com/news</link>
<fsdfe>en-US</language>
<copyright>Copyright (c) 2021 Yahoo! Inc. All rights reserved</copyright>
<psdfsdfl>5</ttl>
<image>
<ti#################ws - Latest News & Headlines</title>
<li#################ahoo.com/news</link>
<url>http://l.yimg.com/rz/d/yahoo_news_en-US_s_f_p_168x21_news.png</url>
</image>
<item>
<tfsd#################yahoo.com/judge-starts-rittenhouse-trial-trivia-171749242.html</link>
<pubDate>2021-11-01T17:17:49Z</pubDate>
<source url="http://www.ap.org/">Associated Press</source>
<guid i#################nhouse-trial-trivia-171749242.html</guid>
<medervvcdvps://s.yimg.com/uu/api/res/1.2/LgB3qIDbxCLhSDMya4_d5Q--~B/aD0zNDExO3c9NTExNjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/843cfc7e16b5c479a8cbd915c532218e" width="130"/>
<medi#################"publishing company"/>
</item>
'''
t_05_responce = {'capacity': 1, 'RSSFeed': 'Yahoo News - Latest News & Headlines', 'RssLink': 'https://www.yahoo.com/news', 'RssDescription': 'Information not presented by this portal.', 'RssLang': 'Information not presented by this portal.',
'RssLogoUrl': 'http://l.yimg.com/rz/d/yahoo_news_en-US_s_f_p_168x21_news.png', 'title_1': 'Information not presented by this portal.', 'link_1': 'Information not presented by this portal.', 'pubDate_1': '2021-11-01T17:17:49Z',
'source_1': ' url="http://www.ap.org/">Associated Press', 'category_1': 'Information not presented by this portal.', 'description_1': 'Information not presented by this portal.', 'media_1': 'Information not presented by this portal.'}