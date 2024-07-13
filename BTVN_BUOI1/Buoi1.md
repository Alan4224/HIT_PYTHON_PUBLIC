Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?

-Từng dòng lệnh Python không được thực thi trực tiếp, mà được dịch sang bytecode trước khi cho vào máy ảo để thực thi. Vì thế, nói rằng Python là compiled language cũng không sai. Nhưng vì quá trình dịch và thực thi bytecode là hoàn toàn tự động và ẩn, nên Python thường được gọi là ngôn ngữ lập trình kiểu thông dịch.

Bài 2:  Tìm hiểu trước kiến thức buổi 2 về :
Các kiểu dữ liệu trong Python
Các toán tử trong Python
Mệnh đề điều kiện và vòng lặp
Kiểu dữ liệu True, False

-Các kiểu dữ liệu trong Python
+Kiểu dữ liệu văn bản: str
+Kiểu dữ liệu số: int, float, complex
+Kiểu dữ liệu dãy: list, tuple, range
+Kiểu dữ liệu ánh xạ: dict
+Kiểu dữ liệu tập hợp: set, frozenset

-Các toán tử trong Python
+Toán tử số học
+Toán tử quan hệ (so sánh)
+Toán tử gán
+Toán tử logic
+Toán tử membership

-Mệnh đề điều kiện và vòng lặp
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if none of the above conditions are true

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
