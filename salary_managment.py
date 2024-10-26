import mysql.connector
from mysql.connector import Error

def update_employee_salary(employee_id, new_salary):
    try:
        # Veritabanı bağlantısı
        connection = mysql.connector.connect(
            host='localhost',          # Sunucu adresi
            user='root',      # Veritabanı kullanıcı adı
            password='1215173,',  # Veritabanı şifresi
            database='dump'   # Veritabanı adı
        )

        if connection.is_connected():
            cursor = connection.cursor()
        
            select_query = "SELECT salary FROM employees WHERE employee_id = %s"
            cursor.execute(select_query, (employee_id,))
            result = cursor.fetchone()
            
            if result:
                update_query = "UPDATE employees SET salary = %s WHERE employee_id  = %s"
                cursor.execute(update_query, (new_salary, employee_id))
                
                connection.commit()
                
                print(f"Maaş güncelleme başarılı!")
                print(f"Eski maaş: {result[0]}")
                print(f"Yeni maaş: {new_salary}")
            else:
                print(f"ID {employee_id} olan çalışan bulunamadı.")

    except Error as e:
        print(f"Hata: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Veritabanı bağlantısı kapatıldı.")

def main():
    while True:
        try:
            print("\n=== Çalışan Maaş Güncelleme Sistemi ===")
            employee_id = int(input("Çalışan ID (Çıkış için -1): "))
            
            if employee_id == -1:
                print("Program sonlandırılıyor...")
                break
                
            new_salary = float(input("Yeni maaş: "))
            
            if new_salary < 17500:
                print("Maaş asgari ücretten düşük olamaz!")
                continue
                
            update_employee_salary(employee_id, new_salary)
            
        except ValueError:
            print("Lütfen geçerli sayısal değerler girin!")
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
