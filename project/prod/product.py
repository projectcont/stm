class Product ():
    def __init__(self, prod_id, categ):

        self.categ=categ
        self.manufacturer_name=""

        keys = ['product_id', 'parent_id', 'product_ean', 'manufacturer_code', 'product_quantity',
                'unlimited', 'product_availability', 'product_date_added', 'date_modify',
                'product_publish', 'product_tax_id', 'currency_id', 'product_template', 'product_url',
                'product_old_price', 'product_buy_price', 'product_price', 'min_price',
                'different_prices', 'product_weight', 'image', 'product_manufacturer_id',
                'product_is_add_price', 'add_price_unit_id', 'average_rating', 'reviews_count',
                'delivery_times_id', 'hits', 'weight_volume_units', 'basic_price_unit_id', 'label_id',
                'vendor_id', 'access', 'name_en-GB', 'alias_en-GB', 'short_description_en-GB',
                'description_en-GB', 'meta_title_en-GB', 'meta_description_en-GB',
                'meta_keyword_en-GB', 'name_ru-RU', 'alias_ru-RU', 'short_description_ru-RU',
                'description_ru-RU', 'meta_title_ru-RU', 'meta_description_ru-RU',
                'meta_keyword_ru-RU']

        values = [2300, 0, '', '', 0.00, 0, '', '2022-03-10 22:22:22', '2022-03-10 22:22:22', 1, 0, 2, 'default', '', 0.0000, 0.0000, 0.000000, 0.000000, 0, 0.0000, '', 0, 0, 3, 0.00, 0, 0, 0, 0.0000, 1, 0, 0, 1, '', '', '', '', '', '', '', 'Пробный 2', 'probnyj-2', '', '', '', '', '']

        self.pr = dict(zip(keys, values))

        self.pr['product_id'] = prod_id
        self.pr['parent_id'] = 0
        self.pr['product_ean'] = ''
        self.pr['manufacturer_code'] = 27
        self.pr['product_quantity'] = 0.00
        self.pr['unlimited'] = 0
        self.pr['product_availability'] = ''
        self.pr['product_date_added'] = '2022-03-10 22:22:22'
        self.pr['date_modify'] = '2022-03-10 22:22:22'
        self.pr['product_publish'] = 1
        self.pr['product_tax_id'] = 0
        self.pr['currency_id'] = 2
        self.pr['product_template'] = 'default'
        self.pr['product_url'] = ''
        self.pr['product_old_price'] = 0.0000
        self.pr['product_buy_price'] = 0.0000
        self.pr['product_price'] = 0.000000
        self.pr['min_price'] = 0.000000
        self.pr['different_prices'] = 0
        self.pr['product_weight'] = 0.0000
        self.pr['image'] = ''
        self.pr['product_manufacturer_id'] = 0
        self.pr['product_is_add_price'] = 0
        self.pr['add_price_unit_id'] = 3
        self.pr['average_rating'] = 0.00
        self.pr['reviews_count'] = 0
        self.pr['delivery_times_id'] = 0
        self.pr['hits'] = 0
        self.pr['weight_volume_units'] = 32
        self.pr['basic_price_unit_id'] = 3
        self.pr['label_id'] = 0
        self.pr['vendor_id'] = 0
        self.pr['access'] = 1
        self.pr['name_en-GB'] = ''
        self.pr['alias_en-GB'] = ''
        self.pr['short_description_en-GB'] = ''
        self.pr['description_en-GB'] = ''
        self.pr['meta_title_en-GB'] = ''
        self.pr['meta_description_en-GB'] = ''
        self.pr['meta_keyword_en-GB'] = ''
        self.pr['name_ru-RU'] = 'Пробный 2'
        self.pr['alias_ru-RU'] = 'probnyj-2'
        self.pr['short_description_ru-RU'] = ''
        self.pr['description_ru-RU'] = ''
        self.pr['meta_title_ru-RU'] = ''
        self.pr['meta_description_ru-RU'] = ''
        self.pr['meta_keyword_ru-RU'] = ''
       # self.pr['extra_field_1'] = ''
       # self.pr['extra_field_2'] = '0'






    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    ''''''
    def __str__(self):
        not_to_show = ['product_availability', 'product_url', 'image', 'product_date_added', 'date_modify',
                       'product_template', 'currency_id', 'add_price_unit_id', 'basic_price_unit_id', 'access',
                       'name_en-GB', 'alias_en-GB', 'short_description_en-GB', 'description_en-GB', 'meta_title_en-GB',
                       'meta_description_en-GB', 'meta_keyword_en-GB', 'meta_title_ru-RU', 'meta_description_ru-RU',
                       'meta_keyword_ru-RU', 'manufacturer_code']

        v=''
        for key in self.pr:
            result=str(self.pr[key])
            if  (len(result)>-10) and result!='0'  and result!='0.000000' and result!='0.0000' and result!='0.000' and result!='0.0' and result!='0.00' :
                if  (key not in not_to_show ) :
                    v=v+' '+key+'='+ result+';'
        v=v+ 'categ=' + str(self.categ)
        v = v + 'manuf_name=' + self.manufacturer_name

        return str(v)


    def printit(self):

        str2 = " ID=" + str(self.pr['product_id'])
        str1 = " Articul=" + self.pr['product_ean']
        str4 = " Category=" + str(self.categ)
        str3 = " Price=" + str(self.pr['product_price'])
        str5 = " Title=" + self.pr['name_ru-RU']
        print(str2+ '____________' + str1 +'____________' + str3+'____________' +  str4 )





















