from django.core.management.base import BaseCommand

from product.models import Product


products = [
    {
        'barcode': 7891000300503,
        'name': 'CAFE SOLUV NESCAFE ORIG VD 100G',
    },
    {
        'barcode': 7896005800157,
        'name': 'CAPPUCCINO 3 CORACOES CLASSIC 200G',
    },
    {
        'barcode': 5601252231058,
        'name': 'AZEITE DE OLIVA GALLO PORTUGAL LT 200ML',
    },
    {
        'barcode': 7896005202074,
        'name': 'FARINHA DE TRIGO DONA BENTA ESPECIAL 1KG',
    },
    {
        'barcode': 7896005232705,
        'name': 'FARINHA DE TRIGO DONA BENTA COM FERMENTO 1KG',
    },
    {
        'barcode': 7896102502909,
        'name': 'CATCHUP TP QUERO TRAD 300G',
    },
    {
        'barcode': 7891700011006,
        'name': 'TEMPERO ARISCO COMPLETO COM PIMENTO PT 300G',
    },
    {
        'barcode': 7891132019038,
        'name': 'TEMPERO SABOR AMI COMPLETO 300G',
    },
    {
        'barcode': 7891700012102,
        'name': 'TEMPERO ARISCO ALHO E SAL PT 300G',
    },
    {
        'barcode': 7891132019045,
        'name': 'TEMPERO SABOR AMI COM PIMENTA 300G',
    },
    {
        'barcode': 7891132019021,
        'name': 'TEMPERO SABOR AMI ALHO E SAL 300G',
    },
    {
        'barcode': 7891000502303,
        'name': 'AMAC DE CARNE MAGGI 120G',
    },
    {
        'barcode': 7891132019717,
        'name': 'TEMPERO SAZON LARANJA MASSAS 60G',
    },
    {
        'barcode': 7891132019403,
        'name': 'TEMPERO SAZON AMARELO LEGUMES 60G',
    },
    {
        'barcode': 7891132019724,
        'name': 'TEMPERO SAZON MARROM FEIJAO 60G',
    },
    {
        'barcode': 7894000200019,
        'name': 'FARINHA MAIZENA CREMOGEMA TRADICIONAL 500G',
    },
    {
        'barcode': 7894000010021,
        'name': 'AMIDO DE MILHO MAIZENA 500G',
    },
    {
        'barcode': 7894000200026,
        'name': 'FARINHA MAIZENA CREMOGEMA TRADICIONAL 200G',
    },
    {
        'barcode': 7894000200057,
        'name': 'FARINHA MAIZENA CREMOGEMA CHOCOLATE 200G',
    },
    {
        'barcode': 7894000010014,
        'name': 'AMIDO DE MILHO MAIZENA 200G',
    },
    {
        'barcode': 7894000200095,
        'name': 'FARINHA MAIZENA CREMOGEMA MORANGO 200G',
    },
    {
        'barcode': 7894000210025,
        'name': 'AMIDO DE MILHO ARROZINA 200G',
    },
    {
        'barcode': 7622300119621,
        'name': 'FERMENTO PO ROYAL 100G',
    },
    {
        'barcode': 7894321722016,
        'name': 'BEB LAC TODDYNHO CHOCOLATE 200ML',
    },
    {
        'barcode': 7894321711171,
        'name': 'ACHOC PO PT TODDY ORIGINAL 200G',
    },
    {
        'barcode': 7891000252604,
        'name': 'FARINHA LACTEA NESTLE LT 400G',
    },
    {
        'barcode': 7891000142202,
        'name': 'LEITE EM PO NESTLE NINHO INSTANTANEO LT 400G',
    },
    {
        'barcode': 7891000100103,
        'name': 'LEITE CONDI MOCA ABRE FACIL LT 395G',
    },
    {
        'barcode': 7891000155806,
        'name': 'SOBREMESA NESTLE MOCA BRIGADEIRO LT 385G',
    },
    {
        'barcode': 7891136051003,
        'name': 'BEB ALC COCKTAIL CAMPARI GF 900ML',
    },
    {
        'barcode': 7896072911145,
        'name': 'SIDRA CERESER MACA  660ML',
    },
    {
        'barcode': 7896002100014,
        'name': 'BEB ALC AGUARDENTE CANINHA 51 GF 965ML',
    },
    {
        'barcode': 7896002108034,
        'name': 'BEB ALC CONHAQUE DOMUS GENGIBRE GF 1L',
    },
    {
        'barcode': 7896022610005,
        'name': 'BEB ALC CONHAQUE S J DA BARRA GF 900ML',
    },
    {
        'barcode': 7896780900196,
        'name': 'VINHO TINTO SUAVE CANCAO 750ML',
    },
    {
        'barcode': 7891200007899,
        'name': 'COLA LOCTITE DUREPOXI 100G',
    },
    {
        'barcode': 7891010032906,
        'name': 'SAB INF JOHNSONS BABY REGULAR 80G',
    },
    {
        'barcode': 7891038352109,
        'name': 'SAB LUX SUAVE BUQUE DOS SONHOS 90G',
    },
    {
        'barcode': 7891024111901,
        'name': 'SAB PALMOLIVE ALOE E OLIVA 90G',
    },
    {
        'barcode': 7896090400027,
        'name': 'SAB FRANCIS CEREJEIRA DO ORIENTE 90G',
    },
    {
        'barcode': 7891024119105,
        'name': 'SAB PROTEX FRESH 90G',
    },
    {
        'barcode': 7891024113905,
        'name': 'SAB PROTEX ULTRA 90G',
    },
    {
        'barcode': 7891024113707,
        'name': 'SAB PROTEX SUAVE 90G',
    },
    {
        'barcode': 7896094924611,
        'name': 'LOCAO CORP LEITE DE COLONIA TRADICIONAL 100ML',
    },
    {
        'barcode': 7896094924635,
        'name': 'LOCAO CORP LEITE DE COLONIA TRADICIONAL 200ML',
    },
    {
        'barcode': 7896806700021,
        'name': 'DESOD CORP LEITE DE ROSAS TRADICIONAL 100ML',
    },
    {
        'barcode': 7891176111040,
        'name': 'COND NEUTROX CLASSICO BRILHO NUTRICAO 100ML',
    },
    {
        'barcode': 7891176111064,
        'name': 'COND NEUTROX CLASSICO BRILHO NUTRICAO 230ML',
    },
    {
        'barcode': 7896094908659,
        'name': 'HIDRAT CORP MONANGE FRUTAS VERMELHAS  200ML',
    },
    {
        'barcode': 7896094908673,
        'name': 'HIDRAT CORP MONANGE FLOR DE LAVANDA 200ML',
    },
    {
        'barcode': 78907874,
        'name': 'OLEO CORP PAIXAO INSPIRADORA 200ML',
    },
    {
        'barcode': 78907881,
        'name': 'OLEO CORP PAIXAO SEDUCAO 200ML',
    },
    {
        'barcode': 78907867,
        'name': 'HIDRAT CORP PAIXAO SEDUTORA 200ML',
    },
    {
        'barcode': 7891176113020,
        'name': 'COND KOLENE ORIGINAL 90ML',
    },
    {
        'barcode': 7891176113044,
        'name': 'COND KOLENE ORIGINAL 300ML',
    },
    {
        'barcode': 7891176113068,
        'name': 'COND KOLENE ORIGINAL 500ML',
    },
    {
        'barcode': 7896094907546,
        'name': 'DESOD SPRAY TRES MARCHAND CLASSIC 100ML',
    },
    {
        'barcode': 7891528038025,
        'name': 'CD SORRISO DENTES BRANCOS 50G',
    },
    {
        'barcode': 7891528030142,
        'name': 'CD SORRISO DENTES BRANCOS 90G',
    },
    {
        'barcode': 7891037744356,
        'name': 'CD CLOSE UP ACAO PROFUNDA RED HOT 90G',
    },
    {
        'barcode': 7891528038827,
        'name': 'CD TANDY TUTTI FRUTTI 50G',
    },
    {
        'barcode': 7891150037595,
        'name': 'SH SEDA CACHOS DEFINIDOS 350ML',
    },
    {
        'barcode': 7891150037526,
        'name': 'SH SEDA PRETOS LUMINOSOS 325ML',
    },
    {
        'barcode': 7891150037397,
        'name': 'SH SEDA CERAMIDAS 325ML',
    },
    {
        'barcode': 7891150037342,
        'name': 'COND SEDA PRETOS LUMINOSOS 350ML',
    },
    {
        'barcode': 7891035500008,
        'name': 'LUSTRA MOVEIS POLIFLOR JASMIM 200ML',
    },
    {
        'barcode': 7891022639001,
        'name': 'DETERG LIMPOL MACA 500ML',
    },
    {
        'barcode': 7891022638004,
        'name': 'DETERG LIMPOL NEUTRO 500ML',
    },
    {
        'barcode': 7891038001205,
        'name': 'SABAO EM PO OMO MULTIACAO 500G',
    },
    {
        'barcode': 7891035210006,
        'name': 'MULTIUSO VEJA ORIGINAL 500ML',
    },
    {
        'barcode': 7896001004528,
        'name': 'ESPONJA MULTIUSO BETTANIN ESFRE BOM PROT UNHA UN',
    },
    {
        'barcode': 7896110091440,
        'name': 'PAPEL HIG PERSONAL FS ORIG NEUTRO 30M 4RL',
    },
    {
        'barcode': 7894650113011,
        'name': 'DETERG DE AUTO CARNU 500ML',
    },
    {
        'barcode': 7896094910904,
        'name': 'ADOCANTE LIQ ZERO CAL 100ML',
    },
    {
        'barcode': 7891149200504,
        'name': 'CERVEJA LT SKOL 350ML',
    },
    {
        'barcode': 7894900030013,
        'name': 'REFRIGERANTE LT FANTA LARANJA 350ML',
    },
    {
        'barcode': 7894900010015,
        'name': 'REFRIGERANTE LT COCA COLA 350ML',
    },
    {
        'barcode': 7894900051513,
        'name': 'REFRIGERANTE PET FANTA UVA 2L',
    },
    {
        'barcode': 7894900031515,
        'name': 'REFRIGERANTE PET FANTA LARANJA 2L',
    },
    {
        'barcode': 7894900011517,
        'name': 'REFRIGERANTE PET COCA COLA 2L',
    },
    {
        'barcode': 7891991001373,
        'name': 'REFRIGERANTE PET ANTARCTICA GUARANA DIET 2L',
    },
    {
        'barcode': 7896009724015,
        'name': 'PILHA RAYOVAC ALCALINA AAA 2UND',
    },
    {
        'barcode': 7896067203026,
        'name': 'BATERIA PANASONIC SUPER HYPER 9V',
    },
    {
        'barcode': 7896010000375,
        'name': 'WHISKY OLD EIGHT 1L',
    },
    {
        'barcode': 7896080001104,
        'name': 'WHISKY TEACHERS HIGHLAND CREAM 1L',
    },
    {
        'barcode': 7893000340107,
        'name': 'MORTADELA MISTA SADIA FAMILIAR 1KG',
    },
    {
        'barcode': 7896102502213,
        'name': 'EXT DE TOMATE QUERO VD 190G',
    },
    {
        'barcode': 7891080400100,
        'name': 'MARGARINA DELICIA COM SAL PT 250G',
    },
    {
        'barcode': 7896010002133,
        'name': 'BEB ALC CONHAQUE DREHER DE GENGIBRE GF 900ML',
    },
    {
        'barcode': 7893000979932,
        'name': 'MARGARINA DELINE COM SAL PT 250G',
    },
    {
        'barcode': 7893000980006,
        'name': 'MARGARINA DELINE COM SAL PT 500G',
    },
    {
        'barcode': 7896058500745,
        'name': 'GOMA DE MASCAR DORI GOMETS 70G',
    },
    {
        'barcode': 7896029027226,
        'name': 'MOLHO MADEIRA UNCLE BENS 340G',
    },
    {
        'barcode': 7896004400075,
        'name': 'LEITE DE COCO SOCOCO TRADICIONAL 200ML',
    },
    {
        'barcode': 78907058,
        'name': 'AMAC FOFO TRADICIONAL AZUL 500ML',
    },
    {
        'barcode': 7894650112014,
        'name': 'CERA AUTO PASTA CARNU SILICONE 200G',
    },
    {
        'barcode': 7894650101018,
        'name': 'CERA AUTO PASTA GRAND PRIX TRADICIONAL 200G',
    },
    {
        'barcode': 7891000379103,
        'name': 'BEB LAC NESCAU CHOCOLATE 200ML',
    },
    {
        'barcode': 7896050500019,
        'name': 'OLEO PEROBA NOVO KING 200ML',
    },
    {
        'barcode': 7894000010038,
        'name': 'AMIDO DE MILHO MAIZENA 1KG',
    },
    {
        'barcode': 7893333229001,
        'name': 'GELATINA ROYAL SEM SABOR INCOLOR 24G',
    },
    {
        'barcode': 7891022101249,
        'name': 'DESINF BOM BRIL KALIPTO EUCALIPTO 750ML',
    },
    {
        'barcode': 7891010035976,
        'name': 'SAB INF JOHNSONS GLICERINADO MEL E VITAMINA E 80G',
    },
    {
        'barcode': 7896072911138,
        'name': 'VINHO BRANCO SUAVE CORTEZANO 900ML',
    },
    {
        'barcode': 7896110083254,
        'name': 'GUARDANAPO SANTEPEL FS 50UN',
    },
    {
        'barcode': 7891132019281,
        'name': 'TEMPERO SAZON VERMELHO CARNES 60G',
    },
    {
        'barcode': 7891038127509,
        'name': 'AMAC FOFO AMARELO 2L',
    },
    {
        'barcode': 7891035115103,
        'name': 'LIMP PISO DESTAC LIRIO E MAGNOLIA RECKITT 500ML',
    },
    {
        'barcode': 7891035116001,
        'name': 'LIMP PISO DESTAC LIMAO 500ML',
    },
    {
        'barcode': 7791130002950,
        'name': 'POLIDOR PASTA PARA SAPATOS NUGGET MARRON 36G',
    },
    {
        'barcode': 7891134001819,
        'name': 'SAB SENADOR CLASSIC 130G',
    },
    {
        'barcode': 7891035651007,
        'name': 'INSET AER DETEFON ACAO TOTAL CLASSICO 300ML',
    },
    {
        'barcode': 78899,
        'name': 'DESODOR DE AMBI BOM AR LAVANDA 360ML',
    },
    {
        'barcode': 7891134001710,
        'name': 'SAB ALMA DE FLORES ESSENCIAS 130G',
    },
    {
        'barcode': 7891528038810,
        'name': 'CD TANDY MORANGO 50G',
    },
    {
        'barcode': 7891132019274,
        'name': 'TEMPERO SAZON VERDE FRANGO 60G',
    },
    {
        'barcode': 7896094908642,
        'name': 'HIDRAT CORP MONANGE FLOR DE CEREJA 200ML',
    },
    {
        'barcode': 7891024194102,
        'name': 'DESINF PINHO SOL ORIGINAL 500ML',
    },
    {
        'barcode': 7891962011295,
        'name': 'TORRADA BAUDUCCO LIGHT 160G',
    },
    {
        'barcode': 7891962000251,
        'name': 'TORRADA BAUDUCCO LEVEMENTE SALGADA 160G',
    },
    {
        'barcode': 7891035502200,
        'name': 'LUSTRA MOVEIS POLIFLOR LAVANDA 200ML',
    },
    {
        'barcode': 7891037000322,
        'name': 'CR PENT SEDA CACHOS COMPORTADOS 300ML',
    },
    {
        'barcode': 7891048043035,
        'name': 'AROMA DR OETKER BAUNILHA 30ML',
    },
    {
        'barcode': 7896001004511,
        'name': 'ESPONJA MULTIUSO BETTANIN BRILHUS REF 451',
    },
    {
        'barcode': 7896009400049,
        'name': 'CD SENSODYNE ORIGINAL 50G',
    },
    {
        'barcode': 7891035060007,
        'name': 'LIMPA ALUMINIO LIQ BRASSO 200ML',
    },
    {
        'barcode': 7896102502220,
        'name': 'EXT DE TOMATE QUERO CP 260G',
    },
    {
        'barcode': 7891176111088,
        'name': 'COND NEUTROX CLASSICO BRILHO NUTRICAO 500ML',
    },
    {
        'barcode': 7891024134702,
        'name': 'CD COLGATE MPA MENTA REFRESCANTE 90G',
    },
    {
        'barcode': 7891024132906,
        'name': 'CD COLGATE MPA MENTA REFRESCANTE 50G',
    },
    {
        'barcode': 7891010036478,
        'name': 'TALCO INF JOHNSONS BABY HORA DO SONO 200G',
    },
    {
        'barcode': 7891022640007,
        'name': 'DETERG LIMPOL COCO 500ML',
    },
    {
        'barcode': 7896001004504,
        'name': 'ESPONJA MULTIUSO BETTANIN ESFRE BOM UND',
    },
    {
        'barcode': 7896017821522,
        'name': 'PEDRA SANIT DESODOR LAVANDA BOUQUET UND',
    },
    {
        'barcode': 7891037144705,
        'name': 'CR PENT SEDA CERAMIDAS 300ML',
    },
    {
        'barcode': 7891000156209,
        'name': 'SOBREMESA NESTLE MOCA CHOCOLATE CREMOSO LT 380G',
    },
    {
        'barcode': 7891010032241,
        'name': 'TALCO INF JOHNSONS 200G',
    },
    {
        'barcode': 7891991001342,
        'name': 'REFRIGERANTE PET ANTARCTICA GUARANA 2L',
    },
    {
        'barcode': 7891132082018,
        'name': 'TEMPERO AJINOMOTO SAL 100G S/PIMENTA',
    },
    {
        'barcode': 7891000389201,
        'name': 'BEB LAC NESTLE NESQUIK MORANGO 200ML',
    },
    {
        'barcode': 7891000197103,
        'name': 'IOG POLPA NESTLE NINHO SOLEIL MORANGO 8UN 360G',
    },
    {
        'barcode': 7896017821546,
        'name': 'PEDRA SANIT DESODOR FLORAL UN',
    },
    {
        'barcode': 7894900061512,
        'name': 'REFRIGERANTE PET SPRITE LIMAO 2L',
    },
    {
        'barcode': 7897664100039,
        'name': 'SABAO EM BARRA MINUANO AZUL 5UND 1KG',
    },
    {
        'barcode': 7897664100053,
        'name': 'SABAO EM BARRA MINUANO LIMAO VERDE 5UND 1KG',
    },
    {
        'barcode': 7891150037250,
        'name': 'COND SEDA CERAMIDAS 325ML',
    },
    {
        'barcode': 7891182850117,
        'name': 'ESMALTE RISQUE NUDES MELISSA 8ML',
    },
    {
        'barcode': 7891700011204,
        'name': 'TEMPERO ARISCO COMPLETO SEM PIMENTA PT 300G',
    },
    {
        'barcode': 7891104393104,
        'name': 'ADOCANTE LIQ ADOCYL SACARINA 100ML',
    },
    {
        'barcode': 7891000126905,
        'name': 'CREME DE LEITE TP NESTLE 200G',
    },
    {
        'barcode': 7894900050011,
        'name': 'REFRIGERANTE LT FANTA UVA 350ML',
    },
    {
        'barcode': 7891700018081,
        'name': 'CATCHUP TP ARISCO TRADICIONAL 300G',
    },
    {
        'barcode': 7896009400162,
        'name': 'CD SENSODYNE EXTRA FRESH 50G',
    },
    {
        'barcode': 7891528038001,
        'name': 'CD SORRISO DENTES BRANCOS 180G',
    },
    {
        'barcode': 7891010030094,
        'name': 'SH INF JOHNSONS BABY TRADICIONAL 200ML',
    },
    {
        'barcode': 7891010030889,
        'name': 'SH INF JOHNSONS BABY CABELOS CLAROS 200ML',
    },
    {
        'barcode': 7896221800016,
        'name': 'TINTURA MARCIA PRETO 10',
    },
    {
        'barcode': 7896221800023,
        'name': 'TINTURA MARCIA CASTANHO CLARO 50',
    },
    {
        'barcode': 7896221800030,
        'name': 'TINTURA MARCIA CASTANHO ESCURO 30',
    },
    {
        'barcode': 7891000451304,
        'name': 'ACHOC PO SOLUV NESTLE 200G',
    },
    {
        'barcode': 7891350002409,
        'name': 'CR BARBEAR BOZZANO MENTOLADO REFRESCANTE 65G',
    },
    {
        'barcode': 7896110000176,
        'name': 'PAPEL HIG PERSONAL VIP FD NEUTRO 30M 4RL',
    },
    {
        'barcode': 7891528038704,
        'name': 'CD PREVENT ANTI PLACA 90G',
    },
    {
        'barcode': 7898941911058,
        'name': 'SUSTAGEN KIDS BAUNILHA LATA 380G',
    },
    {
        'barcode': 7891000155905,
        'name': 'SOBREMESA NESTLE MOCA BEIJINHO LT 365G',
    },
    {
        'barcode': 4005808257553,
        'name': 'DESOD ROLL ON NIVEA MEN DRY IMPACT PLUS 48H 50ML',
    },
    {
        'barcode': 7896013500193,
        'name': 'CR ALISANTE AMACIHAIR RELAXA TRAD',
    },
    {
        'barcode': 7896009728013,
        'name': 'PILHA RAYOVAC ALCALINA AA 2UN',
    },
    {
        'barcode': 7894900910018,
        'name': 'REFRIGERANTE LT KUAT 350ML',
    },
    {
        'barcode': 7894900911510,
        'name': 'REFRIGERANTE PET KUAT 2L',
    },
    {
        'barcode': 7891528038612,
        'name': 'CD SORRISO FRESH PLUS HORTELA EXPLOSION 90G',
    },
    {
        'barcode': 7891528038629,
        'name': 'CD SORRISO FRESH PLUS MENTA HIT 90G',
    },
    {
        'barcode': 41333001043,
        'name': 'BATERIA DURACELL 9V',
    },
    {
        'barcode': 7896017821591,
        'name': 'PEDRA SANIT DESODOR BRISA FLORAL',
    },
    {
        'barcode': 7894900060010,
        'name': 'REFRIGERANTE LT SPRITE 350ML',
    },
    {
        'barcode': 7891182840323,
        'name': 'ESMALTE RISQUE TERROSOS DARA 8ML',
    },
    {
        'barcode': 7896110093444,
        'name': 'PAPEL HIG CHARME FD NEUTRO 30M 4RL',
    },
    {
        'barcode': 7891037744509,
        'name': 'GEL DENTAL CLOSE UP ICE LIQUIFRESH 100G',
    },
    {
        'barcode': 7896014123902,
        'name': 'COND ELSEVE PARIS COLOR VIVE 200ML',
    },
    {
        'barcode': 7897110000500,
        'name': 'BEB ALC AGUARDENTE PEDRA 90 500ML',
    },
    {
        'barcode': 7501009222729,
        'name': 'AP BARB PRESTOBARBA ULTRAGRIP 2UN',
    },
    {
        'barcode': 611269991000,
        'name': 'BEB ENERG RED BULL LT 250ML',
    },
    {
        'barcode': 41333001074,
        'name': 'PILHA DURACELL PEQ AAA 2UN',
    },
    {
        'barcode': 7891022848052,
        'name': 'DESINF BOM BRIL KALIPTO MARINE 750ML',
    },
    {
        'barcode': 7891182120050,
        'name': 'DESOD SPRAY CONTOURE PRIMEIRO AMOR 80ML',
    },
    {
        'barcode': 7891182120067,
        'name': 'DESOD SPRAY CONTOURE LAVANDA FRESH 80ML',
    },
    {
        'barcode': 7891182860116,
        'name': 'ESMALTE RISQUE BRANCOS CRISTAL 8ML',
    },
    {
        'barcode': 7791293784465,
        'name': 'DESOD AER REXONA WOMEN COTTON 175ML',
    },
    {
        'barcode': 7891010030452,
        'name': 'COND INF JOHNSONS BABY TRADICIONAL 200ML',
    },
    {
        'barcode': 7891010030476,
        'name': 'COND INF JOHNSONS BABY CABELOS CLAROS 200ML',
    },
    {
        'barcode': 7891132000449,
        'name': 'TEMPERO SAZON BRANCO ARROZ 60G',
    },
    {
        'barcode': 7898157614545,
        'name': 'TALCO INF GALINHA PINTADINHA 200G',
    },
    {
        'barcode': 7893000394117,
        'name': 'MARGARINA QUALY COM SAL 250G',
    },
    {
        'barcode': 7891024114001,
        'name': 'SAB PROTEX CREAM 90G',
    },
    {
        'barcode': 7891182840095,
        'name': 'ESMALTE RISQUE ROSAS ASTRAL 8ML',
    },
    {
        'barcode': 7896017821515,
        'name': 'PEDRA SANIT DESODOR LAVANDA FRESH',
    },
    {
        'barcode': 7891024132005,
        'name': 'CD COLGATE TRIPLA ACAO MENTA ORIGINAL 90G',
    },
    {
        'barcode': 7891000812105,
        'name': 'MACARRAO INST MAGGI GALINHA 85G',
    },
    {
        'barcode': 7891000812006,
        'name': 'MACARRAO INST MAGGI CARNE 85G',
    },
    {
        'barcode': 7891350011043,
        'name': 'CR BARBEAR BOZZANO HIDRATACAO ALOE VERA 65G',
    },
    {
        'barcode': 7891037009820,
        'name': 'CD CLOSE UP TRIPLE HORTELA 90G',
    },
    {
        'barcode': 7891037009844,
        'name': 'CD CLOSE UP TRIPLE MENTA 90G',
    },
    {
        'barcode': 7896009419270,
        'name': 'CD SENSODYNE MULTI PROTECCION 50G',
    },
    {
        'barcode': 7891182840200,
        'name': 'ESMALTE RISQUE VERMELHOS GABRIELA 8ML',
    },
    {
        'barcode': 7897664130029,
        'name': 'DETERG MINUANO LIMAO 500ML',
    },
    {
        'barcode': 7897664130043,
        'name': 'DETERG MINUANO FRESH 500ML',
    },
    {
        'barcode': 7891000140307,
        'name': 'LEITE EM PO NESTLE NINHO INTEGRAL LT 400G',
    },
    {
        'barcode': 7897664130012,
        'name': 'DETERG MINUANO MACA 500ML',
    },
    {
        'barcode': 7897664130036,
        'name': 'DETERG MINUANO NEUTRO 500ML',
    },
    {
        'barcode': 7896224813082,
        'name': 'CAFE ALMOFADA SANTA CLARA SC 250G',
    },
    {
        'barcode': 7896224814126,
        'name': 'CAFE VACUO SANTA CLARA 250G',
    },
    {
        'barcode': 7891700080415,
        'name': 'CALDO ARISCO GALINHA CAIPIRA 57G',
    },
    {
        'barcode': 7894000000275,
        'name': 'CALDO KNORR GALINHA 57G',
    },
    {
        'barcode': 7891528038568,
        'name': 'CD SORRISO FRESH PLUS MENTHOL IMPACT 90G',
    },
    {
        'barcode': 7894000047515,
        'name': 'SUCO COM LEITE DE SOJA TP ADES PESSEGO 1L',
    },
    {
        'barcode': 7891132019731,
        'name': 'TEMPERO SAZON VERDE LIMAO SALADAS 60G',
    },
    {
        'barcode': 7896102504064,
        'name': 'AZEITONA EM CONSERVA QUERO SEM CAROCO 155G',
    },
    {
        'barcode': 7894000181011,
        'name': 'SUCO COM LEITE DE SOJA TP ADES LARANJA 1L',
    },
    {
        'barcode': 7894000182018,
        'name': 'SUCO COM LEITE DE SOJA TP ADES MACA 1L',
    },
    {
        'barcode': 7896003703238,
        'name': 'BISC CREAM CRACKER MARILAN MANTEIGA 400G',
    },
    {
        'barcode': 7891150037465,
        'name': 'COND SEDA CACHOS COMPORTADOS 325ML',
    },
    {
        'barcode': 7896050500071,
        'name': 'OLEO MAQ KING MULTI-USO 100ML',
    },
    {
        'barcode': 7896050500873,
        'name': 'VASELINA KING 1L',
    },
    {
        'barcode': 7891010087722,
        'name': 'ABS CAREFREE PROTECAO PERFUMADO 15UN',
    },
    {
        'barcode': 7896221800092,
        'name': 'AGUA OXIG CREM MARCIA 20V 70ML',
    },
    {
        'barcode': 7896221800108,
        'name': 'AGUA OXIG CREM MARCIA 30V 70ML',
    },
    {
        'barcode': 7896221800115,
        'name': 'AGUA OXIG CREM MARCIA 40V 70ML',
    },
    {
        'barcode': 7891010560737,
        'name': 'HASTES FLEXI JOHNSONS COTONETE ANTIGERME 75UND',
    },
    {
        'barcode': 7896004814162,
        'name': 'HASTES FLEXI TOPZ ANTIGERME 75UN',
    },
    {
        'barcode': 7896075709107,
        'name': 'TESOURA PARA UNHA MERHEJE BASIC CURVA',
    },
    {
        'barcode': 7891107111910,
        'name': 'OLEO DE GIRASSOL SALADA PET 900ML',
    },
    {
        'barcode': 7501001169374,
        'name': 'ABS ALWAYS TOTAL PROTEC NOTURNO C SECA C ABAS 8UND',
    },
    {
        'barcode': 7896098900109,
        'name': 'SABAO EM BARRA YPE NEUTRO 1KG',
    },
    {
        'barcode': 7893218000107,
        'name': 'BEB ALC COCKTAIL SMIRNOFF ICE GF 275ML',
    },
    {
        'barcode': 7893000650138,
        'name': 'LING CALABRESA SADIA 500G',
    },
    {
        'barcode': 7897664150027,
        'name': 'AMAC MINUANO PETALAS DE ROSAS E JASMIM 2L',
    },
    {
        'barcode': 7891152321197,
        'name': 'BISC CREAM CRACKER FORTALEZA 400G',
    },
    {
        'barcode': 7896058500738,
        'name': 'AMENDOIM DORI JAPONES SALGADO 70G',
    },
    {
        'barcode': 78924338,
        'name': 'DESOD ROLL ON REXONA POWDER 48H  50ML',
    },
    {
        'barcode': 7896072911800,
        'name': 'SUCO CERESER XAROPE GROSELHA 1L',
    },
    {
        'barcode': 7896003703177,
        'name': 'BISC INT CREAM CRACKER MARILAN 420G',
    },
    {
        'barcode': 5601252231287,
        'name': 'AZEITE DE OLIVA GALLO TIPO UNICO LT 500ML',
    },
    {
        'barcode': 7896085813467,
        'name': 'KIT CR ALISANTE ORIGEM ERVAS CEREAIS GRTS CR PENT',
    },
    {
        'barcode': 7896085813450,
        'name': 'KIT CR ALISANTE ORIGEM FLORES FRUTAS 80G',
    },
    {
        'barcode': 7891000522103,
        'name': 'TEMPERO MAGGI CARNE 21G',
    },
    {
        'barcode': 7891000528709,
        'name': 'TEMPERO MAGGI GALINHA 63G',
    },
    {
        'barcode': 7896085813443,
        'name': 'KIT CR ALISANTE ORIGEM MEL AMENDOA GRTS CR PENT',
    },
    {
        'barcode': 7891172421174,
        'name': 'PAPEL HIG NEVE FD NEUTRO 30M 4RL',
    },
    {
        'barcode': 7896005280911,
        'name': 'MIST PARA BOLO DONA BENTA CENOURA 450G',
    },
    {
        'barcode': 41333001005,
        'name': 'PILHA DURACELL ALCALINA AA2 2UND',
    },
    {
        'barcode': 7896058500714,
        'name': 'AMENDOIM DORI CONFEITADO COLORIDO 70G',
    },
    {
        'barcode': 7896058500721,
        'name': 'AMENDOIM DORI CHOCOLATE 70G',
    },
    {
        'barcode': 78902114,
        'name': 'ESC DENT COLGATE TWISTE PLUS MACIA SUAVE REF 2114',
    },
    {
        'barcode': 7896052600090,
        'name': 'REFRIGERANTE PET SCHIN LARANJA 2L',
    },
    {
        'barcode': 7896052600069,
        'name': 'REFRIGERANTE PET SCHIN LIMAO 2L',
    },
    {
        'barcode': 7894000001159,
        'name': 'SUCO COM LEITE DE SOJA TP ADES UVA 1L',
    },
    {
        'barcode': 7891035621109,
        'name': 'REPELENTE CR REPELEX FAMILY CARE 100ML',
    },
    {
        'barcode': 78914971,
        'name': 'HIDRAT CORP PAIXAO RADIANTE FELICIDADE 200ML',
    },
    {
        'barcode': 78914940,
        'name': 'OLEO CORP PAIXAO IRRESISTIVEL 200ML',
    },
    {
        'barcode': 7896045512317,
        'name': 'CERVEJA LT KAISER LAGER 350ML',
    },
    {
        'barcode': 7896005272022,
        'name': 'MIST PARA BOLO DONA BENTA LARANJA 450G',
    },
    {
        'barcode': 7896005272046,
        'name': 'MIST PARA BOLO DONA BENTA COCO 450G',
    },
    {
        'barcode': 7896005272060,
        'name': 'MIST PARA BOLO DONA BENTA FESTA 450G',
    },
    {
        'barcode': 7896005272084,
        'name': 'MIST PARA BOLO DONA BENTA ABACAXI 450G',
    },
    {
        'barcode': 7896005272145,
        'name': 'MIST PARA BOLO DONA BENTA LIMAO 450G',
    },
    {
        'barcode': 7894900563702,
        'name': 'SUCO DEL VALLE KAPO LARANJA 200ML',
    },
    {
        'barcode': 7894900573701,
        'name': 'SUCO DEL VALLE KAPO MARACUJA 200ML',
    },
    {
        'barcode': 7894900593709,
        'name': 'SUCO DEL VALLE KAPO UVA 200ML',
    },
    {
        'barcode': 7898286190132,
        'name': 'VINAGRE MARATA ALCOOL 500ML',
    },
    {
        'barcode': 7891173021793,
        'name': 'PAPEL OFICIO A4 CHAMEQUINHO BRANCO 100FLS',
    },
    {
        'barcode': 7894000030470,
        'name': 'MAIONESE HELLMANNS SC 200G',
    },
    {
        'barcode': 7896005272008,
        'name': 'MIST PARA BOLO DONA BENTA CHOCOLATE 450G',
    },
    {
        'barcode': 7894900603705,
        'name': 'SUCO DEL VALLE KAPO ABACAXI 200ML',
    },
    {
        'barcode': 7894900583700,
        'name': 'SUCO DEL VALLE KAPO MORANGO 200ML',
    },
    {
        'barcode': 7891182006781,
        'name': 'DESOD SPRAY CONTOURE AMOR DA MINHA VIDA 80ML',
    },
    {
        'barcode': 7891152321180,
        'name': 'BISC CREAM CRACKER AGUA E SAL FORTALEZA 400G',
    },
    {
        'barcode': 7898286200015,
        'name': 'CONDIMENTO MISTO MARATA SC 100G',
    },
    {
        'barcode': 7898286190149,
        'name': 'VINAGRE MARATA ALCOOL 750ML',
    },
    {
        'barcode': 7891000001080,
        'name': 'LEITE EM PO COP NESTLE NINHO PREBIO 1 FASE LT 400G',
    },
    {
        'barcode': 7896110007892,
        'name': 'ABS SYM NOT NOITE E DIA COB SUAVE COM ABAS LV8 PG7',
    },
    {
        'barcode': 7896052601516,
        'name': 'SUCO SKINKA FRUTAS CITRICAS 450ML',
    },
    {
        'barcode': 7896052601523,
        'name': 'SUCO SKINKA FRUTAS VERMELHAS 450ML',
    },
    {
        'barcode': 7898286201272,
        'name': 'CAFE SOLUV PURO REFIL 50G',
    },
    {
        'barcode': 7896083800018,
        'name': 'ALVEJANTE QBOA 1L',
    },
    {
        'barcode': 7791293884592,
        'name': 'DESOD AER REXONA WOMEN BAMBOO 175ML',
    },
    {
        'barcode': 7891035209901,
        'name': 'MULTIUSO VEJA FLORAL 500ML',
    },
    {
        'barcode': 7896098900239,
        'name': 'DETERG YPE COCO 500ML',
    },
    {
        'barcode': 7896098900222,
        'name': 'DETERG YPE LIMAO 500ML',
    },
    {
        'barcode': 7896098900215,
        'name': 'DETERG YPE MACA 500ML',
    },
    {
        'barcode': 7891024131909,
        'name': 'CD COLGATE TRIPLA ACAO MENTA ORIGINAL 50G',
    },
    {
        'barcode': 7891152321173,
        'name': 'BISC MAIZENA FORTALEZA 400G',
    },
    {
        'barcode': 7891152321166,
        'name': 'BISC MARIA FORTALEZA 400G',
    },
    {
        'barcode': 7891155005032,
        'name': 'COPO VD NADIR REF-7700 CYLINDER',
    },
    {
        'barcode': 7896221800153,
        'name': 'TINTURA MARCIA PRETO SUAVE 20',
    },
    {
        'barcode': 7893218000213,
        'name': 'WHISKY BELLS 1L',
    },
    {
        'barcode': 7891037010031,
        'name': 'COND SEDA LISO PERFEITO E SEDOSO 325ML',
    },
    {
        'barcode': 7891037010048,
        'name': 'CR PENT SEDA LISO PERFEITO E SEDOSO 300ML',
    },
    {
        'barcode': 7891150037519,
        'name': 'SH SEDA LISO PERFEITO E SEDOSO 325ML',
    },
    {
        'barcode': 7896052600076,
        'name': 'REFRIGERANTE PET SCHIN GUARANA 2L',
    },
    {
        'barcode': 7896052600083,
        'name': 'REFRIGERANTE PET SCHIN COLA 2L',
    },
    {
        'barcode': 7897664140219,
        'name': 'DESINF MINUANO FLORAL 500ML',
    },
    {
        'barcode': 7897664140226,
        'name': 'DESINF MINUANO EUCALIPTO 500ML',
    },
    {
        'barcode': 7896049508514,
        'name': 'DESOD CR TABU TRAD 55G',
    },
    {
        'barcode': 7891182017077,
        'name': 'ESMALTE RISQUE ESCUROS UVA 8ML',
    },
    {
        'barcode': 7891182017053,
        'name': 'ESMALTE RISQUE VERMELHOS CARMIM 8ML',
    },
    {
        'barcode': 7791293999470,
        'name': 'DESOD AER REXONA WOMEN POWDER 175ML',
    },
    {
        'barcode': 7896085812811,
        'name': 'HIDRAT CAP NAZCA ORIGEM PROTECAO 1KG',
    },
    {
        'barcode': 7896085812842,
        'name': 'HIDRAT CAP NAZCA ORIGEM MACIEZ 1KG',
    },
    {
        'barcode': 7896224800686,
        'name': 'CAFE SOLUV SANTA CLARA CLASSICO VD 50G',
    },
    {
        'barcode': 7896224800693,
        'name': 'CAFE SOLUV SANTA CLARA VD 100G',
    },
    {
        'barcode': 7896224800709,
        'name': 'CAFE SOLUV SANTA CLARA VD 200G',
    },
    {
        'barcode': 7896224800716,
        'name': 'CAFE SOLUV SANTA CLARA REFIL 50G',
    },
    {
        'barcode': 7891528020600,
        'name': 'CD SORRISO SUPER REFRESCANTE 90G',
    },
    {
        'barcode': 7891010030391,
        'name': 'SH INF JOHNSONS CACHOS DEFINIDOS 200ML',
    },
    {
        'barcode': 7898286200060,
        'name': 'CAFE ALMOFADA MARATA 250G',
    },
    {
        'barcode': 7891010034511,
        'name': 'ABS SEMPRE LIVRE ADAPT MAX C SUAVE S ABAS 8UND',
    },
    {
        'barcode': 7896003701913,
        'name': 'BISC RECH MARILAN CHOCOLATE 140G',
    },
    {
        'barcode': 7891022849004,
        'name': 'AMAC BOM BRIL MON BIJOU MAGIA 500ML',
    },
    {
        'barcode': 78910942,
        'name': 'REFRIGERANTE PET ANTARCTICA GUARANA 237ML',
    },
    {
        'barcode': 7891515614072,
        'name': 'EMB DE FRANGO PERDIGAO MEIO PEITO CROSS 1KG',
    },
    {
        'barcode': 7896102502183,
        'name': 'EXT DE TOMATE TP QUERO 130G',
    },
    {
        'barcode': 7891000008119,
        'name': 'CEREAL MATINAL NESCAU 270G',
    },
    {
        'barcode': 7891010035631,
        'name': 'ABS SEMPRE LIVRE MAX SUAVE NOTURNO COM ABAS 8UND',
    },
    {
        'barcode': 7896060010492,
        'name': 'ADOCANTE LIQ ASSUGRIN 100ML',
    },
    {
        'barcode': 7896050200124,
        'name': 'BEB ALC AGUARDENTE VELHO BARREIRO GF 910ML',
    },
    {
        'barcode': 7896224800594,
        'name': 'CAFE VACUO SANTA CLARA DESCAFEINADO 250G',
    },
    {
        'barcode': 4005808516667,
        'name': 'PROT SOLAR SWIM E PLAY FPS 60 150ML',
    },
    {
        'barcode': 7891038080408,
        'name': 'SABAO EM PO ALA FLOR DE MARACUJA E MARGARIDA 500G',
    },
    {
        'barcode': 7891268400076,
        'name': 'ENXAG BUCAL LISTERINE TARTAR CONTROL MENTA 250ML',
    },
    {
        'barcode': 7896486100012,
        'name': 'VINHO TINTO SECO LEAO DO NORTE JURUBEBA 600ML',
    },
    {
        'barcode': 7893500020110,
        'name': 'ARROZ BRANCO TIO JOAO 1KG',
    },
    {
        'barcode': 7897664140202,
        'name': 'DESINF MINUANO HERBAL 500ML',
    },
    {
        'barcode': 7896102504002,
        'name': 'AZEITONA EM CONSERVA QUERO 200G',
    },
    {
        'barcode': 7891037013520,
        'name': 'CD CLOSE UP TRIPLE MENTA AMERICANA 90G',
    },
    {
        'barcode': 7897664130319,
        'name': 'DETERG MINUANO MARINE 500ML',
    },
    {
        'barcode': 7897664130302,
        'name': 'DETERG MINUANO COCO 500ML',
    },
    {
        'barcode': 7897664140561,
        'name': 'DESINF MINUANO MARINE 500ML',
    },
    {
        'barcode': 7898080640222,
        'name': 'CREME DE LEITE TP ITALAC 200G',
    },
    {
        'barcode': 7891000011300,
        'name': 'NESTON NESTLE 400G 3 CEREAIS',
    },
    {
        'barcode': 78917361,
        'name': 'SOBREMESA FLAN CARAMELO 2UN 220G',
    },
    {
        'barcode': 7896607100174,
        'name': 'BEB ALC AGUARDENTE PITU GF 965ML',
    },
    {
        'barcode': 7891200343300,
        'name': 'ANTI FERRUGEM LOCTITE SUPER LUB 300ML',
    },
    {
        'barcode': 7898422746803,
        'name': 'SAB DOVE GO FRESH 90G',
    },
    {
        'barcode': 7896007512317,
        'name': 'FRALDA TURMA DA MONICA TRI PROTEC JUMBO M 32UN',
    },
    {
        'barcode': 7898080640239,
        'name': 'BEB LAC ITALAC 200ML',
    },
    {
        'barcode': 7896052601110,
        'name': 'REFRIGERANTE PET SCHIN LIMAO 250ML',
    },
    {
        'barcode': 7896052601103,
        'name': 'REFRIGERANTE PET SCHIN COLA 250ML',
    },
    {
        'barcode': 7896052601127,
        'name': 'REFRIGERANTE PET SCHIN LARANJA 250ML',
    },
    {
        'barcode': 7896003701920,
        'name': 'BISC RECH MARILAN MORANGO 130G',
    },
    {
        'barcode': 7891048040065,
        'name': 'FERMENTO BIOLOGICO DR OETKER SECO INST SC 10G',
    },
    {
        'barcode': 7898366930306,
        'name': 'MOLHO INGLES PALMEIRON 150ML',
    },
    {
        'barcode': 7896098900604,
        'name': 'DESINF YPE PINHO TRADICAO 500ML',
    },
    {
        'barcode': 7891152333084,
        'name': 'MACARRAO LASANHA FORTALEZA 500G',
    },
    {
        'barcode': 7896098902417,
        'name': 'AMAC YPE TERNURA 2L',
    },
    {
        'barcode': 7896279102421,
        'name': 'OLEO CORP MURIEL BABY MASCULINO 100ML',
    },
    {
        'barcode': 7896183210045,
        'name': 'LEITE EM PO GLORIA DESNATADO LT 300G',
    },
    {
        'barcode': 78924222,
        'name': 'DESOD ROLL ON REXONA BAMBOO 48H 30ML',
    },
    {
        'barcode': 7891010047184,
        'name': 'COND INF JOHNSONS BABY CABELOS CACHEADOS 200ML',
    },
    {
        'barcode': 7891024161913,
        'name': 'SH PALMOLIVE NUTRILISS 350ML',
    },
    {
        'barcode': 7891024174210,
        'name': 'SH PALMOLIVE CERAMIDAS FORCE 350ML',
    },
    {
        'barcode': 7891024174135,
        'name': 'SH INF PALMOLIVE KIDS TODO TIPO DE CABELO 350ML',
    },
    {
        'barcode': 7891024114704,
        'name': 'SAB PALMOLIVE EXT FRUTAS 90G',
    },
    {
        'barcode': 7891010503024,
        'name': 'ABS SEMPRE LIVRE ADAPT C SUAVE C ABAS 8UND',
    },
    {
        'barcode': 7891010503031,
        'name': 'ABS SEMPRE LIVRE ADAPT SUAVE SEM ABAS 8UN',
    },
    {
        'barcode': 7501001156176,
        'name': 'ABS ALWAYS SUPER PROTEC BASICO C SUAVE C ABAS 8UND',
    },
    {
        'barcode': 7501001156190,
        'name': 'ABS ALWAYS SUPER PROTEC C SUAVE S ABAS 8UND',
    },
    {
        'barcode': 7891024174630,
        'name': 'COND INF PALMOLIVE KIDS TODO TIPO DE CABELO 350ML',
    },
    {
        'barcode': 7896213000677,
        'name': 'BISC CREAM CRACKER AGUA E SAL VITARELLA 400G',
    },
    {
        'barcode': 7891024174784,
        'name': 'CR PENT PALMOLIVE CERAMIDAS 150ML',
    },
    {
        'barcode': 7896224800679,
        'name': 'CAPPUCCINO SANTA CLARA PT 200G',
    },
    {
        'barcode': 7896013502166,
        'name': 'TINTURA NATUCOR CASTANHO ESCURO 30',
    },
    {
        'barcode': 7896013516231,
        'name': 'TINTURA NATUCOR 67',
    },
    {
        'barcode': 7896013502937,
        'name': 'TINTURA NATUCOR PRETO NATURAL 10',
    },
    {
        'barcode': 7891024172230,
        'name': 'SH PALMOLIVE NEUTRO 350ML',
    },
    {
        'barcode': 7896512909787,
        'name': 'SAB PHEBO ODOR ROSAS 90G',
    },
    {
        'barcode': 7891010500832,
        'name': 'ESC DENT JOHNSONS REACH ESSENCIAL MACIA 30',
    },
    {
        'barcode': 7791969028831,
        'name': 'DESOD AER NIVEA COOL KICK 48H 150ML',
    },
    {
        'barcode': 7891024170335,
        'name': 'COND PALMOLIVE NUTRILISS 350ML',
    },
    {
        'barcode': 7891024174715,
        'name': 'COND PALMOLIVE CERAMIDAS FORCE 350ML',
    },
    {
        'barcode': 7891024172537,
        'name': 'COND PALMOLIVE NEUTRO 350ML',
    },
    {
        'barcode': 7891024174036,
        'name': 'SH PALMOLIVE ANTIARMADO 350ML',
    },
    {
        'barcode': 7896013529361,
        'name': 'TINTURA NATUCOR LOURO NATURAL 70',
    },
    {
        'barcode': 7894650079423,
        'name': 'REPELENTE CR OFF 100ML',
    },
    {
        'barcode': 7891024135020,
        'name': 'CD COLGATE TOTAL 12 WHITENING GEL 90G',
    },
    {
        'barcode': 7791969016036,
        'name': 'DESOD AER NIVEA DRY COMFORT PLUS 48H 150ML',
    },
    {
        'barcode': 7791969016005,
        'name': 'DESOD AER NIVEA FRESH ACTIVE FOR MEN 24H 150ML',
    },
    {
        'barcode': 7791969016012,
        'name': 'DESOD AER NIVEA FRESH NATURAL 24H 150ML',
    },
    {
        'barcode': 7896013502944,
        'name': 'TINTURA NATUCOR PRETO SUAVE 20',
    },
    {
        'barcode': 7896102502893,
        'name': 'CATCHUP TP QUERO PICANTE 300G',
    },
    {
        'barcode': 5601252100972,
        'name': 'AZEITE DE OLIVA GALLO EX VIRGEM LT 200ML',
    },
    {
        'barcode': 7891024134610,
        'name': 'CD COLGATE MPA MENTA REFRESCANTE 180G',
    },
    {
        'barcode': 7896490288829,
        'name': 'MILHO DE CANJICA DONA CLARA 500G',
    },
    {
        'barcode': 7898422742386,
        'name': 'CD CLOSE UP TRIPLE MENTA SILVESTRE 90G',
    },
    {
        'barcode': 78924239,
        'name': 'DESOD ROLL ON REXONA POWDER 48H 30ML',
    },
    {
        'barcode': 7896013502791,
        'name': 'TINTURA NATUCOR 5.0',
    },
    {
        'barcode': 7898286200206,
        'name': 'CAFE SOLUV MARATA VD 100G',
    },
    {
        'barcode': 7898286200022,
        'name': 'COLORIFICO MARATA 100G',
    },
    {
        'barcode': 7891035210433,
        'name': 'MULTIUSO VEJA MACA VERDE 500ML',
    },
    {
        'barcode': 7892840215217,
        'name': 'SALGADINHO ELMA CHIPS SENSACOES PEITO DE PERU 45G',
    },
    {
        'barcode': 7896102502534,
        'name': 'EXT DE TOMATE QUERO TP 320G',
    },
    {
        'barcode': 7891024113783,
        'name': 'SAB PROTEX PROPOLIS 90G',
    },
    {
        'barcode': 7891331010201,
        'name': 'MINGAU NUTRILON BANANA MACA SC 300G',
    },
    {
        'barcode': 7891132001101,
        'name': 'TEMPERO SAZON SABORES DO NORDESTE 60G',
    },
    {
        'barcode': 7891024174432,
        'name': 'COND PALMOLIVE ANTIARMADO 350ML',
    },
    {
        'barcode': 7896013502906,
        'name': 'TINTURA NATUCOR PRETO AZULADO 17',
    },
    {
        'barcode': 7895800304211,
        'name': 'GOMA DE MASCAR TRIDENT HORTELA 8G',
    },
    {
        'barcode': 7895800304228,
        'name': 'GOMA DE MASCAR TRIDENT MENTA 8G',
    },
    {
        'barcode': 7895800304679,
        'name': 'BALA HALLS MORANGO 34G',
    },
    {
        'barcode': 7895800303313,
        'name': 'BALA HALLS EXTRA FORTE 34G',
    },
    {
        'barcode': 7891000026403,
        'name': 'CAFE NESCAFE DESCAFEINADO REFIL SC 50G',
    },
    {
        'barcode': 7896090403127,
        'name': 'SAB FRANCIS VERDE VERBENA DA SICILIA 90G',
    },
    {
        'barcode': 7896090403134,
        'name': 'SAB FRANCIS JASMIM DO MARROCOS 90G',
    },
    {
        'barcode': 7891331002992,
        'name': 'FARINHA LACTEA NUTRI REFIL 230G',
    },
    {
        'barcode': 7898422745301,
        'name': 'CR PENT SEDA PRETOS LUMINOSOS 300ML',
    },
    {
        'barcode': 7896003702057,
        'name': 'BISC RECH MARILAN TORTINHAS CHOCOLATE 160G',
    },
    {
        'barcode': 7891962007366,
        'name': 'BISC RECH BAUDUCCO BARRINHA CHOCOLATE 25G',
    },
    {
        'barcode': 7895800303320,
        'name': 'BALA HALLS MENTA 34G',
    },
    {
        'barcode': 7891024158708,
        'name': 'COND PALMOLIVE ILUMINADOR PRETOS 350ML',
    },
    {
        'barcode': 7891024158609,
        'name': 'SH PALMOLIVE ILUM PRETOS 350ML',
    },
    {
        'barcode': 7897664110311,
        'name': 'SAB ALBANY SUAVE BAMBU 90G',
    },
    {
        'barcode': 7501001410506,
        'name': 'SABAO EM PO ACE ERVA DOCE E CAMOMILA 500G',
    },
    {
        'barcode': 7891182031059,
        'name': 'ESMALTE RISQUE VERMELHOS DESEJO 8ML',
    },
    {
        'barcode': 7891182031097,
        'name': 'ESMALTE RISQUE ULTRACREMOSO OBSESSAO 8ML',
    },
    {
        'barcode': 7896105181767,
        'name': 'BISC INT AGUIA SALT CRACKER 360G',
    },
    {
        'barcode': 7891088006120,
        'name': 'ALGODAO YORK CX 25G',
    },
    {
        'barcode': 7891088007547,
        'name': 'ALGODAO BOLA YORK 50G',
    },
    {
        'barcode': 7897664110298,
        'name': 'SAB ALBANY LAV ALGODAO 90G',
    },
    {
        'barcode': 70330703629,
        'name': 'AP BARB BIC SENSITIVE SHAVER 2UN',
    },
    {
        'barcode': 7894650067451,
        'name': 'PEDRA SANIT GLADE LAVANDA 25G',
    },
    {
        'barcode': 7896015517502,
        'name': 'CD SENSODYNE COOL GEL 50G',
    },
    {
        'barcode': 7891048040003,
        'name': 'FERMENTO EM PO QUIMICO DR OETKER 100G',
    },
    {
        'barcode': 7891000029626,
        'name': 'IOG POLPA MOLICO TRI 6UN 600G',
    },
    {
        'barcode': 7896110003931,
        'name': 'PAPEL HIG PERSONAL FS ORIG JASMIM 30M 4RL',
    },
    {
        'barcode': 7896110003917,
        'name': 'PAPEL HIG PERSONAL FS ORIG LAVANDA 30M 4RL',
    },
    {
        'barcode': 7893500018483,
        'name': 'ARROZ INTEGRAL TIO JOAO TIPO 1 1KG',
    },
    {
        'barcode': 7896224800877,
        'name': 'CAFE SOLUV SANTA CLARA DESCAFEINADO REFIL 50G',
    },
    {
        'barcode': 7891024130728,
        'name': 'ENXAG BUCAL COLGATE PLAX FRESH MINT 60ML',
    },
    {
        'barcode': 7896003701487,
        'name': 'BISC RECH MARILAN TURMIX CHOCOLATE 419G',
    },
    {
        'barcode': 7896098900154,
        'name': 'SABAO EM BARRA YPE ALOE VERA 1KG',
    },
    {
        'barcode': 7896098900130,
        'name': 'SABAO EM BARRA YPE FLORES FRUTAS VERMELHO 1KG',
    },
    {
        'barcode': 7891182880053,
        'name': 'TINTURA NIASI FLUIDGEL CASTANHO CLARO 50',
    },
    {
        'barcode': 7891182880046,
        'name': 'TINTURA NIASI FLUIDGEL CASTANHO MEDIO 40',
    },
    {
        'barcode': 7895800201503,
        'name': 'GOMA DE MASCAR TRIDENT MORANGO 8G',
    },
    {
        'barcode': 7895800300381,
        'name': 'BALA HALLS MENTHOL 34G',
    },
    {
        'barcode': 7895800420003,
        'name': 'BALA HALLS UVA VERDE',
    },
    {
        'barcode': 7894650000380,
        'name': 'INSET AER RAID TRIPLA ACAO BARATAS FORMIGAS 300ML',
    },
    {
        'barcode': 7896105177012,
        'name': 'BISC SALG AGUIA SALT CRACKER ORIGINAL 180G',
    },
    {
        'barcode': 7898080640413,
        'name': 'LEITE CONDI ITALAC 395G',
    },
    {
        'barcode': 7898162880034,
        'name': 'FRALDA SAPEKA REGULAR EG 7UN',
    },
    {
        'barcode': 7898162880027,
        'name': 'FRALDA SAPEKA REGULAR G 7UN',
    },
    {
        'barcode': 7898162880010,
        'name': 'FRALDA SAPEKA REGULAR M 8UN',
    },
    {
        'barcode': 7898162880379,
        'name': 'FRALDA SAPEKA PRATICO EG 16UN',
    },
    {
        'barcode': 7898162880355,
        'name': 'FRALDA SAPEKA PRATICO M 24UN',
    },
    {
        'barcode': 7891000038512,
        'name': 'IOG POLPA NESTLE NESTON VITAMINAS 6UN 600G',
    },
    {
        'barcode': 7896000705907,
        'name': 'TINTURA NIELY COR E TON BORDEAUX 466',
    },
    {
        'barcode': 7896000706133,
        'name': 'TINTURA NIELY COR E TON LOURO ESCURO VERMELHO 666',
    },
    {
        'barcode': 7899026415140,
        'name': 'CR PENT ELSEVE COLOR VIVE 250ML',
    },
    {
        'barcode': 78900554,
        'name': 'CAFE SOLUV NESCAFE ORIG VD 50G',
    },
    {
        'barcode': 7898162880003,
        'name': 'FRALDA SAPEKA REGULAR P 10UN',
    },
    {
        'barcode': 7891000037812,
        'name': 'IOG POLPA NESTLE NINHO SOLEIL 6UN 600G',
    },
    {
        'barcode': 7891010501105,
        'name': 'FIO DENTAL J J REACH ESSENCIAL MENTA 100M',
    },
    {
        'barcode': 7895800308738,
        'name': 'GOMA DE MASCAR TRIDENT FRESH HERBAL 8G',
    },
    {
        'barcode': 7891035116070,
        'name': 'LIMP PISO DESTAC LAVANDA E ALFAZEMA REFIL 500ML',
    },
    {
        'barcode': 7791293008066,
        'name': 'DESOD AER AXE MARINE 90ML',
    },
    {
        'barcode': 7891000306703,
        'name': 'CAFE SOLUV NESCAFE ORIGINAL REFIL SC 50G',
    },
    {
        'barcode': 7891035041006,
        'name': 'ALVEJANTE SEM CLORO VANISH MULTIUSO REFIL 500ML',
    },
    {
        'barcode': 7896102517125,
        'name': 'MILHO VERDE TP QUERO 200G',
    },
    {
        'barcode': 7896102517132,
        'name': 'ERVILHA E MILHO TP QUERO EM CONSERVA 200G',
    },
    {
        'barcode': 7898422745578,
        'name': 'SH SEDA SOS QUEDA 350ML',
    },
    {
        'barcode': 7898422745585,
        'name': 'COND SEDA SOS QUEDA 350ML',
    },
    {
        'barcode': 7791293008141,
        'name': 'DESOD AER DOVE ORIGINAL 48H 169ML',
    },
    {
        'barcode': 7896098906729,
        'name': 'SABAO EM PO TIXAN YPE RADIANTES SC 500G',
    },
    {
        'barcode': 7896098901748,
        'name': 'SABAO EM PO TIXAN YPE MACIEZ FLORAL SC 500G',
    },
    {
        'barcode': 7891132010387,
        'name': 'TEMPERO SABOR AMI TOQUE DE LOURO 300G',
    },
    {
        'barcode': 7896003701289,
        'name': 'BISC WAFER MARILAN RECHEADO LIMAO 140G',
    },
    {
        'barcode': 7891172414121,
        'name': 'PAPEL HIG SCOTT FD NEUTRO 20M 4RL',
    },
    {
        'barcode': 7896020160069,
        'name': 'TALCO PARA OS PES TENYS PE CANFORADO 100G',
    },
    {
        'barcode': 7891167021020,
        'name': 'SARDINHA GOMES DA COSTA TOMATE 125G',
    },
    {
        'barcode': 7891167021013,
        'name': 'SARDINHA GOMES DA COSTA OLEO 125G',
    },
    {
        'barcode': 78923454,
        'name': 'DESOD ROLL ON REXONA MEN V8 50ML',
    },
    {
        'barcode': 7896036093085,
        'name': 'AZEITE DE OLIVA MARIA COMP 200ML',
    },
    {
        'barcode': 7898422746216,
        'name': 'SH CLEAR MEN LIMPEZA DIARIA 2 EM1 200ML',
    },
    {
        'barcode': 7898422746162,
        'name': 'SH CLEAR WOMEN SUAVIDADE E BRILHO 200ML',
    },
    {
        'barcode': 7898422746193,
        'name': 'SH CLEAR WOMEN QUEDA DEFENSE 200ML',
    },
    {
        'barcode': 7898422746179,
        'name': 'SH CLEAR WOMEN ALIVIO DA COCEIRA 200ML',
    },
    {
        'barcode': 7898422746759,
        'name': 'SAB DOVE CREAM BAR 90G',
    },
    {
        'barcode': 7894900700015,
        'name': 'REFRIGERANTE LT COCA COLA ZERO 350ML',
    },
    {
        'barcode': 78900769,
        'name': 'ADOCANTE LIQ DOCE MENOR 100ML',
    },
    {
        'barcode': 7896089030204,
        'name': 'FILTRO DE PAPEL PILAO 102',
    },
    {
        'barcode': 7891022851595,
        'name': 'DETERG LIMPOL LARANJA 500ML',
    },
    {
        'barcode': 7891095009824,
        'name': 'PO PARA SORVETE YOKI COCO 150G',
    }
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        product = [Product(**product) for product in products]

        Product.objects.bulk_create(product)
