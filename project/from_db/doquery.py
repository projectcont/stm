from prod.product import Product
from connectors.connector import *
from format import *

def query_get (  ) :
    '''
    makes query from MySQL database
    gets all the products from MySQL database
    :return: list of Products (with all attributes of each product)
    '''

    myConnection = dbconnect()  #get  connection
    cursor = myConnection.cursor()
    printf2("cursor getted")

    query="SELECT *  FROM `e92gs_jshopping_products` WHERE 1 "
    printf2("query getted")

    cursor.execute(query)
    printf2("cursor executed")

    records=cursor.fetchall()
    printf2("cursor fetched")

    printf("Amount of products on website = ", cursor.rowcount)

    product_list=[]

    for v in records:

        product = Product(v[0],12)
        product.pr['product_id']= v[0]
        product.pr['parent_id']  = v[1]
        product.pr['product_ean'] = v[2]
        product.pr['manufacturer_code']  = v[3]
        product.pr['product_quantity']  = v[4]
        product.pr['unlimited']  = v[5]
        product.pr['product_availability']  = v[6]
        product.pr['product_date_added']  = v[7]
        product.pr['date_modify']  = v[8]
        product.pr['product_publish']  = v[9]
        product.pr['product_tax_id']  = v[10]
        product.pr['currency_id']  = v[11]
        product.pr['product_template'] = v[12]
        product.pr['product_url']  = v[13]
        product.pr['product_old_price']  = v[14]
        product.pr['product_buy_price']  = v[15]
        product.pr['product_price']  = v[16]
        product.pr['min_price'] = v[17]
        product.pr['different_prices']  = v[18]
        product.pr['product_weight']  = v[19]
        product.pr['image']  = v[20]
        product.pr['product_manufacturer_id'] = v[21]
        product.pr['product_is_add_price']  = v[22]
        product.pr['add_price_unit_id']  = v[23]
        product.pr['average_rating'] = v[24]
        product.pr['reviews_count']= v[25]
        product.pr['delivery_times_id']= v[26]
        product.pr['hits'] = v[27]
        product.pr['weight_volume_units']= v[28]
        product.pr['basic_price_unit_id']= v[29]
        product.pr['label_id']= v[30]
        product.pr['vendor_id']= v[31]
        product.pr['access']= v[32]
        product.pr['name_en-GB']= v[33]
        product.pr['alias_en-GB']= v[34]
        product.pr['short_description_en-GB']= v[35]
        product.pr['description_en-GB']= v[36]
        product.pr['meta_title_en-GB']= v[37]
        product.pr['meta_description_en-GB']= v[38]
        product.pr['meta_keyword_en-GB']= v[39]
        product.pr['name_ru-RU']= v[40]
        product.pr['alias_ru-RU']= v[41]
        product.pr['short_description_ru-RU'] = v[42]
        product.pr['description_ru-RU']= v[43]
        product.pr['meta_title_ru-RU']= v[44]
        product.pr['meta_description_ru-RU']= v[45]
        product.pr['meta_keyword_ru-RU']= v[46]
        #product.pr['extra_field_1']= v[47]
        #product.pr['extra_field_2'] = v[48]

        product_list.append (product)

    cursor.close()
    printf2("Cursor is closed")
    myConnection.close()
    printf2("MySQL connection is closed")
    printf2("Data getted from DATABASE")
    printf2('')

    return  product_list


