import dropbox

#access_token is the key
access_token = "sl.AyNTz5Qm2lfvigwKLElI7ZJHvKy8ECjxZ_cBmP9-CyYsvgD1ThhfaHIh1HjdqIQQk1s-kryaWXwi-o3YlTPLMbiswb6Anaw6FR89e_4z9gnCwQ5wj7sOXPrCE979VDdbIq9cKfA"

dbx = dropbox.Dropbox(access_token) #opening the house with the key!

uploadFile = open("C:/Users/User/Downloads/nafis coding/spongebob.png","rb").read()

dbx.files_upload(uploadFile,"/sponge.png",mode=dropbox.files.WriteMode.overwrite)
