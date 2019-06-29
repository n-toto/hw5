#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch
import json
from flask import Flask, render_template, request
from collections import defaultdict
from collections import deque

app = Flask(__name__)
app.debug = True

networkJson = urlfetch.fetch("http://tokyo.fantasy-transit.appspot.com/net?format=json").content  # ウェブサイトから電車の線路情報をJSON形式でダウンロードする
network = json.loads(networkJson.decode('utf-8'))  # JSONとしてパースする（stringからdictのlistに変換する）

@app.route('/')
# / のリクエスト（例えば http://localhost:8080/ ）をこの関数で処理する。
# ここでメニューを表示をしているだけです。
def root():
  return render_template('hello.html')

@app.route('/pata')
# /pata のリクエスト（例えば http://localhost:8080/pata ）をこの関数で処理する。
# これをパタトクカシーーを処理するようにしています。
def pata():
  # とりあえずAとBをつなぐだけで返事を作っていますけど、パタタコカシーーになるように自分で直してください！
  pata = []
  a = request.args.get('word1', '')
  b = request.args.get('word2', '')
  m = max(len(a), len(b))
  for i in range(m):
    if i < len(a):
      pata.append(a[i])
    if i < len(b):
      pata.append(b[i])
  # pata.htmlのテンプレートの内容を埋め込んで、返事を返す。
  return render_template('pata.html', pata="".join(pata))

@app.route('/norikae')
# /norikae のリクエスト（例えば http://localhost:8080/norikae ）をこの関数で処理する。
# ここで乗り換え案内をするように編集してください。

def norikae():
  links = defaultdict(set)
  for line in network:
    for i in range(len(line["Stations"])):
      if i > 0:
        links[line["Stations"][i]].add(line["Stations"][i-1])
      if i < len(line["Stations"])-1:
        links[line["Stations"][i]].add(line["Stations"][i+1])
  print(links)
  station1 = request.args.get('station1', '')
  station2 = request.args.get('station2', '')
  connection = search_target(station1, station2, links)
  route = route_search(station1, station2, connection)
  return render_template('norikae.html', route = route)


# Breadth first search
def search_target(start, goal, links):
    queue = deque([start])
    checked = {start, 0} #set
    connection = {}
    
    while(len(queue)>0):
        if goal in checked:
            return connection
        next = set(links[queue[0]] - checked)
        for v in next:
            connection[v] = queue[0]
        queue += list(next)
        checked.update(next)
        queue.popleft()
        #count += 1
    return ("Not found")


# Search_route
def route_search(station1, station2, connection):
    route = deque()
    s = station2
    while(s != station1):
        route.appendleft(s)
        s = connection[s]
    route.appendleft(station1)
    return route