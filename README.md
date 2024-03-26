# BurstSMS-Tzuchi
This project automates the sending and receiving of mass SMS, to inform subjects about the collection of Food Parcel at Tzuchi. Two program files (FP_SendBurstSMS.py and FP_ReplySMS.py) are used for the automation. 

Please install the latest Python release from https://www.python.org/ to run these programs.
Run the following in the windows command line to install the relevant modules needed after Python installation.

* py -m pip install numpy
* py -m pip install pandas
* py -m pip install openpyxl
* py -m pip install xlrd
* py -m pip install requests

Personal information about the subjects were stored in the excel file : Food-Parcel Masters List.xlsx. Phone numbers, first names and last names are extracted using the program (FP_SendBurstSMS.py), from the excel file. Then, the list extracted was uploaded onto BurstSMS portal using Rest API. The uploaded contact list contains the most recent date stamp with the file name :{date} Food-Parcel List. Subsequently, mass SMS were sent to the subjects within the contact list, through Rest API consisting of a preconfigured message next Saturday (as food parcels are normally delivered on a Saturday morning). A unique message id is generated when the mass SMS is sent, stored in the file message_id.txt.

Please ensure that the excel file Food-Parcel Masters List.xlsx is stored in the same folder as the program files.

To send mass SMS, please run the following command: 

py FP_SendBurstSMS.py

After running FP_SendBurstSMS.py, two files are generated (message_id.txt and BurstSMS_config.py). These two files are required for running the next program FP_ReplySMS.py.
The purpose of FP_ReplySMS.py is to retrieve a list of SMS response from the BurstSMS website. In addition, it also updates the master list excel file with 
with a status of "confirmed" if the SMS response is not a No.

Please note, the program (FP_ReplySMS.py) should only be run at a suitable cutoff time, ideally when all the SMS replies have been received. 

To update the master list excel file, please run the following command:

py FP_ReplySMS.py
