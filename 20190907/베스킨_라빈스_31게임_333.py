print("31 게임")

nums = []
for x in range(31) :
    nums.append(x+1)
print(nums)

a = 1
b = 2
input_cnt = 0
min_input = 1
max_input = 4


while len(nums) != 0:
    
    print()
    user_input = int(input("플레이어 {} 순서, 입력할 숫자는? : ".format(a)))
    if user_input == 0 :
       if min_input < input_cnt:         
           a, b = b, a
           input_cnt = 0
           print(nums)
       else :
           print()
           print("숫자 하나는 반드시 입력해야 합니다")
    elif user_input == 31 :
        print()
        print("플레이어 {} 패배!!".format(a))
        break
    elif user_input != 0 and user_input != nums[0] :
        print("순서대로 입력해주세요")
    else :
        if input_cnt >= max_input-1 :
            print("0으로 종료 해주세요(입력은 취소 됩니다.)")
        else : 
            input_cnt += 1
            if user_input in nums :            
                nums.remove(user_input)
            else :
                print()
                print("잘못된 숫자!! 다시입력!!")
                print(nums)
  
