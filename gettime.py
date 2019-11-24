#-*- coding:utf-8 -*-
from datetime import date
from datetime import datetime


# <시간 변수 사용법>
# + 프로그램은 먼저 사용자 입력 데이터를 기반으로 추천 리스트를 거른 후 시간 변수를 활용하여 추천의 우선순위를 정한다.
# + 즉, 시간 변수는 프로그램의 의사결정에 있어서(ie 프로그램의 뭐 먹을지 추천해줄 때) 사용자 데이터와 독립이다. 

# + 시간 변수의 데이터는 8자리의 float array로 구성된다 (breakfast, lubch, dinner, snack, winter, spring, summer, winter)
# + 시간 변수는 사용자가 프로그램에게 메뉴를 추천받은 후 Feedback에 따라 변화한다.

# + 시간 변수 계산 방법:: 
# + 긍정적인 Feedback(프로그램을 종료 또는 '이거 먹을래요' 버튼 입력 또는 '음식을 먹은 후 피드백이 긍정적일 경우') 일 경우 적절한 배열 index에 1을 더하고 지금까지 이 음식이 추천 된 횟수로 나눈다.
# + 부정적인 Feedback(다음 메뉴 추천 버튼을 누르거나 음식을 먹을 후 피드백이 부정적인 경우)일 경우 적절한 배열 index에 0을 더하고 지금가지 이 음식이 추천된 횟수로 나눈다.
# + 적절히 학습된 이후에는 프로그램이 추천 우선순위를 정할 때 이 배열을 참고한다.

def GetHour(): #output: 현재 시간을 리턴
    #today = time.today()
    return datetime.now().hour

def GetPeriod(): #output: 현재 시각이 어느 시간대에 있는지 리턴
    _time = GetHour()
    if _time == 6 or _time == 7 or _time == 8 or _time == 9:
        return "아침"
    elif _time == 10 or _time == 11 or _time == 12 or _time == 13 or _time == 14 or _time == 15:
        return "점심"
    elif _time == 16 or _time == 17 or _time == 18 or _time == 19 or _time == 20:
        return "저녁"
    elif _time == 21 or _time == 22 or _time == 23 or _time == 0:
        return "밤"
    else:
        return "새벽"

def GetMonth(): #output: 현재 '월'을 리턴
    today=date.today()
    return today.month


def GetSeason(): #output: 현재 계절을 리턴
    mon=GetMonth()
    if mon == 12 or mon == 1 or mon == 2:
        return "겨울"

    elif mon ==3 or mon == 4 or mon == 5:
        return "봄"

    elif mon ==6 or mon == 7 or mon == 8:
        return "여름"

    elif mon==9 or mon == 10 or mon == 11:
        return "가을"

