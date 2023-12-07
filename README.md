# BurstSMS-Tzuchi
This project automate the sending and receiving of BurstSMS Food Parcel delivery for Tzuchi. There are two program file FP_SendBurstSMS.py and FP_ReplySMS.py. 
For these two programs to run, please install the latest Python release from https://www.python.org/
After installation run the following in the windows command line to install the relevant modules needed for the program to run
py -m pip install numpy
py -m pip install pandas
py -m pip install openpyxl
py -m pip install xlrd
py -m pip install requests

The first program (FP_SendBurstSMS.py) extracts phone number, first name and last name from the excel file Food-Parcel Masters List.xlsx. The list extracted is then uploaded onto BurstSMS portal using API. The uploaded contact list will have the most recent date stamp with the name {date} Food-Parcel List. Then, SMS will automatically sent to the contact list through the API with a preconfigured message that has the most recent date (Saturday). 

Before running the program, please make sure the excel file Food-Parcel Masters List.xlsx is in the same folder as the program.

After module installation, to run the first program, type the following: py FP_SendBurstSMS.py

The second program file (FP_ReplySMS.py) relies on the file message_id.txt that was generated when you run the program file FP_SendBurstSMS.py. It also needs the file BurstSMS_config.py that was provided to run. This program used the message id provided to obtain a list of SMS response from the BurstSMS website. Please run the program at a cutoff time when you have determined that you have received all the SMS reply. Then, the program updates the master list excel file with a confirmed response from the SMS response that is not a no (meaning response is Yes or others).

To run the program, type the following on the command prompt: py FP_ReplySMS.py