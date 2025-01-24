import requests
from bs4 import BeautifulSoup

def save_tables(url, class_name):
   
    response = requests.get(url)
    html_content = response.text

   
    soup = BeautifulSoup(html_content, 'html.parser')

    
    tables = soup.find_all('table', class_=class_name)

    for i, table in enumerate(tables):
        
        output_file = f'html_input_{i+1}.txt'
        with open(output_file, 'w', encoding='utf-8') as file:
            table_content = ''.join(str(child) for child in table.contents)
            file.write(table_content)
            file.write('\n')
        print(f"Table {i+1} saved in {output_file}.")


url = input("Enter URL\n")
class_name = 'specif'

save_tables(url, class_name)


