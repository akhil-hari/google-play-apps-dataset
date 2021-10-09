# App Details Dataset Sample (Google Play)
This is a collection of 20165 random apps listed on google.
play store
## Dataset Description
The dataset consists of apps  distributed across following 49 categories.
```
+---------------------+----------+
| *Category*          |*App Count*|
+---------------------+----------+
| ART_AND_DESIGN      |      146 |
| AUTO_AND_VEHICLES   |       55 |
| BEAUTY              |       23 |
| BOOKS_AND_REFERENCE |      848 |
| BUSINESS            |      503 |
| COMICS              |       24 |
| COMMUNICATION       |      212 |
| DATING              |       17 |
| EDUCATION           |     1747 |
| ENTERTAINMENT       |      562 |
| EVENTS              |       23 |
| FINANCE             |      469 |
| FOOD_AND_DRINK      |      144 |
| GAME_ACTION         |      549 |
| GAME_ADVENTURE      |      544 |
| GAME_ARCADE         |      543 |
| GAME_BOARD          |      343 |
| GAME_CARD           |      380 |
| GAME_CASINO         |       37 |
| GAME_CASUAL         |      843 |
| GAME_EDUCATIONAL    |      568 |
| GAME_MUSIC          |       71 |
| GAME_PUZZLE         |     1383 |
| GAME_RACING         |      165 |
| GAME_ROLE_PLAYING   |      796 |
| GAME_SIMULATION     |      545 |
| GAME_SPORTS         |      281 |
| GAME_STRATEGY       |      589 |
| GAME_TRIVIA         |      137 |
| GAME_WORD           |      366 |
| HEALTH_AND_FITNESS  |      884 |
| HOUSE_AND_HOME      |       54 |
| LIBRARIES_AND_DEMO  |       36 |
| LIFESTYLE           |      585 |
| MAPS_AND_NAVIGATION |      176 |
| MEDICAL             |      296 |
| MUSIC_AND_AUDIO     |      695 |
| NEWS_AND_MAGAZINES  |      255 |
| PARENTING           |       77 |
| PERSONALIZATION     |      371 |
| PHOTOGRAPHY         |      312 |
| PRODUCTIVITY        |      724 |
| SHOPPING            |      176 |
| SOCIAL              |      178 |
| SPORTS              |      298 |
| TOOLS               |     1214 |
| TRAVEL_AND_LOCAL    |      330 |
| VIDEO_PLAYERS       |      194 |
| WEATHER             |      397 |
+---------------------+----------+
```
## usage
### loading dataset
```
import pandas
dataset=pandas.read_csv('app_details.csv')
```
### Dispalying Info
```
dataset.info
```
##### Output
```
#   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   id                    20165 non-null  object 
 1   name                  20165 non-null  object 
 2   developer             20165 non-null  object 
 3   category_id           20165 non-null  object 
 4   rating                20165 non-null  float64
 5   number_rating         20165 non-null  int64  
 6   last_app_update       20165 non-null  object 
 7   current_version       20165 non-null  object 
 8   size                  20165 non-null  object 
 9   approx_installs       20165 non-null  object 
 10  content_rating        20165 non-null  object 
 11  details_collected_on  20165 non-null  object 
dtypes: float64(1), int64(1), object(10)
memory usage: 1.8+ MB


```
### Summery of Data
```
dataset.describe()
```
##### Output
```
            rating  number_rating
count  20165.000000   2.016500e+04
mean       4.072809   8.415572e+04
std        0.943172   1.126332e+06
min        0.000000   0.000000e+00
25%        4.000000   1.810000e+02
50%        4.300000   1.568000e+03
75%        4.500000   1.302400e+04
max        5.000000   1.225554e+08

```
### Display First 10 Entries
```
dataset.head(10)
```
##### Output
```
0  aademo.superawesome.tv.awesomeadsdemo2  ...  2021-08-05 18:07:01
1               aasuited.net.contrepetrie  ...  2021-08-04 15:26:04
2                   aasuited.net.mrandmrs  ...  2021-08-06 16:53:36
3                       aasuited.net.word  ...  2021-08-07 10:36:54
4                       ab.exchangeratege  ...  2021-08-07 16:00:01
5                       ab.exchangeratekg  ...  2021-08-02 10:03:49
6                        abc.kids.edu.pro  ...  2021-08-05 18:50:45
7         abdelrahman.wifianalyzerpremium  ...  2021-08-02 19:51:08
8            abdlrhmanshehata.yatadabaron  ...  2021-08-07 16:33:31
9                              abraj.live  ...  2021-08-05 20:00:39

```
Find more info on how to use pandas on datasets => [Python Pandas Tutorial - GeekForGeeks](https://www.geeksforgeeks.org/introduction-to-pandas-in-python/)

## Script used to scrap data
To use the script `app_details.py` you must have <br/>
* Requests
 ```
 pip install requests
 ```
 * Beautiful Soup 4
 ```
 pip install beautifulsoup4
 ```
 <br/>
 
`app_details.py` has two functions:<br/>

>`app_details(id_string)` => This function collects the details of app from its google play page and returns a dictnory if everything goes well.<br/>
>
>`list_ids(id_string)` => This function list out Ids of related apps from an app's google play page and returns a list if everything goes well.<br/>
 
###### Sample output of both functions on id of Netflix App  using python pprint function
```
>>> from pprint import pprint
>>> from app_details import list_ids
>>> from app_details import app_details
>>> 
>>> 
>>> pprint(app_details('com.netflix.mediaclient'))
{'Installs': '1,000,000,000+',
 'category': 'Entertainment',
 'category_id': 'ENTERTAINMENT',
 'content_rating': 'Teen',
 'current_version': 'Varies with device',
 'developer': 'Netflix, Inc.',
 'id': 'com.netflix.mediaclient',
 'name': 'Netflix',
 'number_ratings': '12,151,890',
 'rating': '4.3',
 'size': 'Varies with device',
 'updated': 'October 7, 2021'}
>>> 
>>> 
>>> pprint(list_ids('com.netflix.mediaclient'))
{'com.amazon.avod.thirdpartyclient',
 'com.disney.disneyplus',
 'com.instagram.android',
 'com.netflix.Speedtest',
 'com.netflix.android_vr',
 'com.netflix.ninja',
 'com.netflix.stickers',
 'com.netflix.stickersvaleria',
 'com.spotify.music',
 'com.zhiliaoapp.musically'}​

```
the script can also be tested by running the script fom terminal and  passing the id of the app as commandline argument after the script name
```
python app_details.py  com.netflix.mediaclient
```

