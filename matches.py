import requests
from bs4 import BeautifulSoup
import csv

date = input("please enter a Date in the following formate 'MM/DD/YYYY': ")

page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")


def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    # print(soup)
    championships = soup.find_all("div", {"class": "matchCard"})

    match_details = []

    def get_match_info(championships):
        championship_title = championships.contents[1].find("h2").text.strip()
        all_matches = championships.contents[3].find_all("li")
        # matches = []

        for i in range(len(all_matches)):
            # init objects of matches
            Team_A = all_matches[i].find("div", {"class": "teamA"}).text.strip()
            team_B = all_matches[i].find("div", {"class": "teamB"}).text.strip()
            # number of the match
            match_number = i
            # score of the match
            result = (
                all_matches[i]
                .find("div", {"class": "MResult"})
                .find_all("span", {"class", "score"})
            )
            match_result =f"{result[0].text.strip()} - {result[1].text.strip()}"      # time of the match
            time = all_matches[i].find("div", {"class": "MResult"}).find('span', {'class', 'time'}).text.strip()
            # add match info to matches_dtials
            match_details.append({"num":match_number,"No3 el botoolah":championship_title,"team 1 name":Team_A,"team 2 name":team_B,"match time":time,"score":match_result})

    for i in range(len(championships)):
        get_match_info(championships[i])

    keys = match_details[0].keys()

    with open("/Users/mikawi/Documents/yalahkora.csv", 'w') as output_files:
        dict_writer =csv.DictWriter(output_files, keys)
        dict_writer.writeheader()
        dict_writer.writerows(match_details)
        print("done")

main(page)
