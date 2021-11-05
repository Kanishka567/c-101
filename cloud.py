from os import access
import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token='Oz_JQ2fyIcEAAAAAAAAAAQG_bpS3h0QjBq_IYTSHHbQwRinr_Hvm5up_siRDGOq6'
    transferData=TransferData(access_token)
    file_from=input("enter the file path to transer:->")
    file_to=input("enter the full path to upload to the dropbox:->")
    transferData.upload_file(file_from,file_to)
    print("file has been moved")
main()           
