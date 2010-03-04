#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
   This module is Wrapper Interface for YahooJapan's text analysis API.
   MA, DA, JIM, Furigana, Kousei, Keyphrase Services are avalable.
   
   Simple example of usage is followings
       >>> from yahoo_jtextapi import  YahooTextAPI
       >>> api = YahooTextAPI( 'YOUR API KEY' )
       >>> res = api.ma('僕は日本人です')  # retrieve data with dict object
       >>> print res
       {
       "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", 
       "ma_result": {
         "total_count": "4", 
         "word_list": {
            "word": [
                {
                    "reading": "ぼく", 
                    "pos": "名詞", 
                    "surface": "僕"
                }, 
                {
                    "reading": "は", 
                    "pos": "助詞", 
                    "surface": "は"
                }, 
                {
                    "reading": "にほんじん", 
                    "pos": "名詞", 
                    "surface": "日本人"
                }, 
                {
                    "reading": "です", 
                    "pos": "助動詞", 
                    "surface": "です"
                }
            ]
            }, 
            "filtered_count": "4"
          }, 
          "xsi:schemaLocation": "urn:yahoo:jp:jlp http://jlp.yahooapis.jp/MAService/V1/parseResponse.xsd", 
          "xmlns": "urn:yahoo:jp:jlp"
       }
"""

__author__  = "Matsumoto Taichi (taichino@gmail.com)"
__version__ = "0.1.0"
__license__ = "MIT License"

from yahoo_jtextapi import *
