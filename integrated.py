from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

driver = webdriver.Chrome('../chromedriver.exe')

driver.get("https://web.whatsapp.com")

persons = []

while True:
	inp = input("enter person names or hit enter when ready: ")
	if inp:
		persons.append(inp)
	else:
		break

my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')


lasttext = text = ""

while True:
    sleep(1)
    
    person = driver.find_element(By.XPATH, '//div[@id="main"]//span[@dir="auto"]').text
    if person not in persons:
        continue
    
    for texts in driver.find_elements(By.XPATH, '//div[@class="copyable-text"]'):
        if person in texts.get_attribute("data-pre-plain-text"):
            text = texts.text

    print(lasttext == text, end = " ")
    if not lasttext == text:
        # reply = replies[randrange(len(replies))][:-1]
        reply = my_bot.get_response(text).text
        driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')[-1].send_keys(reply)
        driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')[-1].send_keys(Keys.RETURN)

    lasttext = text
