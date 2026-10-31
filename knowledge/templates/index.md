# ดัชนี template

รหัสต่อไปนี้ใช้อ้างอิง **ชนิดของเอกสาร** และ template ที่เกี่ยวข้อง ไม่ใช่รหัสประจำเอกสาร

| รหัส | ชนิดเอกสาร | ใช้เมื่อ | Template | ตำแหน่งปลายทางแนะนำ |
|---|---|---|---|---|
| `DOC` | เอกสารโครงการ | บันทึกขอบเขต แนวคิด หลักการ หรือการวางแผนโครงการ | [เอกสารโครงการ](docs/project-document.md) | `docs/` |
| `RES` | รายงานวิจัย | ตั้งคำถาม ค้นคว้า สังเคราะห์หลักฐาน และบันทึกข้อจำกัด | [รายงานวิจัย](research/report.md) | `research/` |
| `KIDX` | ดัชนีหัวข้อความรู้ | นำทางระหว่างภาพรวม โน้ต และแหล่งอ้างอิงของหัวข้อ | [ดัชนีหัวข้อ](knowledge/topic-index.md) | `knowledge/{inbox,validated,canonical}/<topic>/index.md` |
| `KOV` | ภาพรวมความรู้ | สรุปความเข้าใจปัจจุบันของหัวข้อจากโน้ตและแหล่งข้อมูล | [ภาพรวม](knowledge/overview.md) | `knowledge/{inbox,validated,canonical}/<topic>/overview.md` |
| `KNOTE` | โน้ตความรู้รายประเด็น | อธิบายแนวคิดหนึ่งประเด็นที่เชื่อมโยงกับโน้ตอื่นได้ | [โน้ตรายประเด็น](knowledge/note.md) | `knowledge/{inbox,validated,canonical}/<topic>/notes/<slug>.md` |
| `KREF` | รายการแหล่งอ้างอิง | รวบรวมและติดตามแหล่งข้อมูลที่ใช้กับหัวข้อความรู้ | [แหล่งอ้างอิง](knowledge/references.md) | `knowledge/{inbox,validated,canonical}/<topic>/references.md` |

ตำแหน่งปลายทางในตารางอ้างอิงจาก repo root ส่วนวงเล็บปีกกาในตำแหน่งปลายทางหมายถึงเลือกโฟลเดอร์ตามสถานะความรู้จริง: `inbox`, `validated` หรือ `canonical` ดูวิธีคัดลอกและปรับ template ที่ [README](templates/README.md)
