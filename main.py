# coding:utf-8
import os,sys
import logging
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_create as db_create


# 初めのタグをデータベース名に設定、入力したタグの引数の数を設定
args = sys.argv
db_name = args[1]
table_name = args[1]
print("タグ総数: " + str(len(args) - 1))
print("データベース名: " + args[1])
if len(args) - 1 > 20:
    logging.error('error')
    print("※ タグは20個まででお願いします ※")
    sys.exit()

# 登録したタグリスト初期化・タグ登録(20個まで登録可)
tags = []
print("【タグ一覧】")
for i in range(1, len(args)):
    if args[i] is not None:
        tags.append(args[i])
        print("登録したタグ" + str(i) + ": " + tags[i-1])
    else:
        break

# DB作成
db_path = "./analysis/db_ranking/" + db_name + ".db"
print("データベースのパス：" + db_path)
if os.path.exists(db_path) == True:
    os.remove(db_path)
    print("データベースを消去しましたので、再度作り直します：" + db_path)
db_create.db_create(db_path, table_name)
print("データベースを作成完了：" + db_path)

# タグ別のリストと動画総数のインスタンス生成 #
print("【キーワードに合致する動画を全てDBに保存】")
stats_tags = stats.Statistics_order_split()

print("1.動画IDをリストに保存")
videoid_list = stats_tags.video_id_taglist(tags)
print("2.投稿者IDをリストに保存")
contributorid_list = stats_tags.contributor_id_taglist(tags)
print("3.動画データ取得日時をリストに保存")
registdate_list = stats_tags.regist_date_taglist(tags)
print("4.動画投稿日時をリストに保存")
uploaddate_list = stats_tags.upload_date_taglist(tags)
print("5.動画タイトルをリストに保存")
title_list = stats_tags.title_taglist(tags)
print("6.再生数をリストに保存")
view_list = stats_tags.view_taglist(tags)
print("7.コメント数をリストに保存")
comment_list = stats_tags.comment_taglist(tags)
print("8.マイリスト数をリストに保存")
mylist_list = stats_tags.mylist_taglist(tags)
print("9.総合ポイントをリストに保存")
total_list = stats_tags.total_taglist(tags)

print("【取得したリストにある動画情報をテーブルに保存】")
db.db_insert(videoid_list, contributorid_list, registdate_list, uploaddate_list, title_list, view_list, comment_list, mylist_list, total_list, db_path, table_name)

# print("【累計総合ポイント高い100人の投稿者の情報を全てDBに保存】")
print("【累計総合ポイント高い100人の投稿者の情報を全てDBに保存】")
db.db_best_100(db_path, table_name)