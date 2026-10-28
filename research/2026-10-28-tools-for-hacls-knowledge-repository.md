# เครื่องมือสำหรับ HACLS: คลังความรู้ที่ Agent ใช้ร่วมกัน

วันที่ค้นคว้า: 28 ตุลาคม 2026  
คำถาม: มีเครื่องมือใดรองรับแนวทาง HACLS ได้ครบ หรือควรประกอบเครื่องมืออย่างไร และมีต้นทุนดูแลรักษาเท่าใด?

## สรุป

**ทำได้ด้วยเครื่องมือที่มีอยู่ แต่ไม่พบเครื่องมือเดียวที่ให้วงจรทั้งหมดตามที่ตกลงไว้โดยไม่ต้องกำหนดกระบวนการเอง** แนวทางที่เหมาะกับช่วงเริ่มต้นคือใช้ Git repository และ Markdown เป็นฐานข้อมูลและประวัติการเปลี่ยนแปลง, ใช้ Pull Request (PR) เป็นช่องทางตรวจรับ, จัด `skills/` ตาม Agent Skills format, และเก็บชุดทดสอบของ Agent ใน `experiments/` ก่อนเลือก evaluation runner เมื่อมี skill ที่ต้องประเมินจริง

แนวทางนี้มีต้นทุนบำรุงรักษา **ต่ำในระยะแรกถึงปานกลางเมื่อคลังโตขึ้น** หากเริ่มจาก Markdown, ดัชนีที่แก้ด้วยมือ และ PR review เท่านั้น ต้นทุนจะเพิ่มจากลิงก์เสีย, ดัชนีไม่ทันเนื้อหา, taxonomy/frontmatter ไม่สม่ำเสมอ และการรัน evaluation ที่ต้องใช้ model/API credentials หากรีบเพิ่มเว็บแอป, ฐานข้อมูล, MCP server, automation หรือ evaluation CI ตั้งแต่แรก จะเพิ่มภาระดูแลโดยยังไม่แก้ปัญหาหลักเรื่องการคัดเลือกความรู้

**สถานะ repo ขณะค้นคว้า:** ไดเรกทอรี `/Users/thanapat/Dev/hacls` ยังไม่ใช่ Git repository (`git status` แจ้งว่าไม่ใช่ repository) ดังนั้น Agent จาก repository อื่นยังดึงผ่าน remote ไม่ได้ จนกว่าจะ initialize Git และตั้ง remote ที่ Agent เหล่านั้นมีสิทธิ์อ่านได้ การแนะนำ Git ข้างล่างเป็น target setup ไม่ใช่ความสามารถที่เปิดใช้งานอยู่แล้ว

## เทียบกับข้อกำหนด

| ความต้องการ | เครื่องมือ/รูปแบบที่รองรับ | ข้อจำกัดและภาระดูแล |
|---|---|---|
| Agent จากโปรเจกต์อื่นดึงคลังกลางผ่าน Git | Git remote และ `clone`/`pull`; Git บันทึกประวัติเป็น commits และนำประวัติจาก remote มารวมได้ [Git merge](https://git-scm.com/docs/git-merge) | ผู้ใช้/Agent ต้องมีสิทธิ์เข้าถึง remote และต้องดึงเวอร์ชันล่าสุดเอง ไม่มีการซิงก์หรือแจ้งเตือนอัตโนมัติจาก Git เพียงอย่างเดียว |
| แยก inbox, validated, canonical และให้เจ้าของอนุมัติ | โฟลเดอร์และสถานะใน Markdown ร่วมกับ PR review, protected branch/rulesets และ CODEOWNERS บน GitHub [protected branches](https://docs.github.com/en/pull-requests/reference/branches), [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) | Git/GitHub ไม่ได้เข้าใจความหมายของสถานะ HACLS โดยอัตโนมัติ ต้องเขียนกติกาในคู่มือและตั้งสิทธิ์/กฎให้ถูก; ผู้ดูแลยังเป็นผู้ตัดสินเนื้อหา |
| ค้นหาความรู้โดยไม่อ่านทั้งคลัง | `README.md` หรือ `knowledge/INDEX.md` พร้อมลิงก์ Markdown; หากต้องการเว็บค้นหา สามารถสร้าง site ด้วย MkDocs จาก Markdown และกำหนด navigation/search [MkDocs docs](https://www.mkdocs.org/user-guide/writing-your-docs/), [configuration](https://www.mkdocs.org/user-guide/configuration/) | ดัชนีที่แก้มือมีต้นทุนเริ่มต้นต่ำแต่เสี่ยงล้าสมัย; MkDocs เพิ่ม dependency, config, build/deploy และต้องดูแล navigation แต่ยังใช้ Markdown ต้นฉบับเดิม |
| ใช้ความรู้ที่เรียนมาเป็น skill แบบพกพา | Agent Skills เป็นรูปแบบเปิด: directory มี `SKILL.md` พร้อม YAML `name`/`description` และอาจมี `references/`, `scripts/`, `assets/`; โหลดคำอธิบายเพื่อค้นพบและโหลดเนื้อหาเมื่อเปิดใช้ [specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx), [overview](https://github.com/agentskills/agentskills) | รูปแบบช่วยพกพาโครงสร้างและคำสั่ง แต่ไม่ได้ทำให้ทุก client รองรับเหมือนกันหรือรับประกันว่า agent จะทำตามได้ดี; ต้องทดสอบกับ client เป้าหมาย และเลี่ยงยัดความรู้ยาว ๆ ซ้ำใน skill |
| เชื่อม skill กับความรู้ที่รองรับ | ใส่ลิงก์ relative ไปยัง `knowledge/canonical/...` ใน `SKILL.md` หรือใน `references/`; ใช้ `metadata` เพิ่มรหัส/เวอร์ชันได้ตาม spec [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx) | ลิงก์ relative ใช้งานง่ายและอยู่ใน Git history แต่ต้องตรวจลิงก์/อัปเดตเมื่อย้ายไฟล์; สเปกไม่ได้กำหนด schema สำหรับ HACLS เช่น `source_ids` จึงต้องกำหนด convention เอง |
| เก็บสมมติฐาน วิธี ผล และเกณฑ์ของ experiments | Markdown/YAML ใน `experiments/`; ถ้าเป็นการทดสอบ output ของ LLM ใช้ Promptfoo ซึ่งเก็บ providers, prompts, tests และ assertions ใน config แล้วรัน eval [getting started](https://www.promptfoo.dev/docs/getting-started/), [assertions](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Promptfoo เหมาะกับการประเมิน output ที่ระบุ input/output และ assertions ได้ แต่ไม่ใช่ workflow อนุมัติความรู้; ต้องจัดการ dependency, provider/model changes, ค่าใช้ API และ credentials อย่างระมัดระวัง |
| ลดโอกาสเผย secrets | GitHub push protection ช่วยบล็อก secret ที่รู้จักก่อนเข้าคลัง และ Gitleaks ทำงานเป็น CLI, GitHub Action หรือ pre-commit hook [GitHub push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection), [Gitleaks](https://github.com/gitleaks/gitleaks) | การสแกนมีข้อจำกัดตามชนิด secret และขนาด push; ไม่แทนการทบทวนข้อมูลส่วนบุคคล/ข้อมูลลับในข้อความทั่วไป [ขอบเขตการตรวจ](https://docs.github.com/en/code-security/reference/secret-security/secret-scanning-scope) |

## ชุดเครื่องมือที่แนะนำ

### ระยะเริ่มต้น: ใช้ Git เป็นระบบหลัก

1. **Git และ remote ส่วนตัวหรือที่ควบคุมสิทธิ์ได้** เป็นแหล่งกลาง; ต้อง initialize repo และตั้ง remote ก่อน Agent จาก repo อื่นจึง clone/pull ได้ โดยใช้ Git CLI ปกติเป็นค่าเริ่มต้น ไม่ต้องมี GitHub MCP server เพื่ออ่านไฟล์/ดึงความรู้
2. **Markdown เป็นรูปแบบเนื้อหาหลัก** และแยกตำแหน่งตาม lifecycle ที่นิยามไว้: `knowledge/inbox/`, `validated/`, `canonical/` การเลื่อนสถานะคือการย้ายไฟล์พร้อม review ไม่ใช่การให้ Agent เขียนทับ canonical โดยตรง
3. **ดัชนีเริ่มต้นหนึ่งหน้า** (`README.md` หรือ `knowledge/INDEX.md`) ระบุวิธีเริ่มอ่าน, ความหมายสถานะ, วิธีเสนอความรู้, และลิงก์ตามหัวข้อ ไม่ต้องสร้าง search engine ในช่วงแรก
4. **PR เป็นจุดอนุมัติ**: ตั้งกฎห้ามเปลี่ยน default branch โดยตรง/ต้อง review และใช้ CODEOWNERS หาก Git host รองรับ เพื่อให้การเปลี่ยน knowledge/canonical และ skills ผ่านเจ้าของคลัง [GitHub branch protection](https://docs.github.com/en/pull-requests/reference/branches), [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
5. **`skills/` ใช้ Agent Skills format** เมื่อเนื้อหานั้นกลายเป็นขั้นตอนที่ Agent ควรทำซ้ำได้; ใน skill บอก trigger, ขั้นตอน, ขอบเขต/ข้อยกเว้น และอ้างอิงความรู้ canonical ด้วย path แบบ relative [Agent Skills spec](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
6. **ทดลองแบบเบา**: บันทึก test case และผลใน Markdown/ไฟล์ข้อมูลก่อน เมื่อเริ่มมี skill ที่ใช้ซ้ำและวัดผลได้ ค่อยพิจารณา Promptfoo สำหรับ assertions และการเปรียบเทียบ output [Promptfoo getting started](https://www.promptfoo.dev/docs/getting-started/)
7. **ความปลอดภัย**: ห้ามเก็บ credentials/secrets ตามนโยบายคลัง; เปิด push protection หาก Git host/แผนรองรับ หรือใช้ Gitleaks ในเครื่อง/CI เสริม [GitHub push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection), [Gitleaks](https://github.com/gitleaks/gitleaks)

### ส่วนเสริมเมื่อเริ่มมีแรงเสียดทาน

- **MkDocs** เมื่อการ browse ใน Git เริ่มไม่สะดวกหรือคลังมีคนใช้มากขึ้น: มันสร้าง static site จาก Markdown, รองรับ navigation และ full-text search ผ่าน config โดยไม่ต้องย้าย source of truth ออกจาก repo [MkDocs writing docs](https://www.mkdocs.org/user-guide/writing-your-docs/), [MkDocs configuration](https://www.mkdocs.org/user-guide/configuration/)
- **GitHub MCP** เป็นทางเลือกเฉพาะเมื่อ Agent รันอยู่ใน environment ที่ไม่สะดวกหรือไม่สามารถ clone repo ได้ และต้องเรียกค้น/อ่าน/สร้าง PR ผ่าน GitHub API/tool interface; ไม่จำเป็นสำหรับ Agent ที่มี filesystem และ Git CLI อยู่แล้ว การเพิ่ม MCP server/tool permission เพิ่ม integration และสิทธิ์ที่ต้องดูแล จึงควรเลือกจากข้อจำกัดของ client จริง ไม่ใช่เป็น dependency ของคลัง
- **Link/frontmatter validation ใน CI** เมื่อปัญหาดัชนีหรือลิงก์เสียเกิดซ้ำ: สร้าง checker ขนาดเล็กตาม convention HACLS แทนการนำระบบฐานข้อมูลมาใช้ก่อนจำเป็น
- **Promptfoo** เมื่อมีชุดงานซ้ำที่ตรวจด้วย assertions ได้; เหมาะกับ regression tests ขนาดเล็กสำหรับ outputs [Promptfoo assertions](https://www.promptfoo.dev/docs/configuration/expected-outputs/). **Inspect AI** ค่อยพิจารณาเมื่อจำเป็นต้องประเมิน agent หลายขั้นตอน/trajectory ด้วย dataset, solver และ scorer [Inspect overview](https://inspect.aisi.org.uk/), [tasks](https://inspect.aisi.org.uk/tasks). ไม่ควรเพิ่มทั้งสองตั้งแต่ต้น และอย่าถือคะแนน eval เป็นการอนุมัติ canonical โดยอัตโนมัติ
- **skills-ref** ตรวจ frontmatter/โครงสร้าง Agent Skills ได้ แต่ repo ของเครื่องมือระบุว่า reference library มีไว้สาธิต ไม่ใช่ production SDK จึงเหมาะเป็น lint เบื้องต้นเท่านั้น [skills-ref README](https://github.com/agentskills/agentskills/blob/main/skills-ref/README.md)

## Trade-offs

### สิ่งที่ได้

- **แหล่งความจริงเดียวและตรวจย้อนหลังได้**: เนื้อหา, skills, experiments และ ADR อยู่ใน version history เดียวกัน และเชื่อมกันด้วย path/link
- **ต้นทุนเริ่มต้นและการย้ายออกต่ำ**: plain text/Markdown อ่านได้โดยตรง ไม่ต้องใช้ service เฉพาะ; Agent ที่อ่าน filesystem/Git ได้ก็เข้าถึงได้
- **กระบวนการตรวจสอบมองเห็นได้**: diff และ PR แสดงว่าใครเปลี่ยนอะไรและเปิดให้แสดงความคิดเห็นก่อน merge; GitHub รองรับ branch rules และ required review [PR review concepts](https://docs.github.com/en/pull-requests/reference/pull-requests), [protected branches](https://docs.github.com/en/pull-requests/reference/branches)
- **ไม่ผูกความรู้ทั้งหมดกับ prompt**: Agent Skills มีการค้นพบ/โหลดคำสั่งแบบ on-demand และสามารถแนบ reference files ได้ [Agent Skills overview](https://github.com/agentskills/agentskills)

### สิ่งที่ต้องยอมรับ

- **ไม่มี workflow semantics สำเร็จรูป**: โฟลเดอร์ `inbox`/`validated`/`canonical` เป็น convention ของ HACLS เอง Git ไม่บังคับความหมายนี้; ต้องอาศัยคู่มือ, PR template/checklist และกฎ branch
- **การทำงานพร้อมกันมี conflict**: Git รวมการเปลี่ยนไฟล์คนละส่วนได้ แต่ไฟล์เดียวที่หลาย Agent แก้พร้อมกันอาจชนกันและต้อง resolve [git merge behavior](https://git-scm.com/docs/git-merge); แยกหนึ่งเรื่องต่อไฟล์และให้ Agent เสนอไฟล์ใหม่ช่วยลดความเสี่ยง
- **การค้นไม่ฉลาดเท่าฐานข้อมูลความหมาย**: ชื่อไฟล์, ดัชนี, full-text site search ทำได้ แต่ไม่รับประกันว่า Agent จะเลือกความรู้ถูกหรือไม่อ่านเนื้อหาล้าสมัย จึงต้องมี metadata `status`, `scope`, `source`, `supersedes` ที่สม่ำเสมอ
- **ความพกพาไม่ได้แปลว่าใช้งานได้เหมือนกันทุก Agent**: Agent Skills ทำให้รูปแบบไฟล์เป็นมาตรฐานเปิด แต่ client ยังต้อง implement การค้นพบ/โหลด และ tool/permission behavior อาจต่างกัน [specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
- **evaluation มีต้นทุนจริง**: ต้องดูแลตัวอย่างงาน, expected behavior, model/provider, และเกณฑ์; ผลจาก model grader อาจเปลี่ยนตาม model/config จึงควรบันทึกเวอร์ชันและตรวจตัวอย่างด้วยคน
- **การเปิดเผยคลังกับการรับข้อเสนอเป็นคนละสิทธิ์**: ให้ Agent อื่นอ่านได้ไม่จำเป็นต้องให้ write access; การเขียน inbox โดยตรงสะดวกแต่เพิ่มความเสี่ยง spam/ข้อมูลอ่อนไหว การให้เสนอผ่าน fork/PR ปลอดภัยและตรวจง่ายกว่า แต่มีขั้นตอนเพิ่ม

## ภาระบำรุงรักษา

| ระดับ | สิ่งที่ดูแล | ภาระโดยประมาณ |
|---|---|---|
| ต่ำ — แนะนำให้เริ่ม | README/index, template เอกสาร, โครงสร้างสถานะ, PR checklist, review โดยเจ้าของ, Git remote | ต่ำ: ส่วนใหญ่เป็นการเขียน/ทบทวนเนื้อหาและจัดหมวด |
| ปานกลาง | MkDocs, validation links/frontmatter, secret scanner/CI, test cases สำหรับ skills | ปานกลาง: ต้องอัปเดต dependencies/config และแก้ build/check failures แต่ตรวจปัญหาซ้ำได้อัตโนมัติ |
| สูง | custom portal/search API, MCP server, auto-ingestion จากหลาย agent, auto-promotion, vector database, dashboard/eval orchestration | สูง: มี application code, hosting/auth/permissions, sync/index freshness, schema migrations, monitoring และ incident handling; ไม่จำเป็นต่อเป้าหมายระยะแรก |

ข้อสรุปเรื่องภาระเป็น **การประเมินเชิงออกแบบ** จากจำนวนระบบและจุดบำรุงรักษาที่ต้องเพิ่ม ไม่ใช่ benchmark เชิงปริมาณจาก vendor

ในสถานะปัจจุบัน ขั้นแรกก่อนเริ่ม workflow ข้าม repo คือ initialize repository, commit โครงสร้าง/เอกสาร, สร้าง remote และกำหนดสิทธิ์อ่านให้ Agent ปลายทาง โดยเก็บ write access ไว้จำกัด หากใช้ GitHub ให้ตั้ง PR review/branch rules ก่อนให้ Agent เสนอแก้ `validated` หรือ `canonical`

## จุดที่ควรระวังในการออกแบบ

1. อย่ารวม “ความรู้ที่ถูกต้อง” กับ “คำสั่งให้ทำ” ในไฟล์เดียวกันโดยไม่แยกประเภท: knowledge อธิบายข้อเท็จจริง/ขอบเขต ส่วน skill ให้ขั้นตอนและชี้กลับไปยัง knowledge
2. ให้ Agent อ่าน index แล้วเลือกอ่าน canonical ที่เกี่ยวข้อง; `inbox` เป็นข้อเสนอ/หลักฐาน ไม่ใช่คำสั่งปฏิบัติงาน
3. ทุกความรู้ที่ย้ายเข้า `canonical` ควรมีแหล่งที่มา, ขอบเขตใช้ได้, วันที่ทบทวน/สถานะ และลิงก์ทดแทนเมื่อเลิกใช้; สิ่งเหล่านี้เป็น schema ของ HACLS ที่ต้องกำหนดเอง
4. เริ่มด้วย PR review ไม่เปิดสิทธิ์เขียนตรงลง canonical; GitHub PR ถูกออกแบบมาเพื่อให้ตรวจ/อภิปรายชุดการเปลี่ยนแปลงก่อนนำเข้า branch หลัก [pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests)
5. Secret scanner เป็นเพียง guardrail: GitHub ระบุข้อจำกัดของชนิด secret และขนาด push ที่ scan ได้ [secret scanning scope](https://docs.github.com/en/code-security/reference/secret-security/secret-scanning-scope) จึงยังต้องตรวจข้อมูลส่วนบุคคลและข้อความลับที่ไม่ใช่ token ด้วยคน

## ข้อเสนอแนะ

**เลือกแนวทาง Git + Markdown + PR + Agent Skills เป็นแกน แล้วค่อยเพิ่ม MkDocs และ evaluation tooling ตามหลักฐานการใช้งาน** ไม่มีเหตุจำเป็นทางเทคนิคให้เริ่มด้วยฐานข้อมูลหรือระบบ RAG สำหรับคลังที่เนื้อหายังจัดการด้วยไฟล์ได้ ข้อกำหนดที่ต้องสร้างเองจริง ๆ คือกติกาสถานะ/metadata, index, review checklist และแนวทางรับข้อเสนอจาก Agent

เกณฑ์บอกว่าควรเพิ่มระบบ: ผู้ใช้หาเนื้อหาไม่เจอบ่อย, ลิงก์/สถานะผิดซ้ำ, มีหลาย Agent เสนอพร้อมกันจน review เป็นคอขวด, หรือมี skill ที่ต้องเปรียบเทียบผลแบบทำซ้ำได้ หากยังไม่เกิดอาการเหล่านี้ การเพิ่มเครื่องมือจะเพิ่มงานดูแลมากกว่าประโยชน์

## แหล่งข้อมูลต้นทาง

- [Git: git-merge](https://git-scm.com/docs/git-merge) — การนำประวัติจาก commits/branch มารวมและการจัดการ conflict
- [GitHub Docs: Protected branches](https://docs.github.com/en/pull-requests/reference/branches) — required review, status checks, code owner approval และกฎ branch
- [GitHub Docs: CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) — การร้องขอ review จากเจ้าของไฟล์
- [GitHub Docs: Pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests) — PR สำหรับ review และหารือการเปลี่ยนแปลงก่อน merge
- [Agent Skills: Specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx) — โครงสร้าง skill, metadata และไฟล์ประกอบ
- [Agent Skills: Repository](https://github.com/agentskills/agentskills) — ภาพรวม format และ progressive disclosure
- [MkDocs: Writing your docs](https://www.mkdocs.org/user-guide/writing-your-docs/) — Markdown source, directory layout, navigation, internal links, metadata
- [MkDocs: Configuration](https://www.mkdocs.org/user-guide/configuration/) — การตั้งค่า site และ search
- [Promptfoo: Getting started](https://www.promptfoo.dev/docs/getting-started/) และ [Assertions & metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) — test cases/assertions สำหรับ eval output
- [GitHub Docs: Push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection) และ [secret scanning scope](https://docs.github.com/en/code-security/reference/secret-security/secret-scanning-scope) — การบล็อกและข้อจำกัดการตรวจ secret
- [Gitleaks repository](https://github.com/gitleaks/gitleaks) — CLI, GitHub Action และ pre-commit hook สำหรับตรวจ secret
- [skills-ref README](https://github.com/agentskills/agentskills/blob/main/skills-ref/README.md) — validator อ้างอิงและข้อจำกัดการใช้งาน
- [Inspect AI overview](https://inspect.aisi.org.uk/) และ [Tasks](https://inspect.aisi.org.uk/tasks) — กรอบประเมิน agent ด้วย task, solver และ scorer
