"# plugin-line-bot

<img src="https://lh3.googleusercontent.com/fUiX2JsPmnEXqLFWOHdkY2wMZrEAe4WTKx-pT4ZP0ApagTsmuGvNW7_5TMvvblqiFkkSc6fjtnHC6_kZJIUXgB4EYsTmRntiDmdGW6jbymVQFhHrV31tf_6y5WnXvqOoBqGndGhEyQBdREky8egfKESXxD8wv2ghTClHteBdJxMt1Ce0kMyAWBPWm4DJ5i4sDJ-oFoeZ1TJo_ZdywRIXt-sMD-aER4r03k-vE4iaQndTRRHnnLMebN_E4beNNuPOQFktxd1X2w8dazZLgirojaYmCsOk9FOYBk5JHiLC-kbkmT5s-PFA0Ht5ZmZbV4hc4LdBgkWqFkQ4VQHl6d4DM_liQkqvjZjDFJLjq55SIHA-q2anhfmqy9wxVVre1ZO1kj3I67YRvUPu2XTv9B8GSizQOdJ7e2jIxS5OI8-Q3n-Y1JwMm9onRKsmu6dS9gW44YDROvsvRvUMhmp1-BSwz24JOpv9NmLaIcnrDQsyBhdn8FgtRkhDe9jNbMga1Y3ONUpkcUdKV584Jt9snEI0GUz6CLQr2wVHVqRkDN01CyZIkPz_KZi81c2QPtQY45DzjedesaHhrZN-hCA3po8tZeOKC5yqiRCh7XXqTVs6vibRWTLEZF-VUw=w1910-h930-no" />

Line 訊息回覆機器人

回傳的參數為 "return_" + LINE API 原參數名稱
如 

    text  =>  return_text
    original_content_url  =>  return_original_content_url

py code 範例
來自 https://github.com/twtrubiks/line-bot-tutorial

蘋果日報

    targetURL = 'http://www.appledaily.com.tw/realtimenews/section/new/'
    head = 'http://www.appledaily.com.tw'
    rs = requests.session()
    res = rs.get(targetURL, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    for index, data in enumerate(soup.select('.rtddt a'), 0):
        if index == 15:
            break
        if head in data['href']:
            link = data['href']
        else:
            link = head + data['href']
        content += link + '\n\n'
    return_text = content
        
正妹圖

    import random
    pictures = ["https://i.imgur.com/qKkE2bj.jpg",
                ...
               "https://i.imgur.com/2cdURNa.jpg"
               ]
    img_url = random.randint(0, len(pictures) - 1)
    return_original_content_url = pictures[img_url]
    return_preview_image_url = pictures[img_url]