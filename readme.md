#Special thanks  
`https://www.djangoproject.com/`
`https://github.com/broderickhyman/ao-bin-dumps`  
`https://github.com/broderickhyman/albiondata-client`  
`https://iconsflow.com/pricing-full`  
`https://bulma.io/`

##手順
`https://docs.djangoproject.com/ja/2.2/intro/`


`python -m pip install --upgrade pip`  
`pip install Django`  
`python manage.py migrate`  
`python manage.py createsuperuser`  
`python manage.py runserver`  

##設計  
  
###view  
```
convertPriceJsonToPriceClass(string jsonData){
    return priceClass prices
}  
updatePriceFromPriceClass(priceClass prices){
    return bool isSucceeded
}  
convertUniqueNameToGoodsId(string uniqueName){
    return string id
}  
convertProfitBetweenCity(string uniqueName,string fromCityName,string toCityName){
    return int profit
}  
calcProfit(string uniqueName,string sortOrder){
    return []{int profit,string fromCityName,string toCityName}
}
requestPriceByUniqueName(string uniqueName){
    return string jsonData
}
```
```
/trade_profit
    目的
        交易に活用する
    機能
        /rank   現在一番利益が出る交易ルートと商品名をソートしながら表示
        /renew  最新利益幅を取得
        /price/<uniqueName> 指定したアイテムの価格を表示
        /profit/<fromCity>/<toCity> 指定した都市間での全アイテムの利益を利益順に表示
        /profit/<fromCity>/<toCity>/<uniqueName>    指定したアイテムと都市間の利益を表示
```

##template
```
base    HTMLの基本要素 (title,script,content)
table   データ一覧表示(tableHeader,data)
form    フォームコンポーネント

rank    base+table+form
price   base+table+form
profit  base+table+form

```