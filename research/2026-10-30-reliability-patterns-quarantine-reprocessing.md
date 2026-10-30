# Research: Quarantine, reprocessing และ pattern ความน่าเชื่อถือที่เกี่ยวข้อง

> **สถานะ:** สังเคราะห์จากเอกสารทางการของผู้ให้บริการ วันที่ค้นคว้า 2026-10-30
> **ขอบเขต:** ตรวจแนวคิดการพักงานที่ประมวลผลไม่สำเร็จ การลองซ้ำ/นำกลับมาประมวลผล และ pattern ที่เกี่ยวข้อง ไม่ได้ตรวจระบบเฉพาะที่ผู้ใช้เรียกว่า “JCM3”

## สรุปข้อค้นพบ

1. **Retry เหมาะกับความผิดพลาดชั่วคราวที่มีโอกาสหายเอง** ไม่ควรลองซ้ำข้อผิดพลาดถาวรหรือ business logic error ควรกำหนดจำนวนครั้ง/ช่วงเวลา จำกัด และพิจารณา exponential backoff กับ jitter เพื่อไม่ให้หลาย instance ยิงซ้ำพร้อมกัน [Microsoft: Retry pattern](https://learn.microsoft.com/th-th/azure/architecture/patterns/retry), [Microsoft: transient faults](https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults)
2. **DLQ เป็นกลไกเก็บข้อความที่ส่งมอบหรือประมวลผลไม่ได้ในระบบ broker** เพื่อให้ตรวจสอบและ resubmit/redrive ภายหลังได้ Azure Service Bus เก็บข้อความไว้จนกว่าจะนำออกและจัดการเอง จึงต้องมีแผน retention และการปฏิบัติการ [Microsoft: Service Bus DLQ](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues), [AWS: SQS redrive](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue-redrive.html)
3. **Quarantine Table ไม่ได้ปรากฏเป็นชื่อมาตรฐานเดียวที่มีนิยามกลางในเอกสารที่ตรวจ** แต่สามารถออกแบบเป็นกลไกใน application/data layer สำหรับเก็บรายการผิดพลาดที่ต้อง query, triage, audit หรือแก้ก่อน replay ได้ ลักษณะนี้อาจทับซ้อนกับ DLQ ในเป้าหมาย แต่รูปแบบ storage, ownership และ workflow ต่างกันตามระบบ. นี่เป็นข้อสังเคราะห์จากเอกสารด้าน DLQ และ outbox ไม่ใช่ข้ออ้างว่ามีมาตรฐานชื่อ “Quarantine Table” [Microsoft: Service Bus DLQ](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues), [Microsoft: Transactional Outbox](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)
4. **การ reprocess ต้องรองรับ duplicate/side effects**: outbox ให้การส่งแบบ at-least-once ในตัวอย่าง Microsoft และเอกสารแนะนำ consumer แบบ idempotent; การ replay จึงต้องกำหนด idempotency key/deduplication หรือวิธีชดเชยให้ชัด [Microsoft: Transactional Outbox with Dataverse](https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/transactional-outbox-pattern), [Microsoft: Transactional Outbox with Cosmos DB](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)
5. **Outbox แก้ปัญหา dual-write ระหว่าง business state กับ event** โดยบันทึกทั้งคู่ใน transaction เดียว แล้วส่ง event ด้วย worker แยกต่างหาก ไม่ใช่รูปแบบเดียวกับ quarantine: outbox เก็บงานส่งออกที่ยังต้องเผยแพร่ ส่วน quarantine/DLQ เก็บงานที่ประมวลผลหรือส่งมอบไม่สำเร็จ [Microsoft: Transactional Outbox](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)
6. **Saga** ใช้จัดการ workflow หลาย local transactions ข้าม service พร้อม compensating transactions เมื่อขั้นตอนล้มเหลว; **CQRS** แยก read/write models เพื่อรองรับความต้องการที่ต่างกัน แต่เพิ่มความซับซ้อนและอาจเกิด eventual consistency. ทั้งคู่ควรเลือกจากข้อกำหนดจริง ไม่ใช่เพิ่มเพราะเป็น pattern ที่รู้จัก [Microsoft: Saga overview](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/patterns), [Microsoft: CQRS](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)

## ตารางช่วยแยกหน้าที่

| กลไก | ใช้เมื่อ | จุดที่ต้องออกแบบ |
|---|---|---|
| Retry | ความผิดพลาดชั่วคราวและการทำซ้ำมีโอกาสสำเร็จ | error classification, finite attempts, timeout, backoff/jitter, idempotency |
| Dead Letter Queue | ข้อความใน broker เกินจำนวน delivery/retry หรือแปรรูปไม่ได้ | reason/metadata, retention, monitoring, inspect/resubmit/redrive |
| Quarantine Table | ต้องเก็บงานผิดพลาดใน storage ของแอปและมี workflow triage/query/control | schema/version, payload protection, operator workflow, state transitions, replay controls |
| Transactional Outbox | ต้องบันทึก business change และ event อย่าง atomic ก่อนส่งออก | relay, ordering, duplicate delivery, cleanup/retention |

ตารางนี้เป็น heuristic สังเคราะห์จากเอกสารที่อ้าง ไม่ใช่ข้อกำหนดของผลิตภัณฑ์หรือมาตรฐานอุตสาหกรรม

## เกณฑ์เลือกเบื้องต้น

- แยก transient failure ออกจาก permanent/data/business error ก่อนกำหนด retry policy.
- หากงานเพียงรอ dependency กลับมา ให้พิจารณา retry แบบจำกัดและ backoff; หาก retry หมดแล้วยังต้องเก็บเพื่อกู้คืน ให้ใช้ DLQ หรือ quarantine ตามความต้องการ query/audit และเครื่องมือที่มี.
- หากต้องคุมการแก้ข้อมูลหรืออนุมัติก่อน reprocess, application-managed quarantine อาจให้ workflow เหมาะกว่า broker DLQ แต่จะเพิ่มภาระ schema, security, retention และการปฏิบัติการ.
- ออกแบบการทำซ้ำให้ปลอดภัย: idempotency key, deduplication record หรือ compensating action ต้องเลือกตาม semantics ของงาน.
- วัด backlog depth, อายุรายการที่เก่าที่สุด, จำนวน retry, DLQ/quarantine count, สาเหตุ และผลลัพธ์ reprocess เพื่อให้รู้ว่าระบบกำลังกู้คืนหรือสะสมงานค้าง.

## หมายเหตุเรื่อง “JCM3”

บริบทที่ได้รับมีเพียงชื่อ “JCM3” โดยไม่มี URL, ชื่อบทความ, ผู้เขียน หรือชื่อระบบเต็ม การค้นชื่อดังกล่าวร่วมกับคำว่า quarantine/reprocess ไม่พบแหล่งต้นทางที่ยืนยันได้ว่าตรงกับ pattern นี้ จึงยังเชื่อมโยงไม่ได้และไม่ควรใช้อ้างอิงข้อเท็จจริง ผลค้นมีหลายความหมายที่ไม่เกี่ยวข้อง จึงไม่ควรเดาว่าเป็นแหล่งใด หากได้ลิงก์หรือชื่อเต็ม จะตรวจว่าคำอธิบายและตัวอย่างใน JCM3 รองรับข้อสรุปส่วนใดได้บ้าง

## แหล่งต้นทางที่ตรวจ

- Microsoft Learn, [Retry pattern](https://learn.microsoft.com/th-th/azure/architecture/patterns/retry) — เงื่อนไขใช้ retry, cancel, backoff และ logging.
- Microsoft Learn, [Transient fault handling](https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults) — error classification, bounded retries, jitter, retry storm และ idempotency.
- Microsoft Learn, [Service Bus dead-letter queues](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues) — DLQ purpose, reason, manual retrieval/resubmit, retention.
- AWS Documentation, [Configure SQS dead-letter queue redrive](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue-redrive.html) — redrive task APIs.
- Microsoft Learn, [Transactional Outbox with Cosmos DB](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos) — atomic state/event persistence and background relay.
- Microsoft Learn, [Transactional Outbox with Dataverse](https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/transactional-outbox-pattern) — at-least-once delivery, idempotent consumers and monitoring considerations.
- Microsoft Learn, [Microservices design patterns](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/patterns) — Saga and related patterns.
- Microsoft Learn, [CQRS pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs) — when to use CQRS, trade-offs and eventual consistency.
