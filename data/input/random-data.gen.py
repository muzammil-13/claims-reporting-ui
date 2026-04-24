import random
from pathlib import Path
from datetime import date

output_dir = Path(__file__).resolve().parent
current_date = date.today()
output_path = output_dir / f"512_{current_date:%Y%m%d}.txt"

segments = ['WGS', 'MED', 'GBD', 'COM', 'NEW', 'TCS', 'LIF']
statuses = ['PAID', 'DENIED', 'PENDING']
processing_types = ['AUTO', 'MANUAL']
rows = []

for _ in range(7):
    claim_id = f"CLM{random.randint(10010, 99999):05d}"
    seg = random.choice(segments)
    status = random.choice(statuses)
    ptype = random.choice(processing_types)
    rows.append(f"{claim_id}|{current_date}|{seg}|{status}|{ptype}")

content = 'ClaimID|ProcessDate|SegmentCode|Status|ProcessingType\n' + '\n'.join(rows) + '\n'
output_path.write_text(content)
print(f"Generated {output_path.name}")