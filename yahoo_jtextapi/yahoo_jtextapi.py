#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
from pyxml2obj import XMLin, XMLout

class YahooTextAPI:
  MA_KNOWN_OPTS        = '''results response filter ma_response ma_filter uniq_response
                            uniq_filter uniq_by_baseform'''.split()
  JIM_KNOWN_OPTS       = 'format mode response dictionary results'.split()
  FURIGANA_KNOWN_OPTS  = 'grade'.split()
  KOUSEI_KNOWN_OPTS    = 'filter_group no_filter'.split()
  KEYPHRASE_KNOWN_OPTS = 'output callback'.split()
  
  def __init__(self, appid):
    self.appid = appid

  def _access(self, url, sentence, options={}, known_opts=[]):
    for key in options:
      if not key in known_opts:
        raise KeyError('%s is not acceptable' % (key))
    params = {
      'appid'     : self.appid,
      'sentence'  : sentence,
    }
    params.update(options)
    params = urllib.urlencode(params)
    return urllib.urlopen(url, params).read()

  def ma(self, sentence, options={}):
    '''
    This method do morphological analysis on the sentence with Yahoo MA API.
    For example, when you process the sentence, "僕は日本人です",
    following will be returned.
    {"ma_result": {
        "total_count":    "8",
        "filtered_count": "8", 
        "word_list": {
            "word": [
                {
                    "surface": "僕",
                    "pos":     "名詞",
                    "reading": "ぼく",
                },
                {
                    "surface": "は",
                    "pos":     "助詞",
                    "reading": "は",
                },
                ...
                (omitted other words)
            ]
         }
      }
      }
    '''
    xml = self._access('http://jlp.yahooapis.jp/MAService/V1/parse',
                       sentence, options, self.MA_KNOWN_OPTS)
    return XMLin(xml, {'forcearray': ['word']})

  def da(self, sentence):
    '''
    This method do dependency parsing on the sentence with Yahoo DA API.
    For example, when you process the sentence, "今日はとても天気が良いです。",
    following will be returned.
    {"Result": {
        "ChunkList": {
            "Chunk": [
                {
                    "Dependency": "3", 
                    "Id": "0", 
                    "MorphemList": {
                        "Morphem": [
                            {
                                "Feature": "名詞,名詞,*,今日,きょう,今日", 
                                "Reading": "きょう", 
                                "Baseform": "今日", 
                                "Surface": "今日", 
                                "POS": "名詞"
                            }, 
                            {
                                "Feature": "助詞,係助詞,*,は,は,は", 
                                "Reading": "は", 
                                "Baseform": "は", 
                                "Surface": "は", 
                                "POS": "助詞"
                            }
                        ]
                    }
                },
                ...
                (omitted other chunk)
            ]
         }
      }
      }
    '''
    xml = self._access('http://jlp.yahooapis.jp/DAService/V1/parse', sentence)
    return XMLin(xml, {'forcearray':['Chunk', 'Morphem']})

  def jim(self, sentence, options={}):
    '''
    This method translate hiragana or romaji to kanji with Yahoo JIM API.
    For example, when you process the sentence, "すもももももももものうち",
    following will be returned.
    {"Result": {
        "SegmentList": {
            "Segment": [
                {
                    "SegmentText": "すももも", 
                    "CandidateList": {
                        "Candidate": [
                            "李も", 
                            "すももも", 
                            "スモモも", 
                            "ｽﾓﾓも", 
                            "酸桃も"
                        ]
                    }
                },
                ...
                (omitted other segment)
             ]
         }
      }
    }
    '''
    xml = self._access('http://jlp.yahooapis.jp/JIMService/V1/conversion',
                       sentence, options, self.JIM_KNOWN_OPTS)
    return XMLin(xml, {'forcearray': ['Segment', 'Candidate']})

  def furigana(self, sentence, options={}):
    '''
    This method retrieve ruby characters for specified sentence with Yahoo Furigana API.
    For example, when you process the sentence, "漢字かな交じり文にふりがなを振ること。",
    following will be returned.
    {"Result": {
        "WordList": {
            "Word": [
                {
                    "Roman": "kanzi", 
                    "Furigana": "かんじ", 
                    "Surface": "漢字"
                }, 
                ...
                (omitted other words)
            ]
        }
      }
    }
    '''
    xml = self._access('http://jlp.yahooapis.jp/FuriganaService/V1/furigana',
                       sentence, options, self.FURIGANA_KNOWN_OPTS)
    return XMLin(xml, {'forcearray': ['word']})

  def kousei(self, sentence, options={}):
    '''
    This method make a sentence proof-readed with Yahoo Kousei API.
    For example, when you process the sentence, "遙か彼方に小形飛行機が見える。",
    following will be returned.
    {"Result": [
        (omitted other Result)
        ...
        {
            "ShitekiInfo": "誤変換", 
            "StartPos": "5", 
            "ShitekiWord": "小型飛行機", 
            "Length": "5", 
            "Surface": "小形飛行機"
        }
     ]
     }
    '''
    xml = self._access('http://jlp.yahooapis.jp/KouseiService/V1/kousei',
                       sentence, options, self.KOUSEI_KNOWN_OPTS)
    return XMLin(xml, {'forcearray': ['result']})

  def keyphrase(self, sentence, options={}):
    '''
    This method extract key phrase from specified sentence with Yahoo Kephrase API.
    For example, when you process the sentence, "東京ミッドタウンから国立新美術館まで歩いて5分で着きます。",
    following will be returned.
    {"Result": [
        {
            "Score": "100", 
            "Keyphrase": "国立新美術館"
        }, 
        {
            "Score": "65", 
            "Keyphrase": "東京ミッドタウン"
        }, 
        {
            "Score": "9", 
            "Keyphrase": "5分"
        }
       ]
     }
    '''
    xml = self._access('http://jlp.yahooapis.jp/KeyphraseService/V1/extract',
                       sentence, options, self.KEYPHRASE_KNOWN_OPTS)
    return XMLin(xml, {'forcearray': ['result']})


if __name__ == '__main__':
  import simplejson as json
 
  def pp(obj):
    if isinstance(obj, list) or isinstance(obj, dict):
      orig = json.dumps(obj, indent=4)
      print eval("u'''%s'''" % orig).encode('utf-8')
    else:
      print obj

  import sys
  from pit import Pit
  import simplejson as json
  config = Pit.get('yahooapis.jp')
  if not config.has_key('test_account'):
    sys.exit(0)
  
  api = YahooTextAPI(config['test_account'])
  res = api.ma('僕は日本人です。日本の漫画家')
  for word in res['ma_result']['word_list']['word']:
    print word['reading'].encode('utf-8'), word['pos'].encode('utf-8'), word['surface'].encode('utf-8')

  res = api.da('今日はとても天気が良いです。')
  for chunk in res['Result']['ChunkList']['Chunk']:
    print chunk['Id'], chunk['Dependency']
    for morphem in chunk['MorphemList']['Morphem']:
      print morphem['Surface'].encode('utf8'), morphem['Feature'].encode('utf-8')

  res = api.jim('すもももももももものうち')
  for seg in res['Result']['SegmentList']['Segment']:
    print seg['SegmentText'].encode('utf-8'), seg['CandidateList']['Candidate'][0].encode('utf-8')

  res = api.furigana('漢字かな交じり文にふりがなを振ること。')
  pp(res)
  for word in res['Result']['WordList']['Word']:
    if 'Furigana' in word:
      print word['Surface'].encode('utf-8'), word['Furigana'].encode('utf-8'), word['Roman'].encode('utf-8')

  res = api.kousei('遙か彼方に小形飛行機が見える。')
  pp(res)
  for siteki in res['Result']:
    print siteki['Surface'].encode('utf-8'), siteki['ShitekiInfo'].encode('utf-8')

  res = api.keyphrase('東京ミッドタウンから国立新美術館まで歩いて5分で着きます。')
  pp(res)
  for phrase in res['Result']:
    print phrase['Keyphrase'].encode('utf-8'), phrase['Score'].encode('utf-8')
