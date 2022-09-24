import socket
import book
import json
from json import JSONEncoder

class DataEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


class SDReceiveBookDataServer:

    HOST = "127.0.0.1"
    PORT = 65432 

    def Listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            print("Aguardando conexão...")
            
            s.bind((self.HOST, self.PORT))
            s.listen()
            
            conn, addr = s.accept()
            
            with conn:

                print(f"Ouvindo em: {addr}")

                while True:
                    data = conn.recv(1024)
                    
                    if not data:
                        break

                    data = str(data, encoding="utf-8")
                    books = data.split("XXXX")
                    books = [b for b in books if b != ""]

                    for book in books:

                        if (len(book) > 0):                            
                            jsonBook = json.loads(book)
                            print(f"Livro Recebido:\n")
                            strBook = json.dumps(jsonBook, indent=4, cls=DataEncoder)
                            print(strBook + "\n")

                            bookProps = [jsonBook['id'], f"\"{jsonBook['title']}\"", f"\"{jsonBook['author']}\"", f"\"{jsonBook['status']}\""]
                            bookRow = ",".join(bookProps)

                            with open('inventory.csv', 'a') as f:
                                f.write("\n")                                
                                f.writelines(bookRow)                                                                

if __name__ == "__main__":
    
    server = SDReceiveBookDataServer()
    server.Listen()