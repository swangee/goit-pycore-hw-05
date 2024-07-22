import sys
from parser import *


log_levels = ['debug', 'info', 'warning', 'error', 'critical']


def is_valid_log_level(log_level) -> bool:
    return log_level.lower() in log_levels


def main():
    if len(sys.argv) == 1:
        print("Please provide an input file")
        return 1

    file_name = sys.argv[1]
    log_level = None

    if len(sys.argv) >= 3:
        log_level = sys.argv[2].lower()

        if not is_valid_log_level(log_level):
            print(f"Invalid log level. Please provide on of [{', '.join(log_levels)}]")
            return 1

    try:
        logs = load_logs(file_name)

        display_log_counts(count_logs_by_level(logs))

        if log_level is not None:
            display_logs(logs, log_level)

    except FileNotFoundError:
        print("Provided file does not exist")
        return 1
    except ValueError as e:
        print("Invalid log file format: " + e.args[0])
        return 1


if __name__ == '__main__':
    main()