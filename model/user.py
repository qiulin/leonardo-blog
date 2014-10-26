#!/usr/bin/env python
# encoding: utf-8

from util.query import Query


class UserModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "user"
        super(UserModel, self).__init__()


