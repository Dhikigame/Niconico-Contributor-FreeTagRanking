# coding:utf-8
import os,sys
import logging
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.db_create as db_create


# # 初めのタグをデータベース名に設定、入力したタグの引数の数を設定
# args = sys.argv
# db_name = args[1]
# table_name = args[1]
# print("タグ総数: " + str(len(args) - 1))
# print("データベース名: " + args[1])
# if len(args) - 1 > 20:
#     logging.error('error')
#     print("※ タグは20個まででお願いします ※")
#     sys.exit()

# # 登録したタグリスト初期化・タグ登録(20個まで登録可)
# tags = []
# print("【タグ一覧】")
# for i in range(1, len(args)):
#     if args[i] is not None:
#         tags.append(args[i])
#         print("登録したタグ" + str(i) + ": " + tags[i-1])
#     else:
#         break

# DB作成
db_path = "./analysis/db_ranking/videonum.db"
table_name = "videonum"
print("データベースのパス：" + db_path)
if os.path.exists(db_path) == True:
    os.remove(db_path)
    print("データベースを消去しましたので、再度作り直します：" + db_path)
db_create.db_create_videonum(db_path, table_name)
print("データベースを作成完了：" + db_path)

# タグ別のリストと動画総数のインスタンス生成 #
print("【動画を全てDBに保存】")
db_allvideo = db.DB_order_split()

print("全ての動画をリストに保存し、ランキングを生成する")
allvideo_list = db_allvideo.allvideo_list(db_path, "so")