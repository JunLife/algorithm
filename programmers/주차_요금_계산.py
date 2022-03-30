import math

def solution(fees, records):
    cur_time = dict()
    car_status = dict()
    cur_fee = dict()
    
    # IN, OUT 계산
    for record in records:
        time, number, status = record.split()
        if status == 'IN':
            car_status[number] = f'IN {time}'
        else:
            before_status = car_status[number]
            car_status[number] = 'OUT'
            
            plus_time(time, before_status.split()[1], number, cur_time, fees)
    
    # 출차되지 않은 경우
    for key, value in car_status.items():
        if value != 'OUT':
            plus_time('23:59', value.split()[1], key, cur_time, fees)
                
    for key, time in cur_time.items():
        cur_fee[key] = fees[1] + math.ceil(max(time, 0) / fees[2]) * fees[3]
        
    answer = dict(sorted(cur_fee.items()))
    return list(answer.values())


def calc_time(time, in_time):
    hour = (int(time.split(':')[0]) - int(in_time.split(':')[0])) * 60
    _min = (int(time.split(':')[1]) - int(in_time.split(':')[1]))
    if _min < 0:
        _min += 60
        hour -= 60
    return hour + _min

def plus_time(time, in_time, key, cur_time, fees):
    plus_time = calc_time(time, in_time)

    if key in cur_time:
        cur_time[key] += plus_time
    else:
        cur_time[key] = plus_time - fees[0]