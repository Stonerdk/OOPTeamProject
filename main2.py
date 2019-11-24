from openpyxl import load_workbook
from collections import OrderedDict
from sim import *

# 엑셀 파일로부터 데이터를 받아들임
def encode(excel):
    wb = load_workbook(excel, data_only=True)
    ws = wb["Sheet1"]

    dic = {ws.cell(2, 1).value: 0}
    for i in range(1, ws.max_column):
        if ws.cell(2, i + 1).value:
            dic[ws.cell(2, 1).value] |= (1 << i)

    for i in range(2, ws.max_row):
        for j in range(1, ws.max_column):
            if ws.cell(i + 1, j + 1).value:
                dic.setdefault(ws.cell(i + 1, 1).value, 0)
                dic[ws.cell(i + 1, 1).value] |= (1 << j)

    # 딕셔너리에 저장된 key값과 인코딩된 비트의 속성을 출력
    #    for recipe in dic:
    #        print()
    #        print(recipe)
    #        for i in range(1, ws.max_column):
    #            if dic[recipe] & (1 << i):
    #                print("# " + ws.cell(1, i+1).value)

    return dic

# encode(input("input .xlsx data : "))
'''
# Int를 받아 BinaryVector를 반환함
def IntToBinV(i):
    v = []
    for p in range(1, BitNum + 1):
        if (i & 1 << (BitNum - p)):
            v.append(1)
        else:
            v.append(0)
    # print(v)
    return v

# 받은 Vector를 그 Vector의 크기로 나누어 Vector를 Standardization
def StdV(v):
    cont = 0
    for p in range(0, BitNum):
        if (v[p] == 1):
            cont = cont + 1

    for i in range(1, BitNum + 1):
        v[i - 1] = v[i - 1] / cont
    return v
    # print(v)
'''

# dictionary는 순서가 없기때문에 순서를 만들어줌.
# 예시 data
# f = {"치킨":542, "피자":436, "탕수육":204, "짜장면":242, "짬뽕": 231}

while True:
    f = encode(input("input .xlsx data : "))
    mode = input("mode (d: Dot product, h: Harmonic mean, c: Cosine) : ")

    if(mode != 'd'and mode !='h'and mode != 'c'):
        print("mode를 잘못입력함.")
        break

    barcode = input("비교하고자 하는 대상 바코드 입력: ")
    barcode = barcode.replace(", ", "")
    barcode = int(barcode,2)
    barcode = IntToBinV(barcode)

    food = OrderedDict(sorted(f.items()))
    print("Similarity Map\n")


    # 정렬되지 않은 Similarity Map
    #Sim_not_sort.Result_print(mode, barcode, food)
    # 정렬된 Similarity Map
    Sim_sort.Result_print(mode, barcode, food)
