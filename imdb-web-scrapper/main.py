from bs4 import BeautifulSoup

import requests


html_text = requests.get('https://www.imdb.com/search/title/?genres=thriller&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e0da8c98-35e8-4ebd-8e86-e7d39c92730c&pf_rd_r=9ARZY1VYEHE4QK4CNR3D&pf_rd_s=center-2&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr2_i_3').text
soup = BeautifulSoup(html_text, 'lxml')

movies = soup.find_all('div', class_='lister-item mode-advanced')

for index, movie in enumerate(movies):
    movie_object = movie.find('h3').text
    movie_description = movie.find_all('p', class_='text-muted')[1].text.replace("  ","")
    movie_link = movie.h3.a['href']
    
    with open(f'output.txt', 'a') as f:
        f.write(f"{movie_object.strip()}\n")
        f.write(f"{movie_description.strip()}\n")
        f.write(f"https://www.imdb.com{movie_link}\n")
        f.write(f"\n\n")
    print("file saved")