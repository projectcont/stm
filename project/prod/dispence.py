from prod.product import Product
from format import *

def dispence_ (base, dop):
    product_list_ext = []
    product_list_upd = []

    eans = [];
    for prod in base:
        eans.append(prod.pr['product_ean'])
    #print( len(eans), " base eans=", eans)

    result=[]
    for prod in dop:
        if prod.pr['product_ean'] in eans:

            product_list_upd.append(prod)
        else:
            product_list_ext.append(prod)

    result = [product_list_ext, product_list_upd]

    print('result_=', len(result[0]), len(result[1]))

    length_product_list_ext=len(product_list_ext)
    length_product_list_upd=len(product_list_upd)

    if not product_list_ext:
        length_product_list_ext=0

    if not product_list_upd:
        length_product_list_upd=0


    printf('')
    printf("New products in EXCEL  = ", str(length_product_list_ext) )
    printf("Updated products in EXCEL  = ", str(length_product_list_upd))
    printf('')

    return result