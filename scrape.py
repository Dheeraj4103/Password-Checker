from bs4 import BeautifulSoup
import requests


def create_custom(link, votes):
    hn = []
    for idx, item in enumerate(link):
        title = link[idx].getText()
        href = item.get('href')
        hn.append({'title': title, 'link': href})
    return hn


def get_top(votes):
    vote_idx = []
    for i in range(len(votes)):
        vote_int = int(votes[i].getText()[:-7])
        if vote_int >= 100:
            vote_idx.append([vote_int, i])

    vote_idx.sort(key=lambda vote_idx: vote_idx[0])
    vote_idx.reverse()
    return vote_idx


def hackernews(link, votes):
    news_li = create_custom(link, votes)
    news_idx = get_top(votes)
    for item1 in news_idx:
        for idx, item in enumerate(news_li):
            if idx == item1[1]:
                print('-----------------------------------------------------------')
                print(item['title'], item['link'], sep='\n', end='\n')
                print('Votes :- ', item1[0])
                print('-----------------------------------------------------------')


def pages(num):
    for ite in [n for n in range(1, num+1)]:
        res = requests.get(f"https://news.ycombinator.com/news?p={ite}")
        soup = BeautifulSoup(res.text, 'html.parser')

        link = soup.select('.storylink')
        votes = soup.select('.score')
        # print(create_custom(link, votes))
        print(f'PAGE {ite}')
        hackernews(link, votes)
        ex = input("Want to Exit![y/n] :- ")
    if ex == 'y':
        exit()


print("GET THE LATEST TECH NEWS")
num = int(input("Enter Number of Pages you want to Explore:- "))
pages(num)
