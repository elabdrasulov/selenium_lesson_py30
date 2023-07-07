import pathlib
from bs4 import BeautifulSoup as BS

def get_soup(html):
    return BS(html, 'lxml')

def get_page_data(soup: BS):
    films = soup.find_all('div', {'class': 'styles_root__ti07r'})
    # print(films)
    
    films_list = []
    
    for film in films:
        title = film.find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
        # print(title.text)
        year = film.find('span', class_='desktop-list-main-info_secondaryText__M_aus')
        year_film_len = [i.replace('\xa0', '') for i in year.text.split(', ') if i]
        desc = film.find('span', class_='desktop-list-main-info_truncatedText__IMQRP').text
        
        films_list.append(
            {
                'title': title,
                'year_and_film_length': year_film_len,
                'description': desc
            }
        )
    
    write_to_json(films_list)
        

def write_to_json(data):
    import json
    with open('films.json', 'a') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
html250 = pathlib.Path('films250_1').read_text()


get_page_data(get_soup(html250))
# with open('films250') as f:
#     html250 = f.read()