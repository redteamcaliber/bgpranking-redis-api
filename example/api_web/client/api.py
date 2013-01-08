#!/bin/python
# -*- coding: utf-8 -*-

try:
    import simplejson as json
except:
    import json

import requests

url = 'http://bgpranking.circl.lu/json'

def all_ranks_single_asn(asn, last_day = None, timeframe = None,
        dates_sources = None, with_details_sources = None):
    query = {'method': 'all_ranks_single_asn'}
    query.update({'asn': asn, 'last_day': last_day,
            'timeframe': timeframe, 'dates_sources': dates_sources,
            'with_details_sources': with_details_sources})
    r = requests.post(url, data=json.dumps(query))
    return r.json

def all_ranks_all_asns(last_day = None, timeframe = None,
        dates_sources = None, with_details_sources = None):
    query = {'method': 'all_ranks_all_asns'}
    query.update({'last_day': last_day, 'timeframe': timeframe,
            'dates_sources': dates_sources,
            'with_details_sources': with_details_sources})
    r = requests.post(url, data=json.dumps(query))
    return r.json

def asn_description(asn, date = None, sources = None):
    query = {'method': 'asn_description'}
    if sources is not None and type(sources) is not type([]):
        sources = [sources]
    query.update({'asn': asn, 'date': date, 'sources': sources})
    r = requests.post(url, data=json.dumps(query))
    return r.json

def ips_description(asn, asn_timestamp, date = None, sources = None):
    query = {'method': 'ips_description'}
    if sources is not None and type(sources) is not type([]):
        sources = [sources]
    query.update({'asn': asn, 'asn_timestamp': asn_timestamp,
            'date': date, 'sources': sources})
    r = requests.post(url, data=json.dumps(query))
    return r.json

def stats(last_day = None, timeframe = None, dates_sources = None):
    query = {'method': 'stats'}
    query.update({'last_day': last_day,'timeframe': timeframe,
            'dates_sources': dates_sources})
    r = requests.post(url, data=json.dumps(query))
    return r.json

def block_owner_description(asn, block):
    query = {'method': 'block_owner_description'}
    query.update({'asn': asn, 'block': block})
    r = requests.post(url, data=json.dumps(query))
    return r.json

def cached_dates():
    query = {'method': 'cached_dates'}
    r = requests.post(url, data=json.dumps(query))
    return r.json

def cached_daily_rank(asn, date = None, sources = None):
    query = {'method': 'cached_daily_rank'}
    if sources is not None and type(sources) is not type([]):
        sources = [sources]
    query.update({'asn': asn, 'date': date, 'sources': sources})
    r = requests.post(url, data=json.dumps(query))
    return r.json

def cached_top_asns(date = None, source = None, limit = None,
        with_sources = None):
    query = {'method': 'cached_top_asns'}
    query.update({'date': date, 'source': source, 'limit': limit,
            'with_sources': with_sources})
    r = requests.post(url, data=json.dumps(query))
    return r.json
