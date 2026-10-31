# HACLS

พื้นที่ทำงานสำหรับเอกสารความรู้ หลักการ วิธีการ ความสามารถ และการทดลองของโครงการ HACLS

## โครงสร้าง

- `docs/` — เอกสารหลักและแนวทางของโครงการ
- `knowledge/inbox/` — ความรู้ที่ยังไม่ผ่านการตรวจสอบ
- `knowledge/validated/` — ความรู้ที่ผ่านการตรวจสอบแล้ว แต่ยังไม่จำเป็นต้องเป็นมาตรฐานกลาง
- `knowledge/canonical/` — ความรู้ที่ได้รับการยอมรับให้เป็นแหล่งอ้างอิงหลัก
- `knowledge/templates/` — แบบร่างและดัชนีชนิดเอกสารความรู้
- `scripts/validate_knowledge.py` — ตรวจตำแหน่งและสถานะของเอกสาร `KNOTE`
- `.codex/hooks.json` — เรียก validator หลัง Agent ใช้เครื่องมือแก้ไขที่ตรงเงื่อนไข
- `methodologies/` — วิธีคิดและกระบวนการ
- `capabilities/` — ความสามารถที่ต้องการให้ Agent ทำได้
- `skills/` — Implementation สำหรับ Agent
- `experiments/` — ผลการทดลองและ Evaluation
- `decisions/` — Architecture Decision Records (ADR)

## ตรวจสอบเอกสารความรู้

รัน `python3 scripts/validate_knowledge.py` เพื่อตรวจว่าไฟล์ `KNOTE` อยู่ใต้โฟลเดอร์สถานะและหัวข้อที่กำหนด และค่า `status` ใน frontmatter ตรงกับโฟลเดอร์

Codex Agent hook ใน `.codex/hooks.json` เรียก validator หลัง `apply_patch` และคำสั่ง `Bash` ที่อ้างถึง `knowledge/` หรือ validator หากเป็นการใช้งานครั้งแรก ให้ตรวจและ trust hook นี้ในหน้า `/hooks` ของ Codex ก่อน เพราะ hook ระดับ repository จะไม่ทำงานจนกว่าจะได้รับ trust
