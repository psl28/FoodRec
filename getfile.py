import urllib.request

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/sN1PIR8qp1SJ6K7syv72qQ/FoodDataSet.json"
urllib.request.urlretrieve(url, "FoodDataSet.json")

print("Download complete.")
