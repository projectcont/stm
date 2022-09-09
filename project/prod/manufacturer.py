def get_manuf_name (manuf_id, manufcorresp):
    manuf_name=""
    for key in manufcorresp:
        if  (manuf_id==key):
            manuf_name=manufcorresp[key]
    return manuf_name




def get_manuf_id (manuf_name, manufcorresp):
    manuf_id=""
    for key in manufcorresp:
        manuf_real=manufcorresp[key]
        if  (  manuf_name.find(manuf_real)>-1 ) :
            manuf_id = key
    return manuf_id




manufcorresp = {1: "ARCOROC",
                2:"ATTRIBUTE",
                3:"DOMENIK",
                4:"FIORETTA",
                5:"GUIDU",
                6:"LUMINARC",
                7:"OSZ",
                8:"BRIVERRE",
                9:"COK",
                10:"C&S",
                11:"CRISTAL",
                12:"ECLAT",
                13:"ENDURA",
                14:"SHELLEY",
                15:"KEYLINK",
                16:"ZHAN",
                18:"SIJ",
                20:"HUNAN",
                21:"HUAWANG",
                22:"ZEAL",
                23:"JINGTAO",
                24:"PERSONALITY",
                25:"ILLA",
                26:"PYREX",
                27:"RISOLI",
                28:"TVS",
                29:"STOR",
                30:"EKA",
                31:"ERSEL",
                32:"TIANJIN",
                33:"FIFA",
                36:"HUAFEI",
                37:"YUNLONG",
                38:"LESHEROS",
                39:"SHALL",
                40:"DOMCRAFT",
                41:"ROZENBAL",
                42:"CURVER",
                43:"NIKA",
                44:"POLIMERBYT",
                45:"VIOLET",
                46:"DEM",
                47:"HOME CENTERS",
                48:"SEGA",
                49:"VIM-ART",
                50:"JINGTAO",
                51:"GP&ME",
                52:"PEDRINI",
                53:"RENGA",
                54:"FENGHUA",
                55:"HUAFEI",
                56:"ARC INTERNATIONAL",
                57:"ARCOPAL",
                58:"CARTORAMA",
                59:"GARDEN ART",
                60:"GREEN WAY",
                61:"HELLO KITTY",
                62:"MONETA",
                63:"NINGBO",
                64:"PAPSTAR",
                65:"SAN MIGUEL",
                66:"SPAAS",
                67:"TAISUN",
                68:"WALTHER-GLAS",
                69:"WENKO",
                70:"YILIDA",
                71:"YUZHOU",
                72:"DOGRULAR",
                73:"KIS ",
                74:"LAOBO",
                75:"TYFOON",
                76:"VILEDA",
                77:"KETER",
                78:"ALLIBERT ",
                79:"ARCOPAL",
                80:"GHIDINI",
                81:"ARO",
                82:"HAUSHALT",
                83:"MULTIPL2000 ",
                84:"SHUNXIANG",
                85:"ZIBO",
                86:"METRO PROFESSIONAL",
                87:"HUA",
                88:"CMIELOW ",
                89:"RADIAN",
                90:"YUEFENG",
                91:"FUNBOX",
                }




