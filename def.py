# 함수 이용 
# ft 시간, fp 시급, 40시간 넘게 일하면 넘은 시간 당 시급 1.5배
# 연봉은 시간 * 시급

def work(hour, rate) :
    if hour > 40 :
        ovwork = (hour - 40) * 1.5 * rate
        regwork = 40 * rate
        pay = ovwork + regwork
    else :
        pay = hour * rate
    return pay

wt = input('work time?')
wr = input('work rate?')

fwt = float(wt)
fwr = float(wr)

xp = work(fwt, fwr)

print("pay = ", xp)