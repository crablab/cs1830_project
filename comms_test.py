# Please remember to only use one of these...or it will break (obvs)

cl = client("localhost", 5027)

cl.send.put("{'id': 'asd'}")

while 1 == 1:
    print("- Queues - \n Recieve: " + str(cl.recieved.qsize()))
    print("Send: " + str(cl.send.qsize()))
    time.sleep(2)
    cl.send.put("{'id': 'asd'}")
    cl.send.put("{'id': 'qwe'}")
    cl.send.put("{'id': 'some stuff'}")


server = server()

while 1 == 1:
    print("- Queues - \n Recieve: " + str(server.recieved.qsize()))
    print("Send: " + str(server.send.qsize()))
    time.sleep(2)

    server.send.put("{'id': 'asd'}")
    server.send.put("{'id': 'qwe'}")
    server.send.put("{'id': 'some stuff'}")
