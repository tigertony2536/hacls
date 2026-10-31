<!-- Type: RES | Document type: Research report -->
# ทักษะที่จำเป็นสำหรับการทำ Proof of Concept (PoC)

- **วันที่:** 2026-10-30
- **สถานะ:** ตรวจแล้ว

## คำถามและเหตุผล

- คำถาม: ผู้ทำ PoC ในช่วงวิเคราะห์ความเป็นไปได้ควรมีทักษะและทำกิจกรรมอะไรบ้าง?
- เหตุผล: ใช้กำหนดขอบเขตการทดลองและประเมินว่าควรเดินหน้าพัฒนา หยุด หรือกลับไปค้นคว้าเพิ่มเติม
- ขอบเขต: สังเคราะห์ทักษะเชิงปฏิบัติสำหรับ PoC ทั่วไปในงานระบบดิจิทัล โดยอาศัยแนวทางทางการจาก Microsoft และ GOV.UK; ไม่ใช่หลักสูตรฝึกอบรมหรือมาตรฐาน SDLC สากล

## วิธีค้นคว้า

ค้นหาและตรวจเอกสารทางการของ Microsoft Learn และ GOV.UK Service Manual ซึ่งอธิบายการกำหนดเป้าหมาย/ขอบเขต PoC การทดลองสมมติฐาน และเกณฑ์ตัดสินใจ ใช้หน้าเอกสารของเจ้าของแนวทางโดยตรง ไม่อ้างบทความสรุปจากบุคคลที่สาม

## ข้อค้นพบ

### หลักฐานจากแหล่งข้อมูล

- Microsoft แนะนำให้กำหนดวัตถุประสงค์และขอบเขต PoC ให้ชัด ระบุข้อมูลที่จะใช้ สภาพแวดล้อม วิธีสาธิต เกณฑ์สำเร็จ และเงื่อนไขที่ถือว่าล้มเหลว พร้อมสื่อสารว่า PoC ยังไม่ใช่ระบบ production [Microsoft Learn: Power BI implementation planning](https://learn.microsoft.com/en-us/power-bi/guidance/powerbi-implementation-planning-bi-strategy-bi-solution-planning).
- Microsoft ระบุว่า PoC ใช้ตรวจสมมติฐานที่ยังค้างและเปิดเผยความซับซ้อนที่อาจไม่เห็นจากการออกแบบทางเทคนิค และเตือนว่าข้อมูลตัวอย่างขนาดเล็กอาจใช้สรุปเรื่อง performance หรือ data quality ไม่ได้ [Microsoft Learn: Power BI implementation planning](https://learn.microsoft.com/en-us/power-bi/guidance/powerbi-implementation-planning-bi-strategy-bi-solution-planning).
- GOV.UK แนะนำให้ช่วง alpha ใช้ prototype ทดลองแนวทางและสมมติฐานที่เสี่ยง โดยทำเฉพาะส่วนที่จำเป็นต่อการทดสอบ ไม่จำเป็นต้องทำทั้งบริการ และให้พิจารณาข้อจำกัดด้านกฎหมาย สัญญา เทคโนโลยีเดิม และผู้มีส่วนเกี่ยวข้อง [GOV.UK Service Manual: How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works).
- GOV.UK ระบุว่าการตัดสินใจไปขั้น beta ควรอาศัยตัวชี้วัดความสำเร็จที่กำหนดไว้ และความมั่นใจว่าทำได้ตามความต้องการผู้ใช้โดยคุ้มค่า รวมถึงมีงบประมาณและบุคลากรเพียงพอ หากยังไม่มั่นใจก็อาจหยุดหรือย้อนกลับไปทำ discovery/alpha [GOV.UK Service Manual: How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works).
- Microsoft แนะนำให้ใช้ sandbox แยกสำหรับ PoC และเตือนว่าโค้ด PoC อาจไม่มี security, logging หรือ error handling ครบ จึงไม่ควรถือเป็น production-ready [Microsoft Learn: Power BI implementation planning](https://learn.microsoft.com/en-us/power-bi/guidance/powerbi-implementation-planning-bi-strategy-bi-solution-planning), [Azure Well-Architected Framework: Collaborate with workload and platform teams](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/collaboration).

### การสังเคราะห์

จากหลักฐานข้างต้น ทักษะที่ผู้ทำ PoC ควรมีหรือจัดให้มีในทีม ได้แก่:

1. **ตีโจทย์และระบุสมมติฐาน** — อธิบายปัญหา/ความต้องการ แล้วเขียนคำถามที่ PoC ต้องตอบให้ตรวจสอบได้ เช่น “เชื่อมต่อระบบต้นทางได้ภายในข้อจำกัดนี้หรือไม่” แนวทางนี้สอดคล้องกับการระบุเป้าหมายและทดสอบสมมติฐานที่ยังไม่คลี่คลาย (เป็นการสังเคราะห์จากคำแนะนำเรื่อง goals, scope และ assumptions ในแหล่งอ้างอิงด้านบน)
2. **จัดลำดับความเสี่ยงและจำกัดขอบเขต** — เลือกความเสี่ยงหรือส่วนที่ไม่แน่นอนที่สุด แล้วทำต้นแบบเพียงเท่าที่จำเป็นเพื่อให้ได้คำตอบ แทนการสร้างระบบครบถ้วน (อนุมานจากคำแนะนำของ GOV.UK ให้ทดสอบส่วนที่ท้าทาย/สมมติฐานเสี่ยง และของ Microsoft ให้จำกัด functional scope)
3. **ออกแบบการทดลองและเกณฑ์วัดผล** — กำหนดข้อมูล สภาพแวดล้อม วิธีทดลอง ตัวชี้วัด เกณฑ์ผ่าน/ไม่ผ่าน และเวลาสิ้นสุดก่อนเริ่ม เพื่อให้ผลนำไปสู่การตัดสินใจได้ (สังเคราะห์จาก checklist ของ Microsoft)
4. **สร้างต้นแบบทางเทคนิคแบบพอดีโจทย์** — มีความสามารถพอจะทดสอบ end-to-end หรือจุดเสี่ยงเฉพาะ แต่แยก sandbox และเข้าใจว่าส่วนใดเป็นข้อจำกัดของต้นแบบ (สังเคราะห์จากแนวทาง PoC ของ Microsoft)
5. **ประเมินข้อจำกัดนอกตัวโค้ด** — ตรวจ dependency, integration, ข้อมูล, กฎหมาย/สัญญา, เทคโนโลยีเดิม, ผู้ใช้และผู้ปฏิบัติงาน รวมถึงต้นทุนและทรัพยากรที่ต้องใช้ต่อ (อนุมานจากข้อจำกัดและปัจจัยความคุ้มค่า/ความพร้อมที่ GOV.UK ระบุ)
6. **วิเคราะห์ผลและสื่อสารการตัดสินใจ** — บันทึกสิ่งที่พิสูจน์ได้ สิ่งที่ยังพิสูจน์ไม่ได้ ข้อจำกัด และข้อเสนอว่าจะเดินหน้า ปรับแนวทาง หรือหยุด พร้อมนำเสนอแก่ผู้ตัดสินใจ (สังเคราะห์จากเกณฑ์การสาธิตและการตัดสินใจของทั้งสองแหล่ง)
7. **ตระหนักเรื่องความปลอดภัยและคุณภาพ** — ใช้ข้อมูลและสภาพแวดล้อมอย่างเหมาะสม และไม่ตีความต้นแบบที่ข้าม controls ว่าใช้จริงได้; ก่อนนำไป production ต้องพัฒนาใหม่หรือยกระดับตามมาตรฐานวิศวกรรมของทีม (Microsoft ระบุชัดว่า PoC อาจขาด security/logging/error handling)

ดังนั้น PoC อาจเป็นกิจกรรมใน feasibility analysis เมื่อคำถามคือ “แนวทางนี้ทำได้จริงและคุ้มค่าพอหรือไม่” แต่การทำ PoC ไม่ได้จำกัดอยู่เฉพาะช่วงนั้น เอกสาร Microsoft วาง PoC ไว้หลังการออกแบบทางเทคนิคและใช้ต่อเนื่องก่อนการพัฒนาเป็นทางการ จึงควรพิจารณาตามคำถามและความเสี่ยงที่ต้องลดในแต่ละโครงการ (ข้อสรุปส่วนหลังเป็นการอนุมานจากลำดับกิจกรรมในเอกสาร ไม่ใช่กฎ SDLC กลาง) [Microsoft Learn: Power BI implementation planning](https://learn.microsoft.com/en-us/power-bi/guidance/powerbi-implementation-planning-bi-strategy-bi-solution-planning).

## ข้อจำกัดและสิ่งที่ยังไม่ทราบ

- แหล่งข้อมูลเป็นแนวทางทางการของผู้ให้บริการ/หน่วยงาน ไม่ใช่การทบทวนงานวิจัยเปรียบเทียบ และรายละเอียดอาจต้องปรับตามอุตสาหกรรม ความเสี่ยง หรือวงจร SDLC ขององค์กร
- คำว่า “ทักษะ” ในรายงานนี้หมายถึงความสามารถ/กิจกรรมที่ทีมต้องครอบคลุม ไม่ได้แปลว่าทุกคนต้องทำได้ครบทุกด้าน
- การประเมิน feasibility ของผลิตภัณฑ์จริงยังอาจต้องมีทักษะเฉพาะโดเมน เช่น privacy, security, performance, accessibility หรือ financial analysis ตามบริบท

## แหล่งอ้างอิง

- Microsoft. “Power BI implementation planning: BI solution planning.” เข้าถึงเมื่อ 2026-10-30. https://learn.microsoft.com/en-us/power-bi/guidance/powerbi-implementation-planning-bi-strategy-bi-solution-planning
- Microsoft. “Collaborate with workload and platform teams.” Azure Well-Architected Framework. เข้าถึงเมื่อ 2026-10-30. https://learn.microsoft.com/en-us/azure/well-architected/architect-role/collaboration
- Government Digital Service. “How the alpha phase works.” GOV.UK Service Manual. เข้าถึงเมื่อ 2026-10-30. https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works
