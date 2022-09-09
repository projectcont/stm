from from_db.doquery import *
from excel.from_excel import *
from prod.dispence import *
from to_db.query_ext import *
from to_db.query_upd import *
from paths import *

def go_(index2:int):
    '''
    function compares to product_lists:
    product_list_from_website (from Mysql database)  and  product_list_from_excel
    function produces two product_lists
    1) excel products which presents on website  (they will be updated)
    2) excel products which not presents on website  (they will be added)
    :param index2: number of lines from Excel to export (0 for all lines )
    '''

    # get product_list from Mysql database
    product_list = query_get ( )

    # get product_list_excel
    # imported product from  excel, assigning id,title, price, manufacturer_id, nip
    product_list_excel = excel_ (pathprice2, 1, index2 )



    # dispence from product_list_excel
    result = dispence_ ( product_list, product_list_excel )
    prod_list_ext=result[0]
    prod_list_upd=result[1]

    # UPDATING products to database
    to_db_upd ( prod_list_upd )

    # change id's
    ids=[]
    for n in product_list:
        ids.append(n.pr['product_id']) ;
    highest_id=max(ids)
    id_=highest_id+1
    for v in prod_list_ext:
         v.pr['product_id']=id_
         id_=id_+1

    printlist("New products:",prod_list_ext)

    # INSERTING products to database
    if len(prod_list_ext)>0: to_db_ext ( prod_list_ext )
    else: print("no products inserted")
















