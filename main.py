from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.amazon.in/Vivo-Shimmer-Storage-Additional-Exchange/product-reviews/B07WJWXHFN/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

text_extracted = requests.get(url)

soup = BeautifulSoup(text_extracted.text, "lxml")

product_name = soup.find('a', class_="a-link-normal").text


review_card = soup.find_all('div', class_="a-section celwidget")
with open("Review.csv", 'w') as file:
    write = csv.writer(file)
    write.writerow(["Product Name:", product_name])
    write.writerow(["Name", "Title", "Description"])
    for review in review_card:
        profile_name = review.find('span', class_='a-profile-name').text
        review_title_a = review.find('a',
                                     class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold')
        review_title = review_title_a.find("span").text
        review_description = review.find('div', class_='a-row a-spacing-small review-data').text.replace("\n", "")
        review_list = [profile_name, review_title, review_description]
        write.writerow(review_list)
