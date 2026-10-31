# Strategic DDD Orchestrator — MVP Design (Draft)

- สถานะ: **Proposed / draft for review**
- วันที่: 2026-10-31
- อ้างอิง: [Project Charter](00-project-charter.md) · [ADR-0001](../decisions/0001-minimum-sufficient-knowledge.md)
- เป้าหมาย: Agent ช่วยมนุษย์ค้นหาขอบเขตโดเมนและบันทึกเหตุผลที่ตรวจสอบได้ โดยไม่ยึดติด tool เดียวหรือสรุปแทนผู้ใช้เมื่อหลักฐานไม่พอ

> เอกสารนี้เป็น *ข้อเสนอ implementation design* ไม่ใช่ความรู้ DDD ที่ผ่านการตรวจเป็น canonical และยังไม่ใช่ผลการทดสอบจริง

## Responsibility Boundary

**Agent รับผิดชอบ:** parse input, ตั้งสมมติฐาน, วาง dependency/frontier ของคำถาม, เลือก technique ให้เหมาะกับความไม่แน่นอน, สรุป evidence + alternatives, สร้าง draft artifacts, ตรวจ gate, รายงาน gaps และผลการประเมิน

**มนุษย์รับผิดชอบ:** อธิบายเป้าหมายธุรกิจและข้อมูลที่ Agent เข้าถึงไม่ได้, ยืนยัน/แก้การตีความโดเมน, เลือก trade-offs และรับรองการตัดสินใจสำคัญ

**ไม่ทำใน MVP:** Tactical DDD, aggregate/entity design, ออกแบบ API/DB/microservice, implement code, บังคับจัด workshop Event Storming ทุกครั้ง, sync Knowledge Hub อัตโนมัติ, เปลี่ยนสถานะความรู้ใน Hub โดยลำพัง

## Input Contract

- รับ artifact ที่ผู้ใช้นำมา เช่น TOR, SRS, user stories, process notes, Event Storming board หรือข้อความธรรมดา
- รับ goal, scope, stakeholders และ constraints ถ้ามี; ไม่บังคับให้ทุกอย่างครบก่อนเริ่ม
- แยก **user-confirmed facts**, **documented claims**, **assumptions**, **unknowns** และ **conflicts**
- ห้ามสร้างรายละเอียดโดเมนที่ไม่มีหลักฐานเพื่อให้ workflow ดูเหมือนสมบูรณ์

## Proposed Workflow และ Evidence Gates

| Stage | Activity / Technique candidates | Output | Evidence Gate |
|---|---|---|---|
| G0 Intake & scope | สกัดโจทย์และ source inventory; คำถามเฉพาะ gap | Scope, objective, sources, unknowns | มีเป้าหมายและขอบเขตงานพอให้วิเคราะห์; gap ที่เหลือติดป้ายไว้ |
| G1 Domain discovery | Process walkthrough, narrative, Big Picture ES *เมื่อเหมาะ*, glossary | Key business events/flows, terms, stakeholders, uncertainties | อธิบาย business flow ที่เกี่ยวข้องได้ หรือบันทึก coverage gap ชัดเจน |
| G2 Subdomain analysis | Business capability grouping; core/supporting/generic classification เป็นข้อเสนอที่ต้องยืนยัน | Candidate subdomains พร้อม rationale/alternatives | ไม่ใช้ CRUD/UI/team structure เป็นเหตุผลเดียว; มี trace สู่ความสามารถหรือกฎธุรกิจ |
| G3 Bounded context hypothesis | Language/model consistency analysis, ownership/responsibility, boundary trade-offs | Candidate bounded contexts & decision points | อธิบาย boundary ด้วย model/language/invariants/ownership evidence; จุดที่ยังไม่ชัดเป็น hypothesis |
| G4 Context relationships | Context map, integration/ownership discussion | Candidate context relationships + unresolved contracts | ไม่ตีความว่า bounded context = microservice; มีหลักฐานและ human confirmation สำหรับข้อสรุปสำคัญ |
| G5 Review & handoff | Evidence audit, coverage check, stop assessment | Draft Strategic Domain Map + decision log + open questions | ผลลัพธ์มี source/assumption/conflict/decision status; ผ่าน stop criteria หรือรายงาน blocked |

**Gate outcome มี 3 แบบ:** \`pass\` (ไปต่อ), \`provisional\` (ทำต่อได้โดยติดป้ายความเสี่ยง), \`blocked\` (ต้องการข้อมูล/การตัดสินใจที่จำเป็นจริง ๆ) การผ่าน Gate ไม่ได้บอกว่า domain model ถูกต้องแน่นอน

## Frontier / Grilling: วิธีถามและหยุด

1. เก็บ decision dependencies เป็น design tree; frontier คือคำถามที่ prerequisite พร้อมแล้ว
2. จัดคำถามตามความเสี่ยงต่อ boundary, ความย้อนกลับยาก และความจำเป็นสำหรับ next gate; ถามเฉพาะ frontier ที่มีผลต่อ next decision
3. เสนอ recommended option พร้อมเหตุผลและ degree of confidence; เปิดให้ผู้ใช้ปฏิเสธหรือเปลี่ยนคำตอบ
4. เมื่อไม่มีคำถามที่ blocking next gate ให้เดินหน้าด้วย provisional assumptions ที่ระบุชัด ไม่วนถามเพื่อให้ครบตามแบบฟอร์ม
5. ถ้า conflict ใน facts / stakeholder goals มีผลต่อ boundary สำคัญ ให้ pause การตัดสินใจนั้น และบันทึก blocker ไม่เติมคำตอบเอง

## Stop Criteria (ไม่ใช่การรอให้ทุกอย่างชัด 100%)

หยุด Discovery และส่ง artifacts ให้ review ได้เมื่อ:

- ทุก decision สำคัญใน scope มีสถานะ \`confirmed\`, \`provisional\` หรือ \`blocked\` พร้อมเหตุผล
- ทุก candidate boundary มีอย่างน้อยหนึ่ง evidence link หรือถูกระบุว่า hypothesis
- ไม่มี unresolved **blocking** question ที่ถูกละเลย
- อธิบาย trade-offs และทางเลือกที่ถูกปฏิเสธได้ในประเด็นที่มีผลกระทบสูง
- ผู้ใช้เห็นสถานะว่าเป็น draft หรือ confirmed และรับรู้ข้อจำกัดของผลลัพธ์

เมื่อผู้ใช้ต้องการหยุดก่อน ให้ส่ง partial artifacts พร้อม gaps และ next questions แทนการอ้างว่า complete

## Proposed Output Artifacts

1. \`strategic-domain-map.md\`: scope, capabilities, candidate subdomains, candidate bounded contexts, relationships, confidence/evidence
2. \`decision-log.md\`: decision, alternatives, rationale, source(s), owner/confirmation status
3. \`open-questions.md\`: blockers, assumptions, conflicts, frontier และ next action
4. Optional \`context-map.mmd\` หลังยืนยัน relationships มากพอ

**Artifact acceptance criteria:** traceable, distinction between fact/hypothesis explicit, scoped, reviewable, reusable without proprietary tooling; missing or conflicting evidence is visible, not hidden

## Derive Knowledge Dependencies (ยังไม่ใช่ไฟล์ที่ผ่านการรับรอง)

| Stage | Required reference candidate | Purpose |
|---|---|---|
| G0, G5 | \`references/evidence-and-stop-criteria.md\` | evidence types, claim status, gating, stop/escalation |
| G1 | \`references/domain-discovery-selection.md\` | when to use lightweight narrative vs Event Storming |
| G2 | \`references/subdomain-analysis.md\` | capability/subdomain classification criteria + counterexamples |
| G3 | \`references/bounded-context-boundaries.md\` | language/model/ownership evidence and trade-offs |
| G4 | \`references/context-relationships.md\` | context map relationship guidance and uncertainty |

Reference เหล่านี้เป็น **candidate dependencies** ต้องตรวจแหล่งที่มาและลด/รวมไฟล์ตามผล evaluation; ยังไม่ควรคัดลอกเนื้อหาจาก inbox แล้วเรียกว่า canonical

## Evaluation Plan (ต้องทดลองจริงก่อนระบุว่าผ่าน)

Run Skill ใน consumer repository ที่ **ไม่มี access ไปยัง Knowledge Hub** แล้วเก็บ input/output + human review:

| Scenario | Expected behavior |
|---|---|
| E1: TOR/process อธิบายครบ | สกัด domain signals, เสนอ boundaries พร้อม evidence และ assumptions |
| E2: Input กำกวม | ถาม frontier ที่มีความสำคัญ ไม่ประดิษฐ์ details |
| E3: Requirements ขัดแย้ง | พบและแสดง conflict; ไม่ finalize boundary ที่ต้องพึ่ง conflict |
| E4: Evidence เพียงพอแล้ว | หยุด questioning, ผลิต artifacts ที่ review ได้ |
| E5: References ไม่เพียงพอ | รายงาน gap, ไม่ claim certainty; เปิด proposal เพิ่ม knowledge |

เก็บ rubric อย่างน้อย: \`traceability\`, \`correctness as judged by domain reviewer\`, \`question relevance\`, \`gate discipline\`, \`stopping behavior\`, \`portability\`. บันทึก pass/fail พร้อมตัวอย่างการตัดสินใจและ failure case; ยังไม่มี benchmark result

## Implementation Order

1. Review และยืนยัน MVP workflow/gates/artifacts ใน PR นี้
2. ตรวจ source knowledge ตาม dependency matrix; curate Required refs โดยคง traceability
3. เขียน \`skills/strategic-ddd/SKILL.md\` และ references ที่ self-contained
4. ติดตั้ง Skill ใน consumer repo แบบ project scope ด้วย Skills CLI; ทดสอบ Agent ที่ใช้จริง
5. รัน E1–E5, เก็บ evidence ใน \`experiments/\` และปรับ Skill ผ่าน PR

## Open Questions

- ขอบเขตขั้น G1: จะรองรับ Process-level Event Storming ใน MVP หรือเป็น follow-up หลัง Strategic DDD?
- รูปแบบ human approval: ต้องยืนยันทุก boundary หรือเฉพาะ high-impact boundaries?
- เกณฑ์ confidence/evidence grading ที่เหมาะกับ solo dev และผู้ใช้ที่ไม่มี SME?
- จะใช้ output เดียวแบบ Markdown เป็นหลัก หรือเพิ่ม mermaid context map ตั้งแต่ MVP?
