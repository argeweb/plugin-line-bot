# 快速上手

此為 ArgeWeb 開發框架之套件，請使用先下載 https://github.com/argeweb/start

相關的安裝方式，請見 argeweb/start 的 README

再使用 manage.py 進行安裝

    manage.py install argeweb/plugin-line-bot

目前有打包一個立即可用的版本，位於 https://github.com/argeweb/plugin-line-bot/releases 裡的 argeweb-line-bot-quick.zip


<a href="https://line.me/R/ti/p/@kpn6654y">https://line.me/R/ti/p/@kpn6654y</a>

<img src="http://imgur.com/a/2nRi7">



---

# 後台設定畫面

<img src="https://lh3.googleusercontent.com/h8jAUuXRJXWS6j5YGzg_jjdWO8QzxE1SP9MUsBIYvpuRaTAueKRbML_kNL7eHF6HnxOx0d6STP9oCOAuR5R-zoNsyuWr4_kdQxeyerJf2GctBd045ATGRDuaDPWhifA13mBcllesz_MvtBj7NDmuGTkx5LhPjOEfVGfe3n_ID5L-VLVyGTqSE4_9OMVP30xY-20vy8Ha87koOdOKBOBNyBS4qfo9nzjwBYyrY3i3RoPXkKc3bg8t-BclcWpA5kfSJWeraTQVMBCYg9OlvooJJtA2JlJu_CZs3cEd4UBDqpUiXihMcSJPVqz1lu0ZTr17OiFlz667w03JesxH6vMUvVvVmrDZIixWGzByHh9S_amUUerBai7QkxtQ-ftLEYY8dc-giSPVOdGiL1NLlQ-592rUZUfp1TUsJtrKjGjNYdGBrLDy207aQvmvcnM8yk9QOA9qXiCWF03OL0Phaidum_LHMcuH2-bLjmEDT__G6tv_Jszzo_d0Nx149f8heUGwKYbW7Gt96N3xtB1GnZONPPuTReVvbVBQEihJ6hNALUpXpEodQ6uZgJ81FZwqHp9tpZveRDYKLEhqKO1-b957Lp9XgVncuHRs_CtuJfPm_1QHrTNZLeepHw=w910-h930-no" />
<br>
<br>
<img src="https://lh3.googleusercontent.com/CKQRE90MKMTRdOIAbXZhSi7ak-k8p1VyS_jtpJu_iroAPphMVK6y-TFKzzNxUa-sFM2u_RHpR79XC4Pp8ttUv1dZfPt2lAHBbL89EZG97QgyOLCva9jA9yQWwebuGzVD-QOSQrjkFDLqOeKy2QErtu6G_Pkh_51IosYNecgr8RuQcOEqrGPTH4x2RTFClqM8XqCPAegpAOI7XAp3SThXrm_D8rdcvKd0fRqzAQ7pnAqFDvH9qkpJWVbbBEf9tcSPWSYhyateYbDeBJ30Qal0ubQvPAx5xxEZs9VqJvSWAHEMY8E9MVp9my9DjbW6_s8FexOL3UWqbzz5f9QXHj5NWzHlCWWfaADsfrACkhKG6vA2g_mzq6dULsnwsBHQ8Cd30eyesBQjGsysqslUPIZjszCqI9Zf5zJUVU8A70TdKvV3XLOFudmTbxgM5d5_I7AbOguFKzcvaQg4ttPCMjTIxP2cR9BURvr6Kry07fWmxqAzYrlg6veoEkQlpMQbDH5hOjeG1wRr4XQnLd9Q0iQvMQg7RmHqZ-_4zNSCI6mLWGf5N22Srnai3XEmQhQ-TAO7R6sIoGlBGcyKwC9TfyHQT_2rxAURDfOOiY9PMtVzHzp6Um3QN0X5ZA=w910-h930-no" />
<br>
<br>
<img src="https://lh3.googleusercontent.com/fUiX2JsPmnEXqLFWOHdkY2wMZrEAe4WTKx-pT4ZP0ApagTsmuGvNW7_5TMvvblqiFkkSc6fjtnHC6_kZJIUXgB4EYsTmRntiDmdGW6jbymVQFhHrV31tf_6y5WnXvqOoBqGndGhEyQBdREky8egfKESXxD8wv2ghTClHteBdJxMt1Ce0kMyAWBPWm4DJ5i4sDJ-oFoeZ1TJo_ZdywRIXt-sMD-aER4r03k-vE4iaQndTRRHnnLMebN_E4beNNuPOQFktxd1X2w8dazZLgirojaYmCsOk9FOYBk5JHiLC-kbkmT5s-PFA0Ht5ZmZbV4hc4LdBgkWqFkQ4VQHl6d4DM_liQkqvjZjDFJLjq55SIHA-q2anhfmqy9wxVVre1ZO1kj3I67YRvUPu2XTv9B8GSizQOdJ7e2jIxS5OI8-Q3n-Y1JwMm9onRKsmu6dS9gW44YDROvsvRvUMhmp1-BSwz24JOpv9NmLaIcnrDQsyBhdn8FgtRkhDe9jNbMga1Y3ONUpkcUdKV584Jt9snEI0GUz6CLQr2wVHVqRkDN01CyZIkPz_KZi81c2QPtQY45DzjedesaHhrZN-hCA3po8tZeOKC5yqiRCh7XXqTVs6vibRWTLEZF-VUw=w910-h930-no" />

---

# 關於參數

回傳的參數為 "return_" + LINE API 原參數名稱
如 

    text  =>  return_text
    original_content_url  =>  return_original_content_url

# 範例

今天

    return_text = datetime.datetime.today().strftime('%Y-%m-%d')

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