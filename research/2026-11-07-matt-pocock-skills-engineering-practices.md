<!-- Type: RES | Document type: Research synthesis -->
# Research: ใช้ Matt Pocock Skills อย่างมีประสิทธิภาพ และบทเรียนสำหรับ HACLS

**วันที่:** 2026-11-07  
**สถานะ:** Research synthesis / ข้อเสนอเชิงออกแบบ (ไม่ใช่ผล benchmark)  
**ต้นฉบับหลัก:** https://github.com/mattpocock/skills  
**โจทย์:** ต้องรู้อะไรจึงใช้ชุด Skills ได้เต็มประสิทธิภาพ และควรเรียนรู้อะไรจากการออกแบบ Skills เพื่อนำมาพัฒนา HACLS?

## Executive Summary

ชุด Matt Pocock Skills เน้นคุณภาพ Software Engineering มากกว่าอัตโนมัติสุดทาง: alignment ก่อน implementation, shared domain language, tight feedback loops, design quality, และ retrospective ของ agent environment. README ระบุว่าแต่ละ skill เล็ก ปรับแต่งได้ และประกอบเป็น workflow ได้ ไม่ใช่ framework ที่ยึดกระบวนการทั้งหมดไว้กับตน [S1].

ข้อสรุปจากการอ่าน source: เรียน **วิธีควบคุมความไม่แน่นอน การทดสอบ การส่งต่อบริบท และการจัดวางกฎ** ก่อนจำชื่อ skills. ใช้ `ask-matt` เป็น router เมื่อยังไม่ทราบเส้นทาง และเรียก `setup-matt-pocock-skills` หนึ่งครั้งต่อ repo เพื่อเตรียม issue tracker, triage labels และ domain docs [S1][S2].

## 1. พื้นฐานที่ผู้ใช้ควรมี

| ความรู้ | สิ่งที่ต้องอธิบายได้ | Skills ที่นำไปใช้ |
|---|---|---|
| Problem framing / decision boundaries | ข้อมูลใดเป็น fact, สมมติฐาน, การตัดสินใจของ human | grilling, grill-with-docs, wayfinder |
| Domain terminology / ADR | glossary เก็บศัพท์; ADR เก็บ trade-off สำคัญ ไม่ใช่เอาโค้ดใส่ glossary | domain-modeling |
| Testing & test seam | ทดสอบพฤติกรรมผ่าน public interface; expected result เป็นอิสระจาก implementation | tdd, codebase-design |
| Vertical slice & DAG | ticket หนึ่งอันส่งมอบพฤติกรรมครบทั้งแนว; blockers กำหนด frontier | to-tickets, implement-spec |
| Bug reproducibility | คำสั่งเดียวที่ fail บน bug จริง รันซ้ำได้ และทำงานเร็ว | diagnosing-bugs |
| Git / issue tracker / CI | fixed point สำหรับ diff, acceptance criteria, checks ที่รันได้ | code-review, implement, retro |
| Context management | เลือก continue/clear/handoff/subagent/compact ให้ถูกช่วง | ask-matt, handoff |
| Skill authoring | description เป็น trigger; progressive disclosure, context pointer, completion criteria | writing-for-agents |

การแบ่งระดับเป็นคำแนะนำของผู้วิจัย ไม่ใช่ข้อบังคับของผู้สร้าง Skills.

## 2. Main Flow ที่แนะนำในต้นฉบับ

`/grill-with-docs` → [`/prototype` หากมี design question ที่ต้องเห็นหรือทดลอง] → `/to-spec` → [`/to-tickets` เมื่อเป็น multi-session] → `/implement` หรือ `/implement-spec` → `/tdd` → `/code-review` → `/retro`.

`ask-matt` อธิบายว่า idea-to-ship เป็น main flow; bug, incoming issues และงานใหญ่มี on-ramp แยก เช่น `diagnosing-bugs`, `triage`, `wayfinder` [S2]. งานเล็กไป `implement` ได้โดยตรง; ไม่จำเป็นต้องเรียกทุก Skill.

**Context boundary:** รักษาบริบทการคิดจาก grilling ถึง to-tickets เมื่อยังอยู่ในช่วงที่โมเดลทำงานได้ดี จากนั้นแต่ละ implementation ticket สามารถเปิด session ใหม่ โดยอ่าน ticket/spec/references เป็นหลัก; ใช้ handoff เมื่อข้าม directory / harness / teammate / side task [S2][S14].

## 3. Patterns สำคัญ (อ่านจาก SKILL.md)

### 3.1 Grilling = decision tree + frontier

`grilling` แผนที่คำถามเป็น decision tree, ถาม frontier ของคำถามที่ prerequisites ตอบแล้วในแต่ละ round, พร้อมข้อแนะนำจาก agent; factual lookup เป็นหน้าที่ agent ส่วน decision เป็นหน้าที่มนุษย์. Stop เมื่อ frontier ว่างและ human ยืนยันความเข้าใจตรงกัน [S3].

**ข้อควรระวัง:** ถามทุกข้อใน frontier อาจมี cognitive load สูงกับผู้ใช้ใหม่; HACLS อาจประเมินการถามแบบเป็นกลุ่มเทียบกับทีละข้อ โดยคง dependency gating เดิมไว้ (ข้อเสนอ ไม่ใช่หลักการที่ Matt กำหนด).

### 3.2 Domain modeling = terminology + decision hygiene

`domain-modeling` ท้าทายคำกำกวม, ตรวจความขัดแย้งกับ glossary และ code, stress-test ด้วย edge cases, เขียนศัพท์ที่ตกลงแล้วลง glossary ทันที. Glossary ไม่ใช่ specification หรือ implementation log; ADR ให้บันทึกอย่างประหยัด เฉพาะที่เปลี่ยนยาก, เหตุผลไม่ชัดหากไร้บริบท, และมี trade-off จริง [S4].

**หมายเหตุ:** README รุ่นตรวจสอบใช้ `GLOSSARY.md`; บางหน้าเก่าหรือ skill ที่ยังอ้าง `CONTEXT.md` อาจสะท้อนช่วงย้าย naming convention. ให้ตรวจไฟล์ในเวอร์ชันที่ติดตั้งและรัน setup ตามจริง [S1][S4].

### 3.3 To-spec ≠ interview

`to-spec` สังเคราะห์บทสนทนาและ codebase ปัจจุบัน **ไม่สัมภาษณ์ซ้ำ**. ก่อนเผยแพร่ spec ต้องเสนอและยืนยัน testing seam. Template มี problem statement, solution, user stories, implementation decisions, testing decisions, out of scope; หลีกเลี่ยง hardcoded file paths ที่เปลี่ยนง่าย [S5].

### 3.4 To-tickets = tracer bullets, DAG, frontier

`to-tickets` แบ่งงานเป็น vertical slice ที่แคบแต่ end-to-end, demo/verify ได้ด้วยตัวเอง และจบใน fresh context window. แต่ละ ticket มี blocking edges. Wide mechanical refactor อาจใช้ expand–migrate–contract แทนการฝืน vertical slice [S6].

### 3.5 TDD = agreed seam + independent expected result

`tdd` ให้ test พฤติกรรมผ่าน public interface มากกว่าทดสอบ internals; ยืนยัน seam ก่อนเขียน test. Anti-pattern คือ assertion ที่คำนวณ expected แบบเดียวกับ implementation (tautological), mocks ที่ผูกกับ implementation, และการเขียน tests ทั้งหมดก่อนแล้วค่อย implement แบบ horizontal slicing [S7]. Skill รุ่นที่อ่านระบุ `red → green` ทีละ slice และให้ทำ refactoring ในช่วง review ไม่ใช่ระหว่าง red-green loop — เป็นรายละเอียดของ skill นี้ ไม่ใช่ข้อสรุปแทนแนว TDD ทุกสาย.

### 3.6 Diagnosing bugs = tight red-capable loop ก่อน hypothesis

`diagnosing-bugs` ให้วิธี reproduce ที่ deterministic, fast, agent-runnable และ assert symptom จริงก่อนเริ่มตั้งทฤษฎี. แนะนำ failing tests, curl, CLI fixture, browser scripts, trace replay, throwaway harness, fuzz, bisect, differential loop. ต้องได้หลักฐานจากการรันจริงของคำสั่งอย่างน้อยหนึ่งครั้ง ก่อนผ่าน Phase 1 [S8].

### 3.7 Code review = Standards axis + Spec axis

`code-review` ดู diff จาก fixed point, สองแกนแยกกัน: Standards (มาตรฐาน repo + code smells แบบ heuristic), Spec (ข้อกำหนดที่ขาด, scope creep, implementation ผิด). Reviewer สองฝั่งแยก context; รายงานต่างหากเพื่อไม่ให้ code-quality ที่ดีบดบังข้อกำหนดที่ผิดหรือกลับกัน [S9].

### 3.8 Retro = ปรับ environment ไม่ใช่เพียงเขียนกฎเพิ่ม

`retro` ดู session แล้วเสนอการปรับ navigation pointers, checks, coding standards, tooling, information access. ความผิดพลาดเชิง mechanical ควรบังคับด้วย deterministic guardrails (lint, typecheck, CI, hooks) ก่อนเพิ่ม instruction; judgement calls อยู่ใน standards/review. แนะนำเก็บ `AGENTS.md` ให้บาง ใช้ pointers [S10].

### 3.9 Skill design = context load vs cognitive load

`writing-for-agents` นิยาม **context pointer** เป็นข้อความที่บอกว่าจะอ่าน reference ใดเมื่อเข้าเงื่อนไขไหน; คำอธิบายของ skill และบรรทัดใน `AGENTS.md` เป็นตัวอย่าง. แยก context load (เนื้อหาที่โหลดติดทุก turn) กับ cognitive load (มนุษย์ต้องจำว่ามีเครื่องมือใด). Progressive disclosure ซ่อน reference เฉพาะ branch ไม่ใช่ซ่อนขั้นตอนหลัก. Step ที่ดีมี checkable completion criterion และ single source of truth [S11].

`SKILL-MECHANICS.md` ระบุ `disable-model-invocation: true` สำหรับ user-invoked, model-invoked มี description ที่เป็น trigger และถูก invoke จาก agent หรือ skills อื่นได้; router ใช้ลดภาระที่มนุษย์ต้องจำ skill จำนวนมาก [S12].

### 3.10 Wayfinder ≠ To-tickets

`wayfinder` จัดการงานที่ยังมองเส้นทางไม่ชัด โดยสร้าง **decision tickets** เพื่อให้ความไม่แน่นอนคลี่คลาย ไม่ใช่ tasks สำหรับลงมือ implement. มี `fog of war`, `destination`, `frontier`; เมื่อเส้นทางชัดจึงส่งต่อ `to-spec`, `to-tickets`. ส่วน `to-tickets` หลังจากปัญหาค่อนข้างชัดแล้ว จัด **delivery tickets** ที่ตรวจรับได้ [S13][S6].

## 4. การนำมาใช้จริง: 3 สถานการณ์

| สถานการณ์ | Recommended flow | Evidence ที่ต้องได้รับ |
|---|---|---|
| ฟีเจอร์ Booking Engine ใหม่ | grill-with-docs → prototype (ถ้ากฎต้องทดลอง) → to-spec → to-tickets → implement + tdd → code-review | glossary/ADR, approved spec, end-to-end slices, test reports, two-axis review |
| API Bug ที่เกิดเฉพาะบางช่วง | diagnosing-bugs → red-capable reproducible command → hypothesis/fix → regression test → review | คำสั่งที่ reproduce ได้, ก่อนแก้ fail/หลังแก้ pass |
| HACLS Strategic DDD Skill ที่ขอบเขตยังไม่ชัด | wayfinder หรือ grilling/domain-modeling → research/prototype เมื่อจำเป็น → spec → experiment/evaluation | decision log, unresolved questions, acceptance criteria, evaluation cases |

ตารางนี้คือการจับคู่เชิงวิเคราะห์ของผู้วิจัย ไม่ใช่การยืนยันว่าทำงานแล้วใน HACLS.

## 5. แนวทางปรับใช้กับ HACLS (proposals)

| Priority | สิ่งที่ควรดึงมา | เหตุผล | Test of success |
|---|---|---|---|
| P0 | Evidence gate + explicit completion criterion | หลีกเลี่ยง Agent บอกว่าจบโดยไม่มีหลักฐาน | หยุดอัตโนมัติเมื่อพิสูจน์เงื่อนไขไม่ได้ |
| P0 | Model-invoked discipline vs user-invoked orchestration | ลด skill collisions/context overhead | Router เรียก flow ที่เหมาะและ shared references ไม่มีนิยามซ้ำ |
| P0 | Domain glossary + ADR hygiene | ลด ambiguity โดยไม่ใช้ glossary เป็น spec | Terms ย้อนอ้าง canonical source ได้; ADR เฉพาะ trade-off สำคัญ |
| P1 | Vertical slices + task DAG | ทำงานทีละผลลัพธ์ที่ตรวจรับได้ | Ticket เดียวมี observable behavior, blockers, acceptance criteria |
| P1 | Two-axis review + independent evidence | จับทั้งผิด spec และผิด standards | รายงานสองแกนพร้อม source/evidence แยกกัน |
| P1 | Retro → guardrails | ลดข้อผิดพลาดเดิมซ้ำ | ข้อผิดพลาด mechanical กลายเป็น test/lint/check |
| P2 | Wayfinder's fog of war | ไม่ฝืนวางแผนละเอียดในงานที่ยังไม่รู้ | Ticket ถาม decision ที่คมชัด; fog เก็บเฉพาะที่ยังระบุ question ไม่ชัด |

**ไม่ควรคัดลอกโดยตรง:** Workflow ทั้งหมดเป็นมาตรฐานบังคับสำหรับทุกงาน; การตั้ง subagents ขนานโดยไม่ดู environment; การใช้ ADR กับทุก decision; การส่งคำถามทั้ง frontier แบบไม่คำนึงถึงความพร้อมผู้เรียน; การถือว่า skill prompts เป็นหลักฐาน correctness.

## 6. สิ่งที่ยังไม่พิสูจน์ / Limits

- นี่เป็น **source-code review และ design analysis** ไม่ใช่ benchmark ประสิทธิภาพ, token savings, bug rate หรือ quality outcomes.
- Behaviour ใน runtime ขึ้นอยู่กับ model, harness, tools, repository state และ version ที่ติดตั้ง.
- Source บางหน้ามีการอ้างชื่อศัพท์เก่า `CONTEXT.md`; ให้ยืนยันจาก commit/version ก่อนใช้งานจริง.
- ข้อเสนอสำหรับ HACLS ต้อง validate ด้วย scenario tests แยกจากการอ่าน SKILL.md.

## Primary sources

- **[S1]** README – https://github.com/mattpocock/skills/blob/main/README.md
- **[S2]** ask-matt – https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md
- **[S3]** grilling – https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md
- **[S4]** domain-modeling – https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md
- **[S5]** to-spec – https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md
- **[S6]** to-tickets – https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md
- **[S7]** tdd – https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md
- **[S8]** diagnosing-bugs – https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md
- **[S9]** code-review – https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md
- **[S10]** retro – https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md
- **[S11]** writing-for-agents – https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md
- **[S12]** SKILL-MECHANICS – https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md
- **[S13]** wayfinder – https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md
- **[S14]** handoff – https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md
- **[S15]** setup-matt-pocock-skills – https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md
- **[S16]** codebase-design – https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md
