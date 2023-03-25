from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.in/Redmi-Storage-Segment-5000mAh-Battery/product-reviews/B0BBN56J5H/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

text_extracted = requests.get(url)

soup = BeautifulSoup(text_extracted.text, "lxml")

product_name = soup.find('a', class_="a-link-normal").text

print(product_name)

review_card = soup.find_all('div', class_="a-section celwidget")

for review in review_card:
    profile_name = review.find('span', class_='a-profile-name').text
    review_title_a = review.find('a',
                                 class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold')
    review_title = review_title_a.find("span").text
    review_description = review.find('div', class_='a-row a-spacing-small review-data').text.replace("\n", "")

    final_dict = {"Name": f"{profile_name}", "Review Title": f"{review_title}",
                  "Review Description": f"{review_description}"}

    print(final_dict)
