import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('decoders_rules_wazuh/0100-fortigate_decoders.xml', 'r', encoding='utf-8') as f:
    text = f.read()

decoders = re.findall(r'<decoder name="([^"]+)">', text)
print(f"Total decoders: {len(decoders)}")
for d in decoders:
    if any(k in d.lower() for k in ['sys', 'event', 'perf', 'stat']):
        print(" ", d)

# Check all orders
orders = re.findall(r'<order>(.*?)</order>', text)
print(f"Total orders: {len(orders)}")
for o in orders:
    if 'mem' in o or 'cpu' in o or 'util' in o:
        print("  Order with mem/cpu/util:", o)
