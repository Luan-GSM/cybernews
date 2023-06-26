#!/usr/bin/env python3

import xmltodict, re
import requests, json

from dynaconf import settings


class Scrapp:
  def __init__(self):
    self.__url = settings.SAMIRNEWS
    self.__title = None
    self.__url_news = None
    self.__url_image = None


  @property
  def title(self):
    return self.__title


  @property
  def url_news(self):
    return self.__url_news


  @property
  def url_image(self):
    expression = r'<img[^>]*src="([^"]+)"'
    matches = re.findall(expression, self.__url_image)

    if matches:
      self.__url_image = matches[0]
    return self.__url_image


  @property
  def get_news(self):
    r = requests.get(self.__url)

    if r.status_code != 200:
      return False

    content = xmltodict.parse(r.text)
    self.__title = content["feed"]["entry"][0]["title"]["#text"]
    self.__url_news = content["feed"]["entry"][0]["link"][4]["@href"]
    self.__url_image = content["feed"]["entry"][0]["content"]["#text"]

    return self
