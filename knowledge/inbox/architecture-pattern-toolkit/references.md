# Architecture Pattern Toolkit: แหล่งอ้างอิง

> **สถานะความรู้:** Inbox — แหล่งต่อไปนี้ตรวจแล้วสำหรับแนวคิด retry, DLQ, outbox, Saga และ CQRS; รายละเอียดเฉพาะของ JCM3 ยังไม่ทราบ

## แหล่งที่ตรวจแล้ว

### Retry pattern

- **ผู้เผยแพร่:** Microsoft Learn / Azure Architecture Center
- **ประเภท:** เอกสาร architecture pattern
- **URL:** https://learn.microsoft.com/th-th/azure/architecture/patterns/retry
- **วันที่เข้าถึง:** 2026-10-30
- **เกี่ยวข้องกับ:** ความผิดพลาดชั่วคราว กลยุทธ์ retry แบบมีขอบเขต การหน่วงเวลา และ trade-off
- **สถานะการตรวจ:** ตรวจแล้ว — ใช้ประกอบการเปรียบเทียบ Retry กับการพักรายการเพื่อกู้คืน

### Transient fault handling

- **ผู้เผยแพร่:** Microsoft Learn / Azure Architecture Center
- **ประเภท:** แนวทางออกแบบระบบ
- **URL:** https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults
- **วันที่เข้าถึง:** 2026-10-30
- **เกี่ยวข้องกับ:** retry limit, backoff, jitter และ dead-letter เมื่อ retry หมด
- **สถานะการตรวจ:** ตรวจแล้ว — ใช้ประกอบข้อควรระวังเรื่อง retry storm และงานที่ล้มเหลวต่อเนื่อง

### Service Bus dead-letter queues

- **ผู้เผยแพร่:** Microsoft Learn
- **ประเภท:** เอกสารผลิตภัณฑ์
- **URL:** https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues
- **วันที่เข้าถึง:** 2026-10-30
- **เกี่ยวข้องกับ:** เหตุผลที่ข้อความเข้าสู่ DLQ การเก็บและการนำข้อความกลับมาจัดการ
- **สถานะการตรวจ:** ตรวจแล้ว — ใช้เป็นตัวอย่าง DLQ ระดับ broker ไม่ใช่นิยามกลางของ Quarantine Table

### Configure SQS dead-letter queue redrive

- **ผู้เผยแพร่:** AWS Documentation
- **ประเภท:** เอกสารผลิตภัณฑ์
- **URL:** https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue-redrive.html
- **วันที่เข้าถึง:** 2026-10-30
- **เกี่ยวข้องกับ:** การ redrive ข้อความจาก SQS DLQ
- **สถานะการตรวจ:** ตรวจแล้ว — ใช้ประกอบความหมายของการนำข้อความกลับเข้าคิว

### Transactional Outbox with Cosmos DB

- **ผู้เผยแพร่:** Microsoft Learn / Azure Architecture Center
- **ประเภท:** แนวทาง architecture
- **URL:** https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos
- **วันที่เข้าถึง:** 2026-10-30
- **เกี่ยวข้องกับ:** การบันทึก state และ event อย่าง atomic และการส่งต่อด้วย background worker
- **สถานะการตรวจ:** ตรวจแล้ว — ใช้แยกหน้าที่ Outbox ออกจาก DLQ/quarantine

### Transactional Outbox Pattern with Dataverse

- **ผู้เผยแพร่:** Microsoft Learn
- **ประเภท:** เอกสาร reference architecture
- **URL:** https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/transactional-outbox-pattern
- **วันที่เข้าถึง:** 2026-10-30
- **เกี่ยวข้องกับ:** at-least-once delivery, consumer idempotency และ monitoring
- **สถานะการตรวจ:** ตรวจแล้ว — ใช้รองรับข้อควรระวังเรื่อง duplicate เมื่อ reprocess

### Saga และ CQRS

- **ผู้เผยแพร่:** Microsoft Learn / Azure Architecture Center
- **ประเภท:** เอกสาร architecture pattern
- **URL:** https://learn.microsoft.com/en-us/azure/architecture/microservices/design/patterns และ https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
- **วันที่เข้าถึง:** 2026-10-30
- **เกี่ยวข้องกับ:** ตัวอย่าง pattern อื่นใน catalog และ trade-off ของ distributed workflows/read-write separation
- **สถานะการตรวจ:** ตรวจแล้วในระดับภาพรวม — ควรอ่านแยกก่อนเขียน profile ราย pattern

## บันทึกการสังเคราะห์

เอกสารอ้างอิงส่วนใหญ่เป็นแนวทางหรือเอกสารผลิตภัณฑ์จากผู้เผยแพร่โดยตรง ไม่ใช่มาตรฐานสากล การจัดประเภทและเกณฑ์เลือกในโน้ตเป็นการสังเคราะห์จากแหล่งเหล่านี้ โปรดดู [บันทึกวิจัย](../../../research/2026-10-30-reliability-patterns-quarantine-reprocessing.md)
