import pika
import os


def callback(ch, method, properties, body):
    print(" [X] Received {!r}".format(body))


if __name__ == "__main__":
    amqp_user = os.environ["AMQP_USER"]
    amqp_pass = os.environ["AMQP_PASS"]

    creds = pika.PlainCredentials(amqp_user, amqp_pass)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=amqp_host, credentials=creds)
    )
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    for method_frame, properties, body in channel.consume("hello"):
        print(f"Received: {body.decode('utf-8')}")
        channel.basic_ack(method_frame.delivery_tag)

    requeued_messages = channel.cancel()
    print("Requeued %i messages" % requeued_messages)

    channel.close()
    connection.close()
