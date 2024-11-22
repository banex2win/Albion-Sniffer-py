# What is Albion-Sniffer-py?
Albion-Sniffer-py is a packet Analyzer for Albion Online Client's market data using the Albion-Data-project through the Python programming language.

# What can I access with Albion-Sniffer-py?
The AlbiPy sniffing thread class allows quick and easy access to datapoint directly from the Albion Online client's network traffic. AlbiPy listens on the Albion Online client's UDP socket in order to record and parse information as it is passed to the game client. AlbiPy gives direct access to the following data on every market order sent to the client:

Order Id

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
