# Niconico-Contributor-FreeTagRanking


ニコニコ動画におけるタイトルもしくはタグに検索キーワードを含む動画を投稿している合計総合ポイントの高い投稿者のランキングのDBを作成するためのスクリプト
( https://github.com/Dhikigame/Niconico-Contributor-TagRanking
の改良版)

A script for creating a ranking of posters with a high total total points who are posting videos that include search keywords in the title or tag of Nico Nico Douga.

We analyze the database as follows and use it in the ranking video
https://www.upload.nicovideo.jp/garage/series/97621


# Requirement
* Python3
* SQLite3
* niconicoAPI
  * getthumbinfo
  * スナップショット検索API v2 (https://site.nicovideo.jp/search-api-docs/snapshot)


# Features

* ランキング用のDBを作成してキーワードに一致する動画の動画IDや再生数のデータを登録する
* そのあとに、投稿者100位のランキングテーブルを作成する
<br>

* Create a ranking DB and register the video ID and playback count data of videos that match the keywords.
* After that, create a ranking table for the 100th contributor

# Usage
```bash
pip install contextlib2 xml-python
```

例として、以下のように端末実行にキーワード含む形で実行することができる

ゲーム.dbというDBが作られ、ゲームまたはアニメのどちらかが含む動画の合計総合ポイントの高い投稿者のランキングのDBを作成
```bash
python main_TableDesignation.py ゲーム アニメ
```

野球.dbというDBが作られ、野球またはバスケまたはサッカーのどれかを含む動画の合計総合ポイントの高い投稿者のランキングのDBを作成
```bash
python main_TableDesignation.py 野球 バスケ サッカー
```


# Author
* Dhiki(Infrastructure engineer & Video contributor)
* https://twitter.com/DHIKI_pico


# License
ご自由に使用いただいて構いません。

Feel free to use it.
