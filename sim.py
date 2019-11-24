from openpyxl import load_workbook
from dictionary import Dictionary
from collections import OrderedDict
    
BitNum = 32

def IntToBinV(i):
    v = []
    for p in range(1, BitNum + 1):
        if (i & 1 << (BitNum - p)):
            v.append(1)
        else:
            v.append(0)
    # print(v)
    return v

def StdV(v):
    cont = 0
    for p in range(0, BitNum):
        if (v[p] != 0):
            cont = cont + v[p]*v[p]

    for i in range(0, BitNum):
        v[i] = v[i] / pow(cont,0.5)
    return v

class Dot(Dictionary):
    def Similarity(v1, v2):
        sum_s = 0.0
        for i in range(0,BitNum): 
           sum_s = sum_s + v1[i]*v2[i]
            
        return sum_s

class Harmonic(Dictionary):
    def Similarity(v1, v2):
        sum_s = 0.0
        for i in range(0,BitNum): 
           if((v1[i]+ v2[i])==0):
               sum_s = sum_s +0
           else:
               sum_s = sum_s + (2*v1[i]*v2[i])/(v1[i]+ v2[i])
        return sum_s

class Cosine(Dictionary):
    def Similarity(v1, v2):
        sum_s = 0.0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for i in range(0,BitNum): 
           sum1 = sum1 + v1[i]*v2[i]
        for i in range(0,BitNum):
           sum2 = sum2 + v1[i]*v1[i]
        for i in range(0,BitNum):
           sum3 = sum3 + v2[i]*v2[i]
        sum2 = pow(sum2,0.5)
        sum3 = pow(sum3,0.5)
        if(sum2*sum3)==0:
           sum_s =sum_s + 0
        else:
           sum_s = sum_s + sum1/(sum2*sum3)
        return sum_s

class Sim_not_sort(Dictionary):
    def Result_print(mode, barcode, f):
        # 0으로 초기화된 Similarity dir
        SM = {}
        
        print("Sort 하지 않은 결과: ========================================\n")
        
        # data 전처리과정. int->binary vector(list) -> standardization
        for name, val in f.items():
            # int val을 binary값으로 변환시킨 값
            val = bin(val)
            #print(f'{name:5} ==> {val:10}')

        for name, val in f.items():
            # int 를 binary vector(List)로 변환시킨 값
            v = IntToBinV(val)
            #print(f'{name:5} ==> {v}')
            # Binary vector(list)를 Standradization한 값
            v = StdV(v)
            #print(f'{name:5} ==> {v}')

        Max_s = 0 # Max Similarity
        self_s = 0 # Self Similarity
        Max_key1 = 0 # Max Similarity를 갖는 key1 
        Max_key2 = 0 # Max Similarity를 갖는 key2

        # SM을 순회
        for y_name, y_val in f.items():
            #X = StdV(IntToBinV(x_val))
            #Y = StdV(IntToBinV(y_val))
            #X = StdV(barcode)
            Y = IntToBinV(y_val)
            X = barcode

            if (mode == 'd'):
                print(f'X : {X}')
                print(f'Y : {Y}')
                self_s = Dot.Similarity(X, X)
                SM[y_name] = Dot.Similarity(X, Y)  # 계산식 들어가는 부분. 계산함수 = Dot Similarity
                s = Dot.Similarity(X, Y)

            elif (mode == 'h'):
                print(f'X : {X}')
                print(f'Y : {Y}')
                self_s = Harmonic.Similarity(X, X)
                SM[y_name] = Harmonic.Similarity(X, Y)  # 계산식 들어가는 부분. 계산함수 = Harmonic Similarity
                s = Harmonic.Similarity(X, Y)

            elif (mode == 'c'):
                print(f'X : {X}')
                print(f'Y : {Y}')
                self_s = Cosine.Similarity(X, X)
                SM[y_name] = Cosine.Similarity(X, Y)  # 계산식 들어가는 부분. 계산함수 = Cosine Similarity
                s = Cosine.Similarity(X, Y)

            print("비교대상", f'{y_name} of s = {s}')

        print(f'자기유사도: {self_s}')
        return SM
        
class Sim_sort(Dictionary):
    def Result_print(mode, barcode, f):
        # 0으로 초기화된 Similarity dir
        SM = {}
        
        print("Sort 한 결과: ========================================\n")
        
        # data 전처리과정. int->binary vector(list) -> standardization
        for name, val in f.items():
            # int val을 binary값으로 변환시킨 값
            val = bin(val)
            #print(f'{name:5} ==> {val:10}')

        for name, val in f.items():
            # int 를 binary vector(List)로 변환시킨 값
            v = IntToBinV(val)
            #print(f'{name:5} ==> {v}')
            # Binary vector(list)를 Standradization한 값
            v = StdV(v)
            #print(f'{name:5} ==> {v}')

        Max_s = 0 # Max Similarity
        self_s = 0 # Self Similarity
        Max_key1 = 0 # Max Similarity를 갖는 key1 
        Max_key2 = 0 # Max Similarity를 갖는 key2

        # SM을 순회
        for y_name, y_val in f.items():
            #X = StdV(IntToBinV(x_val))
            #Y = StdV(IntToBinV(y_val))
            #X = StdV(barcode)
            Y = IntToBinV(y_val)
            X = barcode

            if (mode == 'd'):
                print(f'X : {X}')
                print(f'Y : {Y}')
                self_s = Dot.Similarity(X, X)
                SM[y_name] = Dot.Similarity(X, Y)  # 계산식 들어가는 부분. 계산함수 = Dot Similarity
                s = Dot.Similarity(X, Y)

            elif (mode == 'h'):
                print(f'X : {X}')
                print(f'Y : {Y}')
                self_s = Harmonic.Similarity(X, X)
                SM[y_name] = Harmonic.Similarity(X, Y)  # 계산식 들어가는 부분. 계산함수 = Harmonic Similarity
                s = Harmonic.Similarity(X, Y)

            elif (mode == 'c'):
                print(f'X : {X}')
                print(f'Y : {Y}')
                self_s = Cosine.Similarity(X, X)
                SM[y_name] = Cosine.Similarity(X, Y)  # 계산식 들어가는 부분. 계산함수 = Cosine Similarity
                s = Cosine.Similarity(X, Y)

            #print("비교대상", f'{y_name} of s = {s}')
        
        # 배열에서 두번째값을 반환해주는 함수
        def f2(x):
            return x[1]

        SM_Ordered = OrderedDict(sorted(SM.items(),key=(lambda x:x[1]),reverse = True))
        #print(SM_Ordered)
        k=0
        ret=[]
        for x_name, x_val in SM_Ordered.items():
            ret.append(x_name)
            k+=1
            if k>=5:
                break

        return ret