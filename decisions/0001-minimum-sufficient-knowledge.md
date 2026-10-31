# ADR-0001: Minimum Sufficient Knowledge สำหรับ Agent Skills

- สถานะใน repository: **Proposed (รอ PR review/merge)**
- วันที่: 2026-10-31
- ขอบเขต: HACLS Agent Skills; เริ่มทดลองกับ \`strategic-ddd\`
- การตัดสินใจ: หลักการได้รับความเห็นชอบในบทสนทนาแล้ว แต่ยังไม่ถือเป็นนโยบายใน repository จนกว่า PR จะผ่านการตรวจรับ
- อ้างอิง: [HACLS Project Charter](../docs/00-project-charter.md)

## บริบท

HACLS มี Knowledge Hub ที่เป็นแหล่งอ้างอิงหลัก และต้องการแจกจ่าย Agent Skills ไปใช้ข้าม repository โดยไม่บังคับให้ทุก consumer เข้าถึง Hub ได้ตลอดเวลา ปัญหาคือจะเลือกความรู้ส่วนใดติดไปกับ Skill โดยไม่ทำให้เกิดหลายแหล่งความจริงที่ดูแลไม่ไหว

## Decision

ใช้หลัก **Minimum Sufficient Knowledge** และ **Evidence-Driven Knowledge Packaging**:

1. **Knowledge Hub เป็น Source of Truth** สำหรับความรู้ที่ได้รับการตรวจรับ; \`validated\` และ \`canonical\` มีความหมายตาม Project Charter ส่วน \`inbox\` ห้ามตีความว่าเป็นข้อเท็จจริงที่ยืนยันแล้ว
2. **\`SKILL.md\`** บรรจุ entry point, workflow, responsibility boundaries, decision logic, evidence gates, stop/escalation conditions และลิงก์ไปยัง references ที่จำเป็น
3. **\`skills/<name>/references/\`** บรรจุความรู้ที่ Skill ต้องใช้เพื่อทำงานอย่างถูกต้องแบบ self-contained; โหลดเฉพาะเมื่อถึงขั้นที่ต้องใช้
4. **Derive dependencies backwards**: เริ่มจาก workflow → evidence gates → acceptance criteria → ระบุ knowledge ที่จำเป็น ไม่เลือกเอกสารจากความชอบหรือจำนวนหน้า
5. **Manual curation สำหรับ MVP**: ไม่สร้างระบบซิงก์/ดึงข้อมูล/แพ็กเกจอัตโนมัติจนกว่าจะมีหลักฐานว่าจำเป็น
6. **Change policy: propose**: Agent เสนอการเปลี่ยนแปลงผ่าน PR; ไม่แก้ canonical knowledge หรือเลื่อนสถานะอัตโนมัติ
7. **ไม่พึ่ง implicit model knowledge เป็นหลักฐาน**: สิ่งที่จำเป็นต่อการตัดสินใจ/verify ต้องอยู่ใน dependency ที่อ้างอิงได้หรือ Agent ต้องรายงานว่าไม่เพียงพอ

## การจำแนก Knowledge Dependency

| ระดับ | คำถามตัดสิน | การจัดการ |
|---|---|---|
| Required | ขาดแล้วตัดสินใจผิด ทำ workflow ต่อไม่ได้ หรือ verify/stop ไม่ได้หรือไม่ | Bundle ภายใน Skill และทดสอบแบบ offline จาก Hub |
| Supporting | ช่วยเพิ่มคุณภาพเฉพาะบางกรณี โดยไม่กระทบ correctness ของกรณีหลักหรือไม่ | Optional reference ใน Skill หรือแหล่งภายนอกตามความพร้อม |
| Background | เป็นที่มา/ประวัติ/การศึกษาเพิ่มเติม และไม่จำเป็นต่อ execution หรือไม่ | อยู่ใน Hub พร้อมลิงก์แหล่งอ้างอิง |

**Rule:** ไม่มีการกำหนดโควตาความยาวไฟล์; เกณฑ์คือความสามารถดำเนินงานและให้เหตุผลได้อย่างตรวจสอบได้ ไม่ใช่จำนวน token ที่น้อยที่สุด

## Source Traceability

แต่ละ reference ที่คัดลอกจาก Hub ควรมี metadata หรือส่วนหัวระบุ: \`source_path\`, \`source_revision\` (commit SHA หรือ revision ที่ระบุแน่ชัด), \`curated_at\`, \`verification_status\` และสรุปการย่อ/ปรับเนื้อหา (ถ้ามี)

หากความรู้ยังไม่เป็น \`validated\` หรือ \`canonical\` ห้ามบอกว่าได้รับการรับรอง; ให้ระบุ \`provisional\` และใช้เพื่อทดลองเท่านั้นจนผ่าน review

การอัปเดต Hub ไม่ทำให้ Skill ที่เผยแพร่แล้วอัปเดตโดยอัตโนมัติ ต้องมีการตรวจผลกระทบต่อ reference, ทดสอบใหม่ และปล่อย version/change ผ่าน PR

## ทางเลือกที่พิจารณา

- **ให้ Skill โหลด Hub โดยตรงทุกครั้ง**: ลดการซ้ำ แต่พึ่ง network/auth และ path ของต้นทาง; ไม่เหมาะกับ acceptance test ที่ต้องทำงานแยกโปรเจกต์
- **คัดลอก Knowledge Hub ทั้งหมดเข้า Skill**: self-contained แต่เพิ่ม context/noise และภาระดูแล
- **เขียนความรู้ซ้ำด้วยมือโดยไม่ตาม source**: เริ่มง่าย แต่ drift และ audit ยาก
- **Selected:** curated, traceable references เฉพาะ Required และ Supporting ที่พิสูจน์ความจำเป็นได้

## ผลกระทบ

- ต้องรักษา source traceability และความต่างระหว่าง proposed / validated / canonical
- Skill สามารถติดตั้งข้ามโปรเจกต์ได้โดยไม่ต้องติดตั้ง Hub ทั้งก้อน
- การ sync อัตโนมัติและ runtime retrieval เป็นงานระยะถัดไปเมื่อมีเหตุผลและผลทดสอบรองรับ

## เงื่อนไขตรวจรับ

- ระบุ dependency ของทุก evidence gate ได้ และโยงกลับไปยัง reference/source ได้
- Agent ใช้ Skill ใน consumer repo โดยปิดการเข้าถึง Knowledge Hub แล้วผ่าน test สำหรับ input ปกติ, กำกวม, ขัดแย้ง, หลักฐานพอให้หยุด และความรู้ไม่ครอบคลุม
- เมื่อขาดข้อมูล Agent ไม่สร้างข้อเท็จจริงใหม่; รายงาน assumption/unknown และขอการตัดสินใจเท่าที่จำเป็น
- Skill ที่เปลี่ยนหลัง Knowledge Hub เปลี่ยนต้องผ่าน review + regression test ก่อนเผยแพร่

## ไม่ครอบคลุมใน ADR นี้

- การเลือกวิธีทำ Strategic DDD รายขั้นทั้งหมด (อยู่ใน MVP design)
- ระบบ Knowledge Sync, RAG, MCP, npm package หรือ CLI เฉพาะ HACLS
- การอนุมัติให้ reference ที่ยังไม่ได้ตรวจสอบกลายเป็น canonical โดยอัตโนมัติ
