import requests
import sys
import json

title = input('何を検索しますか? >') 
url = 'https://ja.wikipedia.org/w/api.php'
api_params1 = {
                'action': 'query',
                'titles': title,
                'prop': 'categories',
                'format': 'json'
              }

api_params2 = {
                'action': 'query',
                'titles': title,
                'prop': 'revisions',
                'rvprop': 'content',
                'format': 'xmlfm'
              }
categories = requests.get(url, params=api_params1).json()
json_dump = json.dumps(categories, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
print(json_dump)
page_id = categories['query']['pages']
if '-1' in page_id:
    print('該当するページがありません')
    sys.exit()
    
else:
    id = list(page_id.keys())
    if 'categories' in categories['query']['pages'][id[0]]:
        categories = categories['query']['pages'][id[0]]['categories']
        for t in categories:
            print(t['title'])
    else:
        print('保存できるページを検索できませんでした')
        sys.exit()

admit = input('検索結果を保存しますか?(yes) >') 
if admit == 'yes':
    data = requests.get(url, params=api_params2)
    json_dump = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    print(json_dump)
    with open(title + '.html', 'w', encoding = 'utf_8') as f:
        f.write(data.text)
else:
    print('プログラムを終了します')
    sys.exit()
