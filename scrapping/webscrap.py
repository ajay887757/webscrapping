from bs4 import BeautifulSoup
import requests


def webscraping(self):
    target_url = "https://www.flipkart.com/all/~cs-c470e9d9f4c9893754e997d194ada9b9/pr?sid=ajy,buh&marketplace=FLIPKART&restrictLocale=true&fm=personalisedRecommendation%2FC6&iid=R%3Ab%3Bpt%3Ahp%3Buid%3A8bc7d8f8-097f-11ed-8e6d-413a8cd9e4e3%3B.cid%3AS_F_N_ajy_buh__b___NONE_ALL%3Bnid%3Aajy_buh_%3Bet%3AS%3Beid%3Aajy_buh_%3Bmp%3AF%3Bct%3Ab%3B&ssid=5sqbi5z6bk0000001658467894614&otracker=hp_reco_Top%2BSelection_1_6.dealCard.OMU_cid%3AS_F_N_ajy_buh__b___NONE_ALL%3Bnid%3Aajy_buh_%3Bet%3AS%3Beid%3Aajy_buh_%3Bmp%3AF%3Bct%3Ab%3B_5&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC6_Top%2BSelection_DESKTOP_HORIZONTAL_dealCard_cc_1_NA_view-all_5&cid=cid%3AS_F_N_ajy_buh__b___NONE_ALL%3Bnid%3Aajy_buh_%3Bet%3AS%3Beid%3Aajy_buh_%3Bmp%3AF%3Bct%3Ab%3B"

    response = requests.get(target_url)
    # print(response.content)

    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, "html.parser")

    for image in soup.find_all("img"):
        imageData = image.get("src")
        print(imageData)  # filtering Image data

    # for link in soup.find_all("a"):
    #     data = link.get("href")
    #     print(data)   #filter only href link

    # print(
    #     soup.find(id="review-16a562c5-3bfc-4db1-9580-0259e3b41163")
    # )  # find based on id
    # print(soup.find("a"))
    # print(soup.find_all("a"))  # find all tags
    # print(soup.a)
    # print(soup.p)  # first paragraph
    # print(soup.title.parent.name)
    # print(soup.title.string)
    # print(soup.title)
    # print(soup.title.name)  # title
    # print(soup.prettify())


# if you are calling normal python file than you have to call that function

webscraping(0)  # we passing 0 for possional argument
