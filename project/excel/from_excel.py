import xlrd3 as xlrd
from prod.product import Product
from collections import Counter
from prod.manufacturer import get_manuf_id, manufcorresp
from decimal import Decimal
from format import *


def excel_ (file, index1,index2):
    printf('file=', file)
    printf2 ('Excel -  products getting ')

    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def is_float(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def is_not_nan(num):
        return num == num

    prod_list = []
    eans = []
    number = 0



    book = xlrd.open_workbook(file, on_demand=True)
    sh = book.sheet_by_index(0)
    printf('EXCEL total products =',sh.nrows)
    if index2==0: index2=sh.nrows


    print('lensh ',type(sh.nrows))
    #print("The number of worksheets is {0}".format(book.nsheets))
    #print("Worksheet name(s): {0}".format(book.sheet_names()))
    #print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    #print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))

    range_=sh.nrows
    for rx in range(index1,index2):
        vl= sh.row(rx)

        ean_ =   vl[1].value  # ean

        if type(ean_) is float:
            ean_s=str(round(ean_))
            #print(ean_,'type=',type(ean_),  ean_s,'type=',type(ean_s), )
            ean = ean_s.strip()
        else:
            ean = ean_.strip()

        title = vl[2].value  # title
        nip =   vl[3].value  # number in pack

        # check is it real product line
        if (is_not_nan(ean) and is_int(nip)):

            if ean not in eans:

                prod = Product(1, 98)
                prod.pr['product_ean'] = ean
                prod.pr['name_ru-RU'] = title
                prod.pr['alias_ru-RU'] = ean

                # price part
                if is_float(vl[8].value):
                    price = vl[8].value
                else:
                    price = 0
                prod.pr['product_price'] = round(price*100)/100
                prod.pr['weight_volume_units'] = Decimal(nip)


                # manuf part
                manuf_name_ = vl[6].value;
                manuf_name=manuf_name_.strip()
                manuf_id = get_manuf_id(manuf_name, manufcorresp)
                prod.pr['product_manufacturer_id'] = manuf_id
                prod.manufacturer_name = manuf_name

                prod.pr['product_publish'] = 1

                eans.append(ean)
                prod_list.append(prod)
                #print(prod)

    printf('EXCEL extracted products =',  len(prod_list))
    printf2('Excel - products getted ')
    
    book.release_resources()
    del book
    
    return prod_list














