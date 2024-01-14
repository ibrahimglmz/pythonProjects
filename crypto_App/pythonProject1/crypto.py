import  requests
def get_crypto_data():
    responce = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if responce.status_code == 200:
        return responce.json()



crypto_response = get_crypto_data()
user_input = input("Enter Your crypto Name: ")

for crypto in crypto_response:


    if crypto["currency"] == user_input:
        print(crypto["price"])
        break



