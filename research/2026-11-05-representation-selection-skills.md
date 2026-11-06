<!-- Type: RES | Document type: Research synthesis -->
# Research: Representation Selection in Existing Agent Skills

**วันที่:** 2026-11-05  
**สถานะ:** Synthesis / ข้อเสนอ ไม่ใช่ผล benchmark  
**โจทย์:** Skills ใดมีหลักการเลือก Prose, Table, Diagram, Chart ตามความต้องการของผู้อ่าน และนำมาปรับใช้ใน HACLS อย่างไร?

## Executive Summary

Skills ที่ตรวจสอบส่วนมากเลือกรูปแบบการนำเสนอ **ภายในสื่อที่กำหนดแล้ว** เช่น HTML มิใช่ shared policy สำหรับ chat, Markdown, reports และ tutorials ทุกประเภท

| Skill | หลักการที่นำมาใช้ได้ | ข้อจำกัด |
|---|---|---|
| [html-artifacts](https://github.com/joshuadavidthomas/agent-skills/blob/main/html-artifacts/SKILL.md) | ระบุ reader, governing question, scope; เลือก representation ตาม reader's verb | ใช้กับ HTML artifacts เป็นหลัก |
| [to-html](https://github.com/pbi-agent/skills/blob/main/skills/to-html/SKILL.md) | Visual grammar: table/compare, chart/quantity, diagram/relationship, code/interface | ผลลัพธ์เป็น HTML |
| [visual-explainer](https://github.com/nicobailon/visual-explainer/blob/main/plugins/visual-explainer/SKILL.md) | Figure-driven explanations, figure ต้องสื่อ claim ที่เฉพาะเจาะจง | เน้น visuals มากกว่าตัดสินใจใช้ prose-only |
| [Superpowers writing-skills](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md) | ใช้ Flowchart เมื่อมี non-obvious decision หรือ loop; ไม่ใช้กับ linear steps, reference, code | เป็น skill authoring guidance |
| [pstack technical-writing](https://github.com/cursor/plugins/blob/main/pstack/skills/technical-writing/SKILL.md) | Diátaxis: แยก tutorial/how-to/reference/explanation ตามเจตนา | เลือก genre ไม่ได้เลือก medium ของข้อมูลโดยตรง |

## ข้อค้นพบและการประยุกต์ใช้

- **Reader's question before rendering:** นำแนวคิด governing question มาใช้เป็น default ของทุก Task Skill
- **Presentation is downstream of evidence:** แยก facts/relations/metrics/uncertainty ออกจากการจัดรูปแบบเพื่อหลีกเลี่ยงภาพที่แต่งเติมข้อมูล
- **Minimal sufficient representation:** เริ่มจาก prose/table/diagram ที่เล็กที่สุดซึ่งตอบคำถามได้ เพิ่มรูปแบบที่สองเมื่อมีคำถามรองที่ตอบไม่ได้
- **Avoid diagram-first:** ไม่วาด Flowchart สำหรับ steps ที่เป็นเส้นตรงหรือไม่ต้องตัดสินใจ
- **Genre ≠ Representation:** Tutorial, explanation, how-to และ reference มี selection logic ต่างจากการเลือกระหว่าง Table กับ Diagram

## Design Decision ที่เสนอ

1. จัดทำ [Shared Representation Selection Policy](../docs/guidelines/representation-selection.md) ไว้ใน docs; แยกจาก Task/Renderer Skills
2. ใส่เพียง rule สั้น ๆ ใน `AGENTS.md` พร้อมลิงก์ไปเอกสารกลาง เพื่อไม่ต้องโหลดรายละเอียดทุก turn
3. ให้ Task Skill รับผิดชอบ audience, evidence และสาระของ domain; ให้ Renderer รับผิดชอบรูปแบบปลายทางโดยไม่เพิ่ม business facts
4. ใช้ชุด [evaluation cases](../experiments/representation-selection-evaluation-cases.md) เพื่อตรวจเชิงพฤติกรรมก่อนรับรองเป็นมาตรฐาน; การตรวจ Source Code ของ Skills ไม่ใช่ runtime evaluation

## Method / Limitations

อ้างอิงไฟล์ `SKILL.md` ต้นฉบับของผู้พัฒนาโดยตรง และเปรียบเทียบ selection criteria, evidence guardrails, output medium และข้อจำกัด ไม่ได้ทดลองรัน Skills เหล่านี้ใน runtime เดียวกัน จึงยังไม่มีข้อสรุปเชิงประสิทธิผลเชิงปริมาณ และไม่ได้อ้างว่าไม่พบ Skill ประเภทนี้ที่อื่นทั้งหมด
