
> สถานะ: ร่าง — ตรวจสอบแหล่งอ้างอิงและทดลองใช้กับกรณีศึกษาก่อนกำหนดเป็นแนวทางมาตรฐาน  
> ประเภท: Tool Index / Discovery Method Catalog  
> Parent Note: [[inbox/domain-discovery-toolkit/overview |Domain Discovery Toolkit - Overview]]

## วัตถุประสงค์

Tool Catalog เป็นดัชนีกลางสำหรับค้นหา เปรียบเทียบ และเข้าถึงเครื่องมือหรือกิจกรรมที่ใช้ในการสำรวจ Business Domain

Catalog นี้ช่วยตอบคำถาม 4 ข้อ:

1. เรากำลังพยายามค้นหาหรือทำความเข้าใจอะไร?
    
2. มีเครื่องมือใดที่เหมาะกับช่องว่างความรู้นั้น?
    
3. เครื่องมือแต่ละตัวให้ผลลัพธ์อะไร และมีข้อจำกัดอย่างไร?
    
4. หลังจากได้ผลลัพธ์แล้ว ควรดำเนินการอะไรต่อ?
    

Catalog ทำหน้าที่เป็นดัชนีและข้อมูลสำหรับการเลือก Tool ไม่ใช่คู่มือดำเนิน Workshop ฉบับเต็ม รายละเอียดของแต่ละเครื่องมืออยู่ใน Tool Profile ที่เชื่อมโยงไว้

## 1. Catalog Overview

| ID    | Tool / Technique           | ประเภท                           | คำถามหลักที่ช่วยตอบ                                             | Profile                        |
| ----- | -------------------------- | -------------------------------- | --------------------------------------------------------------- | ------------------------------ |
| DD-01 | Big Picture Event Storming | Collaborative Workshop           | ภาพรวมธุรกิจมีเหตุการณ์อะไรเกิดขึ้น และเชื่อมโยงกันอย่างไร?     | [[Big Picture Event Storming]] |
| DD-02 | Domain Storytelling        | Visual Discovery Technique       | ผู้เกี่ยวข้องทำอะไร ใช้หรือส่งต่ออะไร และทำงานร่วมกันอย่างไร?   | [[Domain Storytelling]]        |
| DD-03 | Process Modeling           | Modeling Activity                | กิจกรรม การตัดสินใจ และเส้นทางของกระบวนการเป็นอย่างไร?          | [[Process Modeling]]           |
| DD-04 | Example Mapping            | Rule Discovery Technique         | กฎทางธุรกิจมีอะไร และมีตัวอย่างใดช่วยยืนยันความเข้าใจ?          | [[Example Mapping]]            |
| DD-05 | Impact Mapping             | Goal and Outcome Mapping         | เป้าหมายคืออะไร ใครมีอิทธิพล และต้องการให้เกิดการเปลี่ยนแปลงใด? | [[Impact Mapping]]             |
| DD-06 | Subdomain Classification   | Strategic DDD Analysis Activity  | ปัญหาทางธุรกิจแบ่งเป็นส่วนใด และส่วนใดสำคัญเชิงกลยุทธ์?         | [[Subdomain Classification]]   |
| DD-07 | Context Mapping            | Strategic DDD Modeling Technique | Bounded Contexts สัมพันธ์และพึ่งพากันอย่างไร?                   | [[Context Mapping]]            |

**ข้อสังเกต:** รายการนี้มีทั้ง Workshop, Technique และ Analysis Activity ไม่ได้หมายความว่าทุกข้อเป็นเครื่องมือในความหมายเดียวกัน ส่วน Process Modeling เป็นชื่อกิจกรรมในภาพรวม ซึ่งต้องเลือกวิธีหรือ Notation ที่เหมาะสมก่อนใช้งานจริง

## 2. Tool Selection Matrix

ใช้ตารางนี้เป็นจุดเริ่มต้นในการเลือก Tool โดยพิจารณาจากสิ่งที่ยังไม่รู้ ไม่ใช่จากลำดับของรายการใน Catalog

|เมื่อพบสถานการณ์นี้|Tool ที่ควรพิจารณา|เหตุผล|
|---|---|---|
|ยังไม่เข้าใจ Business Flow โดยรวม|Big Picture Event Storming|สำรวจและเรียงลำดับ Business Events ร่วมกัน|
|เข้าใจภาพรวมไม่พอที่จะอธิบายงานจริงของผู้เกี่ยวข้อง|Domain Storytelling|เล่าและแสดงกิจกรรมในสถานการณ์จริงผ่าน Actors, Activities และ Work Objects|
|ต้องเข้าใจลำดับกิจกรรม เงื่อนไข การแตกแขนง หรือข้อยกเว้น|Process Modeling|แสดงโครงสร้างของกระบวนการในระดับที่ต้องการ|
|มีกฎหรือข้อกำหนดที่กำกวมและต้องการตัวอย่างประกอบ|Example Mapping|เชื่อมโยง Rules, Examples และ Questions|
|เป้าหมายของโครงการหรือการเปลี่ยนแปลงที่ต้องการยังไม่ชัด|Impact Mapping|เชื่อมโยง Goal, Actors, Impacts และ Deliverables|
|เข้าใจธุรกิจพอที่จะจำแนกส่วนของ Problem Space|Subdomain Classification|วิเคราะห์ Core, Supporting และ Generic Subdomains|
|พอเห็นขอบเขตของ Context แล้ว แต่ยังไม่เข้าใจความสัมพันธ์ระหว่างกัน|Context Mapping|แสดงความสัมพันธ์และรูปแบบการพึ่งพาระหว่าง Bounded Contexts|

รายละเอียดอ้างอิงเพิ่มเติม: [EventStorming](https://www.eventstorming.com/resources/), [Domain Storytelling](https://domainstorytelling.org/quick-start-guide), [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/), [Impact Mapping](https://www.impactmapping.org/drawing.html) และ [Context Mapper](https://contextmapper.org/docs/language-reference/)

## 3. Tool Profiles

### DD-01 — Big Picture Event Storming

**วัตถุประสงค์:** สำรวจภาพรวมของ Business Domain ผ่าน Business Events และลำดับความสัมพันธ์ของเหตุการณ์ เพื่อให้ผู้เกี่ยวข้องสร้างความเข้าใจร่วมกัน

**เหมาะเมื่อ**

- ยังไม่เข้าใจภาพรวมของธุรกิจ
    
- ข้อมูลจาก TOR หรือ Requirements ยังไม่แสดง Business Flow ชัดเจน
    
- มีหลายบทบาทหรือหลายหน่วยงานที่มองกระบวนการแตกต่างกัน
    

**Input:** ความรู้จากผู้เกี่ยวข้อง ข้อมูลโครงการ และกระบวนการปัจจุบันที่ทราบ

**Expected Output**

- Business Event Timeline
    
- ภาพรวม Business Flow
    
- Hotspots และคำถามที่ยังเปิดอยู่
    
- ข้อมูลสำหรับการสำรวจ Domain ในขั้นต่อไป
    

**แนวทางต่อไป:** Process Modeling, Example Mapping หรือ Strategic DDD ตามช่องว่างความรู้ที่เหลือ

**Profile:** [[Big Picture Event Storming]]

**Sources:** [EventStorming — Official Resources](https://www.eventstorming.com/resources/)

### DD-02 — Domain Storytelling

**วัตถุประสงค์:** ทำความเข้าใจการทำงานจริงของ Domain ผ่านเรื่องเล่าจากผู้เกี่ยวข้อง โดยบันทึก Actors, Activities และ Work Objects ด้วยภาษาภาพที่อ่านตามลำดับได้

**เหมาะเมื่อ**

- ต้องการทำความเข้าใจสถานการณ์จริงในงานประจำ
    
- ยังไม่ชัดว่าใครเป็นผู้ทำกิจกรรมใดและใช้ข้อมูลหรือสิ่งของอะไร
    
- ต้องการสำรวจคำศัพท์และความเข้าใจร่วมกันจากเรื่องเล่าที่เป็นรูปธรรม
    

**Input:** สถานการณ์จริงหรือกรณีการทำงานที่มีขอบเขตชัดเจน และผู้ที่มีประสบการณ์ในสถานการณ์นั้น

**Expected Output**

- Domain Story Diagram
    
- Actors, Activities และ Work Objects
    
- ลำดับกิจกรรมและข้อยกเว้นที่พบ
    
- คำศัพท์และคำถามเพิ่มเติม
    

**แนวทางต่อไป:** Big Picture Event Storming หากต้องการภาพรวมที่กว้างขึ้น หรือ Process Modeling หากต้องการวิเคราะห์โครงสร้างกระบวนการเพิ่มเติม

**Profile:** [[Domain Storytelling]]

**Sources:** [Domain Storytelling — Quick-Start Guide](https://domainstorytelling.org/quick-start-guide)

### DD-03 — Process Modeling

**วัตถุประสงค์:** สร้างแบบจำลองกระบวนการเพื่ออธิบายลำดับกิจกรรม การตัดสินใจ เงื่อนไข เส้นทางทางเลือก และการส่งต่องาน

**เหมาะเมื่อ**

- ต้องการรายละเอียดมากกว่าภาพรวม Business Flow
    
- ต้องวิเคราะห์กรณีปกติและกรณียกเว้น
    
- ต้องการตรวจสอบขั้นตอนที่ขาดหายหรือความไม่ชัดเจนในการทำงาน
    

**Input:** Business Flow, Use Cases, Domain Stories หรือข้อมูลกระบวนการที่มีอยู่

**Expected Output**

- Process Diagram
    
- ลำดับกิจกรรมและจุดตัดสินใจ
    
- เส้นทางทางเลือกและข้อยกเว้น
    
- คำถามหรือ Business Rules ที่ต้องตรวจสอบเพิ่มเติม
    

**ข้อควรระวัง:** Process Modeling เป็นกิจกรรมกว้าง ไม่ใช่ Notation เดียว ต้องเลือกวิธีที่เหมาะกับวัตถุประสงค์ หากใช้ EventStorming Process Modeling ควรอ้างอิงรูปแบบนั้นโดยตรง

**แนวทางต่อไป:** Example Mapping เมื่อพบกฎที่ต้องเจาะลึก หรือกลับไปตรวจสอบกับผู้เกี่ยวข้องเมื่อกระบวนการยังไม่ชัดเจน

**Profile:** [[Process Modeling]]

**Sources:** [EventStorming — Official Resources](https://www.eventstorming.com/resources/)

### DD-04 — Example Mapping

**วัตถุประสงค์:** สำรวจและทำความเข้าใจ Rules ผ่าน Examples พร้อมแยกคำถามที่ยังไม่ได้คำตอบ เพื่อลดความกำกวมก่อนนำข้อกำหนดไปพัฒนาหรือทดสอบ

**เหมาะเมื่อ**

- Business Rule ยังคลุมเครือ
    
- ผู้เกี่ยวข้องเข้าใจเงื่อนไขไม่ตรงกัน
    
- ต้องการตรวจสอบเงื่อนไขด้วยสถานการณ์ตัวอย่าง
    

**Input:** Requirement, User Story หรือคำถามเฉพาะที่ต้องการทำความเข้าใจ

**Expected Output**

- Rules
    
- Examples ที่อธิบาย Rules
    
- Questions ที่ยังเปิดอยู่
    
- ขอบเขตงานหรือประเด็นที่ต้องแยกไปสำรวจเพิ่ม
    

**แนวทางต่อไป:** ปรับปรุง Requirements หรือ Acceptance Criteria และนำ Questions ที่ยังไม่ชัดเจนไปตรวจสอบเพิ่มเติม

**Profile:** [[Example Mapping]]

**Sources:** [Cucumber — Example Mapping](https://cucumber.io/docs/bdd/example-mapping/)

### DD-05 — Impact Mapping

**วัตถุประสงค์:** เชื่อมโยงเป้าหมายของธุรกิจกับผู้ที่มีอิทธิพล การเปลี่ยนแปลงพฤติกรรมที่ต้องการ และ Deliverables ที่อาจสนับสนุนเป้าหมายนั้น

**เหมาะเมื่อ**

- ยังไม่เข้าใจเหตุผลหรือผลลัพธ์ที่โครงการต้องการ
    
- ต้องการตรวจสอบว่าข้อกำหนดหรือ Features เชื่อมโยงกับเป้าหมายอย่างไร
    
- ต้องการตั้งคำถามกับสมมติฐานก่อนกำหนดขอบเขต Solution
    

**Input:** Business Goal, ปัญหาที่ต้องการแก้ และข้อมูลเกี่ยวกับผู้เกี่ยวข้อง

**Expected Output**

- Impact Map
    
- Goals, Actors, Impacts และ Deliverables
    
- สมมติฐานและประเด็นที่ต้องตรวจสอบ
    
- แนวทางจัดลำดับความสำคัญของงาน
    

**ข้อควรระวัง:** Impact Mapping ช่วยสำรวจเป้าหมายและผลลัพธ์ ไม่ได้แทนการค้นหา Business Events หรือ Business Rules โดยตรง จึงถือเป็นเครื่องมือสนับสนุน Domain Discovery มากกว่าจะใช้แทน Event Storming

**Profile:** [[Impact Mapping]]

**Sources:** [Impact Mapping — Drawing Impact Maps](https://www.impactmapping.org/drawing.html)

### DD-06 — Subdomain Classification

**วัตถุประสงค์:** วิเคราะห์การแบ่ง Problem Space ออกเป็นส่วนย่อย และประเมินความสำคัญเชิงกลยุทธ์ของแต่ละส่วน

**เหมาะเมื่อ**

- มีความเข้าใจ Business Domain ในระดับหนึ่งแล้ว
    
- ต้องการทำความเข้าใจว่าส่วนใดสร้างความแตกต่างให้ธุรกิจ
    
- ต้องพิจารณาว่าควรลงทุนพัฒนาส่วนใดเอง และส่วนใดอาจใช้โซลูชันทั่วไปได้
    

**Input:** Business Goals, Business Capabilities, Business Flow และข้อมูลเกี่ยวกับความสามารถที่สร้างคุณค่าของธุรกิจ

**Expected Output**

- รายการ Subdomains
    
- การจำแนก Core, Supporting และ Generic
    
- เหตุผลและสมมติฐานที่รองรับการจำแนก
    
- ประเด็นสำหรับการสำรวจ Bounded Contexts ต่อไป
    

**ข้อควรระวัง:** Subdomain Classification เป็นกิจกรรมวิเคราะห์เชิงกลยุทธ์ ไม่ใช่ Workshop ที่มีรูปแบบเดียวตายตัว และการแบ่ง Subdomain ไม่ได้กำหนด Bounded Context ให้ตรงกันโดยอัตโนมัติ

**Profile:** [[Subdomain Classification]]

**Sources:** [SAP — Curated Resources for Domain-Driven Design](https://github.com/SAP/curated-resources-for-domain-driven-design/blob/main/blog/0002-core-concepts.md)

### DD-07 — Context Mapping

**วัตถุประสงค์:** สำรวจและบันทึกความสัมพันธ์ระหว่าง Bounded Contexts เพื่อทำความเข้าใจการพึ่งพา รูปแบบความสัมพันธ์ และผลกระทบจากการเปลี่ยนแปลงข้ามขอบเขต

**เหมาะเมื่อ**

- มีสมมติฐานเกี่ยวกับ Bounded Contexts แล้ว
    
- ต้องเข้าใจว่าแต่ละ Context เชื่อมต่อหรือพึ่งพา Context อื่นอย่างไร
    
- ต้องวิเคราะห์การประสานงานระหว่างทีม หรือการเชื่อมต่อระหว่างระบบ
    

**Input:** Bounded Context Candidates, ความรับผิดชอบของแต่ละ Context และข้อมูลเกี่ยวกับการแลกเปลี่ยนข้อมูลหรือความสามารถ

**Expected Output**

- Context Map
    
- ความสัมพันธ์ระหว่าง Contexts
    
- ขอบเขตการพึ่งพาและการเชื่อมต่อ
    
- ประเด็นเชิงองค์กรหรือเชิงเทคนิคที่ต้องตัดสินใจเพิ่มเติม
    

**ข้อควรระวัง:** Context Map ที่ดีต้องสะท้อนความสัมพันธ์ที่มีหลักฐานหรือมีการระบุว่าเป็นสมมติฐาน ไม่ควรสร้างขอบเขตจากชื่อโมดูลหรือโครงสร้างฐานข้อมูลเพียงอย่างเดียว

**Profile:** [[Context Mapping]]

**Sources:** [Context Mapper — Strategic DDD Patterns](https://contextmapper.org/docs/language-reference/)

## 4. Heuristic Discovery Flow

แผนภาพนี้เป็นแนวทางช่วยตัดสินใจ ไม่ใช่ลำดับบังคับ ทุกขั้นสามารถข้ามหรือย้อนกลับได้ตามข้อมูลที่มี

1. **Clarify Goals** — ใช้ Impact Mapping เมื่อเป้าหมายหรือผลลัพธ์ที่ต้องการยังไม่ชัด
    
2. **Explore Domain Flow** — ใช้ Big Picture Event Storming เมื่อจำเป็นต้องสร้างภาพรวม Business Events หรือ Domain Storytelling เมื่อจำเป็นต้องเข้าใจกิจกรรมจริงของผู้เกี่ยวข้อง
    
3. **Zoom Into Processes** — ใช้ Process Modeling เมื่อต้องเข้าใจลำดับกิจกรรม เงื่อนไข และเส้นทางต่าง ๆ
    
4. **Clarify Rules** — ใช้ Example Mapping เมื่อมี Rules หรือ Requirements ที่ยังคลุมเครือ
    
5. **Analyze Problem Space** — ใช้ Subdomain Classification เมื่อมีหลักฐานเพียงพอที่จะจำแนกส่วนต่าง ๆ ของ Domain
    
6. **Explore Context Relationships** — ใช้ Context Mapping เมื่อมี Bounded Context Candidates และต้องการวิเคราะห์ความสัมพันธ์ระหว่างกัน
    

ก่อนเลือกขั้นตอนต่อไป ให้ประเมินความรู้ที่มีอยู่และผลลัพธ์ที่ต้องการเสมอ หากคำถามได้รับคำตอบและผ่านการตรวจสอบแล้ว ไม่จำเป็นต้องทำ Tool เพิ่มเพียงเพราะอยู่ในรายการถัดไป

## 5. Selection Rules

- เลือก Tool จาก Knowledge Gap ที่ต้องการแก้ ไม่ใช่จากลำดับใน Catalog
    
- หากข้อมูลมีเพียงพอแล้ว ให้ข้าม Tool ที่ไม่เพิ่มคุณค่าต่อการตัดสินใจ
    
- หากมีคำถามหลายประเภท ให้เลือก Tool ที่ตอบคำถามสำคัญที่สุดก่อน หรือใช้หลาย Tool ร่วมกันเมื่อจำเป็น
    
- แยกข้อค้นพบที่ผ่านการตรวจสอบแล้วออกจากสมมติฐานและคำถามที่ยังเปิดอยู่
    
- ใช้ Output ของ Tool ก่อนหน้าเป็น Input สำหรับ Tool ถัดไปได้ แต่ต้องประเมินความเหมาะสมของข้อมูลก่อนเสมอ
    
- ไม่ถือว่า Diagram เป็นข้อเท็จจริงของธุรกิจจนกว่าจะได้รับการตรวจสอบจากหลักฐานหรือผู้เกี่ยวข้องที่เหมาะสม
    

**แหล่งอ้างอิงหลักของเกณฑ์การเลือก:** [[Tool Selection Policy]]

## 6. คำถามที่ยังเปิดอยู่

- ควรเพิ่ม Business Capability Mapping หรือเครื่องมือสำรวจอื่นใน Catalog ตั้งแต่รุ่นแรกหรือไม่?
    
- จะกำหนดเกณฑ์ขั้นต่ำว่า Business Flow เข้าใจชัดเจนเพียงพอแล้วอย่างไร?
    
- จะวัดคุณภาพของ Tool Selection อย่างไร โดยไม่บังคับให้ทุกกรณีต้องได้ Tool ตัวเดียวกัน?
    
- จะจัดการกรณีที่ Tool หลายตัวเหมาะสมกับช่องว่างความรู้เดียวกันอย่างไร?
    
- จะกำหนดหลักฐานขั้นต่ำที่จำเป็นก่อนจำแนก Subdomains และ Bounded Contexts อย่างไร?
    

## 7. Next Steps

1. สร้าง Tool Profiles สำหรับ Tools ที่มีความจำเป็นต่อการทดลองรอบแรก
    
2. จัดทำ Selection Policy ให้เป็นแหล่งอ้างอิงหลักของกฎการเลือก
    
3. เพิ่มตัวอย่าง Diagram และ Expected Outputs ที่เชื่อมโยงกับแต่ละ Profile
    
4. ทดลองเลือก Tool จาก TOR หรือกรณีศึกษาที่มีช่องว่างความรู้แตกต่างกัน
    
5. ปรับปรุง Catalog และ Policy ตามผลการทดลอง ก่อนนำไปใช้ควบคุม AI Agent อย่างจริงจัง