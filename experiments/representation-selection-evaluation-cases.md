# Representation Selection — Evaluation Cases

> สถานะ: Proposed test fixtures · 2026-11-05
> จุดประสงค์: ทดสอบความเหมาะสมของการเลือกรูปแบบ ไม่ใช่ทดสอบความสวยงามหรือความสามารถของ Renderer

## วิธีทดสอบ

ส่งโจทย์แต่ละข้อให้ Agent ที่ติดตั้ง Task Skill จริง เก็บ prompt, output, model/runtime, timestamp และเหตุผลในการเลือกรูปแบบ จากนั้นให้ผู้ประเมินตรวจเกณฑ์ด้านล่างก่อนนำไปใช้งานจริง

### Evaluation cases

| ID | Input / Reader question | Expected primary representation | Must not do |
|---|---|---|---|
| R01 | “Temporary Hold คืออะไร” สำหรับผู้เริ่มต้น | Prose สั้น ๆ | บังคับทำ Diagram ทั้งที่ไม่จำเป็น |
| R02 | “PENDING กับ CONFIRMED ต่างกันอย่างไร” | Table | อธิบายเป็นความเรียงยาวโดยเทียบข้อไม่ตรงกัน |
| R03 | “Booking เปลี่ยนสถานะได้อย่างไร” | State Diagram + guard/condition | แต่ง transition ที่โจทย์ไม่ได้กำหนด |
| R04 | “API Gateway → Ingestion → Consumer มี interaction อย่างไร” | Sequence / Data-flow Diagram | อ้างว่า proposed architecture เป็น As-Is |
| R05 | “latency p95 เปลี่ยนอย่างไรระหว่าง load test” พร้อมข้อมูล timestamp และ unit | Chart + metadata | ละหน่วยหรือช่วงเวลา |
| R06 | “ระบบผ่านเกณฑ์ 1,000 concurrent users หรือไม่” แต่ไม่มี TOR metric/test result | Prose ระบุ unknown + evidence needed | สรุปผ่านจากตัวเลข VUs อย่างเดียว |
| R07 | “วิธีติดตั้งและรัน k6 3 คำสั่ง” | Numbered steps + code | สร้าง Flowchart สำหรับลำดับตรง |
| R08 | “อธิบายเหตุผลเลือก pessimistic lock vs optimistic lock” | Comparison Table + Prose trade-off | ทำ Diagram ที่ไม่อธิบายการตัดสินใจ |
| R09 | “แสดง HTTP response จริงที่ทดสอบได้” | Code/JSON example + source or test evidence | แต่ง response แล้วอ้างว่า captured |
| R10 | “ทำเอกสารสำหรับผู้บริหารว่าระบบรับ load ได้หรือไม่” | Summary prose + relevant metrics/chart + verdict | ใช้ศัพท์เทคนิคจำนวนมากโดยไม่มีการแปลความ |
| R11 | “อธิบาย Event Storming ให้เด็กฝึกงานเริ่มทำ” | Tutorial steps + examples + checkpoint | ใช้ภาพซับซ้อนก่อนอธิบาย concepts |
| R12 | “เขียน flow ระบบจาก API จริง แต่ยังไม่มี source code” | Label To-Be/Unknown + limited outline | เติม edge, owner, event เอง |
| R13 | “สรุปข้อจำกัดของสามแนวทางในเอกสารแนบ” | Table เมื่อมีเกณฑ์ร่วม; prose สำหรับ nuance | สร้างคอลัมน์ที่ข้อมูลไม่รองรับ |
| R14 | “ขอภาพรวม subsystem ที่มี 20 services” | High-level context view + scoped details | ยัดทุก edge ใน Diagram เดียว |

## Pass / Fail rubric

ให้คะแนนแต่ละหมวด 0 = ไม่ผ่าน, 1 = ผ่านบางส่วน, 2 = ผ่าน

1. **Reader intent:** ตอบคำถามหลักและเหมาะกับผู้ฟัง
2. **Representation fit:** เลือกรูปแบบที่ช่วยเข้าใจ/ตัดสินใจจริง; ไม่ทำภาพหรือตารางตกแต่ง
3. **Fidelity:** ความสัมพันธ์ ตัวเลข เวลา และสถานะสอดคล้องกับหลักฐาน; unknown ไม่ถูกแต่ง
4. **Clarity:** ป้ายกำกับ ขอบเขต หน่วย และศัพท์เฉพาะชัดเจน
5. **Non-redundancy:** ถ้ามีหลายรูปแบบ แต่ละรูปแบบตอบคนละคำถาม
6. **Decision readiness:** มีข้อสรุปหรือการกระทำถัดไปเมื่อโจทย์ต้องการ

**Pass criteria (proposed):** ไม่มีหมวดที่ได้ 0 และคะแนนรวมอย่างน้อย 10/12; กรณี fidelity เป็น 0 ถือว่า fail โดยทันที แม้คะแนนรวมสูง

## Result recording template

```markdown
### Run: <case-id> / <date> / <agent-model>
- Prompt:
- Input/evidence:
- Output artifact:
- Primary representation:
- Secondary representation & why:
- Scores: intent / fit / fidelity / clarity / non-redundancy / readiness
- Verdict: PASS / FAIL
- Errors observed:
- Follow-up change proposed:
```

ผลที่เขียนในไฟล์นี้เป็น **test design เท่านั้น** ยังไม่ถือว่าได้รันหรือผ่านการประเมิน Agent จริง

## Policy under test

[Representation Selection Policy](../docs/guidelines/representation-selection.md)
