
# 재고 관리 클래스
class GoodStock:
    def __init__(self, code, stock) -> None:
        
        # 상품 코드
        self.Code = code
        
        # 재고 수량
        self.Stock = stock
        
    # 재고 수량 더하는 함수
    def addStock(self, addstock):
        # 클래스가 가진 재고 수량 변수 = 기존 재고 수량 + 추가 재고 수량
        self.Stock += addstock 
        return self.Stock
    
def main():
    # 객체 생성
    
    # 상품 코드 입력
    code = input("상품 코드를 입력하세요 : ")
    
    # 재고 수량 입력
    stock = int(input("재고 수량을 입력하세요 : "))
    
    obj = GoodStock(code, stock)
    
    # 추가할 수량 입력
    amount = int(input("추가할 수량을 입력하세요 : "))
    
    # 클래스 내부 함수 출력
    total = obj.addStock(amount)
    
    # 총 재고 출력
    print(f"총 재고는 : {total}")
main()