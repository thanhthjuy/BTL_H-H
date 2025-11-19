import random
import matplotlib.pyplot as plt

results = []

def simulate_normal_operation(i):
    results.append((i, "OK"))

def inject_fault(i):
    recovered = random.random() < 0.7
    if recovered:
        results.append((i, "Recovered"))
    else:
        results.append((i, "Failed"))

def run_simulation(total_cycles=20):
    for i in range(1, total_cycles + 1):
        if random.random() < 0.3:
            inject_fault(i)
        else:
            simulate_normal_operation(i)
    return results

def plot_line_chart(results):
    status_map = {"OK": 1, "Recovered": 2, "Failed": 0}
    x = [i for i, r in results]
    y = [status_map[r] for i, r in results]

    plt.figure(figsize=(12,4))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.yticks([0,1,2], ["Failed", "OK", "Recovered"])
    plt.xlabel("Vòng chạy")
    plt.ylabel("Trạng thái")
    plt.title("Tiêm lỗi & Phục hồi hệ thống (Biểu đồ đường)")
    plt.grid(True)
    plt.savefig("fault_injection_line.png")
    plt.show()
    print("[✓] Biểu đồ đường đã lưu: fault_injection_line.png")

if __name__ == "__main__":
    results = run_simulation(20)
    plot_line_chart(results)
