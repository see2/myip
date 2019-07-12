import requests
from bs4 import BeautifulSoup

# TODO

## 1. Check the quality of my ip proxy

class MyIp:
  def  __init__(self):
    self.ip=self.get()

  def get(self):  
    # use this website to get the ip
    url = "https://www.myip.com/"
    response =  requests.get(url)
    soup = BeautifulSoup(response.text)
    b = soup.find("span", id="ip")
    return b.text
  
  def __repr__(self):
      return "<Your IP is :%s>" % (self.ip)

  def __str__(self):
      return "From str method of Test: Your IP is :%s" % (self.ip)