from kafka import KafkaConsumer


## define a consumer that waits for messages

def kafka_python_consumer():
    #consumer= KafkaConsumer(topics="ingestion-topic",group_id="mypythonconsumer",bootstrap_servers="localhost:9092",)
    consumer = KafkaConsumer('ingestion-topic', group_id='mypythonconsumer',bootstrap_servers='kafka:9092', api_version=(2,8,0),)
    

    for msg in consumer:
        print(msg)


print("start consumming")


kafka_python_consumer()

print('done')