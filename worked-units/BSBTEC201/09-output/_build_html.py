#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stage 09C: convert BSBTEC201 learner guide markdown into branded Canvas HTML pages.
One page per section per the canvas-html SKILL (v2). Inline styles only. En dashes only."""
import re, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
LG = os.path.join(ROOT, "..", "04-output", "bsbtec201-learner-guide.md")
OUT = os.path.join(ROOT, "html")
os.makedirs(OUT, exist_ok=True)

PRIMARY="#101F14"; OLIVE="#B2D0B6"; TINT="#F5FAF6"; MID="#E8F5EC"; SILVER="#D9E0DC"
EN=u"–"
UNIT="BSBTEC201"; TITLE="Use business software applications"

def esc(t): return html.escape(t, quote=False)

def inline(t):
    t=esc(t)
    t=re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t=re.sub(r'`(.+?)`', r'<code style="background:#eef3ef;padding:1px 4px;border-radius:3px;">\1</code>', t)
    # bare urls -> links
    t=re.sub(r'(?<!")(https?://[^\s<]+)', r'<a href="\1">\1</a>', t)
    return t

def footer():
    return (f'<div style="background:#000000;color:#ffffff;font-size:13px;padding:10px 20px;'
            f'display:flex;justify-content:space-between;align-items:center;border-radius:4px 4px 0 0;margin-top:30px;">'
            f'<div style="display:flex;align-items:center;gap:10px;">'
            f'<img style="height:20px;width:auto;" src="[LEARNBUILT_EMBLEM_CANVAS_URL]" alt="Learnbuilt" />'
            f'<span>[BUYER_RTO_NAME] | RTO [BUYER_RTO_NUMBER]</span></div>'
            f'<div>{UNIT} {EN} {esc(TITLE)}</div></div>')

def banner(src):
    return (f'<p><img style="width:100%;border-radius:10px;margin-bottom:30px;" '
            f'src="[CANVAS_FILE_URL:{src}]" alt="Section banner" /></p>')

def title_block(num, name, subtitle=None):
    sub = (f'<p style="color:{OLIVE};margin:10px 0 0 0;font-size:16px;">{esc(subtitle)}</p>') if subtitle else ''
    head = f'{num} {EN} {esc(name)}' if num else esc(name)
    return (f'<div style="background:{PRIMARY};padding:30px;border-radius:8px;margin-bottom:30px;">'
            f'<h1 style="color:white;margin:0;font-size:28px;">{head}</h1>{sub}</div>')

def para(t): return f'<p style="font-size:15px;color:#000000;line-height:1.6;">{inline(t)}</p>'
def h2(t): return f'<h2 style="color:#101f14;font-size:20px;margin-top:30px;margin-bottom:10px;">{esc(t)}</h2>'

def ul(items):
    lis=''.join(f'<li style="margin-bottom:6px;">{inline(i)}</li>' for i in items)
    return f'<ul style="font-size:15px;color:#000000;line-height:1.8;padding-left:20px;margin-bottom:20px;">{lis}</ul>'

def example_callout(items):
    body=''.join(f'<li style="margin-bottom:6px;">{inline(i)}</li>' for i in items)
    return (f'<div style="background:{OLIVE};color:#101f14;padding:20px;margin-bottom:15px;border-radius:6px;">'
            f'<strong>Examples across Australian workplaces</strong>'
            f'<ul style="margin:10px 0 0 0;padding-left:20px;line-height:1.7;">{body}</ul></div>')

def activity_box(heading, lines):
    body=''.join(para(l) for l in lines)
    return (f'<div style="background:{TINT};padding:30px;border-left:4px solid {OLIVE};border-radius:6px;margin-bottom:30px;">'
            f'<h3 style="color:#101f14;">{esc(heading)}</h3>'
            f'<p style="font-size:13px;font-style:italic;color:#666;margin-top:-5px;margin-bottom:15px;">'
            f'This activity is optional and not assessed. You can ask your assessor to review your answers, but it is not marked.</p>'
            f'{body}</div>')

def key_box(heading, inner):
    return (f'<div style="background:{TINT};padding:30px;border-left:8px solid {PRIMARY};margin-bottom:30px;border-radius:8px;">'
            f'<h3 style="margin-top:0;color:#101f14;">{esc(heading)}</h3>{inner}</div>')

def table(rows):
    head=rows[0]; body=rows[2:]
    th=''.join(f'<th style="padding:12px 14px;text-align:left;">{inline(c)}</th>' for c in head)
    trs=''
    for i,r in enumerate(body):
        bg=TINT if i%2==0 else MID
        tds=''.join(f'<td style="padding:12px 14px;">{inline(c)}</td>' for c in r)
        trs+=f'<tr style="background:{bg};">{tds}</tr>'
    return (f'<table style="width:100%;border-collapse:collapse;font-size:15px;margin-bottom:30px;border-radius:8px;overflow:hidden;">'
            f'<thead style="background:{PRIMARY};color:white;"><tr>{th}</tr></thead><tbody>{trs}</tbody></table>')

def page(fname, title_tag, body):
    doc=(f'<!-- Canvas page: {title_tag} | brand-neutral, inline styles only -->\n'
         f'<div style="max-width:900px;margin:0 auto;font-family:Calibri,Arial,sans-serif;">\n{body}\n{footer()}\n</div>\n')
    with open(os.path.join(OUT,fname),'w',encoding='utf-8') as f: f.write(doc)
    return fname

# ---- parse learner guide ----
text=open(LG,encoding='utf-8').read()
lines=text.split('\n')

def md_blocks(md):
    """Yield ('para',text)/('ul',items)/('table',rows)/('activity',(head,lines))/('example',items)/('h2',t)/('resource',items) blocks."""
    blocks=[]; i=0; L=md.split('\n')
    while i < len(L):
        ln=L[i].rstrip()
        if not ln.strip(): i+=1; continue
        if ln.startswith('> '):  # blockquote = activity
            q=[]
            while i<len(L) and L[i].startswith('>'):
                q.append(L[i].lstrip('>').strip()); i+=1
            head=q[0].replace('**','') if q else 'Activity'
            blocks.append(('activity',(head,[x for x in q[1:] if x]))); continue
        if ln.startswith('|'):  # table
            rows=[]
            while i<len(L) and L[i].startswith('|'):
                rows.append([c.strip() for c in L[i].strip().strip('|').split('|')]); i+=1
            blocks.append(('table',rows)); continue
        if ln.startswith('- '):  # list
            items=[]
            while i<len(L) and L[i].startswith('- '):
                items.append(L[i][2:].strip()); i+=1
            blocks.append(('ul',items)); continue
        if ln.startswith('**Examples across industries**'):
            i+=1; items=[]
            while i<len(L) and L[i].strip().startswith('- '):
                items.append(L[i].strip()[2:].strip()); i+=1
            blocks.append(('example',items)); continue
        blocks.append(('para',ln)); i+=1
    return blocks

def render_blocks(blocks):
    out=''
    for kind,val in blocks:
        if kind=='para': out+=para(val)
        elif kind=='ul': out+=ul(val)
        elif kind=='table': out+=table(val)
        elif kind=='example': out+=example_callout(val)
        elif kind=='activity':
            head,body=val; out+=activity_box(head, body if body else [''])
    return out

# split into sections by headings
pages=[]; pageno=1
# locate Unit Overview content and How this guide works
def section_text(start_pat, stop_pats):
    m=re.search(start_pat, text)
    if not m: return ''
    start=m.end()
    ends=[text.find(s,start) for s in stop_pats if text.find(s,start)!=-1]
    end=min(ends) if ends else len(text)
    return text[start:end].strip()

# Page 1: Unit Overview
hpg=section_text(r'## How this guide works\n', ['\n---','## Unit Overview'])
ovv=section_text(r'## Unit Overview\n', ['\n## Module 1'])
ov_body = title_block(None, f'{UNIT} {EN} {TITLE}', 'Learner Guide')
ov_body += key_box('How this guide works', render_blocks(md_blocks(hpg)))
ov_body += render_blocks(md_blocks(ovv))
pages.append((f'{UNIT}_Page{pageno:02d}_UnitOverview.html','Unit Overview', ov_body)); pageno+=1

# Modules and sections
mod_re=re.compile(r'^## Module (\d): (.+)$', re.M)
mods=list(mod_re.finditer(text))
for mi,mm in enumerate(mods):
    mnum=mm.group(1); mtitle=mm.group(2).strip()
    mstart=mm.end()
    mend=mods[mi+1].start() if mi+1<len(mods) else text.find('\n## How this unit builds')
    body=text[mstart:mend]
    # module intro paragraph (text before first ###)
    first_sec=re.search(r'^### ', body, re.M)
    intro=body[:first_sec.start()].strip() if first_sec else body.strip()
    # sections
    sec_re=re.compile(r'^### (\d\.\d) (.+?)\n(.*?)(?=^### |\Z)', re.M|re.S)
    secs=list(sec_re.finditer(body))
    # module intro page
    mi_body=banner(f'bsbtec201-module-{mnum}-header.jpg')
    mi_body+=title_block(f'Module {mnum}', mtitle)
    mi_body+=render_blocks(md_blocks(intro))
    mi_body+='<h2 style="color:#101f14;font-size:20px;margin-top:30px;margin-bottom:10px;">In this module</h2>'
    mi_body+=ul([f'{s.group(1)} {s.group(2).strip()}' for s in secs])
    # assessment readiness + resources (### non-numbered)
    ar=re.search(r'^### Assessment Readiness.*?\n(.*?)(?=^### |\Z)', body, re.M|re.S)
    if ar:
        arb=ar.group(1).strip()
        mi_body+=key_box(f'Assessment Readiness {EN} Module {mnum}', render_blocks(md_blocks(arb)))
    ur=re.search(r'^### Useful resources.*?\n(.*?)(?=^### |\Z)', body, re.M|re.S)
    if ur:
        items=[l[2:].strip() for l in ur.group(1).strip().split('\n') if l.strip().startswith('- ')]
        mi_body+=h2(f'Useful resources {EN} Module {mnum}')+ul(items)
    pages.append((f'{UNIT}_Page{pageno:02d}_Module{mnum}Intro.html', f'Module {mnum}: {mtitle}', mi_body)); pageno+=1
    # section pages
    for s in secs:
        snum=s.group(1); sname=s.group(2).strip(); scontent=s.group(3).strip()
        sb=banner(f'bsbtec201-section-{snum.replace(".","-")}-header.jpg')
        sb+=title_block(snum, sname)
        sb+=render_blocks(md_blocks(scontent))
        pages.append((f'{UNIT}_Page{pageno:02d}_Section{snum.replace(".","-")}.html', f'Section {snum}: {sname}', sb)); pageno+=1

# Final page: foundation skills + wrapping up
fs=section_text(r'## How this unit builds your foundation skills\n', ['\n## Wrapping up'])
wu=section_text(r'## Wrapping up\n', ['\Z'])
fb=title_block(None, f'Foundation skills and wrap-up')
fb+=h2('How this unit builds your foundation skills')+render_blocks(md_blocks(fs))
fb+=h2('Wrapping up')+render_blocks(md_blocks(wu))
pages.append((f'{UNIT}_Page{pageno:02d}_Wrapup.html','Foundation skills and wrap-up', fb)); pageno+=1

for fname,tt,body in pages:
    page(fname,tt,body)
print(f"Wrote {len(pages)} HTML pages to {OUT}")
for fname,_,_ in pages: print("  "+fname)
