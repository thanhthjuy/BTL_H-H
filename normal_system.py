import time

def simulate_normal():
    print("\n=== HỆ THỐNG CHẠY BÌNH THƯỜNG ===\n")
    for i in range(1, 21):
        print(f"[OK] Vòng {i}: Hệ thống hoạt động ổn định.")
        time.sleep(0.1)

    print("\n=== KẾT THÚC QUÁ TRÌNH CHẠY BÌNH THƯỜNG ===\n")

if __name__ == "__main__":
    simulate_normal()
