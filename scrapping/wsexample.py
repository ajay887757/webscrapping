from bs4 import BeautifulSoup
import requests


def WebScrapingRealExample():
    target_url = "https://www.flipkart.com/all/~cs-c470e9d9f4c9893754e997d194ada9b9/pr?sid=ajy,buh&marketplace=FLIPKART&restrictLocale=true&fm=personalisedRecommendation%2FC6&iid=R%3Ab%3Bpt%3Ahp%3Buid%3A8bc7d8f8-097f-11ed-8e6d-413a8cd9e4e3%3B.cid%3AS_F_N_ajy_buh__b___NONE_ALL%3Bnid%3Aajy_buh_%3Bet%3AS%3Beid%3Aajy_buh_%3Bmp%3AF%3Bct%3Ab%3B&ssid=5sqbi5z6bk0000001658467894614&otracker=hp_reco_Top%2BSelection_1_6.dealCard.OMU_cid%3AS_F_N_ajy_buh__b___NONE_ALL%3Bnid%3Aajy_buh_%3Bet%3AS%3Beid%3Aajy_buh_%3Bmp%3AF%3Bct%3Ab%3B_5&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC6_Top%2BSelection_DESKTOP_HORIZONTAL_dealCard_cc_1_NA_view-all_5&cid=cid%3AS_F_N_ajy_buh__b___NONE_ALL%3Bnid%3Aajy_buh_%3Bet%3AS%3Beid%3Aajy_buh_%3Bmp%3AF%3Bct%3Ab%3B"

    response = requests.get(target_url)
    # print(response.content)

    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, "html.parser")

    titles = []
    prices = []
    images = []

    for d in soup.find_all("div", attrs={"class": "_2kHMtA"}):
        title = d.find("div", attrs={"class": "_4rR01T"})
        TitleString = title.string
        # print(TitleString)
        price = d.find("div", attrs={"class": "_30jeq3 _1_WHN1"})
        PriceString = price.string
        # print(PriceString)
        image = d.find("img", attrs={"class": "_396cs4 _3exPp9"})
        ImageSrc = image.get("src")
        # print(ImageSrc)

        # aapending Data into list

        titles.append(TitleString)
        prices.append(PriceString)
        images.append(ImageSrc)

    print(titles)
    print(prices)
    print(images)


WebScrapingRealExample()
