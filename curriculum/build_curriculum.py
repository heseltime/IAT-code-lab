"""Build the Coding Lab curriculum PDF.

    python3 curriculum/build_curriculum.py        # run from the lab root

Needs ReportLab (pip install reportlab). Writes Coding_Lab_Curriculum_2026_v<VERSION>.pdf in the lab root.
Edit the content below (VERSION, SESSIONS, ...), bump VERSION, and run the script again.

Reading sections follow the course paper: Liu et al. 2026, "Dive into Claude Code", arXiv:2604.14228v3.
Keep them in sync with the reading map in reading/coding-agents.md.
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

# --------------------------------------------------------------------------------------------------
# Content
# --------------------------------------------------------------------------------------------------
VERSION = "0.9.1"
YEAR = "2026"
INSTITUTION = "Internationale Akademie Traunkirchen"
SUBTITLE = "AI &amp; Programming/Software Engineering"
LAB_LEAD = ("Jack Heseltine", "https://www.linkedin.com/in/heselt-in-e/")
PAPER_TITLE = "Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems"
PAPER_URL = "https://arxiv.org/pdf/2604.14228"

INTRO = (
    "A project-based programme guiding high school students from first principles to a working AI-assisted "
    "software project — learning to code with modern tools, collaborate like professionals, and share their "
    "work with the world. Each session pairs hands-on work with assigned sections from the course paper: "
    f'<a href="{PAPER_URL}"><u><i>{PAPER_TITLE}</i></u></a> (Liu et al., 2026).'
)

ARROW = '<font name="Symbol">→</font>'
GEQ = '<font name="Symbol">≥</font>'

# (number, title, bullets, reading, duration). <br/> forces a line break. Reading lines must fit about 84 pt
# (about 28 characters), or the cell wraps on its own.
SESSIONS = [
    ("0", "Overview, Demo &amp;<br/>Housekeeping",
     ["Project scope walkthrough and live demo",
      "Claude Code licence setup &amp; tool installation",
      "Ground rules &amp; getting to know each other",
      "To do: fix session dates for the full programme"],
     "§1 Introduction · §2 Design<br/>Philosophies &amp; Principles",
     "~1 session"),
    ("1", "Git, Python &amp; Code Agents",
     ["Command-line basics, Git fundamentals, Python crash-course",
      "What is a coding agent? Claude commands &amp; core concepts",
      f"Neural networks {ARROW} tokens {ARROW} emergent behaviour {ARROW} today's AI coding tools"],
     "§3 Architecture Overview ·<br/>§4 Turn Execution: The<br/>Agentic Query Loop",
     "~1 session"),
    ("2", "Project Repo Setup",
     ["Git review; clone &amp; structure the shared project repository",
      "Homework: write a project README with Claude Code",
      "Find or generate a starter dataset (school-related data preferred)",
      f"Define {GEQ} 1 knowledge-base skill; bonus: propose a scheduled automation"],
     "§6 Extensibility (MCP, Skills,<br/>Plugins, Hooks) · §7 Context<br/>Construction &amp; Memory",
     "~1 session"),
    ("3", "Lab Block",
     ["Hands-on build sprints — implement your planned project features",
      "Regular knowledge-sharing rounds &amp; short peer mini-presentations",
      "Iterative feedback loops between sessions"],
     "§5 Tool Authorization · §8<br/>Subagent Delegation · §9<br/>Session Persistence",
     "up to 5<br/>sessions"),
    ("4", "Architecture, Extensions &amp;<br/>Learning Paths",
     ["Higher-level thinking: system architecture and design patterns",
      "Concepts: Open Knowledge Format (OKF), knowledge graphs, code graphs",
      "Software engineering today — how professional teams work",
      "Individual next-step learning goals for continued coding growth"],
     "§10 Comparative Analysis<br/>(Claude Code, OpenClaw,<br/>Hermes Agent) · §11 Related<br/>"
     "Work · §12 Discussion",
     "~1 session"),
    ("5", "Stories, Epics &amp; Closing",
     ["Modern company workflows: Scrum, epics, user stories",
      "Wrap up project repo; start using tools for your own schoolwork",
      "Optional: software company site visit and/or Lange Nacht der Forschung (coding showcase event)",
      "Optional: final presentations at IAT round-table"],
     "§2.4 Long-term Developer<br/>Capability · §13 Future<br/>Directions · §14 Conclusion",
     "~1–2<br/>sessions"),
]

NOTE = (
    "The lab will communicate via WhatsApp group and also receive important updates like the finalized schedule "
    "there. Please let the instructor know if you do not want to or cannot use this platform."
)
FOOTER_LEFT = ("Total programme: approx. 10–12 sessions · Tools: Claude Code, Git,<br/>Python, VS Code "
               "· Session dates fixed in first meeting")

# --------------------------------------------------------------------------------------------------
# Design (matches the v0.9 layout)
# --------------------------------------------------------------------------------------------------
NAVY = colors.HexColor("#1A2B4A")
BLUE = colors.HexColor("#2E6DA4")
ORANGE = colors.HexColor("#F0A500")
GREY = colors.HexColor("#6B7280")
INK = colors.HexColor("#1C1C1E")
STRIPE = colors.HexColor("#EEF4FB")
RULE = colors.HexColor("#DDEAF5")

S = {
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=NAVY),
    "inst": ParagraphStyle("inst", fontName="Helvetica-Bold", fontSize=8, leading=12, textColor=NAVY,
                           alignment=TA_RIGHT),
    "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=8, leading=11, textColor=GREY, alignment=TA_RIGHT),
    "intro": ParagraphStyle("intro", fontName="Helvetica", fontSize=7.5, leading=11, textColor=GREY),
    "th": ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=BLUE),
    "th_date": ParagraphStyle("th_date", fontName="Helvetica-Bold", fontSize=8, leading=10,
                              textColor=colors.white, alignment=TA_CENTER),
    "num": ParagraphStyle("num", fontName="Helvetica-Bold", fontSize=9, leading=10, textColor=colors.white,
                          alignment=TA_CENTER),
    "session": ParagraphStyle("session", fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=NAVY),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=7, leading=10, textColor=INK),
    "reading": ParagraphStyle("reading", fontName="Helvetica", fontSize=6.5, leading=9.5, textColor=BLUE),
    "duration": ParagraphStyle("duration", fontName="Helvetica", fontSize=6.5, leading=9, textColor=GREY),
    "foot_l": ParagraphStyle("foot_l", fontName="Helvetica", fontSize=7, leading=9, textColor=GREY,
                             alignment=TA_CENTER),
    "foot_r": ParagraphStyle("foot_r", fontName="Helvetica", fontSize=7, leading=9, textColor=GREY,
                             alignment=TA_RIGHT),
}
S["bullet_next"] = ParagraphStyle("bullet_next", parent=S["bullet"], spaceBefore=2)
COL_WIDTHS = [8 * mm, 42 * mm, 54 * mm, 34 * mm, 18 * mm, 18 * mm]


def build(out: Path) -> None:
    version_line = f"{INSTITUTION} · {YEAR} · v{VERSION}"
    name, url = LAB_LEAD
    header = Table(
        [[Paragraph("Coding Lab Curriculum", S["title"]),
          [Paragraph(version_line, S["inst"]),
           Paragraph(SUBTITLE, S["meta"]),
           Paragraph(f'in English · Lab Lead: <a href="{url}"><u>{name}</u></a>', S["meta"])]]],
        colWidths=[96 * mm, 78 * mm],
        style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]),
    )

    rows = [[Paragraph("", S["th"]), Paragraph("Session", S["th"]), Paragraph("What you'll learn &amp; do", S["th"]),
             Paragraph("Assigned reading", S["th"]), Paragraph("Duration", S["th"]),
             Paragraph("Date", S["th_date"])]]
    for num, title, bullets, reading, duration in SESSIONS:
        cell = [Paragraph("• " + b, S["bullet"] if i == 0 else S["bullet_next"]) for i, b in enumerate(bullets)]
        rows.append([Paragraph(num, S["num"]), Paragraph(title, S["session"]), cell,
                     Paragraph(f'<a href="{PAPER_URL}">{reading}</a>', S["reading"]),
                     Paragraph(duration, S["duration"]), ""])

    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("BACKGROUND", (0, 1), (0, -1), BLUE),
        ("BACKGROUND", (-1, 1), (-1, -1), colors.white),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, ORANGE),
        ("LINEBELOW", (0, 1), (-1, -2), 0.4, RULE),
        ("BOX", (0, 0), (-1, -1), 0.5, BLUE),
        ("LINEBEFORE", (-1, 1), (-1, -1), 1, BLUE),
    ]
    for r in range(1, len(rows)):
        style.append(("BACKGROUND", (1, r), (-2, r), STRIPE if r % 2 == 0 else colors.white))
    table = Table(rows, colWidths=COL_WIDTHS, style=TableStyle(style))

    footer = Table(
        [[Paragraph(FOOTER_LEFT, S["foot_l"]), Paragraph(version_line, S["foot_r"])]],
        colWidths=[254.79, 481.23 - 254.79],
        style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]),
    )

    doc = SimpleDocTemplate(
        str(out), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=36.685, bottomMargin=18 * mm,
        title="Coding Lab Curriculum", author=name, subject=f"{INSTITUTION} {YEAR} v{VERSION}",
    )
    doc.build([
        header,
        HRFlowable(width="100%", thickness=2, color=ORANGE, lineCap="round", spaceBefore=2 * mm, spaceAfter=5 * mm),
        Paragraph(INTRO, S["intro"]),
        Spacer(1, 4),
        table,
        Spacer(1, 3 * mm),
        Paragraph(NOTE, S["intro"]),
        HRFlowable(width="100%", thickness=0.5, color=STRIPE, spaceBefore=3.5, spaceAfter=0),
        footer,
    ])


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    out = root / f"Coding_Lab_Curriculum_{YEAR}_v{VERSION}.pdf"
    build(out)
    print(f"wrote {out}")
