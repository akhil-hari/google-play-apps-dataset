import requests
from bs4 import BeautifulSoup as bs
import sys
import re
from pprint import pprint

#################################################
#################################################
####### Written by Akhil Hari         ###########
####### https://github.com/akhil-hari ###########
#################################################
#################################################



'''

#### This function collects details of an app by scrapping the google play page of the app using its app_id.

'''

def app_details(id_string):
	baseUrl="https://play.google.com/store/apps/details?id="
	
	details={'id':'','name':'','developer':'','category':'','category_id':'','rating':0,'number_ratings':0,'Installs':'0+','updated':'','current_version':'0.0.0','content_rating':'','size':'0B'}
	try:
		page=requests.get(baseUrl+id_string)
		if page.status_code==200:
			#print(id_string+' :200 0k')
			soup=bs(page.content,"html.parser")
			details['id']=id_string
			details['name']=soup.find('h1',class_='AHFaub').find('span').get_text()
			details['developer']=soup.find_all('a',class_=['hrTbp','R8zArc'])[0].get_text()
			details['category']=soup.find_all('a',class_=['hrTbp','R8zArc'])[1].get_text()
			details['category_id']=soup.find_all('a',class_=['hrTbp','R8zArc'])[1]['href'].split('/')[4]
		
			if (soup.find('div',class_='pf5lIe')!=None) and (soup.find('span',class_=['AYi5wd','TBRnV'])!=None):
				details['rating']=soup.find('div',class_='pf5lIe').find_all('div')[0]['aria-label'].split()[1]
				details['number_ratings']=soup.find('span',class_=['AYi5wd','TBRnV']).find_all('span')[0].get_text()
			else:
				details['rating']='0'
				details['number_ratings']='0'
				
				
			adnl_table=soup.find('div',class_='IxB2fe').find_all('div')
	
	
			for i in adnl_table:
		
				if i.find('div',class_="BgcNfc")!=None:
				
					if i.find('div',class_="BgcNfc").get_text()=='Installs':
	
						details['Installs']=i.find('span','htlgb').get_text()
					elif i.find('div',class_="BgcNfc").get_text()=='Updated':
						details['updated']=i.find('span','htlgb').get_text()
					elif i.find('div',class_="BgcNfc").get_text()=='Current Version':
						details['current_version']=i.find('span','htlgb').get_text()
					
					elif i.find('div',class_="BgcNfc").get_text()=='Content Rating':
						details['content_rating']=i.find('div','IQ1z0d').find_all('div')[0].get_text()
						
					
					elif i.find('div',class_="BgcNfc").get_text()=='Size':
		
						details['size']=i.find('span','htlgb').get_text()
			
					else:
						continue
			return details
		elif page.status_code==404:
			print('\n\t\033[1;31;48mSearch on '+id_string+' returned a 404(Not Found) on google play\033[1;37;0m\n\n');
			return None
		else:
			print('\n\n\t\033[1;31;48mPage returned an invalid response: '+str(page.status_code)+'\033[1;37;0m\n\n')
			return None
	
					
	except requests.exceptions.ConnectionError as e:
		print('\n\t\033[1;31;48mUnable to connect to the server try again.\033[1;37;0m\n')
		return None
			
	
		
'''

#### This function lists app_ids of related apps by scrapping the google play page of the app .

'''		

def list_ids(id_string):
	startURL="https://play.google.com/store/apps/details?id="+id_string
	result=set()
	try:
		page=requests.get(startURL)
		soup=bs(page.content,'html.parser')
		for a in soup.find_all('a',href=re.compile('id=[a-z_]+\.[a-z_]+[a-z._]*')):
			result.add(a['href'].split('=')[1])
		
		return result
		
	except requests.exceptions.ConnectionError as e:
		print('\n\n\t\033[1;31;48mPage returned an invalid response: '+str(page.status_code)+'\033[1;37;0m\n\n')
		return None





if __name__=='__main__':
	url='com.google.android.googlequicksearchbox'
	try:
		url=sys.argv[1]
	except BaseException:
		pass
		
	details_result=app_details(url)
	list_result=list_ids(url)
	
	print('\n\n\nDetails of App\n\n')
	if details_result :
		pprint(details_result)
	else:
		print('\t\033[1;31;48mSomething Went Wrong While Collecting Details\033[1;37;0m\n')
	
	print('\n\n\nApp_ids of other related apps.\n\n')
	if list_result :
		pprint(list_result)
	else:
		print('\t\033[1;31;48mSomething Went Wrong While Listing \033[1;37;0m\n')
	
