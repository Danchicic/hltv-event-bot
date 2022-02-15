import fake_useragent
import requests
from bs4 import BeautifulSoup
import lxml


def main(url):
    href = url.split('/')
    event_id = href[4]
    url = f'https://www.hltv.org/events/{event_id}/matches'
    headers = {
        "user-agent": fake_useragent.UserAgent().random
    }
    all_matches = []

    main_p = requests.get(url, headers=headers)
    main_p = main_p.text
    src = main_p
    soup = BeautifulSoup(src, 'lxml')
    try:
        playing_card = soup.find_all("div", class_='upcomingMatchesSection')
        for blocks in playing_card:
            playing_day = blocks.find("span", class_='matchDayHeadline')
            day = playing_day.text
            matches = blocks.find_all("div", class_='upcomingMatch')
            for block in matches:
                teams = block.find_all('div', class_='matchTeamName')
                team1 = teams[0].text
                team2 = teams[1].text

                match_time = block.find("div", class_='matchTime').text
                t = match_time.split(':')
                moscow_t = int(t[0]) + 2
                for time in t:
                    t[0] = str(moscow_t)
                match_time = ':'.join(t)

                all_matches.append(f'{day[-2:]} числа сыграют {team1} против {team2} в {match_time} (по МСК)')
                # print(f'{day[-2:]} числа сыграют {team1} против {team2} в {match_time} (по МСК)')
    finally:
        return all_matches

# print(main('https://www.hltv.org/events/6219/iem-katowice-2022-play-in'))
