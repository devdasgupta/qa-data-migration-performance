from db_activity import Database
from graphite_activity import Graphite
import config as c


PDS_SQL = 'select kb_class, count(kb_class) as count  from ont_record group by kb_class'
SY_APPS_SQL = 'select record_class, count(record_class) from data_transformation_waitingrecord group by record_class'


if __name__=='__main__':
    pds_db = Database('syapse_apps_pds_dev')
    graph = Graphite(c.GRAPHITE_ENDPOINT, 2003)

    data = pds_db.fetch_all_db_data(PDS_SQL)

    for field, val in data:
        graph.send_message('Data_Transformation.syapse_apps_pds.ont_record', field, val)
        # print(field, val)

    del pds_db

    pds_stg_db = Database('syapse_apps_dev')
    records = pds_stg_db.fetch_all_db_data(SY_APPS_SQL)
    for field, value in records:
        graph.send_message('Data_Transformation.syapse_apps.data_transformation_waitingrecord', field, value)
        # print(field, value)

    del pds_stg_db
    del graph
