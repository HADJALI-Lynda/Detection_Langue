from kafka import KafkaProducer
import json
import numpy as np
import time

with open('test.json') as json_data:
    data = json.load(json_data)

p = KafkaProducer(bootstrap_servers=['localhost:9092'])

for db in data:
        p.send('text', json.dumps(db).encode('utf-8'))
        print('envoyÃ©')
        print(db)
        p.flush()
        time.sleep(3)
