persons = ['Muchu']

lasttext = text = ""

while True:
    sleep(1)
    
    person = driver.find_element(By.XPATH, '//div[@id="main"]//span[@dir="auto"]').text
    if person not in persons:
        continue
    
    for texts in driver.find_elements(By.XPATH, '//div[@class="copyable-text"]'):
        if person in texts.get_attribute("data-pre-plain-text"):
            text = texts.text

    print(lasttext, text)
    if not lasttext == text:
        # reply = replies[randrange(len(replies))][:-1]
        reply = my_bot.get_response(text).text
        driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')[-1].send_keys(reply)
        driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')[-1].send_keys(Keys.RETURN)

    lasttext = text
