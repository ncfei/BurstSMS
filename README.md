# BurstSMS-Tzuchi
This project automates the sending and receiving of mass SMS, to inform subjects about the collection of Food Parcel at Tzuchi. Two program files (FP_SendBurstSMS.py and FP_ReplySMS.py) are used for the automation. 

Please install the latest Python release from https://www.python.org/ to run these programs.
Run the following in the windows command line to install the relevant modules needed after Python installation.
py -m pip install numpy
py -m pip install pandas
py -m pip install openpyxl
py -m pip install xlrd
py -m pip install requests

Personal information about the subjects were stored in the excel file : Food-Parcel Masters List.xlsx. Phone numbers, first names and last names are extracted using the program (FP_SendBurstSMS.py), from the excel file. Then, the list extracted was uploaded onto BurstSMS portal using Rest API. The uploaded contact list contains the most recent date stamp with the file name :{date} Food-Parcel List. Subsequently, mass SMS were sent to the subjects within the contact list, through Rest API consisting of a preconfigured message that has the closest date on a Saturday (as food parcels are normally delivered on a Saturday morning). 

Please ensure that the excel file Food-Parcel Masters List.xlsx is within the same folder as the program files.

The following command should be typed on the command prompt to run the program for sending mass SMS: FP_SendBurstSMS.py

The second program file (FP_ReplySMS.py) relies on the two files (message_id.txt and BurstSMS_config.py) generated, after running the program file FP_SendBurstSMS.py.
A list of SMS response from the BurstSMS website were obtain using the message id. Next, please run the program at a cutoff time suitable, when all the SMS reply were received. Then, the master list excel file is updated with a confirmed response from the SMS response, that negates a no (meaning response is Yes or others).

The following command should be typed on the command prompt after receiving the SMS to update the excel file: py FP_ReplySMS.py