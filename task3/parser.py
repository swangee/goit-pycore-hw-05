from collections import defaultdict


def parse_log_line(line: str) -> dict:
    """
    Parses a log line into a dictionary with keys: date, time, level, message and log that that contains
    original log line

    :param line: formatted log line like "date time log_level message"
    :return:
    """
    parts = line.split(" ")

    if len(parts) < 4:
        raise ValueError

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].lower(),
        "message": " ".join(parts[3:]),
        "log": line.strip(),
    }


def load_logs(file_path: str) -> list:
    """
    Loads log file by file_path and returns a list of parsed logs

    :param file_path:
    :return:
    """
    logs = []

    with open(file_path, "r") as f:
        pos = 0
        line = f.readline()

        while line:
            try:
                logs.append(parse_log_line(line))
            except ValueError:
                raise ValueError(f"failed to parse log string at line {pos}")

            line = f.readline()
            pos += 1

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    levels = defaultdict(int)

    for log in logs:
        levels[log["level"]] += 1

    return levels


def display_log_counts(counts: dict):
    display_header()
    display_table(counts)


def display_header():
    print("Рівень логування | Кількість")
    print("-----------------|----------")


def display_table(counts: dict):
    for level, count in counts.items():
        print("{:<17}| {}".format(level, count))


def display_logs(logs: list, log_level: str):
    print(f"\nДеталі логів для рівня '{log_level.upper()}':")

    filtered_logs = filter_logs_by_level(logs, log_level)
    if len(filtered_logs) == 0:
        print("Логів із заданим рівнем не знайдено")
        return

    for log in filtered_logs:
        print(log["log"])
