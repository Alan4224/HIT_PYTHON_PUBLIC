# Bài 5: Thầy giáo Ba và Nasus.	
# Thầy giáo Ba là một người đẹp trai, tài năng, tư duy tốt. Thầy thích các số 1, 3, 7, 5, 9 vì vậy các số trong hệ thập phân có chữ số cuối cùng  là một trong năm số trên thì thầy đều thích. Sắp tới là một dịp đặc biệt, Nasus là một học sinh đã được thầy giúp đỡ rất nhiều. Vì vậy anh ấy muốn tặng thầy các con số mà thầy thích. Nasus có một list chứa các số nguyên, Nasus đố các bạn trong list đó có bao nhiêu số mà thầy Ba sẽ thích, hãy in các số đó lên màn hình theo thứ tự tăng dần.
# Input:
# 	Dòng đầu tiên là một số nguyên N: số lượng số mà Nasus có, 1 <= N <= 100
# 	Dòng thứ hai có N số nguyên, mỗi số cách nhau bởi một dấu cách. Giá trị mỗi số nằm trong đoạn [1, 1000]
# Output: 
# 	Dòng đầu tiên là số lượng số thầy Ba thích trong các số Nasus có
# 	Dòng thứ hai là các số thầy Ba thích theo thứ tự tăng dần mà Nasus có

# Ví dụ:

# Input                                 # Output
# 10                                    # 4 
# 1 4 29 187 2 30 50 87 12 34           # 1 29 87 187
                                        # (Các số đều có chữ số cuối là một trong 5 số 1, 3, 5, 7, 9)

N = int(input("Nhập N: "))
lst = list(map(int, input("Nhập list: ").split()))
l = []
for i in lst:
    i = list(str(i))  
    if i[-1] in ['1', '3', '5', '7', '9']:  
        l.append(int(''.join(i)))  
print(len(l))
l.sort()
print(l)