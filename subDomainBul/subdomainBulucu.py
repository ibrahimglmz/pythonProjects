import  requests


def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass



target_input = "google.com"
with open("subdomains.txt", "r") as subdomain_list:
put_url = "https://jsonplaceholder.typicode.com/todos/15"
entry_al = input("Entry Giriniz : ")

to_do_item_15 = {f"userId":entry_al, "title": "put title", "completed": False}
put_response = requests.put(put_url, json=to_do_item_15)
print(put_response.json())



dosyayı bulamadıgı ıcın hata verıyor """"""