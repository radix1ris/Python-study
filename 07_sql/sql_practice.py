import sqlite3
connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
def add_user(name,age):
    cursor.execute("""
    INSERT INTO users(name,age)
    VALUES(?,?)
    """,(name,age,))
    connection.commit()
    return cursor.lastrowid

def get_user(user_id):
    cursor.execute("""
    SELECT * FROM users
    WHERE id = ?
    """,(user_id,))
    result = cursor.fetchone()
    return result

def update_user_age(user_id,age):
    cursor.execute("""
    UPDATE users
    SET age = ?
    WHERE id = ?
    """,(age,user_id,))
    result = cursor.rowcount
    connection.commit()
    return result
    
def delete_user(user_id):
    cursor.execute("""
    DELETE FROM users
    WHERE id = ?
    """,(user_id,))
    connection.commit()
    result = cursor.rowcount
    return result

def main_manu():
    print("1.ユーザー登録")
    print("2.ユーザー検索")
    print("3.年齢変更")
    print("4.ユーザー削除")
    print("5.終了")
    try:
        menu_number = int(input("番号を選択:"))
        if menu_number <= 0 or menu_number >= 6:
            print("1~5の数字を入力してください")
        else:
            return menu_number
    except ValueError:
        print("数字を入力してください")

def main():
    while True:
        menu_number = main_manu()
        if menu_number == 1:
            name = input("登録する名前を入力:")
            try:
                age = int(input("年齢を入力:"))
                if age < 0 or age > 120:
                    print("年齢は0~120の範囲で入力してください")
                else:
                    result = add_user(name,age)
                    print(f"登録しました(ID:{result})")
            except ValueError:
                print("数字を入力してください")
        elif menu_number == 2:
            try:
                user_id = int(input("検索するユーザーIDを入力:"))
                result = get_user(user_id)
                if result is None:
                    print("ユーザーが見つかりませんでした")
                else:
                    print(f"ID: {result[0]}")
                    print(f"名前: {result[1]}")
                    print(f"年齢: {result[2]}")
            except ValueError:
                print("数字を入力してください")
        elif menu_number == 3:
            try:
                user_id = int(input("変更するユーザーIDを入力:"))
                age = int(input("変更後の年齢を入力:"))
                if age < 0 or age > 120:
                    print("年齢は0~120の範囲で入力してください")
                else:
                    result = update_user_age(user_id,age)
                    if result == 0:
                        print("ユーザーが見つかりませんでした")
                    else:
                        print("年齢を変更しました")
            except ValueError:
                print("数字を入力してください")
        elif menu_number == 4:
            try:
                user_id = int(input("削除したいユーザーのIDを入力:"))
                result = delete_user(user_id)
                if result == 0:
                    print("ユーザーが見つかりませんでした")
                else:
                    print("ユーザーを削除しました")
            except ValueError:
                print("数字で入力してください")
        elif menu_number == 5:
            print("終了します")
            break

main()
connection.close()











