---
type: KNOTE
status: inbox
tags: [domain-discovery, taxonomy, agent-skills]
---

# Domain Discovery Taxonomy

Taxonomy นี้จำแนกแนวคิดใน Domain Discovery Toolkit ตามบทบาทและระดับของแนวคิด เพื่อช่วยให้ Developer และ Agent เลือกวิธีได้ตรงกับช่องว่างความรู้ โดยไม่มอง Framework, Technique และกลไกเลือกวิธีเป็นสิ่งประเภทเดียวกัน

## หมวดหมู่

| หมวด | บทบาท | ตัวอย่างจาก Toolkit |
|---|---|---|
| **แนวทางและกรอบคิด** | ให้หลักการและมุมมองกว้างสำหรับทำความเข้าใจและออกแบบระบบ | Domain-Driven Design (DDD) |
| **วิธีสำรวจ Domain** | ช่วยค้นหาข้อเท็จจริงเกี่ยวกับเหตุการณ์ ผู้เกี่ยวข้อง กิจกรรม เป้าหมาย และกฎ | Big Picture Event Storming, Domain Storytelling, Example Mapping, Impact Mapping |
| **กิจกรรมและเทคนิควิเคราะห์** | จัดโครงสร้างสิ่งที่ค้นพบเพื่อวิเคราะห์กระบวนการหรือขอบเขตของ Domain | Process Modeling, Subdomain Classification, Context Mapping |
| **กลไกเลือกและประสานวิธี** | ประเมินช่องว่างความรู้ เลือกวิธี และกำหนดลำดับหรือการส่งต่อ | Selection Policy, Decision Tree, Tool Selection Matrix, Tool Handoff Rules |
| **Workflow การค้นพบ** | เชื่อมการประเมิน input การเลือกวิธี การดำเนินงาน และการพิจารณาขั้นถัดไป | Domain Discovery Workflow, Discovery Playbook |
| **การประเมินคุณภาพ** | ตรวจว่าผลลัพธ์เพียงพอและตอบโจทย์การตัดสินใจหรือไม่ | Output Quality, Exit Criteria, Tool Selection Evaluation |

หมวดเหล่านี้จัดตามหน้าที่ ไม่ใช่ลำดับบังคับ และบางวิธีอาจเกี่ยวข้องกับมากกว่าหนึ่งหมวด ให้เลือกหมวดหลักจากผลลัพธ์ที่วิธีนั้นมุ่งสร้าง แล้วใช้ links ระบุความสัมพันธ์เพิ่มเติม

## การแยกสิ่งที่มักสับสน

- **DDD** เป็นแนวทางหรือกรอบคิด ไม่ใช่เครื่องมือเดี่ยว
- **Event Storming** เป็นวิธีสำรวจ Domain ซึ่งใช้แนวคิดจาก DDD ได้ แต่ไม่ใช่ DDD ทั้งหมด
- **Subdomain Classification** และ **Context Mapping** เป็นกิจกรรม/เทคนิควิเคราะห์เชิงกลยุทธ์ในแนวทาง DDD
- **Decision Tree** เป็นกลไกนำทางการเลือกวิธี ไม่ใช่วิธีค้นหาข้อเท็จจริงทางธุรกิจโดยตรง
- **Tool Catalog** เป็นรายการและแหล่งนำทาง ไม่ใช่ workflow หรือ selection policy ด้วยตัวเอง

## วิธีนำ Taxonomy ไปใช้

1. เริ่มจากระบุการตัดสินใจที่ต้องรองรับและช่องว่างความรู้ที่ขัดขวางการตัดสินใจนั้น
2. ใช้หมวดเป็นตัวช่วยค้นหาวิธีที่เกี่ยวข้อง ไม่เลือกวิธีจากชื่อหรือความคุ้นเคยเพียงอย่างเดียว
3. ตรวจเงื่อนไข `ใช้เมื่อ`, input, output, ข้อจำกัด และความสัมพันธ์จาก Tool Catalog/Profile
4. ดำเนินวิธีที่เลือก แล้วตรวจผลลัพธ์กับเกณฑ์คุณภาพและ Exit Criteria
5. หากยังมีช่องว่าง ให้กลับไปเลือกวิธีถัดไปหรือขอข้อมูลจาก Domain Expert

Taxonomy นี้กำหนดภาษาสำหรับจัดหมวด ส่วนรายละเอียดคุณสมบัติและการเลือกใช้แต่ละวิธียังคงอยู่ในเอกสารอ้างอิง ไม่ทำซ้ำไว้ที่นี่

## เอกสารที่เกี่ยวข้อง

- [Taxonomy of Agent Workflow Methods](../../agent-workflows/notes/Taxonomy%20of%20Agent%20Workflow%20Methods.md) — หมวดข้ามโดเมนสำหรับแนวคิดที่ใช้กับ Skills หลายประเภท
- [Domain Discovery Toolkit: ภาพรวม](../overview.md) — เป้าหมาย ขอบเขต องค์ประกอบ และ workflow ของ Toolkit
- [Tool Catalog](Tool%20Catalog.md) — รายการวิธี Selection Matrix และ Tool Profiles

## แหล่งอ้างอิง

- [Domain Discovery Toolkit: ภาพรวม](../overview.md)
- [Tool Catalog](Tool%20Catalog.md)
