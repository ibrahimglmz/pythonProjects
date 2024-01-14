import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class userRepository:
    def __init__(self):
        self.users = []
        self.isLoggIn = False
        self.currentUser = {}
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                users = json.load(file)
                for index, user_data in enumerate(users, start=1):
                    user = json.loads(user_data)
                    newUser = User(user["username"], user["password"], user["email"])
                    self.users.append(newUser)
                    print(f'{index}. {newUser.__dict__}')

                print(self.users)

    def HesapOlustur(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print("Kullanici Hesabı Oluşturuldu")

    def KayitOl(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggIn = True
                self.currentUser = user
                print(f" Kullanıcı {username} ve Şifre Doğru . Login Yapıldı")
                break

    def logout(self):
        self.isLoggIn = False
        self.currentUser = {}
        print("Cıkış Yapıldı")

    def identity(self):
        if self.isLoggIn:
            print(f'username: {self.currentUser["username"]}')
        else:
            print("Giriş Yapılamadı ")

    def saveToFile(self):
        user_list = []
        for user in self.users:
            user_list.append(json.dumps(user.__dict__))
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(user_list, file,ensure_ascii=False, indent=2)


repository = userRepository()
while True:
    print('Menü'.center(50, '-'))
    secim = input('1-register: \n2-login: \n3-Logout: \n4-identity: \n5-Exit:\n')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('Username: ')
            password = input('Password: ')
            email = input('Email: ')
            user = User(username=username, password=password, email=email)
            repository.HesapOlustur(user)
            print(repository.users)
        elif secim == '2':
            if repository.isLoggIn:
                print('Zaten Giriş Yaptınız')
            else:
                username = input('Username: ')
                password = input('Password: ')
                repository.KayitOl(username, password)
        elif secim == '3':
            repository.logout()

        elif secim == '4':
            repository.identity()
        elif secim == '5':
            pass

    # repostiry oluştur  girişe login oluştur bunları save et  def(fonsyon kullan)
