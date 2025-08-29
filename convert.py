output = ""
INPUT = "assets/demo-subtitles.srt"
from collections import defaultdict
timestamps = defaultdict(str)
with open(INPUT, "r") as file:
    lines = file.readlines()
    last_timestamp = None
    in_timestamp_context = False
    for line in lines:
        if line.strip().isdigit():
            in_timestamp_context = True
            continue
        if in_timestamp_context:
            last_timestamp = line.strip()
            in_timestamp_context = False
            continue
        if len(line.strip()) == 0:
            continue

        timestamps[last_timestamp] = line.strip()
        
final_list = "<ol>"
template = """
<li>
    <a href="#"><span class="ts">{ts}</span></a> {text}
</li>
"""
for timestamp, line in timestamps.items():
    ts_parts = timestamp.split(" ")
    ts_start = ts_parts[0].split(",")[0]
    ts_end = ts_parts[1].split(",")[0]
    final_list += template.format(ts=ts_start, text=line)
final_list += "</ol>"
with open("out.html", "w+") as file:
    file.write(final_list)
