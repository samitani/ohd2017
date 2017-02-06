
# PPAP is Programmable Art of Pin

## PPAP とは

![PPAP](https://github.com/samitani/ohd2017/raw/master/logo.png "PPAP")

* iPad で描いた絵をピンアートとして出力します

[![Alt text for your video](http://img.youtube.com/vi/EOE0tW7oABs/0.jpg)](https://www.youtube.com/embed/EOE0tW7oABs)


## 部品

|モノ                          |     説明             |
|-----------------------------|----------------------|
| ステッピングモータ [SM-42BYG011](http://akizukidenshi.com/catalog/g/gP-05372/) | ウデを左右に移動するためのモーター |
| ギア、ボルト、六角ナット        | ウデ用のレール |
| モータドライバ TB6674PG x 1   | ステッピングモータ制御用 |
| DCモータ [FA-130RA-2270](http://akizukidenshi.com/catalog/g/gP-06437/) x 10 | ピンを押し出す棒の駆動用 |
| モータドライバ [SN754410NE](http://akizukidenshi.com/catalog/g/gI-05277/) x 5 | DCモータ制御用 |
| Raspberry Pi 2 + Wifi アダプタ | モータドライバ制御、サーバからのデータの読み取り |


## 参考資料
* http://maplewine.up.seesaa.net/image/Arduino_BipolarStepperMoter.png
* http://izawa-web.com/lazarus/lazarus.html
