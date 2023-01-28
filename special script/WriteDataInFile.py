import os

scraping_files = os.listdir('C:\\Users\\Stas\\Desktop\\hl7conv\\scraping datas')

for files in scraping_files:

    datas = open(f'C:\\Users\\Stas\\Desktop\\hl7conv\\scraping datas\\{files}', 'r',encoding='utf-8')
    text = datas.readlines()

    with open('C:\\Users\\Stas\\Desktop\\hl7conv\\hl7conv\\schemas\\versions\\v2_1\\enums.py', 'a', encoding='utf-8') as f:
        for x in text:
            f.write(x)
        f.close()



# file = open('/scraping datas/0001 Admitive Sex.txt', 'r')
#
# lines = file.readlines()
#
# for x in lines:
#     with open('../scraping datas/1322.txt', 'a') as ff:
#         ff.write(x)
#     ff.close()