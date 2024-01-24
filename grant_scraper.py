import requests
from bs4 import BeautifulSoup
import csv

def fetch_grant_summary(grant_url):
    response = requests.get(grant_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    summary_div = soup.find('div', {'class': 'grant_grant__breakword__72hvW'})
    if summary_div:
        return ' '.join(p.text for p in summary_div.find_all('p'))
    return 'Summary not found'

def scrape_grants():
    base_url = 'https://www.find-government-grants.service.gov.uk'
    current_page_url = '/grants'
    data = []

    response = requests.get(base_url + current_page_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    grants = soup.find_all('a', {'data-cy': 'cyGrantNameAndLink'})
    for grant in grants:
        grant_name = grant.text.strip()
        grant_url = base_url + grant['href']
        grant_summary = fetch_grant_summary(grant_url)
        data.append({'Name': grant_name, 'URL': grant_url, 'Summary': grant_summary})

    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'URL', 'Summary'])
        writer.writeheader()
        writer.writerows(data)

# Main execution
grant_data = scrape_grants()
save_to_csv(grant_data, 'grants_data.csv')
