# coding:utf8
from .models import Db


# 获得某月存量
def get_duration_by_month_and_company(month=None, company_name=None):
    pipeline = [
        {
            '$match': {'InnerMark': 'No',
                       'CompanyName': company_name}
        },
        {
            '$project': {
                # "D": "$DiskSpace",
                # "M": "$MemoryLimit",
                # "duration": {'$subtract': ['$DiskSpace', '$MemoryLimit']},
                'cmp': {
                    '$and': [
                        {
                            '$lte': ["$BusinessCreateMonth", month]
                        },
                        {
                            '$or': [
                                {'$gt': ["$BusinessDeleteMonth", month]},
                                {'$eq': ['$DeleteTime', None]}
                            ]
                        }
                    ]
                }
            }
        },
        {
            '$match': {'cmp': True}
        },
        {
            '$group': {
                '_id': "$cmp",
                'count': {'$sum': 1},
                # 'disk_count': {'$sum': '$D'},
                # 'memory_count': {'$sum': '$M'},
            }
        }
    ]
    cur = Db._get_collection().aggregate(pipeline)
    try:
        result = cur.next()
    except StopIteration:
        return 0
    cur.close()
    return result['count']


# 获得某周存量
def get_duration_by_week_and_company(week=None, company_name=None):
    pipeline = [
        {
            '$match': {'InnerMark': 'No',
                       'CompanyName': company_name}
        },
        {
            '$project': {
                # "D": "$DiskSpace",
                # "M": "$MemoryLimit",
                'cmp': {
                    '$and': [
                        {
                            '$lte': ["$BusinessCreateWeek", week]
                        },
                        {
                            '$or': [
                                {'$gt': ["$BusinessDeleteWeek", week]},
                                {'$eq': ['$DeleteTime', None]}
                            ]
                        }
                    ]
                }
            }
        },
        {
            '$match': {'cmp': True}
        },
        {
            '$group': {
                '_id': "$cmp",
                'count': {'$sum': 1},
                # 'disk_count': {'$sum': '$D'},
                # 'memory_count': {'$sum': '$M'}
            }
        }
    ]
    cur = Db._get_collection().aggregate(pipeline)
    try:
        result = cur.next()
    except StopIteration:
        return 0
    cur.close()
    return result['count']


# 获得某日存量
def get_duration_by_day_and_company(day=None, company_name=None):
    pipeline = [
        {
            '$match': {'InnerMark': 'No',
                       'CompanyName': company_name}
        },
        {
            '$project': {
                # "D": "$DiskSpace",
                # "M": "$MemoryLimit",
                'cmp': {
                    '$and': [
                        {
                            '$lte': ["$BusinessCreateDay", day]
                        },
                        {
                            '$or': [
                                {'$gt': ["$BusinessDeleteDay", day]},
                                {'$eq': ['$DeleteTime', None]}
                            ]
                        }
                    ]
                }
            }
        },
        {
            '$match': {'cmp': True}
        },
        {
            '$group': {
                '_id': "$cmp",
                'count': {'$sum': 1},
                # 'disk_count': {'$sum': '$D'},
                # 'memory_count': {'$sum': '$M'}
            }
        }
    ]
    # 创建游标
    cur = Db._get_collection().aggregate(pipeline)
    try:
        result = cur.next()
    except StopIteration:
        return 0
    cur.close()
    return result['count']
