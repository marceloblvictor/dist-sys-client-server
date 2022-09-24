import socket
import book
import json
import time
from json import JSONEncoder

class DataEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


class SDSendBookDataClient:

    HOST = "127.0.0.1"
    PORT = 65432 

    def Send(self, data):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))

            message = ""

            for book in data:
                bookSerializedData = json.dumps(book, indent=4, cls=DataEncoder)
                
                print("Processando dados do seguinte livro:")
                print(bookSerializedData)
                time.sleep(0.25)
                print(".")
                time.sleep(0.25)
                print(".")
                time.sleep(0.25)
                print(".")
                time.sleep(0.25)

                message = message + bookSerializedData + "XXXX"

            time.sleep(0.25)
            s.sendall(bytearray(message, encoding="utf-8"))
            print("Envio concluído!")                       


if __name__ == "__main__":
    client = SDSendBookDataClient()    

    books = []

    id = 0

    while True:

        answer = input("Deseja adicionar algum livro? (y\\n)\n")

        if answer == "y":
            title = input("Qual o titutlo do livro?\n")
            author = input("Qual o autor do livro?\n")
            status = input("Qual o status do livro?\n")

            books.append(book.Book(str(id), title, author, status))
            id += 1
        else:
            break            

    if (len(books) > 0):
        client.Send(books)
    
    

    

