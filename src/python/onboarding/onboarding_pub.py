import time
from src.protocols.python import telemetry_pb2
from src.python.messaging import Publisher

def main():
    publisher = Publisher(address="tcp://127.0.0.1:5555", topic="telemetry")
    temp = 1
    while True:
        message = telemetry_pb2.telemetry(temperature=temp, depth=1)
        temp += 1
        if (temp >= 10):
            temp = 1
        publisher.publish(message)
        time.sleep(1)

if __name__ == "__main__":
    main()