print("플레이 인원을 입력하세요.")

players = int(input())
player = list(range(players))
playetTurn = 0

print("마지막 숫자를 입력하세요.")
maxCount = int(input())
curruntCount = 1
array = list(range(maxCount + 1))
array.remove(0)
print(array)   

isFirst = False

print("숫자가 선정 되었습니다." , maxCount , " 을 말하는 플레이어는 패배합니다.")

while len(array) != 1 :
     #Player Turn
     trun = True
     isFirst = False
     print("시작 숫자 :", array[0])
     count = 0
     while trun:
          print("숫자를 입력 해 주세요.", " 현재 플레이어 :", "Player", player[playetTurn])
          if playetTurn > len(player) : 
               playetTurn = 0 

          playerNum = int(input())
          
          if playerNum == 0 :
               if isFirst == False :
                    print("첫 숫자는 0이 아니여야 합니다.")
                    continue

               print("넘겼습니다.")
               trun = False
               count = 0
          elif array[0] != playerNum :
               print("순서대로 진행해야 합니다. 현재 숫자 :", array[0])
               continue
          else :
               if playerNum in array :
                         isFirst = True
                         array.remove(playerNum)
                         count += 1
                         if len(array) == 1 or  count == 3 :
                              break
     print(array)
     playetTurn += 1
     print("플레이어의 턴이 종료 되었습니다.")

print("게임 종료! 이번 게임은 플레이어" , player[playetTurn] , " 가 패배 하였습니다." )
