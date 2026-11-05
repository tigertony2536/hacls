# Representation Selection Policy

> **สถานะ:** Proposed — รอการตรวจรับผ่าน Pull Request  
> **เวอร์ชัน:** 0.1.0 · 2026-11-05  
> **ขอบเขต:** การสื่อสารผลวิเคราะห์ คำอธิบาย รายงาน Tutorial และ Artifact จาก Agent ใน HACLS  
> **ประเภท:** Shared guideline; ไม่ใช่ Skill ที่ต้องเรียกใช้ทุกครั้ง

## 1. หลักการ

**เลือก Representation ตามคำถามที่ผู้อ่านต้องตอบ ไม่ใช่ตามรูปแบบที่เครื่องมือสร้างได้หรือความสวยงามของผลลัพธ์**

ข้อมูลชุดเดียวกันอาจต้องใช้ Prose, Table, Diagram, Chart, Checklist, Code หรือ Evidence คนละส่วน แต่การเพิ่มรูปแบบใหม่ต้องช่วยตอบ **คำถามอีกข้อ** หรือแก้ข้อจำกัดด้านความเข้าใจจริง ๆ

ลำดับคุณภาพ: **ความถูกต้อง → ความเหมาะสมกับการตัดสินใจ → ความเข้าใจง่าย → ความกระชับ → ความสวยงาม**

### แยกสองระดับก่อน

1. **Information structure:** ข้อเท็จจริง เหตุผล ความสัมพันธ์ เวลา ตัวเลข สมมติฐาน หลักฐาน และข้อจำกัด
2. **Presentation representation:** วิธีแสดงโครงสร้างนั้นแก่ผู้อ่าน เช่น ความเรียง ตาราง Diagram หรือ Chart

ห้ามใช้การออกแบบ Presentation เป็นเหตุผลในการเติมข้อมูลที่ขาดจาก Information structure

## 2. ขั้นตอนเลือก Representation

1. **Frame the reader's job:** ระบุผู้อ่าน (ใคร), คำถามหลัก (อยากรู้อะไร), การกระทำ/การตัดสินใจถัดไป (จะทำอะไรต่อ) และขอบเขต (อะไรไม่รวม) เมื่อจำเป็น
2. **Identify information shape:** จำแนกว่าเนื้อหาหลักเป็นเหตุผล การเปรียบเทียบ ลำดับ ความสัมพันธ์เชิงโครงสร้าง แนวโน้มเชิงตัวเลข วิธีทำ พฤติกรรมจริง หรือหลักฐาน
3. **Choose the simplest sufficient form:** เลือกรูปแบบหลักแบบเดียวที่ตอบคำถามได้ชัดก่อน โดยคำนึงถึงสื่อปลายทาง (Chat, Markdown, Document, HTML)
4. **Add only complementary representations:** เพิ่มรูปแบบที่สองต่อเมื่อรูปแบบแรกตอบอีกคำถามหนึ่งไม่ได้; แต่ละภาพ/ตารางควรมีประโยคระบุสิ่งที่สื่ออย่างชัดเจน
5. **Validate fidelity and usability:** ตรวจหลักฐาน ความถูกต้องของลูกศร หน่วย กฎ/เงื่อนไข ขอบเขต และความเข้าใจของกลุ่มเป้าหมาย

หากเป็นคำถามสั้น ๆ ที่ Prose สองประโยคตอบได้ครบแล้ว **ไม่ต้องทำตารางหรือ Diagram** เพียงเพราะ Policy นี้ถูกโหลด

## 3. Decision Matrix

| Reader's question / งานของผู้อ่าน | Primary form | จุดเด่น | เมื่อไรไม่ควรใช้ |
|---|---|---|---|
| ทำไม? หมายถึงอะไร? มี trade-off อย่างไร? | **Prose** | ถ่ายทอดเหตุผล คำจำกัดความ เงื่อนไข ข้อสรุป | เปรียบเทียบตัวเลือกจำนวนมากในย่อหน้าเดียว |
| แตกต่างกันอย่างไร? ตัวเลือกใดเหมาะ? | **Table** | สแกนเกณฑ์เดียวกันข้ามตัวเลือก | แต่ละช่องเป็นย่อหน้ายาวหรือไม่มีมิติเทียบร่วมกัน |
| ขั้นตอนมีเงื่อนไข/ลูปอย่างไร? | **Flowchart / Decision Tree** | แสดงจุดตัดสินใจและเส้นทาง | ขั้นตอนเชิงเส้นสั้น ๆ: ใช้ numbered steps |
| ใครเรียกใครก่อนหลัง? | **Sequence Diagram** | แสดง interaction และลำดับเวลา | ต้องการเพียงรายการ endpoint หรือโครงสร้างระบบ |
| ระบบประกอบด้วยอะไรและสัมพันธ์กันอย่างไร? | **Architecture / Context Map / ER** | แสดง boundary, ownership, relationship | รายละเอียดกฎหรือเหตุผลซึ่งรูปภาพสื่อไม่ได้ |
| สถานะเปลี่ยนได้อย่างไร? | **State Diagram** | แสดง transition ที่อนุญาต | สื่อ interaction ข้าม service |
| ค่าเปลี่ยนตามเวลา/กระจาย/สัมพันธ์กันอย่างไร? | **Chart** | เห็นแนวโน้ม รูปแบบ และจุดผิดปกติ | ต้องอ่านค่าที่แน่นอนทุกตัว หรือไม่มีข้อมูลพอ |
| ควรทำอะไร ตรวจอะไร ผ่านเกณฑ์หรือไม่? | **Checklist** | ทำตาม/ตรวจสอบเป็นข้อได้ | ใช้แทนเหตุผลหรือหลักฐาน |
| Contract / syntax / response จริงมีรูปร่างอย่างไร? | **Code / Example** | สื่อรูปแบบที่ตรวจสอบหรือทดลองได้ | ต้องการคำอธิบายระดับภาพรวมสำหรับผู้ไม่ใช่เทคนิค |
| รู้ได้อย่างไรว่าทำงานจริง? | **Evidence / Test Result** | แสดง assertion, output, metric พร้อมวิธีทำซ้ำ | ใช้ภาพผลลัพธ์โดยไม่มีแหล่งกำเนิดหรือเกณฑ์ผ่าน |

**Genre ไม่เท่ากับ Representation:** Tutorial, How-to, Reference, Explanation เป็น *ชนิดงานเขียน*; ภายในแต่ละชนิดยังเลือก Prose/Table/Diagram ได้ตามโจทย์

## 4. กฎสำหรับ Diagram และ Chart

- **One diagram, one governing question:** ระบุให้ได้ว่า Diagram ตอบคำถามอะไร หากตอบไม่ได้ควรตัดออก
- **Use the right grammar:** Sequence = interaction ตามเวลา; State = transition; C4 = ภาพรวมระบบ; ER = cardinality; Flowchart = branching/loop
- ระบุขอบเขตและสัญลักษณ์ โดยเฉพาะความหมายของลูกศร; แสดงส่วนที่ละไว้เมื่ออาจนำไปสู่การสรุปผิด
- อย่าสร้าง topology, dependency, ลำดับเวลา, business rule, percent, benchmark หรือ sample data ที่ไม่มีหลักฐานเพื่อทำให้ภาพดูครบ
- สำหรับ Chart ให้ระบุ **หน่วย ช่วงเวลา ปริมาณตัวอย่าง (ถ้าเกี่ยวข้อง) แหล่งที่มา และเกณฑ์อ้างอิง**; ถ้ามีค่าจำนวนน้อยที่ต้องอ่านแม่นยำ ให้ใช้ Table
- อย่าใช้สีเพียงอย่างเดียวเพื่อสื่อความหมาย; ใช้ป้ายกำกับและคำอธิบายข้อความเสริม

## 5. Evidence & epistemic labels

เมื่องานเกี่ยวกับระบบจริง งานวิจัย หรือการออกแบบที่ยังไม่ยืนยัน ให้แยกเนื้อหาอย่างเหมาะสม:

- **Verified / Observed:** มีหลักฐานที่ตรวจสอบได้ เช่น Source Code, Log, Test Output, Official Doc
- **Inferred:** เป็นการอนุมานจากหลักฐาน; ระบุเงื่อนไขและความไม่แน่นอน
- **Proposed / To-Be:** เป็นข้อเสนอเชิงออกแบบ ยังไม่ใช่พฤติกรรมปัจจุบัน
- **Unknown:** ยังไม่มีข้อมูลพอ ห้ามใส่เป็นข้อเท็จจริงใน Diagram หรือ Table

หากหลักฐานไม่ครบ ให้ลดขอบเขตของ Representation หรือแสดงช่องว่าง ไม่ใช่เติมส่วนที่หาย

## 6. ตัวอย่างการเลือกแบบผสม

### กรณี A — Booking System (Temporary Hold)

- **Prose:** ทำไมต้องมี Hold และ TTL
- **Table:** สถานะ PENDING (ยังไม่หมดอายุ), CONFIRMED, EXPIRED, CANCELLED มีผลต่อ Slot อย่างไร
- **State Diagram:** เส้นทาง transition และ precondition
- **Evidence:** Concurrency test พิสูจน์ว่า 20 requests จอง Slot เดียวกันแล้วสำเร็จได้ไม่เกิน 1 ราย

ทั้งสี่รูปแบบตอบคนละคำถาม; State Diagram ไม่สามารถใช้แทน Concurrency Evidence

### กรณี B — Load Test

- **Prose:** แปลความ TOR ว่าความพร้อมกัน (concurrent users) ต่างจาก RPS และกำหนดนิยามงานทดสอบ
- **Chart:** latency/throughput/error rate ตามเวลา
- **Table:** p95, error rate, VUs, thresholds, test environment
- **Evidence:** k6 raw results, command/config, server-side metrics
- **Conclusion:** ผ่าน/ไม่ผ่าน/ยังสรุปไม่ได้ โดยเชื่อมกลับไปเกณฑ์ TOR

### กรณี C — Tutorial

ใช้ขั้นตอนสั้น ๆ + ตัวอย่างที่ทำตามได้เป็นหลัก เพิ่ม Flowchart เฉพาะจุดเลือกวิธีที่ซับซ้อน และ Checklist สำหรับ checkpoint; ไม่จำเป็นต้องวาด Diagram ทุก Step

## 7. Responsibility Boundary ใน HACLS

```text
Task Skill (Research / Tutorial / Verification / Domain Analysis)
  ├─ กำหนด reader question, learning/decision objective, facts, evidence
  └─ ใช้ Shared Representation Selection Policy
       ├─ เลือก Prose / Table / Diagram / Chart / Checklist / Code / Evidence
       ├─ ตรวจความเหมาะสมและ fidelity
       └─ ส่ง output specification ไปยัง Renderer เมื่อจำเป็น
            └─ Markdown / Mermaid / HTML / DOCX / Presentation ฯลฯ
```

**ไม่สร้าง Skill ใหม่เพื่อบังคับให้ Agent ทุกครั้งต้องเลือกภาพ:** เอกสารนี้เป็น Shared Policy; Task Skill เป็นเจ้าของความถูกต้องของโดเมน; Renderer เป็นเจ้าของการแปลงสู่สื่อเฉพาะ ห้าม Renderer เพิ่ม business fact โดยไม่มีที่มา

### Precedence และ fallback

1. ข้อกำหนดผู้ใช้/งาน/ชนิดไฟล์ที่ชัดเจนมีลำดับก่อน (เช่น ต้องเป็นตาราง CSV, ต้องเป็น PDF, หรือห้ามใช้ภาพ)
2. กฎเฉพาะทางของ Task Skill และความถูกต้องของข้อมูลมาก่อน preference เชิงรูปแบบ
3. Policy นี้เป็นค่าเริ่มต้นเมื่อไม่มีรูปแบบกำหนดไว้
4. หากสื่อไม่รองรับการแสดงผล ให้ fallback เป็นข้อความมีโครงสร้างพร้อมคำอธิบาย ไม่สร้าง Renderer เพิ่มโดยไม่จำเป็น

## 8. Acceptance Criteria

- [ ] ระบุคำถามหลักของผู้อ่านได้ หรือคำถามชัดจากบริบทอยู่แล้ว
- [ ] Primary representation ช่วยตอบคำถามได้โดยตรงและเป็นรูปแบบที่ง่ายที่สุดที่เพียงพอ
- [ ] เมื่อใช้หลายแบบ แต่ละแบบมีหน้าที่ต่างกัน ไม่ใช่ตกแต่งซ้ำ
- [ ] ส่วนที่เป็น Verified / Inferred / Proposed / Unknown แยกได้เมื่อจำเป็น
- [ ] Diagram/Chart ไม่สร้างข้อเท็จจริงที่ขาด และมีขอบเขต/หน่วย/คำอธิบายที่จำเป็น
- [ ] หลักฐานเชิงทดสอบระบุเกณฑ์และวิธีตรวจซ้ำ ไม่ใช้ screenshot เป็นข้อพิสูจน์เพียงอย่างเดียว
- [ ] ผู้อ่านเป้าหมายค้นคำตอบและตัดสินใจต่อได้ ไม่ต้องถอดรหัส jargon หรือสี
- [ ] ถ้า Prose อย่างเดียวเพียงพอ ไม่มี Diagram/Table ที่ไร้ประโยชน์

## 9. Anti-patterns

| Anti-pattern | แนวทางแก้ |
|---|---|
| Diagram-first | ตั้ง governing question ก่อนสร้างภาพ |
| Table as essay | เก็บคุณสมบัติที่เทียบกันได้ในเซลล์ ย้ายเหตุผลไป Prose |
| Flowchart for trivial steps | เปลี่ยนเป็น numbered steps |
| Prose for many-option comparison | ใช้ Table เทียบมิติเดียวกัน |
| Chart without units or source | เพิ่ม metadata หรือถอยกลับเป็น Table |
| False completeness | แยก Unknown / Assumption แทนการเดา |
| Repeated visuals with same meaning | ใช้หนึ่งรูปแบบต่อหนึ่งหน้าที่ |

## 10. การนำไปใช้และการทวนสอบ

- `AGENTS.md` ควรลิงก์มายัง Policy นี้ด้วยข้อความสั้น ๆ ไม่คัดลอกเนื้อหาทั้งหมด
- Task Skills โหลดและปรับใช้เฉพาะส่วนที่เกี่ยวข้อง ไม่โหลด Renderer โดยไม่จำเป็น
- ทดลองกับ [Representation Evaluation Cases](../../experiments/representation-selection-evaluation-cases.md) และบันทึกข้อผิดพลาด/ข้อยกเว้นก่อนส่งเสริมเป็นมาตรฐานที่ยอมรับ
- การ Merge PR เป็นขั้นตรวจรับเอกสาร แต่ไม่ได้หมายความว่ามีการทดสอบ Agent Runtime แล้ว; ต้องบันทึกผลประเมินแยกต่างหาก

## 11. แหล่งอ้างอิงเชิงแนวคิด

กฎข้างต้นเป็น **การสังเคราะห์สำหรับ HACLS** ไม่ใช่การคัดลอกกฎจาก Skill ใดเพียงตัวเดียว

- [html-artifacts](https://github.com/joshuadavidthomas/agent-skills/blob/main/html-artifacts/SKILL.md) — Reader's verb, governing question, evidence fidelity
- [to-html](https://github.com/pbi-agent/skills/blob/main/skills/to-html/SKILL.md) — Visual grammar by reader's decision
- [visual-explainer](https://github.com/nicobailon/visual-explainer/blob/main/plugins/visual-explainer/SKILL.md) — Figure-driven visual explanation
- [Superpowers: writing-skills](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md) — หลีกเลี่ยง flowchart ที่ไม่จำเป็น
- [pstack: technical-writing](https://github.com/cursor/plugins/blob/main/pstack/skills/technical-writing/SKILL.md) — Diátaxis / genre selection
- [Research synthesis](../../research/2026-11-05-representation-selection-skills.md)
