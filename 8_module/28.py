# calendar 모듈
import calendar

calendar.prcal(2025)

calendar.prmonth(2024, 12)

print(calendar.weekday(2024, 12, 15)) # 날짜에 해당하는 요일 정보

# 날짜로 요일 알아내기
import datetime
import calendar

days = ['월', '화', '수','목','금','토','일']
weekday = datetime.date.today().weekday()
print('오늘은 '+days[weekday]+'요일')

weekday = datetime.date(2025, 12, 25).weekday()
print('크리스마스는 '+days[weekday]+'요일')

# 함수로 바꾸기
def getWeekday(yyyy, mm, dd):
    days = ['월', '화', '수','목','금','토','일']
    weekday = datetime.date(yyyy, mm, dd).weekday()
    print(f'{yyyy}년 {mm}월 {dd}일 {days[weekday]}요일')

getWeekday(2024, 12, 24)