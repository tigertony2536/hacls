# Domain Discovery Toolkit: ภาพรวม

> สถานะ: ร่างใน inbox — ตรวจสอบข้อเท็จจริงและแหล่งอ้างอิงก่อนนำไปใช้เป็นแนวทาง  
> ประเภท: Knowledge Base / Tool Selection System / Discovery Playbook

## สรุป

**Domain Discovery Toolkit** คือชุดความรู้และแนวทางสำหรับช่วย Developer หรือ AI Agent สำรวจ Business Domain และเลือกใช้เครื่องมือที่เหมาะสมกับสถานการณ์อย่างมีเหตุผล

เป้าหมายไม่ใช่การบังคับให้ทุกโครงการทำ Domain-Driven Design (DDD) หรือ Workshop ทุกประเภทตามลำดับตายตัว แต่เป็นการระบุว่าโครงการยังขาดความเข้าใจเรื่องใด ควรใช้เครื่องมือใดเพื่อค้นหาคำตอบ และผลลัพธ์ที่ได้เพียงพอสำหรับการตัดสินใจขั้นต่อไปหรือไม่

Toolkit ประกอบด้วย 3 ส่วนสำคัญ:

1. **Tool Knowledge Base** — คลังข้อมูลของเครื่องมือแต่ละตัว รวมถึงคุณสมบัติ คำศัพท์ วิธีใช้งาน ข้อจำกัด และตัวอย่างผลลัพธ์
    
2. **Tool Selection System** — กลไกประเมินช่องว่างความรู้และเลือกเครื่องมือผ่าน Selection Policy และ Decision Tree
    
3. **Discovery Execution & Evaluation** — แนวทางดำเนินการ บันทึกผลลัพธ์ ตรวจสอบคุณภาพ และตัดสินใจว่าจะสำรวจอะไรต่อ
    

สำหรับการใช้งานกับ AI Agent สามารถใช้ Skill เป็นตัวควบคุมกระบวนการเลือกเครื่องมือ และแยก Tool Profiles, Policies, Playbooks และ Examples ออกเป็นเอกสารอ้างอิง เพื่อให้ความรู้สามารถนำกลับมาใช้ซ้ำข้ามโครงการได้

หลักการสำคัญคือ **เลือกเครื่องมือตามช่องว่างความรู้และการตัดสินใจที่ต้องการรองรับ ไม่ใช่เลือกตามลำดับขั้นตอนที่กำหนดไว้ล่วงหน้า**

## ขอบเขต

### ครอบคลุม

- การระบุช่องว่างความรู้เกี่ยวกับ Business Domain จาก TOR, Requirements และข้อมูลที่มีอยู่
- การรวบรวมและเปรียบเทียบเครื่องมือสำหรับ Domain Discovery
- การกำหนด Tool Profiles ที่มี Properties, Terms, Example Artifacts, Usage Guidelines และ Exit Criteria
- การสร้าง Tool Catalog, Selection Policy, Decision Tree และ Discovery Workflow
- การเชื่อมโยงเครื่องมือที่เกี่ยวข้อง และกำหนดเงื่อนไขการส่งต่อระหว่างเครื่องมือ
- การจัดทำ Output Templates, Example Artifacts และเกณฑ์ตรวจสอบผลลัพธ์
- การนำ Toolkit ไปใช้ผ่าน AI Agent Skills และการประเมินคุณภาพการเลือกเครื่องมือ
- การบันทึกสมมติฐาน คำถามที่ยังเปิดอยู่ และประเด็นที่ต้องตรวจสอบกับผู้รู้ Domain

### ไม่ครอบคลุม

- การบังคับใช้ DDD แบบครบทุกขั้นตอนในทุกโครงการ
- การแทนที่ความรู้และการยืนยันข้อเท็จจริงจาก Domain Experts
- การถือว่า Diagram หรือตัวอย่างใน Toolkit เป็นข้อสรุปของธุรกิจจริงโดยอัตโนมัติ
- การกำหนด Solution Architecture, Database Schema หรือ API Contract โดยตรงจากผลลัพธ์ Domain Discovery
- การสร้าง Decision Engine แบบเขียนโปรแกรมตั้งแต่เริ่มต้น หาก Skill และเอกสารอ้างอิงยังตอบโจทย์ได้
- การรับรองว่า Tool ใด Tool หนึ่งสามารถค้นพบ Domain Model หรือ Bounded Context ที่ถูกต้องได้โดยลำพัง

## แนวคิดหลัก

### 1. Tool Knowledge Base

รวบรวมข้อมูลเกี่ยวกับเครื่องมือแต่ละตัวในรูปแบบมาตรฐาน เพื่อให้ทั้ง Developer และ Agent เข้าใจวัตถุประสงค์ ขอบเขต และวิธีใช้งานได้ตรงกัน

Tool Profile ควรประกอบด้วย:

- Properties — วัตถุประสงค์ ขอบเขต Input, Output และข้อจำกัด
- Terms & Concepts — คำศัพท์ที่จำเป็นต่อการใช้เครื่องมือ
- Example Artifact — ตัวอย่าง Diagram หรือผลลัพธ์ที่เสร็จแล้ว
- Usage Guidelines — เมื่อใดควรใช้ เมื่อใดไม่ควรใช้ และวิธีใช้งาน
- Common Mistakes — ข้อผิดพลาดที่พบบ่อย
- Exit Criteria — เกณฑ์ที่ใช้พิจารณาว่าผลลัพธ์เพียงพอแล้วหรือไม่
- Related Tools และ References — เครื่องมือที่เกี่ยวข้องและแหล่งอ้างอิง

โน้ตย่อย:

- [[Tool Catalog]]
- [[Tool Profile Specification]]
- [[Terms and Concepts Glossary]]
- [[Example Artifacts Library]]

### 2. Tool Selection System

กลไกเลือกเครื่องมือต้องเริ่มจากการวิเคราะห์สถานการณ์และช่องว่างความรู้ ไม่ใช่เริ่มจากการเลือก Tool ตัวแรกในรายการ

องค์ประกอบสำคัญ:

- **Selection Policy** — แหล่งอ้างอิงหลักของเกณฑ์และเงื่อนไขการเลือก Tool
- **Decision Tree** — ภาพสรุปเส้นทางการเลือก Tool ตามสถานการณ์
- **Tool Catalog** — ดัชนีสำหรับค้นหาและเปรียบเทียบเครื่องมือ
- **Domain Tool Selector Skill** — คำสั่งให้ Agent ประเมินบริบท เลือก Tool พร้อมให้เหตุผล และตรวจสอบผลลัพธ์

ควรหลีกเลี่ยงการเขียนกฎชุดเดียวกันซ้ำในหลายเอกสาร โดยกำหนดให้ Selection Policy เป็นแหล่งอ้างอิงหลัก ส่วน Decision Tree เป็นภาพสรุปของกฎเหล่านั้น

โน้ตย่อย:

- [[Tool Selection Decision Tree]]
- [[Tool Selection Policy]]
- [[Domain Tool Selector Skill]]

### 3. Discovery Workflow

Workflow แสดงภาพรวมของการทำงานตั้งแต่รับข้อมูลโครงการจนถึงตัดสินใจขั้นต่อไป

1. Assess Input — ประเมินข้อมูลและความรู้ Domain ที่มีอยู่
2. Identify Knowledge Gaps — ระบุสิ่งที่ยังไม่เข้าใจหรือยังตัดสินใจไม่ได้
3. Select Tool — พิจารณา Tool Profiles และ Selection Policy
4. Execute Discovery — ดำเนินการตาม Usage Guidelines หรือ Playbook
5. Evaluate Output — ตรวจสอบผลลัพธ์เทียบกับ Exit Criteria
6. Decide Next Step — ระบุว่าควรสำรวจต่อ เปลี่ยน Tool หรือหยุดเมื่อบรรลุเป้าหมายแล้ว

Workflow นี้เป็นวงจรที่ย้อนกลับไปสำรวจเพิ่มเติมได้ ไม่ใช่กระบวนการแบบเส้นตรงที่ต้องทำทุกขั้นตอนเสมอไป

โน้ตย่อย:

- [[Domain Discovery Workflow]]
- [[Discovery Playbook]]
- [[Output Quality and Exit Criteria]]
- [[Tool Handoff Rules]]

### 4. Initial Tool Set

ชุดเครื่องมือเริ่มต้นควรครอบคลุมปัญหาการค้นพบ Domain ที่แตกต่างกัน โดยไม่จำเป็นต้องรวบรวมทุกแนวคิดของ DDD ตั้งแต่แรก

|Tool / Technique|วัตถุประสงค์หลัก|
|---|---|
|Big Picture Event Storming|สำรวจภาพรวม Business Events และ Business Flow|
|Domain Storytelling|สำรวจปฏิสัมพันธ์ระหว่างผู้เกี่ยวข้อง กิจกรรม และระบบ|
|Process Modeling|วิเคราะห์ลำดับกิจกรรม การตัดสินใจ และเส้นทางของกระบวนการ|
|Example Mapping|สำรวจ Business Rules, Examples และ Questions|
|Strategic DDD|วิเคราะห์ Subdomains และ Bounded Contexts|
|Context Mapping|สำรวจความสัมพันธ์ระหว่าง Bounded Contexts|

รายการนี้เป็นชุดเริ่มต้นสำหรับการศึกษาและทดลองใช้งาน ไม่ใช่รายการบังคับ และเครื่องมือแต่ละตัวมีขอบเขตกับระดับรายละเอียดต่างกัน

โน้ตย่อย:

- [[Big Picture Event Storming]]
- [[Domain Storytelling]]
- [[Process Modeling]]
- [[Example Mapping]]
- [[Strategic DDD]]
- [[Context Mapping]]

### 5. Output, Quality และ Evaluation

Toolkit ต้องช่วยให้ผู้ใช้ตรวจสอบได้ว่า การเลือก Tool และผลลัพธ์ที่ได้มีประโยชน์ต่อการตัดสินใจจริงหรือไม่

สิ่งที่ควรจัดเตรียม:

- Output Templates สำหรับบันทึกผลลัพธ์จากแต่ละ Tool
- Example Artifacts ที่ผ่านการตรวจสอบความถูกต้องในบริบทตัวอย่าง
- Exit Criteria สำหรับกำหนดเงื่อนไขความเพียงพอของผลลัพธ์
- Assumptions & Uncertainty Log สำหรับเก็บคำถามและสมมติฐานที่ยังไม่ได้รับการยืนยัน
- Evaluation Cases สำหรับทดสอบว่า Agent เลือก Tool ได้เหมาะสมกับสถานการณ์หรือไม่
- Versioning & Changelog สำหรับติดตามการเปลี่ยนแปลงของ Profiles และ Policies

โน้ตย่อย:

- [[Discovery Output Templates]]
- [[Assumptions and Uncertainty Log]]
- [[Tool Selection Evaluation]]
- [[Toolkit Versioning]]

## คำถามที่ยังเปิดอยู่

- จะใช้ Markdown เป็นรูปแบบหลักทั้งหมดในระยะแรก หรือควรมี YAML/JSON Metadata สำหรับค้นหาและกรอง Tools ตั้งแต่ต้น?
- เกณฑ์ใดใช้ประเมินว่า Knowledge Gap มีนัยสำคัญเพียงพอที่จะต้องใช้ Tool เพิ่มเติม?
- จะจำแนก Tool, Technique, Workshop, Framework และ Analysis Activity อย่างไรให้ไม่ปะปนกัน?
- Tool Cards ควรมีรายละเอียดระดับใดจึงเพียงพอสำหรับ Agent โดยไม่สร้างภาระในการดูแลรักษามากเกินไป?
- จะตรวจสอบความถูกต้องของ Profiles, Examples และ Decision Policies จากแหล่งอ้างอิงใด?
- จะสร้าง Evaluation Cases แบบใดเพื่อทดสอบว่า Agent เลือก Tool ตามบริบท ไม่ใช่เลือกตามลำดับที่คุ้นเคย?
- เมื่อ Tool Selection Skill ไม่สามารถตัดสินใจได้อย่างมั่นใจ ควรกำหนดให้ Agent สำรวจข้อมูลเพิ่ม เสนอทางเลือก หรือขอคำตอบจากผู้ใช้ในกรณีใดบ้าง?
- จะจัดการความรู้ที่นำไปใช้ซ้ำข้ามโครงการ โดยแยกหลักการทั่วไปออกจาก Business Rules ของแต่ละโครงการอย่างไร?

## Next Steps

1. กำหนด Tool Profile Specification ให้เป็นรูปแบบกลาง
    
2. สร้าง Tool Catalog และ Selection Policy ฉบับแรก
    
3. ทำ Big Picture Event Storming เป็น Tool Profile ตัวอย่าง พร้อม Example Artifact และ Usage Guidelines
    
4. ทดลองใช้ Tool Selector กับกรณีศึกษาอย่างน้อย 2–3 สถานการณ์ที่มีช่องว่างความรู้แตกต่างกัน
    
5. ปรับปรุง Selection Policy และเพิ่ม Evaluation Cases จากผลการทดลอง