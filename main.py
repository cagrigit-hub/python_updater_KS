import requests
import time
def python_updater():
    url_for_playlist = "https://v1.nocodeapi.com/xxxxxxxxxxxxxxxxxxxxx/yt/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    params = {}
    r = requests.get(url = url_for_playlist, params = params)
    result_playlist = r.json()


    for i in range(len(result_playlist["items"])):
        video_url = "https://v1.nocodeapi.com/xxxxxxxxxxxxxxxxxp/yt/xxxxxxxxxxxxxxxx/videos?id=" + \
                    result_playlist["items"][i]["snippet"]["resourceId"]["videoId"]
        params2 = {}
        r2 = requests.get(url=video_url, params=params2)
        result_video = r2.json()
        title = result_playlist["items"][i]["snippet"]["title"]
        date = result_playlist["items"][i]["snippet"]["publishedAt"][0:10]
        view = result_video["items"][0]["statistics"]["viewCount"]

        url_search = f"https://v1.nocodeapi.com/xxxxxxxxxxxxxxxxx/google_sheets/xxxxxxxxxxxxxx/search?tabId=Sheet2&searchKey=VIDEO&searchValue={title}"
        params_search = {}
        r_search = requests.get(url=url_search, params=params_search)
        result_search = r_search.json()

        if result_search == []:
            url_sheet = "https://v1.nocodeapi.com/xxxxxxxxxxxxxxx/google_sheets/xxxxxxxxxxxxxxxxxx?tabId=Sheet2"
            params_Sheet = {}
            data_sheet = [[
                title,
                view,
                f'=IF(B{i+2}>999,"EVET","HAYIR")',
                date,
                f'=IF(MONTH(D{i + 2}) = MONTH(TODAY()),"HAYIR",IF( MONTH(TODAY()) - MONTH(D{i + 2}) > 1 , "EVET" , IF(DAY(D{i + 2}) - DAY(TODAY()) > 0 , "HAYIR" , "EVET")))',
                f'=IF(C{i+2} = "HAYIR",IF(E{i+2}="HAYIR",1,0),1)',
                f'=SUM($B${i+1}:B{i+2})'
            ]]
            r = requests.post(url=url_sheet, params=params, json=data_sheet)
            print(title + " başarıyla eklendi!")

        else:
            url_update = "https://v1.nocodeapi.com/xxxxxxxxxxxxxx/google_sheets/xxxxxxxxxxxxxxx"
            params_update = {"tabId": "Sheet2"}
            data = {"row_id": i+2, "IZLENME SAYISI": view}
            r_update = requests.put(url=url_update, params=params_update, json=data)
            result_update = r_update.json()
            print(title + " başarıyla güncellendi!")


while True:
    python_updater()
    time.sleep(86400)



