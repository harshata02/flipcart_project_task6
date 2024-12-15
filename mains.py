
from utils.extracthtml import getHtml

import pandas as pd


flipUrl ="https://www.flipkart.com/search?q=laptop&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_2_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop&requestId=47a536a2-566d-4b97-9820-976978e26ab1"

flipHeaders={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

if __name__ =='__main__':

    flipData =getHtml(websiteUrl=flipUrl,showbrowser=True,screenshotName='lap')


 
    lap_titles = [ t.text() for t in flipData.css('div[class="KzDlHZ"]')]
    print(len(lap_titles))
    print(lap_titles)

    lap_prices=[p.text() for p in flipData.css('div[class="Nx9bqj _4b5DiR"]')]
    print(lap_prices)

    lap_discount =[d.text() for d in flipData.css('div[class="UkUFwK"]')]
    print(lap_discount)

    lap_specifications=[s .text() for s in flipData.css('div[class="_6NESgJ"]')]
    print(lap_specifications)

    lap_ratings =[r .text() for r in flipData.css('span[class="Wphh3N"]')]
    print(lap_ratings)

    lap_info ={

        'lap_name': lap_titles,
        'lap_pricing':lap_prices,
        'lap_discounts':lap_discount,
        'lap_speciality':lap_specifications,
        'lap_rating':lap_ratings
    }

    for i in range(len(lap_info['lap_name'])):
         print(f"Name: {lap_info['lap_name'][i]}") 
         print(f"Price: {lap_info['lap_pricing'][i]}") 
         print(f"Discount: {lap_info['lap_discounts'][i]}") 
         print(f"Specification: {lap_info['lap_speciality'][i]}") 
         print(f"Rating: {lap_info['lap_rating'][i]}") 
         print("-" * 24)

    data_list = [] 
    for i in range(len(lap_info['lap_name'])):
       data_list.append({ 
           'Name': lap_info['lap_name'][i],
           'Price': lap_info['lap_pricing'][i], 
                         'Discount': lap_info['lap_discounts'][i], 
                         'Specification': lap_info['lap_speciality'][i], 
                         'Rating': lap_info['lap_rating'][i]
                         })
    df = pd.DataFrame(data_list) 
    df.to_csv("laptop_info.csv")  

                         
       




    