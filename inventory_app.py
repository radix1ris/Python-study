#在庫管理アプリ
import json
def save_product(products):
    with open("products.json","w",encoding="utf-8")as file:
        json.dump(products,file,ensure_ascii=False,indent=4)

def load_products():
    with open("products.json","r",encoding="utf-8")as file:
        products = json.load(file)
        return products

products = load_products()
#商品追加
def add_product(products,target_product):
    for product in products:
        if product["name"] == target_product["name"]:
            return False
    products.append(target_product)
    return True

#商品検索
def find_product(products,search_product):
    for product in products:
        if product["name"] == search_product:
            return product
    return False

#在庫変更
def update_stock(products,name_product,add_stock):
    for product in products:
        if product["name"] == name_product:
            product["stock"] = add_stock
            return True
    return False

#商品削除
def delete_product(products,name_product):
    for product in products:
        if product["name"] == name_product:
            products.remove(product)
            return True
    return False


def main_menu():
    print("1.商品追加")
    print("2.商品検索")
    print("3.在庫変更")
    print("4.商品削除")
    print("5.終了")
    try:
        menu_number = int(input("メニュー番号を入力:"))
        if menu_number > 0 and menu_number < 6:
            return menu_number
        else:
            print("１～５を入力してください")
    except ValueError:
        print("数字を入力してください")
    
def main():
    while True:
        menu_number = main_menu()
        if menu_number == 1:
            name = input("商品名を入力:")
            try:
                price = int(input("金額を入力:"))
                stock = int(input("個数を入力:"))
            except ValueError:
                print("金額と個数は数字で入力してください")
                continue
            if price < 0:
                print("金額は0以上で入力してください")
                continue

            if stock < 0:
                print("個数は0以上で入力してください")
                continue

            target_product = {
                "name": name,
                "price": price,
                "stock": stock
            }
            result = add_product(products,target_product)
            if result == True:
                save_product(products)
                print("商品を追加しました")
            else:
                print("既に存在している商品です")
            
        elif menu_number == 2:
            search_product = input("検索する商品名を入力:")
            result = find_product(products,search_product)
            if result == False:
                print("商品が見つかりませんでした")
            else:
                print(f"商品名:{result['name']}")
                print(f"価格:{result['price']}")
                print(f"在庫数:{result['stock']}")
        elif menu_number == 3:
            name_product = input("商品名を入力:")
            try:
                add_stock = int(input("在庫数を入力:"))
            except ValueError:
                print("個数は数字で入力してください")
                continue
            if add_stock < 0:
                print("個数は0以上で入力してください")
                continue
            result = update_stock(products,name_product,add_stock)
            if result == True:
                save_product(products)
                print(f"{name_product}の在庫数を{add_stock}に変更しました")
            else:
                print("商品がみつかりませんでした")
        elif menu_number == 4:
            name_product = input("削除する商品名を入力:")
            result = delete_product(products,name_product)
            if result == True:
                save_product(products)
                print(f"{name_product}を削除しました")
            else:
                print("商品が見つかりませんでした")
        elif menu_number == 5:
            break
main()







    
