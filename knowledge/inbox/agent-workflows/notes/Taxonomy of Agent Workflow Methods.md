---
type: KNOTE
status: inbox
tags: [agent-skills, taxonomy, workflow]
---

# Taxonomy of Agent Workflow Methods

เอกสารนี้จัดหมวดแนวทาง วิธีปฏิบัติ และเครื่องมือที่ Skills ใช้เพื่อคิด ตัดสินใจ ดำเนินงาน และตรวจผล โดยจำแนกตามหน้าที่หลัก เพื่อช่วยเลือกโครงสร้างให้เหมาะกับปัญหา ไม่ได้กำหนดว่าทุก Skill ต้องใช้ทุกหมวด

## หมวดหมู่ตามหน้าที่

| หมวด | หน้าที่ | ตัวอย่าง |
|---|---|---|
| **แนวทางและกรอบคิด** | ให้หลักการหรือแบบจำลองกว้างเพื่อมองปัญหาและออกแบบวิธีทำงาน | DDD สำหรับการออกแบบซอฟต์แวร์, risk-based thinking |
| **วิธีค้นพบและเก็บข้อมูล** | ดึงความรู้หรือข้อเท็จจริงจากผู้ใช้ ระบบ หรือแหล่งข้อมูล | interview, Event Storming, Domain Storytelling, research |
| **โครงสร้างการตัดสินใจและวิเคราะห์** | จัดทางเลือก เงื่อนไข สมมติฐาน หรือ dependency เพื่อเลือกขั้นถัดไป | decision tree, decision table, hypothesis tree, dependency graph |
| **Workflow และการควบคุมสถานะ** | กำหนดลำดับ ขั้น สถานะ และเงื่อนไขการเปลี่ยนขั้น | plan–execute–verify loop, state machine, incident workflow |
| **การตรวจสอบและประเมินผล** | ตรวจความครบถ้วน คุณภาพ ความเสี่ยง หรือผลลัพธ์เทียบเกณฑ์ | checklist, rubric, risk matrix, FMEA, exit criteria |
| **การจัดลำดับและจัดสรรงาน** | เลือกสิ่งที่ควรทำก่อนตามคุณค่า ต้นทุน หรือข้อจำกัด | impact–effort matrix, prioritization policy |

## ใช้หมวดให้ถูกระดับ

คำว่า “tool” อาจหมายถึงสิ่งที่มีหน้าที่และระดับต่างกัน จึงควรบันทึกชนิดของรายการให้ชัดด้วย:

- **Framework / approach** ให้กรอบคิดกว้าง เช่น DDD
- **Technique / method** เป็นวิธีทำกิจกรรมเฉพาะ เช่น Event Storming หรือ Example Mapping
- **Reasoning structure** จัดรูปแบบการวิเคราะห์ เช่น decision tree หรือ hypothesis tree
- **Workflow / process** กำหนดการทำงานหลายขั้น เช่น plan–execute–verify
- **Evaluation instrument** ตรวจผลกับเกณฑ์ เช่น checklist หรือ rubric

หมวดหน้าที่กับชนิดของรายการเป็นคนละมิติ เช่น decision tree เป็น reasoning structure ที่ใช้ในหมวดการตัดสินใจ หรือ Event Storming เป็น technique ในหมวดการค้นพบและเก็บข้อมูล ทั้งคู่ไม่ควรถูกนำไปเทียบเป็นตัวเลือกชนิดเดียวกันโดยไม่มีบริบท

## หลักเลือกใช้กับ Skill

1. ระบุผลลัพธ์ที่ Skill ต้องสร้างหรือการตัดสินใจที่ต้องรองรับ
2. ระบุข้อมูลที่ยังขาดและข้อจำกัดของงาน
3. เลือกหมวดที่ตรงกับหน้าที่ที่ขาด แล้วเลือกรายการเฉพาะจากหมวดนั้น
4. ใช้โครงสร้างเสริมเฉพาะเมื่อช่วยจัดการ dependency, uncertainty, state หรือ quality ได้จริง
5. กำหนด input, output, เงื่อนไขไปต่อ และเกณฑ์จบให้ตรวจสอบได้

ตัวอย่าง: Skill สำหรับ Domain Discovery อาจใช้ interview เพื่อเก็บบริบท, decision tree เพื่อเลือกวิธีสำรวจ, Event Storming เพื่อสร้างความเข้าใจร่วม และ checklist เพื่อประเมินผลลัพธ์ แต่ไม่จำเป็นต้องใช้ทุกอย่างหากช่องว่างความรู้แคบและชัดอยู่แล้ว

## ขอบเขตกับ Taxonomy เฉพาะทาง

Taxonomy นี้เป็นหมวดระดับข้ามโดเมนสำหรับ Skills ส่วนรายการเฉพาะของแต่ละโดเมนควรอยู่ในคลังความรู้ของโดเมนนั้น และเชื่อมกลับมาที่นี่เมื่อใช้แนวคิดร่วมกัน

- [Domain Discovery Taxonomy](../../domain-discovery-toolkit/notes/Domain%20Discovery%20Taxonomy.md) — จำแนกกรอบคิด วิธีสำรวจ และกลไกเลือกวิธีใน Domain Discovery Toolkit
- [เครื่องมือจัดโครงสร้างการคิดสำหรับ Skills](เครื่องมือจัดโครงสร้างการคิดสำหรับ-skills.md) — คำอธิบายเครื่องมือ reasoning และ workflow พร้อมเกณฑ์เลือกใช้

## แหล่งอ้างอิง

- บทสนทนาเรื่องการจำแนกเครื่องมือสำหรับ Skills และ Domain Discovery (2026-10-30)
- [Domain Discovery Toolkit: ภาพรวม](../../domain-discovery-toolkit/overview.md)
- [Domain Discovery Taxonomy](../../domain-discovery-toolkit/notes/Domain%20Discovery%20Taxonomy.md)
