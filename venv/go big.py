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
        return num[0] + iunit[0] + '整'
    so.append('整')
    haszero = True
    for i, n in enumerate(istr):
        n = int(n)
        if i % 4 == 0:  # 在圆、万、亿等位上，即使是零，也必须有单位
            if i == 8 and so[-1] == iunit[4]:  # 亿和万之间全部为零的情况
                so.pop()  # 去掉万
            so.append(iunit[i])
            if n != 0:
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
