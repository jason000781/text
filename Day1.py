import random
##游戏
##摇骰子猜大小+下注

##摇骰子的函数
def roll_dice(numbers = 3,points = None):
    print('<<<<<ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

##将点数转化为大小
def roll_result(total):
    isBig = 11<=total<=18
    isSmall = 3<=total<=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

##下注金额和赔率
def bet_game(youWin,youBet,amount):
    rate = 1
    if youWin:
        amount = amount + youBet*rate
        print('You gained ',youBet, 'you have {} now'.format(amount))
        return amount
    else :
        amount = amount - youBet*rate
        print('You lost ', youBet, 'you have {} now'.format(amount))
        return amount

##开始游戏的函数
def start_game(amount):
    print('<<<<GAME STARTS! >>>>>')
    choices = ['Big','Small']
    you_choice = input('Big or Small : ')
    youBet = int(input('How much you wannna bet ？ -'))
    if you_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = you_choice == roll_result(total)
        if youWin:
            print('The points are ',points,'You win!')
            amount = bet_game(youWin,youBet,amount)
        else:
            print('The poinrs are ',points,'You lose!')
            amount = bet_game(youWin, youBet,amount)
        if amount <= 0:
            print('Game over!')
        else :
            start_game(amount)
    else :
        print('Invalid Words')
        start_game(amount)

# start_game(1000)




##检测号码的真实性
##若存在则发送验证码信息
##长度不少于11位
##为联通、移动、电信号段中的一个电话号码
##因为是输入号码界面，输入除号码外其他字符的可能性可以忽略

def detection_number():
    CN_mobile = ['134','135','136','137','138','139','150','151','152','157','158','159','182','184','187','188','147','178','1705']
    CN_union = ['130','131','132','155','156','185','186','145','176','1709']
    CN_telecom = ['133','153','180','181','189','177','1700']
    scan = input('Enter Your number:')
    if 0<len(scan)<11:
        print('Invalid length,you number should be in 11 digits')
        detection_number()
    else :
        if scan[0:3]or scan[0:4] in CN_mobile:
            print('Operator : China Mobile')
            print('We are sending verification code via text to your phone:',scan)
        elif scan[0:3]or scan[0:4] in CN_union:
            print('Operator : China Union')
            print('We are sending verification code via text to your phone:', scan)
        elif scan[0:3]or scan[0:4] in CN_telecom:
            print('Operator : China Telecom')
            print('We are sending verification code via text to your phone:', scan)
        else :
            print('No such a operator')
            detection_number()
# detection_number()
