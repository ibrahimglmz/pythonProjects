from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Edge()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")

        usernameInput = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        passwordInput = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        WebDriverWait(self.browser, 20).until(
            EC.url_to_be("https://www.instagram.com/")
        )

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")

        try:
            followers_button = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers/')]"))
            )
            followers_button.click()

            dialog = WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//ul"))
            )

            # Wait for the followers to load
            WebDriverWait(dialog, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//li"))
            )

            followers = dialog.find_elements(By.XPATH, "//li")

            following = []
            notFollowing = []

            for follower in followers:
                username_element = follower.find_element(By.XPATH, ".//a[@title]")
                followButton = follower.find_element(By.XPATH, ".//button")

                username = username_element.get_attribute("title")
                followText = followButton.text

                if followText == "Following":
                    following.append(username)
                else:
                    notFollowing.append(username)

            print("Beni takip edenler:")
            for follower in following:
                print(follower)

            print("Beni takip etmeyenler:")
            for follower in notFollowing:
                print(follower)


            # Save the followers and following lists to a file
            with open("followers.txt", "w", encoding="UTF-8") as file:
                file.write("Beni takip edenler:\n")
                for follower in following:
                    file.write(follower + "\n")

                file.write("\nBeni takip etmeyenler:\n")
                for follower in notFollowing:
                    file.write(follower + "\n")

        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
instgrm = Instagram(username, password)
instgrm.signIn()
instgrm.getFollowers()


