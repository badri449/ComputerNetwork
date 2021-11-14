# import the socketserver module of Python
import socketserver
code = 'SECRET'
# Create a Request Handler
# In this TCP server case - the request handler is derived from StreamRequestHandler
class MyTCPRequestHandler(socketserver.StreamRequestHandler):
    def get(self,data):
      ans =""
      for i in data:
        if i>='0' and i>='9':
          ans =ans + i
      return ans
# handle() method will be called once per connection
    def handle(self):
        data = str(self.request.recv(1024),"utf-8")
        # Receive and print the data received from client
        print("Message from client: "+self.data) 
        # Send reply
        if code not in data:
          reply = "Secret code not found."
        else:
          ans = self.get(data)
          reply = "Digits: "+ ans +" Count: "+str(len(ans))
        self.request.sendall(bytes(reply,"utf-8"))

            
# Create a TCP Server instance

with socketserver.TCPServer(("10.10.10.2", 5000), MyTCPRequestHandler) as server:
  server.serve_forever()
