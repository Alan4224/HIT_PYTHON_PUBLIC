# Bài 4. 
# Viết chương trình Python thực hiện các yêu cầu sau:
# Xây dựng lớp Tam thức bậc hai với các thuộc tính là các hệ số a, b, c kiểu thực
# và các phương thức:
# Khởi tạo các giá trị cho các hệ số a, b, c.
# __str__ in tam thức lên màn hình (ax2+bx+c)
# Cộng, trừ hai tam thức (cộng, trừ hệ số tương ứng).
# Xây dựng chương trình khai báo 2 tam thức. Khởi gán giá trị cho các hệ số và
# thực hiện đảo dấu của 2 tam thức. Tính và in ra màn hình các tam thức là tổng và hiệu của 2 tam thức đã đảo dấu ở trên.

class TamThuc:
    def __init__(self,a,b,c) -> None:
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        print(f"{self.a}x2+{self.b}x+{self.c}")

    def Cong(self,other):
        a=self.a+other.a
        b=self.b+other.b
        c=self.c+other.c
        return TamThuc(a,b,c)
    
    def Tru(self,other):
        a=self.a-other.a
        b=self.b-other.b
        c=self.c-other.c
        return TamThuc(a,b,c)
    
    def Dao(self):
        self.a=-self.a
        self.b=-self.b
        self.c=-self.c

tamthuc1 = TamThuc(1,2,3)
tamthuc2 = TamThuc(4,5,6)
tamthuc1.Dao()
tamthuc2.Dao()
tamthucTong=TamThuc.Cong(tamthuc1,tamthuc2)
tamthucHieu=TamThuc.Tru(tamthuc1,tamthuc2)
tamthucTong.__str__()
tamthucHieu.__str__()
