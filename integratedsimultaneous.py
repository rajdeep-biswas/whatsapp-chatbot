from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException

driver = webdriver.Chrome('../chromedriver.exe')

driver.get("https://web.whatsapp.com")

my_bot = ChatBot(name='PyBot', read_only=True,
         logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                 'chatterbot.logic.BestMatch'])

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

yourname = "Rajdeep"
persons = {}

while True:
    try:
        with open('peoplelist.txt', 'r') as f:
            for person in f:    
                person = person.strip()
                # print(person, end = " ")
                driver.find_element(By.XPATH, '//span[@title="' + person + '"]').click()
                sleep(1)

                if person not in persons:
                    persons[person] = {
                      "lastmessage": ""
                    }

                checkwindow = driver.find_element(By.XPATH, '//div[@id="main"]//span[@dir="auto"]').text
                if checkwindow not in persons:
                    continue
                        
                if yourname in driver.find_elements(By.XPATH, '//div[@class="copyable-text"]')[-1].get_attribute("data-pre-plain-text"):
                    continue

                for texts in driver.find_elements(By.XPATH, '//div[@class="copyable-text"]'):
                    if person in texts.get_attribute("data-pre-plain-text"):
                        text = texts.text

                newmessage = text.strip()

                if newmessage != persons[person]["lastmessage"]:
                    # print(person + ": reply")

                    if newmessage in ['', ' ']:
                        reply = "thanks for your human picture, i don't understand it"
                    else:
                        try:
                            reply = my_bot.get_response(newmessage).text
                        except KeyError:
                            reply = "I do not have a response for that"
                        except IndexError:
                            reply = "I do not have a response for that"

                    driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')[-1].send_keys(reply)
                    driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')[-1].send_keys(Keys.RETURN)

                persons[person]["lastmessage"] = newmessage

    except StaleElementReferenceException:
        persons[person]["lastmessage"] = ""
        continue
    except ElementClickInterceptedException:
        persons[person]["lastmessage"] = ""
        continue
