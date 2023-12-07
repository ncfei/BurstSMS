import pytest
import FP_ReplySMS
import pathlib
import datetime
from datetime import date

class Test_ReplySMS():
    def test_get_response(self):
        # Obtain responses of the BurstSMS from the function response multipage in the class ExtractSMS
        # Initialise the class ExtractSMS
        self.RetrieveSMS = FP_ReplySMS.ExtractSMS()
        # Retrieve message id
        self.RetrieveSMS.mess_id()
        # Obtain the list of SMS response from burstSMS and determine the length of the response list
        SMS_res = self.RetrieveSMS.response_multipage()
        res_len = len(SMS_res)
        assert res_len != 0, "There are no response from the SMS requests"

    def test_update_excel(self):
        # Initialise the class ExtractSMS
        self.RetrieveSMS = FP_ReplySMS.ExtractSMS()
        # Retrieve message id
        self.RetrieveSMS.mess_id()
        # Obtain the list of SMS response from burstSMS and determine the length of the response list
        SMS_res = self.RetrieveSMS.response_multipage()
        # Initialise the class Update Excel with the list of SMS response
        Up_Excel = FP_ReplySMS.Update_Excel(SMS_res)
        # Update the excel file with the confirmed response
        Up_Excel.change_excel()
        path = pathlib.Path(r'Food-Parcel Master List.xlsx')
        timestamp = path.stat().st_mtime
        modified_date = datetime.datetime.fromtimestamp(timestamp)
        mdate = str(modified_date)
        today = date.today()
        assert str(today) in mdate