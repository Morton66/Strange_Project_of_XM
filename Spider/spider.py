import urllib.request
import ssl
import re
class Spider(object):
	"""docstring for Spider"""
	def __init__(self, arg):
		#super(Spider, self).__init__()
		self.start_url = arg	
		self.website="https://www.zchome.cn/book/22218/"
		self.start=True
		self.count=0
		#self.list_table=[]
	def check(self,num):
		pattern=re.compile(r'[0-9]+_[0,1,2,3]?')
		a=pattern.match(num)
		if a==None:
			return True
		else:
			return False
	def context_parse(self,text):
		#print(isinstance(text,str))
		#print('111')
		text=text.replace('<br />',"").replace("&nbsp;&nbsp;&nbsp;&nbsp;","").replace("<br />","\n").replace("<br /","")
		#print(self.list_table[self.count])
		f=open('{}.txt'.format(self.stitle[self.count]),'a')
		f.write(text)
		#f.save()
		f.close()
		#print(text)
	def loadpage(self,site=None):
		if self.start==True:
			url=self.start_url
		else:	
			if self.check(site)==True:
				self.other_page_find(site)
			url=self.website+site+'.html'
		html=self.html_load(url)
		self.context_split(html)	

		#print(url)
	def html_load(self,url):
		user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
		headers={'User-Agent': user_agent}
		#print('111')
		req=urllib.request.Request(url,headers=headers)
		response=urllib.request.urlopen(req)
		#获取每个网页的html代码
		html=response.read().decode('gbk')
		return html
		#print(html)
	def context_split(self,html):
		if self.start==True:
			pattern=re.compile(r'<a.*?href="/book/22218/(.*?).html".*?title=".*?">(.*?)</a></dd>',re.S)
			list_of_table=pattern.findall(html)
			#print('111')
			list_of_table.pop(0)
			
			table=[]
			title=[]
			for i in list_of_table:
				p=list(i)
				table.append(p[0])
				'''
				m='第七卷朝天子 第一百一十三章 君臣相见可能安?'
				print(isinstance(p[1],str))
				if p[1]==m
					p[1]=p[1].replace("\?","l")
					print(p[1])
				'''
				p[1]=p[1].replace("?","？")
				#print(p[1])
				title.append(p[1])
			self.stable=table
			self.stitle=title
			f=open('html.txt','w')
			f.write(str(list_of_table))
			f.close()
			#print(self.stable)
			#print(list(list_of_table[0])[0])
			#print(isinstance(list(list_of_table[0])[0],str))
		else:
			pattern=re.compile(r'<div.*?class="panel-body".*?id="htmlContent">(.*?)<br>',re.S)
			contest=pattern.findall(html)
			self.context_parse(contest[0])
			#print(contest)
	def control_spider(self):
		while True:
			if self.start==True:				
				self.loadpage()
				self.start=False
				#print('11')
			else:
				#print('555')
				try:
					for i in self.stable:
						#self.contest=[]
						self.loadpage(i)
						self.count+=1
						print(self.count,"  ",self.stitle[self.count])
				except Exception as e:
					print(e)
					break
	def other_page_find(self,web_site):
		for i in range(2,10):
			url=self.website+web_site+'_'+str(i)+'.html'
			html=self.html_load(url)
			pattern=re.compile(r'<div.*?class="panel-body".*?id="htmlContent">(.*?)<br>',re.S)
			contest=pattern.findall(html)
			if contest !=None and contest !=['\n']:
				self.stable.append(web_site+'_'+str(i))
				self.stitle.append(self.stitle[self.count])
				#print(contest)
				f=open('html.txt','a')
				f.write('   '+str(web_site+'_'+str(i)))
				f.close()
			else:
				break


if __name__=='__main__':
	spider=Spider('https://www.zchome.cn/book/22218.html')

	spider.control_spider()