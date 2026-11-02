import json
import matplotlib.pyplot as plt

INPUT_FILE = "summary.json"
OUTPUT_FILE = "average_temperature_by_device.png"

def load_device_data(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"Error: File not found: {path}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Error: Invalid JSON in {path}: {e}")
    except OSError as e:
        raise SystemExit(f"Error: Could not read {path}: {e}")

    if not isinstance(data, list) or not data:
        raise SystemExit("Error: JSON must contain a non-empty list of device records.")

    required = {"device_id", "avg_temperature"}
    for i, record in enumerate(data, start=1):
        if not isinstance(record, dict) or not required.issubset(record):
            raise SystemExit(
                f"Error: Record {i} is missing required keys: {sorted(required)}"
            )
        try:
            float(record["avg_temperature"])
        except (TypeError, ValueError):
            raise SystemExit(
                f"Error: Record {i} has a non-numeric avg_temperature."
            )

    return data

def plot_average_temperatures(data):
    device_ids = [record["device_id"] for record in data]
    avg_temperatures = [float(record["avg_temperature"]) for record in data]

    plt.figure(figsize=(max(7, 0.8 * len(device_ids)), 5))
    bars = plt.bar(device_ids, avg_temperatures, color="#4C72B0")

    for bar, temp in zip(bars, avg_temperatures):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{temp:.1f}",
            ha="center",
            va="bottom",
        )

    plt.title("Average Temperature per Device")
    plt.xlabel("Device ID")
    plt.ylabel("Average Temperature")

    # Bug 2: prevent x-axis labels from overlapping
    plt.xticks(rotation=45, ha="right")

    # Bug 3: leave space above the tallest bar and its label
    plt.ylim(0, max(avg_temperatures) * 1.15)

    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    plt.show()

if __name__ == "__main__":
    data = load_device_data(INPUT_FILE)
    plot_average_temperatures(data)