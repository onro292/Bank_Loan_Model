
import requests

url = "http://127.0.0.1:5000/"

new_row = {"age": 35, "income": 140, "family": 3,"ccavg": 5,
                                          "education": 5, "mortgage":0, "securities": 1,
                                          "cd":0, "online": 1, "credit":0}
r = requests.get("http://DESKTOP-96JCJMN:5000", params=new_row)
print(r.text)
