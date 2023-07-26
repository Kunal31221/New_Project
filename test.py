# # # # # # import json
# # # # # # from urllib.parse import quote_plus
# # # # # #
# # # # # # class BaseEncoderDecoder:
# # # # # #     def __init__(self, alphabet):
# # # # # #         self.alphabet = alphabet
# # # # # #
# # # # # #     def encode(self, num):
# # # # # #         if num == 0:
# # # # # #             return self.alphabet[0]
# # # # # #         arr = []
# # # # # #         arr_append = arr.append
# # # # # #         _divmod = divmod
# # # # # #         base = len(self.alphabet)
# # # # # #         while num:
# # # # # #             num, rem = _divmod(num, base)
# # # # # #             arr_append(self.alphabet[rem])
# # # # # #         arr.reverse()
# # # # # #         return ''.join(arr)
# # # # # #
# # # # # #     def decode(self, string):
# # # # # #         base = len(self.alphabet)
# # # # # #         strlen = len(string)
# # # # # #         num = 0
# # # # # #         idx = 0
# # # # # #         for char in string:
# # # # # #             power = (strlen - (idx + 1))
# # # # # #             num += self.alphabet.index(char) * (base ** power)
# # # # # #             idx += 1
# # # # # #         print(num)
# # # # # #         return num
# # # # # #
# # # # # # # class URLShortener:
# # # # # # #     def __init__(self):
# # # # # # #         self.url_mapping = {}
# # # # # # #         self.counter = 10000
# # # # # # #         self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # # # # # #         self.encoder_decoder = BaseEncoderDecoder(self.alphabet)
# # # # # # #
# # # # # # #     def generate_short_url(self, long_url):
# # # # # # #         short_url = self.counter
# # # # # # #         self.counter += 1
# # # # # # #         self.url_mapping[long_url] = short_url
# # # # # # #
# # # # # # #     def process_url(self, json_input):
# # # # # # #         data = json.loads(json_input)
# # # # # # #         long_url = data['long_url']
# # # # # # #         self.generate_short_url(long_url)
# # # # # # #         short_url = self.url_mapping[long_url]
# # # # # # #         encoded_short_url = self.encoder_decoder.encode(short_url)
# # # # # # #         return encoded_short_url
# # # # # # #
# # # # # # #     def decode_short_url(self, encoded_short_url):
# # # # # # #         short_url = self.encoder_decoder.decode(encoded_short_url)
# # # # # # #         for long_url, url_id in self.url_mapping.items():
# # # # # # #             if url_id == short_url:
# # # # # # #                 return long_url
# # # # # # #
# # # # # # #         return None
# # # # # # #
# # # # # # #
# # # # # # # url_json = '{"long_url": "https://www.google.com/search?q=helloworld"}'
# # # # # # #
# # # # # # # shortener = URLShortener()
# # # # # # # encoded_short_url = shortener.process_url(url_json)
# # # # # # # print("Encoded Short URL:", encoded_short_url)
# # # # # # #
# # # # # # # decoded_long_url = shortener.decode_short_url(encoded_short_url)
# # # # # # # print("Decoded Long URL:", decoded_long_url)
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # # import json
# # # # # # # #
# # # # # # # # class URLShortener:
# # # # # # # #     def __init__(self):
# # # # # # # #         self.url_mapping = {}
# # # # # # # #         self.counter = 10000
# # # # # # # #         self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # # # # # # #         self.encoder_decoder = BaseEncoderDecoder(self.alphabet)
# # # # # # # #
# # # # # # # #     def generate_short_url(self, long_url):
# # # # # # # #         short_url = self.counter
# # # # # # # #         self.counter += 1
# # # # # # # #         self.url_mapping[long_url] = short_url
# # # # # # # #
# # # # # # # #     def process_url(self, json_input):
# # # # # # # #         data = json.loads(json_input)
# # # # # # # #         long_url = data['long_url']
# # # # # # # #         self.generate_short_url(long_url)
# # # # # # # #         short_url = self.url_mapping[long_url]
# # # # # # # #         encoded_short_url = self.encoder_decoder.encode(short_url)
# # # # # # # #         return encoded_short_url
# # # # # # # #
# # # # # # # #     def decode_short_url(self, encoded_short_url):
# # # # # # # #         short_url = self.encoder_decoder.decode(encoded_short_url)
# # # # # # # #         for long_url, url_id in self.url_mapping.items():
# # # # # # # #             if url_id == short_url:
# # # # # # # #                 return long_url
# # # # # # # #
# # # # # # # #         return None
# # # # # # # #
# # # # # # # #
# # # # # # # # def lambda_handler(event, context):
# # # # # # # #     url_json = '{"long_url": "https://www.google.com/search?q=helloworld"}'
# # # # # # # #
# # # # # # # #     shortener = URLShortener()
# # # # # # # #     encoded_short_url = shortener.process_url(url_json)
# # # # # # # #     print("Encoded Short URL:", encoded_short_url)
# # # # # # # #
# # # # # # # #     decoded_long_url = shortener.decode_short_url(encoded_short_url)
# # # # # # # #     print("Decoded Long URL:", decoded_long_url)
# # # # # # # #
# # # # # # # #     return {
# # # # # # # #         'statusCode': 200,
# # # # # # # #         'body': json.dumps({'encoded_short_url': encoded_short_url, 'decoded_long_url': decoded_long_url})
# # # # # # # #     }
# # # # # #
# # # # # # import sqlalchemy
# # # # # #
# # # # # # from sqlalchemy import create_engine, Column, Integer, String
# # # # # # from sqlalchemy.ext.declarative import declarative_base
# # # # # # from sqlalchemy.orm import sessionmaker
# # # # # #
# # # # # # from sqlalchemy import create_engine, Column, Integer, String
# # # # # # from sqlalchemy.ext.declarative import declarative_base
# # # # # # from sqlalchemy.orm import sessionmaker
# # # # # #
# # # # # # Base = declarative_base()
# # # # # #
# # # # # #
# # # # # # class URLMapping(Base):
# # # # # #     __tablename__ = 'url_mappings'
# # # # # #     id = Column(Integer, primary_key=True)
# # # # # #     short_url = Column(String(255))
# # # # # #     long_url = Column(String(255))
# # # # # #     current_counter_number = Column(Integer)
# # # # # #
# # # # # #
# # # # # # class URLShortener:
# # # # # #     def __init__(self):
# # # # # #         self.url_mapping = {}
# # # # # #         self.counter = 10000
# # # # # #         self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # # # # #         self.encoder_decoder = BaseEncoderDecoder(self.alphabet)
# # # # # #         self.user = 'root'
# # # # # #         self.password = quote_plus('Sandhya@1221')
# # # # # #         self.host = 'localhost'
# # # # # #         self.database = 'mydatabase'
# # # # # #         self.engine = create_engine(f'mysql+mysqlconnector://{self.user}:{self.password}@{self.host}/{self.database}')
# # # # # #         Base.metadata.create_all(self.engine)
# # # # # #         Session = sessionmaker(bind=self.engine)
# # # # # #         self.session = Session()
# # # # # #
# # # # # #     def generate_short_url(self, long_url):
# # # # # #         existing_mapping = self.session.query(URLMapping).filter_by(current_counter_number=self.counter).first()
# # # # # #         if existing_mapping:
# # # # # #             self.counter += 1
# # # # # #             existing_mapping.long_url = long_url
# # # # # #             self.url_mapping[long_url] = existing_mapping.short_url
# # # # # #         else:
# # # # # #             short_url = self.counter
# # # # # #             self.counter += 1
# # # # # #             self.url_mapping[long_url] = short_url
# # # # # #             encoded_short_url = self.encoder_decoder.encode(short_url)
# # # # # #             url_mapping = URLMapping(short_url=encoded_short_url, long_url=long_url,
# # # # # #                                      current_counter_number=self.counter)
# # # # # #             self.session.add(url_mapping)
# # # # # #         self.session.commit()
# # # # # #
# # # # # #     def process_url(self, json_input):
# # # # # #         data = json.loads(json_input)
# # # # # #         long_url = data['long_url']
# # # # # #         self.generate_short_url(long_url)
# # # # # #         short_url = self.url_mapping[long_url]
# # # # # #         encoded_short_url = self.encoder_decoder.encode(short_url)
# # # # # #         url_mapping = URLMapping(short_url=encoded_short_url, long_url=long_url, current_counter_number=self.counter)
# # # # # #         self.session.add(url_mapping)
# # # # # #         # self.session.commit()
# # # # # #         return encoded_short_url
# # # # # #
# # # # # #     def decode_short_url(self, encoded_short_url):
# # # # # #         short_url = self.encoder_decoder.decode(encoded_short_url)
# # # # # #         for long_url, url_id in self.url_mapping.items():
# # # # # #             if url_id == short_url:
# # # # # #                 return long_url
# # # # # #
# # # # # #         return None
# # # # # #
# # # # # #
# # # # # # url_json = '{"long_url": "https://www.google.com/search?q=helloworld"}'
# # # # # #
# # # # # # shortener = URLShortener()
# # # # # # encoded_short_url = shortener.process_url(url_json)
# # # # # # print("Encoded Short URL:", encoded_short_url)
# # # # # #
# # # # # # decoded_long_url = shortener.decode_short_url(encoded_short_url)
# # # # # # print("Decoded Long URL:", decoded_long_url)
# # # # #
# # # # # import json
# # # # # from urllib.parse import quote_plus
# # # # # from sqlalchemy import create_engine, Column, Integer, String
# # # # # from sqlalchemy.ext.declarative import declarative_base
# # # # # from sqlalchemy.orm import sessionmaker
# # # # #
# # # # #
# # # # # class BaseEncoderDecoder:
# # # # #     def __init__(self, alphabet):
# # # # #         self.alphabet = alphabet
# # # # #
# # # # #     def encode(self, num):
# # # # #         if num == 0:
# # # # #             return self.alphabet[0]
# # # # #         arr = []
# # # # #         arr_append = arr.append
# # # # #         _divmod = divmod
# # # # #         base = len(self.alphabet)
# # # # #         while num:
# # # # #             num, rem = _divmod(num, base)
# # # # #             arr_append(self.alphabet[rem])
# # # # #         arr.reverse()
# # # # #         return ''.join(arr)
# # # # #
# # # # # Base = declarative_base()
# # # # #
# # # # #
# # # # # class URLMapping(Base):
# # # # #     __tablename__ = 'url_mappings'
# # # # #     id = Column(Integer, primary_key=True)
# # # # #     short_url = Column(String(255))
# # # # #     long_url = Column(String(255))
# # # # #     current_counter_number = Column(Integer)
# # # # #
# # # # #
# # # # # class URLShortener:
# # # # #     def __init__(self):
# # # # #         self.url_mapping = {}
# # # # #         self.counter = 10000
# # # # #         self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # # # #         self.encoder_decoder = BaseEncoderDecoder(self.alphabet)
# # # # #         self.user = 'root'
# # # # #         self.password = quote_plus('Sandhya@1221')
# # # # #         self.host = 'localhost'
# # # # #         self.database = 'mydatabase'
# # # # #         self.engine = create_engine(f'mysql+mysqlconnector://{self.user}:{self.password}@{self.host}/{self.database}')
# # # # #         Base.metadata.create_all(self.engine)
# # # # #         Session = sessionmaker(bind=self.engine)
# # # # #         self.session = Session()
# # # # #
# # # # #     def generate_short_url(self, long_url):
# # # # #         max_counter = self.session.query(URLMapping).order_by(URLMapping.current_counter_number.desc()).first()
# # # # #         if max_counter:
# # # # #             self.counter = max_counter.current_counter_number + 1
# # # # #
# # # # #         existing_mapping = self.session.query(URLMapping).filter_by(current_counter_number=self.counter).first()
# # # # #         if existing_mapping:
# # # # #             existing_mapping.long_url = long_url
# # # # #             existing_mapping.short_url = self.encoder_decoder.encode(self.counter)
# # # # #             self.url_mapping[long_url] = existing_mapping.short_url
# # # # #         else:
# # # # #             short_url = self.counter
# # # # #             self.url_mapping[long_url] = short_url
# # # # #             encoded_short_url = self.encoder_decoder.encode(short_url)
# # # # #             url_mapping = URLMapping(short_url=encoded_short_url, long_url=long_url,
# # # # #                                      current_counter_number=self.counter)
# # # # #             self.session.add(url_mapping)
# # # # #         self.session.commit()
# # # # #
# # # # #     def process_url(self, json_input):
# # # # #         data = json.loads(json_input)
# # # # #         long_url = data['long_url']
# # # # #         existing_mapping = self.session.query(URLMapping).filter_by(long_url=long_url).first()
# # # # #         if existing_mapping:
# # # # #             self.url_mapping[long_url] = existing_mapping.short_url
# # # # #         else:
# # # # #             self.generate_short_url(long_url)
# # # # #         encoded_short_url = self.url_mapping[long_url]
# # # # #         return encoded_short_url
# # # # #
# # # # #
# # # # # url_json = '{"long_url": "https://www.google.com/search?q=helloworlkkrrr"}'
# # # # #
# # # # # shortener = URLShortener()
# # # # # encoded_short_url = shortener.process_url(url_json)
# # # # # print("Encoded Short URL:", encoded_short_url)
# # # # #
# # # # #
# # # # import requests
# # # #
# # # # url = "https://app.intouchemr.com/ite/secure/emr/index.xhtml"
# # # #
# # # # payload = 'formHomeAction=formHomeAction&javax.faces.ViewState=5501848220427797453%3A-2216954104205830030&formHomeAction%3Aj_idt719=35268&formHomeAction%3AemrRecordTbl2_rppDD=10&formHomeAction%3AemrRecordTbl2_selection=&formHomeAction%3AemrRecordTbl_rppDD=10&formHomeAction%3AemrRecordTbl_selection=&formHomeAction%3AemrRecordTbl11_rppDD=10&formHomeAction%3AemrRecordTbl11_selection=&formHomeAction%3AemrRecordTblFlowsheet_rppDD=10&formHomeAction%3AemrRecordTblFlowsheetprie_rppDD=10&formHomeAction%3AtblCancelNoShow_selection=&formHomeAction%3AemrRecordTbl%3A0%3Aj_idt881=formHomeAction%3AemrRecordTbl%3A0%3Aj_idt881'
# # # # headers = {
# # # #   'host': 'app.intouchemr.com',
# # # #   'connection': 'keep-alive',
# # # #   'cache-control': 'max-age=0',
# # # #   'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
# # # #   'sec-ch-ua-mobile': '?0',
# # # #   'sec-ch-ua-platform': '"Windows"',
# # # #   'upgrade-insecure-requests': '1',
# # # #   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
# # # #   'origin': 'https://app.intouchemr.com',
# # # #   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# # # #   'sec-fetch-site': 'same-origin',
# # # #   'sec-fetch-mode': 'navigate',
# # # #   'sec-fetch-user': '?1',
# # # #   'sec-fetch-dest': 'document',
# # # #   'referer': 'https://app.intouchemr.com/ite/secure/emr/index.xhtml?patientID=134008',
# # # #   'accept-language': 'en-US,en;q=0.9',
# # # #   'content-type': 'application/x-www-form-urlencoded',
# # # #   'Cookie': 'JSESSIONID=_RUZWch85TsQ90YdKWfcDzs-iikfOU3LwaL1Z4Qn.ip-10-0-7-121'
# # # # }
# # # #
# # # # response = requests.request("POST", url, headers=headers, data=payload)
# # # #
# # # # print(response.text)
# # # #
# # #
# # #
# # # def start(list_str):
# # #     len_str = len(list_str[0])
# # #     for i in range(1, len(list_str)):
# # #         temp_length = min(len_str, len(list_str[i]))
# # #         while temp_length > 0 and list_str[0][0: temp_length] != list_str[i][0:temp_length]:
# # #             temp_length = temp_length - 1
# # #             if temp_length == 0:
# # #                 return ""
# # #
# # #     return list_str[0][0:temp_length]
# # #
# # #
# # # list_str = ["flower", "flow", "flight"]
# # # print(start(list_str))
# # #
# # #
# # # def start(list_str):
# # #     len_str = len(list_str[0])
# # #
# # #     for i in range(1, len(list_str)):
# # #         temp_length = min(len_str, len(list_str[i]))
# # #         while temp_length > 0 and list_str[0][0: temp_length] != list_str[i][0:temp_length]:
# # #             temp_length2 = temp_length - 1
# # #             if temp_length2 == 0:
# # #                 return (0)
# # #
# # #     return list_str[0][0:temp_length]
# # #
# # #
# # #
# # # list_str = ["flower", "flow", "flight"]
# # # print(start(list_str))
# # #
# # #
# # # strs = ["flower", "flow", "flight"]
# # #
# # # def longestCommonPrefix(strs):
# # #     l = len(strs[0])
# # #     for i in range(1, len(strs)):
# # #         length = min(l, len(strs[i]))
# # #         while length > 0 and strs[0][0:length] != strs[i][0:length]:
# # #             length = length - 1
# # #             if length == 0:
# # #                 return 0
# # #     return strs[0][0:length]
# # #
# # # print(longestCommonPrefix(strs))
# #
# # import requests
# #
# # url = "https://app.intouchemr.com/ite/secure/emr/index.xhtml"
# #
# # # payload = 'formHomeAction=formHomeAction&javax.faces.ViewState=4310915008999380836%3A-7794844434082267905&formHomeAction%3Aj_idt719=35147&formHomeAction%3AemrRecordTbl2_rppDD=10&formHomeAction%3AemrRecordTbl2_selection=&formHomeAction%3AemrRecordTbl_rppDD=10&formHomeAction%3AemrRecordTbl_selection=&formHomeAction%3AemrRecordTbl11_rppDD=10&formHomeAction%3AemrRecordTbl11_selection=&formHomeAction%3AemrRecordTblFlowsheet_rppDD=10&formHomeAction%3AemrRecordTblFlowsheetprie_rppDD=10&formHomeAction%3AtblCancelNoShow_selection=&formHomeAction%3AemrRecordTbl%3A2%3Aj_idt881=formHomeAction%3AemrRecordTbl%3A2%3Aj_idt881'
# # # payload = 'formHomeAction=formHomeAction&javax.faces.ViewState=857045703133094505%3A4264488818283221140&formHomeAction%3Aj_idt719=35268&formHomeAction%3AemrRecordTbl2_rppDD=10&formHomeAction%3AemrRecordTbl2_selection=&formHomeAction%3AemrRecordTbl_rppDD=10&formHomeAction%3AemrRecordTbl_selection=&formHomeAction%3AemrRecordTbl11_rppDD=10&formHomeAction%3AemrRecordTbl11_selection=&formHomeAction%3AemrRecordTblFlowsheet_rppDD=10&formHomeAction%3AemrRecordTblFlowsheetprie_rppDD=10&formHomeAction%3AtblCancelNoShow_selection=&formHomeAction%3AemrRecordTbl%3A1%3Aj_idt881=formHomeAction%3AemrRecordTbl%3A1%3Aj_idt881'
# # # payload = 'formHomeAction=formHomeAction&javax.faces.ViewState=857045703133094505%3A4264488818283221140&formHomeAction%3Aj_idt719=35268&formHomeAction%3AemrRecordTbl2_rppDD=10&formHomeAction%3AemrRecordTbl2_selection=&formHomeAction%3AemrRecordTbl_rppDD=10&formHomeAction%3AemrRecordTbl_selection=&formHomeAction%3AemrRecordTbl11_rppDD=10&formHomeAction%3AemrRecordTbl11_selection=&formHomeAction%3AemrRecordTblFlowsheet_rppDD=10&formHomeAction%3AemrRecordTblFlowsheetprie_rppDD=10&formHomeAction%3AtblCancelNoShow_selection=&formHomeAction%3AemrRecordTbl11%3A0%3Aj_idt966=formHomeAction%3AemrRecordTbl11%3A0%3Aj_idt966'
# # payload = 'formHomeAction=formHomeAction&javax.faces.ViewState=857045703133094505%3A4264488818283221140&formHomeAction%3Aj_idt719=35268&formHomeAction%3AemrRecordTbl2_rppDD=10&formHomeAction%3AemrRecordTbl2_selection=&formHomeAction%3AemrRecordTbl_rppDD=10&formHomeAction%3AemrRecordTbl_selection=&formHomeAction%3AemrRecordTbl11_rppDD=10&formHomeAction%3AemrRecordTbl11_selection=&formHomeAction%3AemrRecordTblFlowsheet_rppDD=10&formHomeAction%3AemrRecordTblFlowsheetprie_rppDD=10&formHomeAction%3AtblCancelNoShow_selection=&formHomeAction%3AemrRecordTbl%3A6%3Aj_idt881=formHomeAction%3AemrRecordTbl%3A6%3Aj_idt881'
# # headers = {
# #   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
# #   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# #   'content-type': 'application/x-www-form-urlencoded',
# #   'Cookie': 'JSESSIONID=fzo_EmZm8EGNS_EJOoiF73UXbiDmt6ryv1pi1IS-.ip-10-0-7-121'
# # }
# #
# # response = requests.request("POST", url, headers=headers, data=payload)
# #
# # print(response.text)
#
#
# def start(input_str):
#     length1 = len(input_str[0])
#     for i in range(1, len(input_str)):
#         length2 = min(length1, len(input_str[i]))
#         while length2 > 0 and input_str[0][0:length2] != input_str[i][0:length2]:
#             length2 = length2 - 1
#             if length2 == 0:
#                 return ""
#     return input_str[0][0:length2]
#
#
# if __name__ == '__main__':
#     input_str = ["flower", "flow", "flight"]
#     print(start(input_str))

from enum import Enum
from datetime import datetime


class CarCategory(Enum):
    COMPACT = 1
    PREMIUM = 2
    MINIVAN = 3


class CarRentalSystem:
    baseDayRental = 50
    kilometerPrice = 10

    def __init__(self):
        self.bookings = {}

    def register_rental(self, booking_number, customer_name, car_category, rental_time, mileage_at_pickup):
        if booking_number in self.bookings:
            return "Booking number already exists. Please use a unique booking number."

        if car_category not in CarCategory:
            return "Invalid car category."

        self.bookings[booking_number] = {
            "customer_name": customer_name,
            "car_category": car_category,
            "rental_time": rental_time,
            "mileage_at_pickup": mileage_at_pickup
        }

        return "Rental registration successful."

    def calculate_price(self, booking_number, return_time, current_mileage):
        if booking_number not in self.bookings:
            return "Booking number not found. Please provide a valid booking number."

        rental_info = self.bookings[booking_number]
        car_category = rental_info["car_category"]
        rental_time = rental_info["rental_time"]
        mileage_at_pickup = rental_info["mileage_at_pickup"]

        days_rented = (return_time - rental_time).days
        kilometers_driven = current_mileage - mileage_at_pickup

        if car_category == CarCategory.COMPACT:
            price = self.baseDayRental * days_rented
        elif car_category == CarCategory.PREMIUM:
            price = self.baseDayRental * days_rented * 1.2 + self.kilometerPrice * kilometers_driven
        elif car_category == CarCategory.MINIVAN:
            price = self.baseDayRental * days_rented * 1.7 + (self.kilometerPrice * kilometers_driven * 1.5)
        else:
            return "Invalid car category."

        return price


def run_test_cases():
    car_system = CarRentalSystem()

    print(car_system.register_rental(1, "John Doe", CarCategory.COMPACT, datetime(2023, 7, 26, 10, 0), 10000))
    print(car_system.register_rental(2, "Jane Smith", CarCategory.PREMIUM, datetime(2023, 7, 27, 12, 0), 12000))
    print(car_system.register_rental(3, "Bob Johnson", CarCategory.MINIVAN, datetime(2023, 7, 28, 15, 0), 15000))

    print(car_system.calculate_price(1, datetime(2023, 7, 28, 10, 0), 11000))  # Compact car
    print(car_system.calculate_price(2, datetime(2023, 7, 29, 12, 0), 13000))  # Premium car
    print(car_system.calculate_price(3, datetime(2023, 7, 30, 15, 0), 16000))  # Minivan car


run_test_cases()
