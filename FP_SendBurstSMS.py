# Program FP_SendBurstSMS.py filters extracts a list of phone number, first name and last name from the masters list for
# Tzuchi food parcel collection. After the list was extracted, it uploads the list into the BurstSMS website through
# API. Then, it automatically send each of the recipients of the list an SMS with a predefined message.

# Program Written by: Chooi Fei Ng
# Email: fei.ngc@gmail.com

from datetime import date, timedelta
import numpy as np
import pandas as pd
import requests
import BurstSMS_config

class ExtractList():

    def __init__(self):
        self.list = []

    def extract_excel(self):
        try:
            # Read excel file and place it in a dataframe
            df = pd.read_excel('Food-Parcel Master List.xlsx')
        except:
            print('Error FPSendSMS 01: File unavailable, cannot read file.')
        # print(df)
        # read the last column of the dataframe
        lastcol = df.iloc[:, -1]
        # print(lastcol)
        # Read the phone number, first and lastname of the dataframe
        first3col = df.iloc[:, 0:3]
        # print(first3col)
        # print(len(first3col))
        # extract = pd.concat([first3col,lastcol],axis=1)
        # extract.iloc[0] = extract.iloc[0].astype(int)
        # print(extract)
        i = 0
        j = False
        ind = 'Phone Firstname Lastname'.split()
        # Go through the dataframe
        while(i <= len(first3col)-1):
            # If the last column indicates send
            if(lastcol.iloc[i] == 'Sent' or lastcol.iloc[i] == 'sent'):
                if(j == False):
                    # The list to be send is empty so create a new dataframe with the list
                    listsend = pd.DataFrame(first3col.iloc[i])
                    j = True
                else:
                    # Add to the listsend dataframe
                    listsend=pd.concat([listsend,first3col.iloc[i]],axis=1)
                #print(i)
                #print(first3col.iloc[i])
                #print(lastcol.iloc[i])
            i = i + 1

        #print(listsend)
        # Transpose the list sent
        listT = listsend.T
        #print(listT)
        # print(listT['Phone'])
        # Convert the phone number to integer
        listT.iloc[:, 0] = listT.iloc[:, 0].astype('int64')
        # print(listT)
        # Assign self.list to the transposed list
        self.list = listT
        #print(self.list)
        return self.list
class SendBurstSMS():

    def __init__(self,contactList):
        # Initialise class
        self.list = contactList
        self.listid = 0
        self.add_errorflag = False
    def todays_date(self):
        # Obtain todays date
        today = date.today()
        dateformat = today.strftime("%Y%m%d")
        return(dateformat)
        #print(dateformat)
    def create_contactlist(self):
        today = self.todays_date()
        #print(today)
        # Create new contact list
        Listname = str(today) + ' Food-Parcel List'
        # The url to send the burstsms list
        url = "https://api.transmitsms.com/add-list.json"

        # create a new contact list name
        payload = {'name': Listname}
        files = []
        # Basic Authorisation API key and secret
        headers = {
            'Authorization': BurstSMS_config.apiKey
        }

        # Make the POST request to the url with
        # Response received from newly created contact list
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        # Reformat response into json dictionary format
        res_json = response.json()
        #print(res_json)
        if (response.status_code != 200):
            print("Error FPSendSMS 02: List creation was unsuccessful")
        else:
            self.listid = res_json["id"]
            # List creation was successful
            # print(response.status_code)
            # print(res_json["id"])
            # Url to add contacts to the list that was created previously
            url2 = "https://api.transmitsms.com/add-to-list.json"
            # Go through the list of people to send the SMS

            for i in range(len(self.list)):
                # Contact information to send the SMS
                body = {'list_id': self.listid,  # Id for the list that was created previously
                        'countrycode': 'au',  # Country code
                        'msisdn': self.list.iloc[i, 0],  # Phone number
                        'first_name': self.list.iloc[i, 1],  # First name
                        'last_name': self.list.iloc[i, 2]}  # Last name
                # print(body)
                # POST the contacts one by one to url2 with body as data
                # Response received is stored as response2
                response2 = requests.request("POST", url2, headers=headers, data=body, files=files)
                # Convert the response to json format
                res2_json = response2.json()
                #print(res2_json)
                # print(response2.status_code)
                # Print error message if the status code is not 200
                if (response2.status_code != 200):
                    print("Error FPSendSMS 03: Unable to add contacts to list")
                    self.add_errorflag = True

    def send_burstsms(self):
        if (self.add_errorflag == False):
            # No error, contact list successfully added
            # Obtain tomorrow date
            newdate = date.today() + timedelta(days=1)
            tomorrow = newdate.strftime("%d %B")
            # print(tomorrow)
            # The new api url to automatically send the sms
            url3 = "https://api.transmitsms.com/send-sms.json"
            files = []
            # Basic Authorisation API key and secret
            headers = {
                'Authorization': BurstSMS_config.apiKey
            }

            # Structure the message that needs to be sent with tomorrows date
            send_message = 'Dear [Firstname],\n\n' + \
                           'TZU CHI Food Relief tomorrow ' + tomorrow + ' 9:30am @ 60 Rosebank Square, Salisbury. Not guaranteed after 10:30am.\n\n' + \
                           'Park in basement car park and take lift to Ground level.\n\n' + \
                           'Reply by 8PM TODAY:\n' + \
                           '- \"Y\" to register, OR\n' + \
                           '- \"N\" if you cannot come\n\n' + \
                           'Call 3272 7938 if unsure.\n\n' + \
                           '[unsub-reply-link]'
            # print(send_message)
            # The body of the message to be sent that includes the message and the contact list id
            send_body = {'message': send_message,
                         'list_id': self.listid}  # Id for the list that was created previously

            # Perform API POST request to url3
            # POST the contacts one by one to url2 with body as data
            # Response received is stored as response2
            response3 = requests.request("POST", url3, headers=headers, data=send_body, files=files)
            # print(response3.status_code)
            #print(response3.status_code)
            res3_json = response3.json()
            #print(res3_json)
            # If there is an error code in the response print Error message
            if (response3.status_code != 200):
                print("Error FPSendSMS 04: Unable to send SMS to contacts in list")
            else:
                # Open the file that stores message id
                f = open('message_id.txt', 'w')
                # Write the message id into the above file
                f.write(str(res3_json['message_id']))
                # Close the file
                f.close()


# Call the class and function
# Initialise the class Extract List
RetrieveList = ExtractList()
# Retrieve list from excel file
Contact_List = RetrieveList.extract_excel()
# Initialise the class SendBurstSMS
SendSMS = SendBurstSMS(Contact_List)
SendSMS.create_contactlist()
SendSMS.send_burstsms()
