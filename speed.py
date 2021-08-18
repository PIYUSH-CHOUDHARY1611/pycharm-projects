import pyspeedtest

test = pyspeedtest.SpeedTest()
ping = test.ping()
download = test.download()
upload = test.upload()
url ="www.google.com"
print(f"Ping:{ping}\nDownload Speed{download}\nUpload Speed:{upload}")
