import json
import csv
import sys
import math

def load_stats(path):
    stats = {}
    try:
        with open(path, newline="", encoding='utf-8') as f:
            for row in csv.DictReader(f):
                try:
                    temp = float(row["temperature"])
                    dev  = row["device_id"].strip()
                    status = row["status"]
                except (TypeError, ValueError, KeyError, AttributeError) as e:
                    print("Skipped: ", row, "-> ", repr(e))
                    continue
                if not math.isfinite(temp) or not dev:
                    continue
                if dev not in stats:
                    stats[dev] = {"count": 0, "temp_sum": 0.0, "error_count": 0}
                s = stats[dev]
                s["count"] += 1
                s["temp_sum"] += temp
                if status == "ERROR":
                    s["error_count"] += 1
    except FileNotFoundError:
        sys.exit(f"Error: {path} not found")
    return stats


def build_output(stats):
    output = []
    for dev, s in stats.items():
        avg = s["temp_sum"] / s["count"]
        if avg <= 80.0:
            output.append({
                "device_id"  : dev,
                "total_records": s["count"],
                "avg_temperature": round(avg, 2),
                "error_count": s["error_count"],
            })
    return output

def main():
    stats = load_stats("device_telemetry.csv")
    output = build_output(stats)
    
    with open("summary.json", "w", encoding='utf-8') as f:
        json.dump(output, f, indent = 2)

    print(f"{'Device':<10}{'Records':>8}{'Avg Temp':>10}{'Errors':>8}")
    for d in output:
        print(f"{d['device_id']:<10}{d['total_records']:>8}{d['avg_temperature']:>10}{d['error_count']:>8}")
    

if __name__ == "__main__":
    main()