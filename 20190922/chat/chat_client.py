import socket
from time import localtime, strftime
from threading import Thread
from datetime import datetime



HOST = input('연결 대상 네트워크 주소를 입력해주세요. : ')
PORT = 9009
PORT1 = 9010

def rcvMsg(sock):
   print('대화방에 참여하신것을 환영합니다.')
   print('명령어 확인은 /help를 입력해주세요.')

   while True:
      try:
         data = sock.recv(1024)
         if not data:
            break
         print(data.decode())

      except :
         pass

def getFileFromServer(filename):
   data_transferred = 0
    
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect_ex((HOST, PORT1))
      sock.sendall(filename.encode())

      data = sock.recv(1024)
      if not data:
         print('"[%s]"가 서버에 존재하지 않거나 전송 중 오류가 발생하였습니다.' %filename)
         rcvMsg(sock)
         return 

      with open('./'+filename, 'wb') as f:
         try:
            while data:
               f.write(data)
               data_transferred += len(data)
               data = sock.recv(1024)
               
         except Exception as e:
            print(e)

   print('"[%s]"의 전송이 완료되었습니다. 전송량은 [%d]byte 입니다.' %(filename, data_transferred))

def runChat():   
   start = datetime.now()
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((HOST, PORT))
      t = Thread(target=rcvMsg, args=(sock,))
      t.daemon = True
      t.start()

      while True:
         msg = input()
         if msg == '/quit':
            sock.send(msg.encode())
            break

         if msg == '/rcvfile':
            filename = input('다운로드 받으실 파일이름을 입력해주세요: ')
            getFileFromServer(filename)
         
         if msg == '/time':
            print('현재시간은', strftime('%Y-%m-%d %X\t', localtime()), '입니다.')
         
         if msg == '/help':
            print('/rcvfile - 서버측 서버코드 내 위치한 디렉토리의 파일 다운로드')
            print('/time - 현재시간 확인')
            print('/atime - 접속시간 확인')
            print('/quit - 접속종료')
            print('/tj - 제작자정보')
            pass

         if msg == 'tj':
            print('happy python programing')
            pass

         if msg == '/atime':
            end = datetime.now()
            elapsed = end - start
            print('총 접속 시간: ', end='');print(elapsed)
            elapsed_ms = int(elapsed.total_seconds()*1000)
            print('총 접속 시간: %dms' %elapsed_ms)
            pass

         sock.send(msg.encode())
 
runChat()
