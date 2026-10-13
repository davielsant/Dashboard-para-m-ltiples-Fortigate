import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('FORTIGATE_ Informe Completo de Seguridad Gestionada (FortiAnalyzer).json', 'r', encoding='utf-8') as f:
    d = json.load(f)

target_pids = ['panel-2', 'panel-10', 'panel-18', 'panel-30', 'panel-31', 'panel-32', 'panel-60', 'panel-64']

for pid in target_pids:
    p = d['spec']['elements'][pid]['spec']
    print('='*60)
    print(f"[{pid}] Title: '{p.get('title')}' | Viz: {p.get('vizConfig', {}).get('group')}")
    print(f"  FieldConfig defaults: {p.get('vizConfig', {}).get('spec', {}).get('fieldConfig', {}).get('defaults')}")
    print(f"  Options: {p.get('vizConfig', {}).get('spec', {}).get('options')}")
    for idx, q in enumerate(p['data']['spec']['queries']):
        qs = q['spec']['query']['spec']
        print(f"  Query {idx} (Ref: {q.get('spec', {}).get('refId')}):")
        print(f"    Lucene: {qs.get('query')}")
        print(f"    Metrics: {qs.get('metrics')}")
        print(f"    BucketAggs: {qs.get('bucketAggs')}")
