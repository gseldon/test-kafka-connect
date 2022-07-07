from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['rc1a-l39ro11aorbc4pgf.mdb.yandexcloud.net:9091'],
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_password='PRODUCER_PASSWORD',
    sasl_plain_username='ag_v6navkk_PRODUCER',
    ssl_cafile="/usr/local/share/ca-certificates/Yandex/YandexCA.crt")

# producer.send('ag_v6navkk_DicomSender', b'test message', b'key')
print(producer.bootstrap_connected())
producer.flush()
producer.close()
