
import re
from datetime import datetime
from config import TIME_FORMAT

def parse_line(line):
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\]\[(\w+)\] (.+)"
    match = re.match(pattern, line)
    if match:
        time_str, level, module, message = match.groups()
        timestamp = datetime.strptime(time_str, TIME_FORMAT)
        return {
            "time": timestamp,
            "level": level,
            "module": module,
            "message": message
        }
    return None
