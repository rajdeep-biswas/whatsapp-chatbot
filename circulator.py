from time import sleep

# webdriver can fetch 18 most recent chats in current view

persons = {}

while True:
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

            for texts in driver.find_elements(By.XPATH, '//div[@class="copyable-text"]'):
                if person in texts.get_attribute("data-pre-plain-text"):
                    text = texts.text

            newmessage = text

            if persons[person]["lastmessage"] and newmessage != persons[person]["lastmessage"]:
                # print(person + ": reply")
                reply = my_bot.get_response(text).text
                driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')[-1].send_keys(reply)
                driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')[-1].send_keys(Keys.RETURN)
            else:
                print(person + ": don't reply")

            persons[person]["lastmessage"] = newmessage
