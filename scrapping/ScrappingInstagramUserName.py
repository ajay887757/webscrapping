from bs4 import BeautifulSoup
import requests


def Instagramwebscraping(target_url):

    response = requests.get(target_url)

    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, "html.parser")
    user_details=soup.find("meta",attrs={"name":"twitter:title"}) # Instagram
    user_details_string=user_details["content"]
    UserFullDetails=user_details_string.split("(")
    Data=UserFullDetails[1].split(")")
    user_name=Data[0]
    Name=UserFullDetails[0].rstrip()
    

    print("Name",Name)
    print("user_name",user_name)
    

Instagramwebscraping("https://www.instagram.com/p/Cj989gAPfs8/")
# Instagramwebscraping("https://www.instagram.com/p/CYUcr6yB0E3/")
