"""Create a labeled draft overview; requires reportlab (not needed for Pages hosting)."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("DejaVu",normal="DejaVu",bold="DejaVuBold",italic="DejaVu",boldItalic="DejaVuBold")
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
ROOT = Path(__file__).resolve().parents[1]
sections = [
 ('Purpose', 'Framers Linguistic Protocol (FLP) is an open-source initiative to improve legal clarity, transparency, consistency, and citizen agency. Its stated mission is to expose vague, contradictory, or exploitative legal language and support public understanding of law.'),
 ('Proposed approach', 'The existing project material describes linguistic analysis, cross-state legal templates, cryptographic validation, and public feedback. Together, these are intended to make legal interpretations easier to inspect and proposed revisions easier to discuss.'),
 ('Technology under consideration', 'The project explores decentralized tools such as Ocean Protocol, smart contracts, token-based data access controls, and AI-assisted language analysis. This overview does not establish that any of these capabilities has been implemented or deployed.'),
 ('Participation and governance', 'The project proposes participation incentives and governance transparency through a token system identified as FRA. Token issuance, contract addresses, decision procedures, security controls, and implementation milestones remain unspecified in the available repository material.'),
 ('Open questions for a full white paper', 'A complete specification still needs a defined scope, source-selection rules, a review and dispute process, a governance model, a technical architecture, a security and privacy model, and measurable evaluation criteria. These are gaps to resolve, not approved project commitments.'),
 ('Sources and status', 'Prepared from the Website bundle, docs/about.html, docs/index.html, docs/faq.html, and docs/README.md at repository commit 3c439c3 (May 2, 2025 UTC). The original file named FLP_Whitepaper.pdf contained only placeholder text. This replacement is a short editorial reconstruction pending founder review, not the recovered full white paper. Repository: https://github.com/FramersFLA/FramersLP'),
]
styles=getSampleStyleSheet()
for style in styles.byName.values():
 style.fontName='DejaVu'
styles['Heading2'].fontName='DejaVuBold'
styles.add(ParagraphStyle(name='FLPTitle',fontName='DejaVu',fontSize=28,leading=32,textColor=colors.HexColor('#172733'),spaceAfter=14))
styles['BodyText'].fontSize=10
styles['BodyText'].leading=14
styles['Heading2'].fontSize=12
styles['Heading2'].spaceBefore=13
styles['Heading2'].textColor=colors.HexColor('#172733')
story=[Paragraph('Framers Linguistic Protocol',styles['FLPTitle']),Paragraph('WHITE PAPER DRAFT / PROJECT OVERVIEW',styles['Heading2']),Paragraph('Freedom through clarity.',styles['BodyText']),Spacer(1,10),Paragraph('<b>Status: reconstructed draft - pending founder review</b><br/>Prepared September 30, 2026. This document summarizes existing project material and does not represent an approved technical specification.',styles['BodyText'])]
for title,body in sections:
 story += [Paragraph(title,styles['Heading2']),Paragraph(body,styles['BodyText'])]
def footer(canvas,doc):
 canvas.setFont('DejaVu',8);canvas.setFillColor(colors.HexColor('#53616b'));canvas.drawString(48,28,'FLP | Draft overview | Pending founder review');canvas.drawRightString(564,28,str(doc.page))
SimpleDocTemplate(str(ROOT/'docs/FLP_Whitepaper.pdf'),pagesize=(612,792),rightMargin=48,leftMargin=48,topMargin=42,bottomMargin=48,title='FLP - Draft white paper overview',author='Framers Linguistic Protocol',invariant=1).build(story,onFirstPage=footer,onLaterPages=footer)
