---
type: KNOTE
status: inbox
tags:
  - event-storming
---
# ระดับของ Event Storming

โดยหลักแล้ว Big Picture Event Storming ไม่จำเป็นต้องมีองค์ประกอบทั้งหมดเหล่านี้ เพราะ Big Picture ES เน้นทำความเข้าใจภาพรวม Business Landscape ไม่ใช่การออกแบบระบบซอฟต์แวร์ในรายละเอียด

เราต้องแยกองค์ประกอบตามระดับของ Event Storming ให้ชัดเจน

## 1. เปรียบเทียบองค์ประกอบแต่ละระดับ

| Element             | Big Picture        | Process Level | Software Design |
| ------------------- | ------------------ | ------------- | --------------- |
| Domain Event        | **หลัก**           | **หลัก**      | **หลัก**        |
| Actor               | **หลัก**           | **หลัก**      | มีได้           |
| External System     | มีได้              | มีได้         | มี              |
| Command             | ไม่จำเป็น          | **หลัก**      | มี              |
| Policy              | ไม่จำเป็น          | **หลัก**      | มี              |
| Aggregate           | ไม่ควรลงรายละเอียด | อาจกล่าวถึง   | **หลัก**        |
| Read Model          | ไม่จำเป็น          | มีได้         | มี              |
| UI / User Interface | ไม่จำเป็น          | มีได้         | มี              |
| Hotspot             | **หลัก**           | **หลัก**      | มีได้           |

หมายเหตุ: ตารางนี้เป็นการแนะนำขอบเขตการใช้งาน ไม่ใช่ข้อห้ามตายตัวของ Event Storming

## 2. องค์ประกอบที่ควรมีใน Big Picture ES

**Domain Event (Core)**

สิ่งที่เกิดขึ้นแล้วในธุรกิจ เช่น Booking Created, Booking Confirmed

**Actor / Person**

ใครเป็นผู้กระทำหรือเกี่ยวข้องกับเหตุการณ์ เช่น Customer, Administrator, Staff

**External System**

ระบบภายนอกที่มีส่วนใน Business Process เช่น Payment Gateway, Identity Provider

**Hotspot**

จุดที่มีความไม่แน่นอน ความขัดแย้ง หรือคำถามที่ยังตอบไม่ได้

**Timeline / Process Cluster**

ลำดับเวลาและกลุ่มกระบวนการที่ช่วยให้เห็นภาพรวม

## 3. ทำไมไม่ควรใส่ Command, Policy, Aggregate ตั้งแต่ต้น?

ลองดูตัวอย่าง Booking Engine

สมมุติเรามี Event ดังนี้

Booking Created

Booking Confirmed

เมื่ออยู่ใน Big Picture เราต้องการเข้าใจว่า:

- ใครเป็นผู้สร้าง Booking?
- ทำไม Booking จึงถูก Confirm?
- มีเหตุการณ์ใดเกิดขึ้นก่อนหรือหลัง?
- มี Business Rule หรือความไม่ชัดเจนอะไรบ้าง?
- กระบวนการนี้เกี่ยวข้องกับกระบวนการอื่นอย่างไร?

เราไม่จำเป็นต้องตอบตั้งแต่ตอนนี้ว่า:
- Command ชื่อ `CreateBooking` หรือ `CreateBookingHold`
- Policy จะเรียก Command ใด
- Aggregate คือ Booking หรือ Resource
- Read Model จะชื่อ `AvailableResources`
- UI จะมีหน้า Booking Form อย่างไร

คำถามเหล่านี้เป็นเรื่องของ Process Design และ Software Design มากกว่า

## 4. ความสัมพันธ์กับ Event Storming 3 ระดับ

Level 1

Big Picture ES

# Business Landscape

ค้นหาว่าธุรกิจทำอะไร มีเหตุการณ์อะไร และกระบวนการต่าง ๆ เชื่อมโยงกันอย่างไร

Event · Actor · External System · Hotspot

Level 2

Process Modeling ES

# Business Process

เจาะลึกกระบวนการหนึ่งว่าทำงานอย่างไร อะไรเป็นตัวกระตุ้น และมีเงื่อนไขอะไร

Command · Policy · Actor · Event · Read Model · External System

Level 3

Software Design ES

# Software Model

ออกแบบว่าจะสร้างซอฟต์แวร์อย่างไรเพื่อรองรับ Business Process

Aggregate · Command · Domain Event · Policy · Read Model · UI

ข้อควรระวัง: Event Storming ไม่ได้มีมาตรฐานบังคับว่าแต่ละระดับต้องใช้ Post-it ชุดใดแบบตายตัว รายการข้างต้นเป็นการแบ่งขอบเขตเพื่อให้ใช้งานง่าย

## 5. คำแนะนำสำหรับ Lean DDD Workflow ของเรา
ผมแนะนำให้ใช้ Big Picture ES แบบ Minimal ก่อน:

|ใช้|ไม่ต้องใช้ในรอบแรก|
|---|---|
|Domain Event|Command|
|Actor|Aggregate|
|External System|Read Model|
|Hotspot|UI|
|Timeline / Cluster|Policy|

จากนั้นเมื่อเลือก Business Process ที่ต้องการศึกษาแล้ว ค่อยทำ Process Level ES เพื่อค้นหา Command, Policy และ Read Model

หลักคิดสำคัญ: อย่าเพิ่งถามว่าเราจะสร้าง Software Component อะไร จนกว่าเราจะเข้าใจว่า Business ต้องการให้เกิดอะไรขึ้น

นี่เป็นวิธีลดการออกแบบเกินความจำเป็น (Over-engineering) โดยยังรักษาประโยชน์หลักของ DDD ไว้ครับ
## เหตุผลหรือหลักฐาน

[อธิบายเหตุผล ตัวอย่าง หรือหลักฐาน พร้อมแยกข้อเท็จจริงออกจากการตีความ]

## เชื่อมโยง

- [ชื่อโน้ตหรือหัวข้อ](ลิงก์) — [อธิบายว่าความคิดเชื่อมโยงกันอย่างไร]

## แหล่งที่มา

- [ชื่อแหล่ง](URL หรือ references.md#รายการ) — [ข้อกล่าวอ้างหรือส่วนที่แหล่งนี้รองรับ]
