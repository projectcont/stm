from prod.product import Product
from connectors.connector import *
from format import *

def to_db_upd ( prod_list_upd ):
    '''
    makes query to MySQL database,
    updates products, with their prices
    '''

    printf2("Connecting for updating database")
    myConnection = dbconnect ()
    cursor = myConnection.cursor()
    printf2("cursor getted")

    # Update single record now
    printf2("Updating a records... ")
    query_upd = """Update `e92gs_jshopping_products` set product_price = %s, product_publish=1 where product_ean = %s """

    for v in prod_list_upd:

        args_upd = (v.pr['product_price'], v.pr['product_ean'] )

        cursor.execute(query_upd, args_upd )
        myConnection.commit()

    printf2("Records Updated successfully! ")  

    cursor.close()
    printf2("Cursor is closed")
    myConnection.close()
    printf2("MySQL connection is closed")
    printf2("Data sended to DATABASE")
