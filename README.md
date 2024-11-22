# What is Albion-Sniffer-py?
Albion-Sniffer-py is a packet Analyzer for Albion Online Client's market data using the Albion-Data-project through the Python programming language.

# What can I access with Albion-Sniffer-py?
The AlbiPy sniffing thread class allows quick and easy access to datapoint directly from the Albion Online client's network traffic. AlbiPy listens on the Albion Online client's UDP socket in order to record and parse information as it is passed to the game client. AlbiPy gives direct access to the following data on every market order sent to the client:

Order Id <br />
Silver Per Unit

Total Silver

Item Amount

Item Tier

Order Type

Buyer/Seller Name

Item Enchantment

Item Quality

Order Expiry Date


# What are the limits of Albion-Sniffer-py?
this script was inspired by the AlbiPy Script that was published by hrichharms , It utilizes the Albion-Data-Project which can be downloaded here: https://www.albion-online-data.com
This Script is only Limited by the Data that the Albion-Data-Project gives (which is The best Albion Online Market Data Sniffer)

# How do i run/use Albion-Sniffer-py?
1- First you need to download the Albion Data Project which can be found here: https://www.albion-online-data.com or here: https://github.com/ao-data/albiondata-client/releases

2- After Downloading it and Fully Inistalling it -- *IN ITS DEFULT PATH* -- you can now Download the Albion-Sniffer-py and Use it
Note: If you Decide to store the Albion-Data-Project file into another Directory you will have to change the directory in the Albion-Sniffer-Py.py here:
![Untitleds](https://github.com/user-attachments/assets/b15e260e-9396-40a0-9f52-1b90c425e22d)

3- Download the Albion-Sniffer-py.py File and put in in your Project Folder

4- The Code is Used As The Following Example:
```python
from Albion-Sniffer-py import *
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

Alternatively, the collected data, orders can be written to json simply by typecasting the sniffer data object to a string then writing it to file.

```python
from Albion-Sniffer-py import *
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
Id -> A unique id for the specific order
UnitPriceSilver -> The price buying or selling one item from the given market order
TotalPriceSilver -> The total amount of silver involved in the order
Amount -> The quantity of items being bought or sold in the order
Tier -> The tier of the item being bought or sold if applicable
IsFinished -> Seems more like a backend boolean for the developer's database but I'm not sure
AuctionType -> Whether this is a buy order or a sell order
HasBuyerFetched -> If the order is a buy order this is a boolean determining whether the buyer has fetched the order. This seems like a largely backend attribute.
HasSellerFetched -> If the order is a sell order this is a boolean determining whether the seller has fetched the order. This, again, seems like a largely backend attribute.
SellerCharacterId -> If the order is a sell order, this is the unique id of the character that posted the sale.
SellerName -> If the order is a sell order, this is the in game name of the character that posted the sale.
BuyerCharacterId -> If the order is a buy order, this is the unique id of the character that posted the buy order.
BuyerName -> If the order is a buy order, this is the in game name of the character that posted the buy order.
ItemTypeId -> This is the item type identifier. Example: Adept's Longbow with 1 level of enchantment = T4_2H_LONGBOW@1
ItemGroupTypeId -> Same as ItemTypeId without the enchantment difference
EnchantmentLevel -> The enchantment level of the item being bought or sold if applicable
QualityLevel -> The quality of the item being bought or sold expressed as an integer if applicable
Expires -> The expiry date of the order
ReferenceId -> To be totally honest, I have no idea what this is. Probably something for the backend database I'm not sure.

