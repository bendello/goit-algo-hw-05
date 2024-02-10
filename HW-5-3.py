import sys
import re
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)', line)
    if match:
        return {'timestamp': match.group(1), 'level': match.group(2), 'message': match.group(3)}
    else:
        return {'timestamp': '', 'level': '', 'message': ''}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log = parse_log_line(line.strip())
                logs.append(log)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_log_file> [log_level]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")

if __name__ == "__main__":
    main()