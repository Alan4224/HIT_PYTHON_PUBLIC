# Bài 2:(25 điểm):
# Trong một cuộc thi đi bộ đặc biệt tại công viên, một chú rùa quyết định tham gia và đặt mục tiêu chinh phục một đoạn đường dài. Chú rùa bắt đầu hành trình từ điểm xuất phát tại tọa độ 0 và phải đến đích ở tọa độ x (x>0) trên con đường thẳng. Mỗi bước đi của chú rùa có thể dài từ 1 đến 3 đơn vị. Bạn được giao nhiệm vụ giúp chú rùa tính toán số bước tối thiểu cần thiết để hoàn thành cuộc thi.
# Đầu vào:
# Một số nguyên x (1≤x≤1,000) — tọa độ của điểm đích mà chú rùa cần phải đến.
# Đầu ra:
# In ra số bước tối thiểu mà chú rùa cần để di chuyển từ điểm 0 đến điểm x một cách nhanh nhất.
# Test:

# Input
# Output
# 10
# 4



d= int(input())
print(int(d/3)+d%3)