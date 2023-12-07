import FP_SendBurstSMS

class Test_SendBurstSMS():
     def test_ExtractList(self):
         self.RetrieveList = FP_SendBurstSMS.ExtractList()
         self.ContactList = self.RetrieveList.extract_excel()
         list_len = len(self.ContactList)
         assert list_len != 0, "Retrieved contact list from excel empty"
