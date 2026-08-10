# Calculate hours worked (CLI-friendly)
import argparse
import re
import sys

def calculate_hours_worked(start_time="11:00", end_time="17:30"):
    """Calculate total hours worked between two times in HH:MM format.

    Accepts times that cross midnight (e.g., 22:00 02:00 -> 4 hours).
    Returns a float number of hours.
    """
    def parse_time(t):
        if not re.match(r"^\d{1,2}:\d{2}$", t):
            raise ValueError(f"Invalid time format: {t!r}. Expected HH:MM")
        h, m = map(int, t.split(":"))
        if not (0 <= h < 24 and 0 <= m < 60):
            raise ValueError(f"Invalid time value: {t!r}. Hours 0-23, minutes 0-59")
        return h * 60 + m

    start_minutes = parse_time(start_time)
    end_minutes = parse_time(end_time)

    if end_minutes < start_minutes:
        # Assume crossing midnight
        end_minutes += 24 * 60

    total_minutes_worked = end_minutes - start_minutes
    return total_minutes_worked / 60.0


def format_hours(hours_float):
    hours_int = int(hours_float)
    minutes = round((hours_float - hours_int) * 60)
    return f"{hours_int}h {minutes}m ({hours_float:.2f} hours)"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate hours worked between two times (HH:MM).")
    parser.add_argument("start", nargs="?", default="11:00", help="Start time in HH:MM (default: 11:00)")
    parser.add_argument("end", nargs="?", default="17:30", help="End time in HH:MM (default: 17:30)")
    args = parser.parse_args()

    try:
        hours = calculate_hours_worked(args.start, args.end)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)

    print(format_hours(hours))
