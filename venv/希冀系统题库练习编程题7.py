'''import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

hzList = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']#汉字list
dwList = ['','拾','佰','仟']#单位list

def workf(List):
    ansStr = ''
    global hzList
    global dwList
    iSum = 0
    if List == ['0','0','0','0']:
        return ''
    while List[-1] == '0' and len(List) > 0:
        del List[-1]
    x = 0
    while List[x] == '0':
        List[x] = ''
        x += 1
    for x in range(len(List)-1,-1,-1):
        if List[x] == '0':
            if ansStr[-1] != '零':
                ansStr += '零'
        elif List[x] != '':
            ansStr += hzList[int(List[x])] + dwList[x]
        else:
            pass
    return ansStr

n = input()
List = []
for x in range(len(n)):
    List.append(n[x])
List.reverse()
iLen = len(n)
if n == '0':
    print('零元')
else:
    ansStr = ''
    if iLen >= 9:
        ansStr += workf(List[8:iLen])
        ansStr += '亿'
        iLen = 8
    if iLen >= 5:
        if len(ansStr) > 2:
            if ansStr[-2] in dwList and List[0:8] != ['0','0','0','0','0','0','0','0']:
                ansStr += '零'
        ansStr += workf(List[4:iLen])
        if workf(List[4:iLen]) != '':
            ansStr += '万'
        iLen = 4
    if iLen >= 1:
        if len(List) > 4 and ansStr != '':
            if List[3] == '0' and ansStr[-1] == '万':
                ansStr += '零'
        ansStr += workf(List[:iLen])
    print(ansStr + '元整')'''
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

def main():
    money = input()
    tempstrcn = chcurrency(money)
    print(tempstrcn)

def chcurrency(value):
    num = ('零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖')
    iunit = ['元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟', '万', '拾', '佰', '仟']
    dunit = ('角', '分')
    istr =value
    istr = istr[::-1]
    so = []
    if float(istr) == 0:
        return num[0] + iunit[0]

    so.append('整')
    haszero = True
    for i, n in enumerate(istr):
        n = int(n)
        if i % 4 == 0:  # 在圆、万、亿等位上，即使是零，也必须有单位
            if i == 8 and so[-1] == iunit[4]:  # 亿和万之间全部为零的情况
                so.pop()  # 去掉万
            so.append(iunit[i])
            if n == 0:  # 处理这些位上为零的情况
                if not haszero:  # 如果以前没有加过零
                    so.insert(-1, num[0])  # 则在单位后面加零
                    haszero = True  # 标记加过零了
            else:  # 处理不为零的情况
                so.append(num[n])
                haszero = False  # 重新开始标记加零的情况
        else:  # 在其他位置上
            if n != 0:  # 不为零的情况
                so.append(iunit[i])
                so.append(num[n])
                haszero = False  # 重新开始标记加零的情况
            else:  # 处理为零的情况
                if not haszero:  # 如果以前没有加过零
                    so.append(num[0])
                    haszero = True
    so.reverse()
    return ''.join(so)
main()
