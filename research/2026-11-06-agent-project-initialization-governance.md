<!-- Type: RES | Document type: Research synthesis -->
# Research: Project Initialization, Rules, and Governance for Coding Agents

**วันที่:** 2026-11-06  
**สถานะ:** Research synthesis / ข้อเสนอ ยังไม่ใช่ canonical policy  
**คำถาม:** ก่อนเริ่มพัฒนา software ด้วย coding agent ควรออกแบบ rules, context, skills, constraints, permissions, quality gates และโครงสร้าง repo ด้วยวิธีคิดใด?  
**ขอบเขต:** แนวทาง coding agents (Codex, Claude Code, GitHub Copilot, Cursor) และข้อเสนอสำหรับโครงการ HACLS; ไม่ได้ benchmark หรือแก้ไข rules ที่บังคับใช้จริง

## Executive summary

**ข้อสรุปหลัก:** ไม่ใช่การสร้าง `AGENTS.md` ให้ครอบคลุมทุกอย่าง แต่เป็นการออกแบบ *working contract* ของคน-เอเจนต์ พร้อมระบบบังคับใช้และตรวจรับที่เหมาะกับความเสี่ยง โดยเริ่มจากข้อจำกัดที่สำคัญจริง แล้วจัดแต่ละเรื่องไว้ในกลไกที่ถูกต้อง

1. ข้อมูลที่จำเป็นเสมอ → root instructions สั้นและแม่นยำ เช่น `AGENTS.md` (เมื่อ tool รองรับ)
2. เรื่องเฉพาะ directory/ไฟล์ → path-scoped instructions หรือ nested instructions ตาม runtime
3. ความรู้เชิงลึก → docs/ADR/knowledge ที่ค้นและอ่าน *ตามความเกี่ยวข้อง*
4. ขั้นตอนซ้ำได้ที่มี input/process/output → task-specific Skill; ไม่บังคับทุก task ให้อ่าน
5. สิ่งที่ตรวจได้แบบ deterministic → formatter, linter, compiler, test, CI; **อย่าใช้ prompt เป็นตัวคุมหลัก**
6. การกระทำเสี่ยงหรือ irreversible → permissions, sandbox, credential/network boundaries, approval gates; **prompt ไม่ใช่ security boundary**
7. คุณภาพที่พิสูจน์ได้ → acceptance criteria + evidence จากการรันจริง + review + evaluation scenarios

หมวดหมู่เหล่านี้เป็นกรอบสังเคราะห์สำหรับ HACLS ไม่ใช่ชื่อ/มาตรฐานสากลตายตัว

## วิธีค้นคว้าและข้อจำกัด

อ่านเอกสารเจ้าของเทคโนโลยีโดยตรงจาก OpenAI Developers, Anthropic Claude Code, GitHub Docs, Cursor Docs และ agents.md และตรวจโครงสร้าง repo HACLS บน branch `dev` ผ่าน GitHub connector (2026-11-06) แยกข้อเท็จจริงของ platform ออกจากข้อเสนอการออกแบบตามบริบท

**ไม่ได้ทดลอง runtime / ไม่ได้ benchmark** ว่า layout ใดทำให้คุณภาพดีขึ้นเท่าใด; ไม่ยกตัวอย่างไฟล์เป็นมาตรฐานบังคับร่วมกันทุก agent. Feature support, instruction precedence และ hook behavior แตกต่างตามเครื่องมือและรุ่น

## หลักฐานจากผู้พัฒนาเครื่องมือ

| แหล่ง | สิ่งที่ตรวจพบ | นัยต่อการออกแบบ |
|---|---|---|
| [AGENTS.md](https://agents.md/) | ไฟล์ Markdown สำหรับบอก context, build/test และ conventions ให้ coding agent | ใช้เป็น README-for-agents ที่กระชับ ไม่ใช่สำเนา documentation ทั้ง repo |
| [Codex: Iterating Development Workflows](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex) | `AGENTS.md` เป็น optional, `GOALS.md`, `PLANS.md`, `PROMPTS.md`, `harness/` เป็น convention ตัวอย่าง ไม่ใช่ required files | กำหนด goal, plan, acceptance criteria, phase context ตามความจำเป็น อย่าคัดลอกทุกไฟล์โดยอัตโนมัติ |
| [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Skill มาก/description กว้างทำให้เลือกผิดหรือ context รก; ไม่ควรบังคับอ่านทุก doc ก่อนทุก edit | ทำ instructions minimal; references ใช้ on-demand; ระบุ trigger อย่างแคบ |
| [OpenAI: Custom Code Review Rules](https://developers.openai.com/blog/custom-code-review-rules-for-codex) | แนะนำ consequential/non-obvious invariant, narrow scope, safe path; formatter และ mechanical checks อยู่ CI | กฎที่ดีบอกความเสี่ยงและทางเลือกที่ถูก ไม่ใช่แค่ "เขียนโค้ดให้ดี" |
| [Claude Code Skills](https://code.claude.com/docs/en/skills) | Skill body โหลดเมื่อมีการใช้; `SKILL.md` สำหรับ procedure ซ้ำได้ | แยก workflow ออกจาก always-on instructions |
| [Claude Code Settings](https://code.claude.com/docs/en/settings) | Permissions/hooks/settings สามารถกำหนดตาม scope เครื่องมือ | แยก prose rules จาก machine-enforced settings |
| [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | รองรับ repository-wide, path-specific, agent instructions ตาม surface | ถ้าต้องใช้หลาย agent ต้องมี adapter/config แต่ละ platform ตาม compatibility จริง |
| [Cursor Project Rules](https://docs.cursor.com/context/rules-for-ai) | Project Rules สามารถ scoped ด้วย path และเลือก always/auto/manual/agent-requested | เลือกการโหลด context ตามความจำเป็น |
| [OpenAI Skills in API](https://developers.openai.com/cookbook/examples/skills_in_api) | Skill เหมาะกับ reusable conditional procedure; ไม่ใช่งาน one-off หรือ live side effect | อย่าเปลี่ยนทุก convention เป็น skill |
| [OpenAI Sandbox security](https://developers.openai.com/api/docs/guides/agents-api/environments/security) และ [Guardrails & Approvals](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) | ใช้ isolation, network/credential restrictions และ approvals เป็น control | ข้อห้ามใน prompt เป็นเพียง guidance ไม่ใช่ enforcement |
| [OpenAI Skill Evals](https://developers.openai.com/blog/eval-skills) | ควรตรวจ behavior จาก trace/ผลลัพธ์จริง ไม่ใช่เพียง final response | มี eval ของการเลือก skill/ทำตาม rule/verification |

## Framework: เริ่มคิดจากปัญหา ไม่ใช่รูปแบบไฟล์

### 1. Identify risk, then define invariant

ก่อนเขียน rule ให้ถามว่า *ถ้า agent ทำผิด จะเกิดผลเสียใด?* หากผลเสียน้อยและ tool ตรวจได้ ให้ใช้ automation; หากเป็น domain invariant หรือ decision ที่ตรวจจาก syntax ไม่ได้ ให้ใช้ scoped guidance และ tests/evidence

ตัวอย่าง:
- ความเสี่ยง: API เปลี่ยน response เดิมจน client พัง → invariant: ไม่เปลี่ยน published response shape โดยไม่มี compatibility plan → ทำ contract test + review rule
- ความเสี่ยง: route handler เรียก external database แบบ write โดยพลการ → invariant: external source เป็น read-only → enforce DB permission + architecture test + rule ที่อธิบาย ownership
- ความเสี่ยง: agent refactor เกิน scope → ขีดเส้น files/surfaces ที่แก้ได้, approval เมื่อขยายขอบเขต, และตรวจ diff ก่อนส่ง

### 2. Choose the mechanism

| ถ้าคำตอบคือ… | ใช้กลไกหลัก | ทำไม |
|---|---|---|
| "ต้องรู้เรื่องนี้ทุก task" | `AGENTS.md` / tool-specific global instructions | Always-on, short |
| "เฉพาะเมื่อทำ backend/frontend/migration" | nested/path rules | หลีกเลี่ยง irrelevant context |
| "ขั้นตอนเพื่อทำ Spike/DDD/Load Test" | `SKILL.md` + references/scripts | Reusable procedure, load on demand |
| "ข้อเท็จจริงของระบบหรือ rationale" | docs/ADR/knowledge | Source of truth, ไม่ต้อง inject ตลอด |
| "ตรวจ format/type/security/config ได้" | lint/test/CI/schema/permissions | Machine-verifiable enforcement |
| "ต้องเลือกขั้นตอนต่อไปของ SDLC" | orchestration / task plan / approval | Dynamic sequencing ไม่ใช่ standing code rule |
| "ต้องจำผลของงานนี้เพื่อใช้ต่อ" | task/phase context + decision log | Durable state, scoped to a work item |

### 3. Set scopes, responsibilities, and authority

แนะนำ 4 ระดับเป็น **ข้อเสนอ HACLS**: (A) reusable organizational baseline, (B) project-specific contract, (C) subsystem/path scope, (D) task/phase-specific instructions.

อย่า assume precedence ข้ามเครื่องมือ: Codex, Claude Code, Copilot และ Cursor โหลด rules ต่างวิธีกัน. ให้ inventory ที่มา/ความสำคัญของ rules และทดสอบ conflict resolution ใน target runtime แทนการถือว่า `AGENTS.md` override ทุกสิ่ง

### 4. Express rules as testable working agreements

Template สำหรับหนึ่ง rule:

- **Context / trigger:** ใช้เมื่อใด และกระทบพื้นที่ไหน
- **Risk / invariant:** สิ่งที่ต้องรักษา พร้อมเหตุผล
- **Required action / safe path:** ต้องทำอย่างไรและตัวเลือกที่ปลอดภัย
- **Verification:** จะพิสูจน์การปฏิบัติตามอย่างไร (test, command, review)
- **Exception / escalation:** ตอนไหนต้องถาม/ขออนุมัติ และใครมีอำนาจตัดสิน
- **Owner / review date (ถ้าคุ้มค่า):** ใครทบทวน rule เมื่อ codebase เปลี่ยน

ตัวอย่างกฎไม่ดี: "เขียนโค้ดสะอาด และอย่าแก้ของเก่า"  
ตัวอย่างกฎดีกว่า: "เมื่อแก้ public API ให้รักษา request/response contract ที่เผยแพร่แล้ว หรือเสนอ compatibility plan ก่อนทำ breaking change; รัน contract tests และแนบ diff/ผลการรันทดสอบ"

### 5. Design verification and controls separately

- Static gates: format, typecheck, lint, unit/integration/contract tests, secret scanning
- Dynamic gates: run service/app, ตรวจ observable behavior, replayable script/log/evidence
- Human gates: cross-boundary architecture, destructive operations, production deploy, irreversible migration
- Security controls: sandbox, restricted credentials, network access, branch protection, required review; ไม่ใช้ instruction text เป็นเส้นแบ่งความปลอดภัย

Agent ควรรายงาน **สิ่งที่รันจริง**, คำสั่ง/หลักฐาน, ข้อผิดพลาด, tests ที่ไม่ได้รันพร้อมเหตุผล และสิ่งที่ยังไม่ทราบ

### 6. Evaluate and refine

สร้างชุดกรณีใช้งานสั้น ๆ เช่น:
1. การแก้ typo ไม่ถูกบังคับอ่าน docs ทั้ง repo
2. การแก้ public API เจอ compatibility constraint และ test
3. การเปลี่ยน schema ใช้ migration procedure ที่ถูกต้อง
4. การแก้โค้ดธรรมดาไม่ trigger skill ที่ไม่เกี่ยวข้อง
5. ขอให้ deploy production โดยไม่มี approval → หยุดที่ boundary ที่กำหนด

ตรวจทั้ง rule adherence, noise/false positive, unintended edits, quality evidence และเวลาที่เสียไป; นำ lessons จาก PR/review มาเสนอปรับ rule ไม่ใช่เพิ่ม rule ทุกครั้งที่โมเดลพลาด

## Proposed minimum starter layout for a consumer development repo

```text
project/
├── AGENTS.md                       # concise, repo-wide working contract
├── README.md                       # human setup and overview
├── docs/
│   ├── architecture.md             # boundaries and context, read on demand
│   └── decisions/                  # decisions with rationale
├── .agents/
│   └── skills/                     # example portable skills location; adapt runtime
├── scripts/
│   └── verify.sh                   # repeatable local checks
├── tests/
└── .github/
    └── workflows/ci.yml            # enforce machine checks
```

**นี่คือ proposed structure ไม่ใช่ไฟล์ที่ agent ทุกค่ายอมรับเหมือนกัน**. หากใช้ Codex ให้ตรวจ convention และ discovery path ของเวอร์ชันจริง; Claude Code ใช้ `.claude/skills/` ได้; Copilot มี `.github/copilot-instructions.md` และ `.github/instructions/`; Cursor มี `.cursor/rules/`. เพิ่ม platform-specific adapter เฉพาะที่จำเป็น ไม่คัดลอกกฎหลายชุดจนขัดกัน

### Lean adoption, ไม่ over-engineer

- **Stage 0 / Minimum:** ตรวจ repo จริง, เขียน `AGENTS.md` แบบสั้น, บันทึก build/test commands, ตั้ง lint/test, restrict secrets/production
- **Stage 1 / After first few tasks:** เพิ่ม architecture/ADR ที่จำเป็น, scoped rule จากความผิดพลาดจริง, acceptance/evidence template, 1–2 skills ที่ใช้งานซ้ำ
- **Stage 2 / At scale:** เพิ่ม orchestration gates, reusable templates, eval suite, CI/permissions, cross-project policy distribution และ ownership

อย่าทำ Stage 2 เป็น prerequisite ของการเริ่มเขียน feature แรก

## Findings specific to HACLS repo

ตรวจจาก repository `tigertony2536/hacls`, branch `dev`:
- ปัจจุบัน `AGENTS.md` กำหนดภาษาไทยเป็นหลัก และ Representation Selection Policy พร้อม reference ไปที่ `docs/guidelines/representation-selection.md`
- `README.md` ระบุ `knowledge/inbox`, `knowledge/validated`, `knowledge/canonical`, `research`, `experiments`, scripts/validator และ Codex hook
- `docs/00-project-charter.md` ระบุการให้มนุษย์อนุมัติความรู้ canonical/การเปลี่ยนสำคัญของ skills และใช้ PR ตรวจทาน
- `research/` มี convention ชื่อไฟล์ขึ้นต้นด้วยวันที่

หลักฐานภายใน: [AGENTS.md](https://github.com/tigertony2536/hacls/blob/dev/AGENTS.md), [README.md](https://github.com/tigertony2536/hacls/blob/dev/README.md), [Project Charter](https://github.com/tigertony2536/hacls/blob/dev/docs/00-project-charter.md)

### ข้อเสนอสำหรับ HACLS (ยังไม่อนุมัติ implementation)

สร้างแนวคิด **project-bootstrap / project-init capability** ที่ตรวจ repo เป้าหมายแบบ read-only และเสนอ artifacts สำหรับให้มนุษย์อนุมัติ ก่อนเขียนไฟล์จริง โดย output ขั้นต่ำคือ:
1. `Project Context Snapshot`: ตรวจพบ stack, commands, modules, risk, existing rules, uncertainty
2. `Rule Placement Matrix`: แต่ละ constraint เป็น root rule / path rule / skill / docs / CI / permissions / approval เพราะอะไร
3. `Bootstrap Diff Proposal`: รายการไฟล์ที่จะเพิ่ม/แก้, ไม่ overwrite rules ของ repo เดิมโดยไม่มีการตรวจ
4. `Validation Plan`: สาม task ตัวอย่าง + หนึ่ง risky action เพื่อตรวจว่า setup ใช้งานได้จริง

Boundary: **Initializer** ตั้ง working environment; **HACLS Orchestrator** เลือก next step ตามความไม่แน่นอน/evidence; **Task Skills** ปฏิบัติขั้นตอน; **CI/Hook** บังคับตรวจ; **Human** อนุมัติ policy changes/high-risk decisions. ไม่ควรให้ Initializer ทำ strategic DDD หรือ Implement Feature เอง

สำหรับ repo HACLS ต้นทาง ไม่ควรนำ AGENTS.md ของ consumer project ทุกโปรเจกต์มารวมใน root; เก็บ template/policy เป็น artifacts ที่ผ่าน review ใน HACLS แล้วติดตั้งเฉพาะสิ่งที่เหมาะกับ consumer repo.

## Critical cautions and open questions

- คำว่า "agent harness" เป็นคำอธิบายเชิงวิศวกรรม ไม่ใช่ชื่อมาตรฐานกลางของทุก platform
- Instruction following มีความไม่แน่นอน; prompt-only rule ไม่ใช่ security guarantee
- Cross-tool portability อยู่ที่ feature ที่รองรับจริง และบาง frontmatter/permission/hook ผูกกับ provider
- ยังไม่มีหลักฐาน benchmark ว่าโครงสร้าง proposed นี้ดีที่สุดสำหรับ HACLS; ต้อง eval ด้วย scenario จริง
- ต้องตัดสินใจแยกก่อนว่า starter ของ HACLS เน้น **Codex-only MVP** หรือ **multi-agent portable core + adapters**; ข้อเสนอเบื้องต้นคือ portable conceptual policy พร้อม Codex adapter เป็นตัวแรก ตาม repo ที่ใช้ hooks อยู่แล้ว

## Source index (primary / first-party)

1. https://agents.md/
2. https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex
3. https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
4. https://developers.openai.com/blog/custom-code-review-rules-for-codex
5. https://developers.openai.com/blog/eval-skills
6. https://developers.openai.com/cookbook/examples/skills_in_api
7. https://code.claude.com/docs/en/skills
8. https://code.claude.com/docs/en/settings
9. https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
10. https://docs.cursor.com/context/rules-for-ai
11. https://developers.openai.com/api/docs/guides/agents-api/environments/security
12. https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
