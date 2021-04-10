# coding:utf-8
import statistics
import analysis.db as db


class Statistics_order_split:
    def __init__(self):
        self.video_id = list()
        self.contributor = list()
        self.contributor_id = list()
        self.regist_date = list()
        self.upload_date = list()
        self.view = list()
        self.comment = list()
        self.mylist = list()
        self.total = list()

    def video_id_taglist(self, tag):
        db_data = db.DB_order_split()
        self.video_id = db_data.tag_videoid_list_sql(tag)
        print(self.video_id)
        return self.video_id
    def contributor_taglist(self, tag):
        db_data = db.DB_order_split()
        self.contributor = db_data.tag_contributor_list_sql(tag)
        print(self.contributor)
        return self.contributor
    def contributor_id_taglist(self, tag):
        db_data = db.DB_order_split()
        self.contributor_id = db_data.tag_contributorid_list_sql(tag)
        print(self.contributor_id)
        return self.contributor_id
    def regist_date_taglist(self, tag):
        db_data = db.DB_order_split()
        self.regist_date = db_data.tag_registdate_list_sql(tag)
        print(self.regist_date)
        return self.regist_date
    def upload_date_taglist(self, tag):
        db_data = db.DB_order_split()
        self.upload_date = db_data.tag_uploaddate_list_sql(tag)
        print(self.upload_date)
        return self.upload_date
    def title_taglist(self, tag):
        db_data = db.DB_order_split()
        self.title = db_data.tag_title_list_sql(tag)
        print(self.title)
        return self.title
    def view_taglist(self, tag):
        db_data = db.DB_order_split()
        self.view = db_data.tag_viewlist_sql(tag)
        print(self.view)
        return self.view
    def comment_taglist(self, tag):
        db_data = db.DB_order_split()
        self.comment = db_data.tag_commentlist_sql(tag)
        print(self.comment)
        return self.comment
    def mylist_taglist(self, tag):
        db_data = db.DB_order_split()
        self.mylist = db_data.tag_mylistlist_sql(tag)
        print(self.mylist)
        return self.mylist
    def total_taglist(self, tag):
        db_data = db.DB_order_split()
        self.total = db_data.tag_totallist_sql(tag)
        print(self.total)
        return self.total
    def follow_taglist(self, tag):
        db_data = db.DB_order_split()
        self.follow = db_data.tag_follow_list_sql(tag)
        print(self.follow)
        return self.follow
    def follower_taglist(self, tag):
        db_data = db.DB_order_split()
        self.follower = db_data.tag_follower_list_sql(tag)
        print(self.follower)
        return self.follower