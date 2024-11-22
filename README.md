# What is Albion-Sniffer-py?
Albion-Sniffer-py is a packet Analyzer for Albion Online Client's market data using the Albion-Data-project through the Python programming language.

# What can I access with Albion-Sniffer-py?
The Albion-Sniffer-py is a tool that works in combination with the Albion-Data-Project to retrieve market data that the Albion-Data-Project collects, it can retrieve Buy orders and sell orders and generally doesnot miss anything<br />
these are the relevant information that you can access using Albion-Sniffer-py (Example code on how to do it is further down)<br />

Order Id <br />
Silver Per Unit <br />
Total Silver <br />
Item Amount <br />
Item Tier <br />
Order Type <br />
Buyer/Seller Name <br />
Item Enchantment <br />
Item Quality <br />
Order Expiry Date <br />


# What are the limits of Albion-Sniffer-py?
this script was inspired by the AlbiPy Script that was published by hrichharms , the main diffrence between Albion-Sniffer-py and AlbiPy is that this script doesnot attempt to decrypt the market data 
that arrives to your pc, it utilizes the albion-data-project to do that which is alot better than what AlbiPy Does , threw testing AlbiPy will get 20-30 sell orders from the market and alot of times the Albipy doesnot
work as intended due to data being moved around (example: you might try to access the order id and get the Silver per unit price) and the data being out of range

on the other hand Albion-Sniffer-py uses the albion-data-project to gather the data and decrypt it which threw my hours of testing it has always got all 50 sell orders instead of the 20-30 that albipy gets
it has never in my testing faced any problem with data being moved around or not being assigned to its correct call (for example if you call for the order Id you will always get the order Id)


It utilizes the Albion-Data-Project which can be downloaded here: https://www.albion-online-data.com <br />
This Script is only Limited by the Data that the Albion-Data-Project gives (which is The best Albion Online open source  Market Data Sniffer api) <br />

# How do i run/use Albion-Sniffer-py?
1- First you need to download the Albion Data Project which can be found here: https://www.albion-online-data.com or here: https://github.com/ao-data/albiondata-client/releases <br />
2- After Downloading it and Fully Inistalling it -- *IN ITS DEFULT PATH* -- you can now Download the Albion-Sniffer-py and Use it <br />
Note: If you Decide to store the Albion-Data-Project file into another Directory you will have to change the directory in the Albion-Sniffer-Py.py here: <br />
![Untitleds](https://github.com/user-attachments/assets/b15e260e-9396-40a0-9f52-1b90c425e22d)

3- Download the Albion-Sniffer-py.py File and put in in your Project Folder <br />
4- The Code is Used As The Following Example: <br />
```python
from Albion-Sniffer-Py import *
import time

sniffer = Sniffer()
sniffer.start() # Starts Recording the Market Data

time.sleep(5) # The Ammount of time you want it to record for

sniffer.stop() # Stops Recording the Market Data
orders = sniffer.get_output() # Gets The Data Collected

for order in orders:
    print(orders['Id'])
    print(orders['UnitPriceSilver'])
    print(orders['TotalPriceSilver'])
    print(orders['Amount'])
    print(orders['Tier'])
    print(orders['IsFinished'])
    print(orders['AuctionType'])
    print(orders['HasBuyerFetched'])
    print(orders['HasSellerFetched'])
    print(orders['SellerCharacterId'])
    print(orders['SellerName'])
    print(orders['BuyerCharacterId'])
    print(orders['BuyerName'])
    print(orders['ItemTypeId'])
    print(orders['ItemGroupTypeId'])
    print(orders['EnchantmentLevel'])
    print(orders['QualityLevel'])
    print(orders['Expires'])
    print(orders['ReferenceId'])
```

Alternatively, the collected data, orders can be written to json simply by typecasting the sniffer data object to a string then writing it to file. <br />

```python
from Albion-Sniffer-Py import *
import time

sniffer = Sniffer()
sniffer.start() # Starts Recording the Market Data

time.sleep(5) # The Ammount of time you want it to record for

sniffer.stop() # Stops Recording the Market Data
orders = sniffer.get_output() # Gets The Data Collected
output_file = open("output.json", "w")
output_file.write(str(orders))
output_file.close()
```
Note: The above code and AlbiPy in general can only capture market data that is received by the client while the thread is recording (between sniffer.start() and sniffer.stop()).

# List of datapoint attributes:
Id -> A unique id for the specific order <br />
UnitPriceSilver -> The price buying or selling one item from the given market order <br />
TotalPriceSilver -> The total amount of silver involved in the order <br />
Amount -> The quantity of items being bought or sold in the order <br />
Tier -> The tier of the item being bought or sold if applicable <br />
IsFinished -> Seems more like a backend boolean for the developer's database but I'm not sure <br />
AuctionType -> Whether this is a buy order or a sell order <br />
HasBuyerFetched -> If the order is a buy order this is a boolean determining whether the buyer has fetched the order. This seems like a largely backend attribute. <br />
HasSellerFetched -> If the order is a sell order this is a boolean determining whether the seller has fetched the order. This, again, seems like a largely backend attribute. <br />
SellerCharacterId -> If the order is a sell order, this is the unique id of the character that posted the sale. <br />
SellerName -> If the order is a sell order, this is the in game name of the character that posted the sale. <br />
BuyerCharacterId -> If the order is a buy order, this is the unique id of the character that posted the buy order. <br />
BuyerName -> If the order is a buy order, this is the in game name of the character that posted the buy order. <br />
ItemTypeId -> This is the item type identifier. Example: Adept's Longbow with 1 level of enchantment = T4_2H_LONGBOW@1 <br />
ItemGroupTypeId -> Same as ItemTypeId without the enchantment difference <br />
EnchantmentLevel -> The enchantment level of the item being bought or sold if applicable <br />
QualityLevel -> The quality of the item being bought or sold expressed as an integer if applicable <br />
Expires -> The expiry date of the order <br />
ReferenceId -> To be totally honest, I have no idea what this is. Probably something for the backend database I'm not sure. <br />

# Final words
i would like to thank hrichharms for inspiring me to make this script , you can find his script here: https://github.com/hrichharms/AlbiPy <br />
further more i would like to Thank all the members Past , Present , And Future for the Albion-Data-Project Decolpment team, non of this would be possible without them <br />
you can find there Program here: https://www.albion-online-data.com and you can join there discord here: https://discord.gg/TjWdq24 <br />
Please support them Finnacially here : https://ko-fi.com/aodp2024 or Verbally as it helps alot  <br />

# How to Contact Me

you can contact me threw discord at ".banom" or threw gmail at "ignitingvenom@gmail.com" <br />
this program is absloutly free and no Payment is required what so ever to use it, but if you want to help me my paypal is : mohamed.essam200216@gmail.com

