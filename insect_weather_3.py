#!/usr/bin/python3.5
#-*- coding=UTF-8 -*-

import urllib.request
import re

def getHtml(url):
	page = urllib.request.urlopen(url)
	#通过request打开url，输出page为byte流
	html = page.read().decode('utf-8')
	#将从page中读取到的流解码成UTF-8编码
	page.close
	return html

def get_city(html):
	reg = r'<title>【(.+?)天气】.+?</title>'	#正则表达式 匹配title标签内 至少一个任意字符+天气+至少一个任意字符
	get_list = re.findall(reg,html)		#根据获取的网页解码和正则表达式获得城市名称
	if len(get_list)>0:							
		return get_list[0]					#返回匹配数据
	else:
		return "无数据"

def get_start(html):		
	reg=r'<h1>.+?（今天.+?</h1>'		#正则表达式 获取今天天气信息
	get_list = re.findall(reg,html)
	if len(get_list)>0:
		return get_list[0]
	else:
		return "无数据"

def get_end(html):
	reg=r'<h1>.+?（明天.+?</h1>'		#正则表达式 获取明天天气信息
	get_list = re.findall(reg,html)
	if len(get_list)>0:
		return get_list[0]
	else:
		return "无数据"

def get_block(html):
	start=html.find(get_start(html))
	end=html.find(get_end(html))
	block=html[start:end]		#获取数据后放入一个List[]
	return block

def get_block_date(block):
	reg=r'<h1>(.+?)（今天.+?</h1>'
	get_list = re.findall(reg,block)
	if len(get_list)>0:
		return get_list[0]
	else:
		return "无数据"

def get_block_air(block):
	reg=r'p class="wea" title="(.+?)".+?'
	get_list = re.findall(reg,block)
	if len(get_list)>0:
		return get_list[0]
	else:
		return "无数据"

def get_block_day_tmp(block):
	reg=r'<span>([0-9]+).+?</span>'
	get_list = re.findall(reg,block)
	if len(get_list)>0:
		return get_list[0]
	else:
		return "无数据"

def get_block_night_tmp(block):
	reg=r'<i>([0-9]+).+?</i>'
	get_list = re.findall(reg,block)
	if len(get_list)>0:
		return get_list[0]
	else:
		return "无数据"

def get_block_wind(block):
	reg=r'<i>([^0-9]+)</i>'
	get_list = re.findall(reg,block)
	if len(get_list)>0:
		return get_list[0]
	else:
		return "无数据"

html = getHtml("http://www.weather.com.cn/weather/101010100.shtml")
block=get_block(html)

print("所在城市:"+get_city(html))
print("查询日期:"+get_block_date(block))
print("天气情况:"+get_block_air(block))
print("日间温度:"+get_block_day_tmp(block))
print("夜间温度:"+get_block_night_tmp(block))
print("风力指数:"+get_block_wind(block))

