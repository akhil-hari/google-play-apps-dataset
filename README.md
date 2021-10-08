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

