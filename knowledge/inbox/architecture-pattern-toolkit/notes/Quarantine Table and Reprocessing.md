---
type: KNOTE
status: inbox
tags: [architecture, reliability, data-processing]
---

# Quarantine Table และการประมวลผลซ้ำ

> **สถานะ:** บันทึกแนวคิดเบื้องต้นจากการอ่าน JCM3; ยังไม่ได้ตรวจแหล่งต้นฉบับ

## แนวคิด

ในโน้ตนี้ Quarantine Table หมายถึงแนวทางระดับ application/data layer สำหรับจัดเก็บรายการที่ประมวลผลไม่สำเร็จ เพื่อไม่ให้ข้อมูลที่มีปัญหาหายไปหรือขัดขวางรายการอื่น การเก็บรายการไว้พร้อมสถานะและเหตุผลช่วยให้ผู้ปฏิบัติงานตรวจสอบ แก้สาเหตุ และตัดสินใจนำรายการกลับเข้ากระบวนการได้ ทั้งนี้ **ไม่พบว่า Quarantine Table เป็นชื่อ pattern มาตรฐานที่มีนิยามเดียว** ในแหล่งทางการที่ตรวจ แนวทางนี้จึงเป็นการสังเคราะห์และอาจมีขอบเขตทับซ้อนกับ Dead Letter Queue

Reprocessing คือการนำรายการที่ถูกพักไว้กลับมาประมวลผลอีกครั้ง หลังแก้ข้อมูล แก้ configuration หรือแก้ defect แล้ว ควรมองเป็น workflow ที่มีการควบคุม ไม่ใช่การยิงซ้ำโดยไม่มีขอบเขต Microsoft แนะนำให้กำหนด retry ให้เหมาะกับ transient fault และใช้ dead-letter เมื่อ retry ครบแล้วยังล้มเหลว [Retry pattern](https://learn.microsoft.com/th-th/azure/architecture/patterns/retry), [Transient fault handling](https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults)

## กลไกที่ควรพิจารณา

- เก็บ payload หรือ reference ที่พอระบุต้นฉบับได้ พร้อม error, เวลา, จำนวนครั้ง และเวอร์ชันของ handler/schema ที่เกี่ยวข้อง
- แยกสถานะ เช่น `quarantined`, `ready_to_reprocess`, `processing`, `resolved` และ `discarded` ให้สอดคล้องกับ workflow จริง
- ให้การ reprocess ทำซ้ำได้อย่างปลอดภัย (idempotent) หรือกำหนดการป้องกัน duplicate อย่างชัดเจน
- จำกัดสิทธิ์และบันทึก audit เมื่อมีการดู แก้ไข หรือสั่ง reprocess ข้อมูล
- กำหนด retry limit, backoff, การแบ่ง batch และการหยุดเมื่อพบความล้มเหลวซ้ำ
- ทำให้สังเกตได้: จำนวนรายการค้าง อายุรายการ สาเหตุหลัก อัตราสำเร็จหลัง reprocess และรายการที่เกิน SLA

## เหมาะเมื่อ

- การทิ้งรายการที่ผิดพลาดทำให้เกิดผลกระทบหรือสูญเสียข้อมูลที่ยอมรับไม่ได้
- ต้องมีการตรวจสอบหรือแก้ไขโดยคนก่อนกลับมาทำงาน
- ต้องการประวัติและการควบคุมการกู้คืนที่ query/triage ได้

## ต้นทุนและข้อควรระวัง

- เพิ่มพื้นที่เก็บข้อมูลและภาระดูแลวงจรชีวิต/retention ของข้อมูล
- ต้องระวังข้อมูลส่วนบุคคล ความลับ และการควบคุมสิทธิ์ใน payload ที่ถูกพักไว้
- การ reprocess อาจสร้าง side effect ซ้ำ หากงานเดิมไม่ idempotent
- ระบบ broker อาจมี DLQ และ redrive ในตัวอยู่แล้ว ควรเทียบความสามารถนั้นก่อนสร้างตาราง quarantine เพิ่ม [Microsoft Service Bus DLQ](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues), [AWS SQS redrive](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue-redrive.html)
- Transactional Outbox แก้ปัญหา dual-write ระหว่าง state กับ event; เป็นคนละหน้าที่กับที่พักรายการซึ่งประมวลผลล้มเหลว [Microsoft Transactional Outbox](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)
- การแก้ schema หรือ business rule อาจทำให้รายการเก่าใช้ซ้ำไม่ได้ ต้องมีขั้นตอน migration หรือแปลงข้อมูล
- หากปริมาณสูงและระบบเป็น message-driven, Dead Letter Queue อาจเหมาะกว่า; หากแค่ transient failure, bounded retry with backoff อาจเพียงพอ ทั้งนี้ขึ้นกับความต้องการ audit และวิธีปฏิบัติการ

## เทียบกับแนวทางใกล้เคียง

| แนวทาง | จุดเน้น | ประเด็นตัดสินใจ |
|---|---|---|
| Retry with Backoff | ลองใหม่อัตโนมัติเมื่อคาดว่าความล้มเหลวชั่วคราว | จำกัดจำนวนครั้งและหลีกเลี่ยง retry storm |
| Dead Letter Queue | แยกข้อความจาก broker ที่ประมวลผลไม่ได้ | retention, tooling และขั้นตอน redrive |
| Quarantine Table | เก็บสถานะ/ข้อมูลเพื่อ triage และ workflow ที่ควบคุมได้ | เหมาะเมื่อจำเป็นต้อง query, audit หรือแก้ก่อน reprocess |

## คำถามก่อนนำไปใช้

- ความผิดพลาดชนิดใดควร retry อัตโนมัติ และชนิดใดควร quarantine ทันที?
- จะป้องกันผลข้างเคียงซ้ำจากการประมวลผลเดิมอย่างไร?
- ใครมีสิทธิ์แก้และสั่ง reprocess? ต้องมี approval หรือ audit ระดับใด?
- จะกำหนด retention, encryption และการลบข้อมูลอย่างไร?
- จะจัดการกับรายการที่ยังล้มเหลวหลัง reprocess อย่างไร?

## แหล่งที่มาและความเชื่อมโยง

- จุดเริ่มต้นของการสำรวจนี้มาจากสิ่งที่ผู้ใช้อ่านใน “JCM3” แต่ชื่อดังกล่าวยังระบุแหล่งไม่ได้ จึงไม่ใช้เป็นหลักฐานของข้อสรุป ดู [รายการแหล่งอ้างอิง](../references.md)
- [บันทึกวิจัยจากเอกสารทางการ](../../../research/2026-10-30-reliability-patterns-quarantine-reprocessing.md) — เปรียบเทียบ Retry, DLQ, Quarantine และ Outbox
- [[Pattern Catalog]] — เปรียบเทียบกับ Retry, Dead Letter Queue และ Idempotent Consumer
