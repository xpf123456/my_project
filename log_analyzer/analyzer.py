
from parser import parse_line
from config import LOG_PATH, KEYWORDS, MODULES

def analyze_log():
    stats = {k: 0 for k in KEYWORDS}
    module_count = {m: 0 for m in MODULES}
    events = []

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        for line in f:
            parsed = parse_line(line)
            if not parsed:
                continue

            msg = parsed["message"]
            for k in KEYWORDS:
                if k in msg:
                    stats[k] += 1
                    events.append((parsed["time"], k, msg))
            if parsed["module"] in MODULES:
                module_count[parsed["module"]] += 1

    return stats, module_count, events
