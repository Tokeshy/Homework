'''
That's the place for file creation and convertation
'''

import os, sys  # some OS actions
import CustomFuncs


def LetItBe(output_format: int, data_to_save: dict, pdf_name: str, html_name: str, curent_path: str):
   '''
   takes file type, file name, dict w data, current system path.
   as the easiest way to create PDf first we create html,
   then convert to PDF (if needs) 

   output_format explications:
   1 - html
   2 - pdf
   3 - html + pdf
   '''
   CustomFuncs.VerbosePrint('creating temp file...')
   generated_html = GenHtml(data_to_save, curent_path)

   CustomFuncs.VerbosePrint('scan inp format type...')
   if output_format == 1 :
      try:
         os.rename(generated_html, curent_path + os.sep + html_name +'.html')
         print(f'Output file was generated as {html_name}')
      except:
         print(f"File playing error - check util permissions!\nCan't create file {html_name}")
   else: 
      try:
         CustomFuncs.VerbosePrint('trying import convertapi...')
         import convertapi
      except:
         CustomFuncs.VerbosePrint('....Faild\n Try to install then import...')
         try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", 'convertapi'])
         except:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", 'convertapi'])
            CustomFuncs.VerbosePrint('....Done')
      
      #CustomFuncs.VerbosePrint('creating temp file...')   
      generated_pdf = curent_path + os.sep + pdf_name +'.pdf'

      try:
         convertapi.api_secret = 'YSxRXaPLxLaCKjfL'  # it's a demo so not a real "secret"
         (convertapi.convert('pdf', { 'File': generated_html })).file.save(generated_pdf)
      except:
         print(f"For some reason can't save {pdf_name}\nCheck util permissions!")
         
      if output_format == 2:
         os.remove(generated_html)
         print(f'Output file was generated as {pdf_name}')
         #delete html and quit
      elif output_format == 3:
         print(f'Output files was generated as {pdf_name} and {html_name}')


def GenHtml(data_to_save: dict, curent_path: str) -> str :
   '''
   It may looks like a cheating, but html +\- = txt
   so we just create temp file and write there ours future html
   and if needs we will kill it later

   Hm,i wonder which is worse - dragging a file junk with templates, or re-inventing the wheel..
   So only reviewer will say
   don't forget to clean up your eyes with holy water..after all of this )))
   '''
   CustomFuncs.VerbosePrint('....Generating HTML "head"...')

   file_holder =[]  # it's here we put future html
    
   capacity = str(data_to_save['capacity'])
   rss_feed = str(data_to_save['RSSFeed'])
   rss_link = str(data_to_save['RssLink'])
   rss_description = str(data_to_save['RssDescription'])
   rss_lang = str(data_to_save['RssLang'])
   rss_media = str(data_to_save['RssLogoUrl'])

   #generating news head
   file_holder.append('<!DOCTYPE html>')
   file_holder.append('<html>')
   file_holder.append('<head>')
   file_holder.append('	<title>Some ugly html creator ever create this</title>')
   file_holder.append('</head>')
   file_holder.append('<body>')

   file_holder.append('<table align="center" border="1" cellpadding="1" cellspacing="1" style="width:480px">')
   file_holder.append('<caption>News that can be printed, yet</caption>')
   file_holder.append('<tbody>')
   file_holder.append('<tr>')
   file_holder.append('<td>')

   file_holder.append(f'<p><strong>All the news we found </strong>-&nbsp;&nbsp;{capacity}</p>')
   file_holder.append(f'<p><strong>Feed(s) is (are):&nbsp;</strong>{rss_feed}</p>')
   file_holder.append(f'<p><strong>Link(s):&nbsp;</strong> &nbsp;{rss_link}</p>')
   file_holder.append(f'<p><strong>Description(s):&nbsp;</strong>{rss_description}</p>')
   file_holder.append(f'<p><strong>Rss lang is (if it&#39;s not a multi-resourced)&nbsp;</strong>-&nbsp;&nbsp; &nbsp;{rss_lang}</p>')
   file_holder.append(f'<p><strong>and the logo</strong>))</p>')
   file_holder.append(f'<p><img alt="{rss_media}" src="{rss_media}" style="float:left; height:32px; width:32px" /></p>')
   file_holder.append('</tr>')

   CustomFuncs.VerbosePrint('....Done')
   CustomFuncs.VerbosePrint('....Generating HTML "News section"...')

   for currend_id in range(1, int(data_to_save['capacity']) + 1):  # news forming loop
      file_holder.append('<tr>')
      file_holder.append('<td>')

      news_title = str(data_to_save['title_' + str(currend_id)])
      news_link = str(data_to_save['link_' + str(currend_id)])
      news_pub_date = str(data_to_save['pubDate_' + str(currend_id)])
      news_source = str(data_to_save['source_' + str(currend_id)])
      news_category = str(data_to_save['category_' + str(currend_id)])
      news_description = str(data_to_save['description_' + str(currend_id)])
      news_media = str(data_to_save['media_' + str(currend_id)])

      file_holder.append(f'<p><strong>Title: {news_title}</strong></p>')
      file_holder.append(f'<p><strong>News link -&nbsp;<a href="{news_link}" target="_blank">source</a>&nbsp; &nbsp;&nbsp;</strong></p>')
      file_holder.append(f'<p><strong>News publication date - {news_pub_date}&nbsp;</strong>&nbsp;</p>') 
      file_holder.append(f'<p><strong>News category - {news_category}</strong></p>')
      file_holder.append(f'<p><strong>News description - {news_description}</strong></p>')
      file_holder.append('<p><strong>Media:&nbsp;</strong></p>')
      file_holder.append(f'<p><img alt="{news_media}" src="{news_media}" style="float:left; height:180px; width:180px" /></p>')

      file_holder.append('</td>')
      file_holder.append('</tr>')

   CustomFuncs.VerbosePrint('....Done')
   CustomFuncs.VerbosePrint('....Finishing HTML works...')
   file_holder.append('</tbody>')
   file_holder.append('</table>')
   file_holder.append('<p>&nbsp;</p>')
   file_holder.append('</body>')
   file_holder.append('</html>')
   CustomFuncs.VerbosePrint('....Done')

   temp_html = curent_path + os.sep + 'TempT.html' 

   CustomFuncs.VerbosePrint('Writing....')

   with open(curent_path + os.sep + 'TempT.txt', 'w') as temp_file:
      for line in file_holder:
         temp_file.write(line + '\n')
   temp_file.close

   if os.path.exists(temp_html):
      try:
         os.remove(temp_html)
      except:
         print('File playing error - check util permissions!')
   
   try:
      os.rename(curent_path + os.sep + 'TempT.txt', temp_html)
      CustomFuncs.VerbosePrint('....Done')
   except:
      print('File playing error - check util permissions!')
   
   return temp_html
