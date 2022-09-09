from prod.product import Product
from format import *
from connectors.connector import *

def to_db_ext( prod_list_ext ):
    '''
    makes query to MySQL database,
    inserts new products, with their attributes and categories
    '''

    printf2("Connecting for inserting database")
    myConnection = dbconnect ()
    cursor = myConnection.cursor()
    printf2("cursor getted")

    query = """ INSERT INTO `e92gs_jshopping_products`(`product_id`, `parent_id`, `product_ean`, `manufacturer_code`, `product_quantity`,
                                       `unlimited`, `product_availability`, `product_date_added`, `date_modify`,
                                       `product_publish`, `product_tax_id`, `currency_id`, `product_template`, `product_url`,
                                       `product_old_price`, `product_buy_price`, `product_price`, `min_price`,
                                       `different_prices`, `product_weight`, `image`, `product_manufacturer_id`,
                                       `product_is_add_price`, `add_price_unit_id`, `average_rating`, `reviews_count`,
                                       `delivery_times_id`, `hits`, `weight_volume_units`, `basic_price_unit_id`, `label_id`,
                                       `vendor_id`, `access`, `name_en-GB`, `alias_en-GB`, `short_description_en-GB`,
                                       `description_en-GB`, `meta_title_en-GB`, `meta_description_en-GB`,
                                       `meta_keyword_en-GB`, `name_ru-RU`, `alias_ru-RU`, `short_description_ru-RU`,
                                       `description_ru-RU`, `meta_title_ru-RU`, `meta_description_ru-RU`,
                                       `meta_keyword_ru-RU`)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    query_categ = """ INSERT INTO `e92gs_jshopping_products_to_categories`(`product_id`, `category_id`, `product_ordering`)
        VALUES(%s,%s,%s) """

    for v in prod_list_ext:
        v1 = v.pr['product_id']
        v2 = v.pr['parent_id']
        v3 = v.pr['product_ean']
        v4 = v.pr['manufacturer_code']
        v5 = v.pr['product_quantity']
        v6 = v.pr['unlimited']
        v7 = v.pr['product_availability']
        v8 = v.pr['product_date_added']
        v9 = v.pr['date_modify']
        v10 = v.pr['product_publish']
        v11 = v.pr['product_tax_id']
        v12 = v.pr['currency_id']
        v13 = v.pr['product_template']
        v14 = v.pr['product_url']
        v15 = v.pr['product_old_price']
        v16 = v.pr['product_buy_price']
        v17 = v.pr['product_price']
        v18 = v.pr['min_price']
        v19 = v.pr['different_prices']
        v20 = v.pr['product_weight']
        v21 = v.pr['image']
        v22 = v.pr['product_manufacturer_id']
        v23 = v.pr['product_is_add_price']
        v24 = v.pr['add_price_unit_id']
        v25 = v.pr['average_rating']
        v26 = v.pr['reviews_count']
        v27 = v.pr['delivery_times_id']
        v28 = v.pr['hits']
        v29 = v.pr['weight_volume_units']
        v30 = v.pr['basic_price_unit_id']
        v31 = v.pr['label_id']
        v32 = v.pr['vendor_id']
        v33 = v.pr['access']
        v34 = v.pr['name_en-GB']
        v35 = v.pr['alias_en-GB']
        v36 = v.pr['short_description_en-GB']
        v37 = v.pr['description_en-GB']
        v38 = v.pr['meta_title_en-GB']
        v39 = v.pr['meta_description_en-GB']
        v40 = v.pr['meta_keyword_en-GB']
        v41 = v.pr['name_ru-RU']
        v42 = v.pr['alias_ru-RU']
        v43 = v.pr['short_description_ru-RU']
        v44 = v.pr['description_ru-RU']
        v45 = v.pr['meta_title_ru-RU']
        v46 = v.pr['meta_description_ru-RU']
        v47 = v.pr['meta_keyword_ru-RU']

        args = (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,
         v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,
         v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,
         v31,v32,v33,v34,v35,v36,v37,v38,v39,v40,
         v41,v42,v43,v44,v45,v46,v47,)

        cursor.execute(query, args)

        myConnection.commit()


        args_categ = (v.pr['product_id'], v.categ, 4)
        cursor.execute(query_categ, args_categ)
        myConnection.commit()


    cursor.close()
    printf2("Cursor is closed")
    myConnection.close()
    printf2("MySQL connection is closed")
    printf2("Data sended to DATABASE")
