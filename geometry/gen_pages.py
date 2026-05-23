import os

OUTPUT_DIR = "/sessions/serene-wonderful-mayer/mnt/outputs"

def css():
    return """:root{--cream:#FBF6EC;--cream-deeper:#F4ECDC;--ink:#2B2520;--ink-soft:#6B635C;--peach:#FFD0BC;--mint:#BFE6D2;--lilac:#DDD2F2;--butter:#FFE39B;--sky:#C2DDF2;--coral:#FF6B5A;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}html{scroll-behavior:smooth;}body{font-family:'Nunito',sans-serif;background:var(--cream);color:var(--ink);overflow-x:hidden;line-height:1.55;-webkit-font-smoothing:antialiased;}
.blob{position:fixed;border-radius:50%;filter:blur(60px);opacity:.45;z-index:0;pointer-events:none;}
@keyframes float{0%,100%{transform:translate(0,0) scale(1);}50%{transform:translate(30px,-40px) scale(1.08);}}
header{position:sticky;top:0;z-index:100;background:rgba(251,246,236,.88);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--cream-deeper);padding:18px 48px;display:flex;justify-content:space-between;align-items:center;}
.logo{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:600;font-size:21px;letter-spacing:-.02em;display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);}
.logo-mark{width:32px;height:32px;background:var(--ink);border-radius:50%;display:inline-flex;align-items:center;justify-content:center;color:var(--butter);font-family:'Fraunces',serif;font-weight:600;font-size:17px;}
.logo-badge{font-family:'Nunito',sans-serif;font-size:11px;font-weight:700;color:var(--ink-soft);background:var(--cream-deeper);padding:3px 10px;border-radius:999px;margin-left:2px;}
nav ul{display:flex;list-style:none;gap:4px;align-items:center;}nav a{text-decoration:none;color:var(--ink);font-weight:600;font-size:13px;padding:8px 15px;border-radius:999px;transition:background .2s;}nav a:hover{background:var(--cream-deeper);}.nav-cta{background:var(--ink);color:var(--cream)!important;}.nav-cta:hover{background:var(--coral)!important;}
.hero{position:relative;z-index:1;padding:68px 48px 52px;max-width:860px;margin:0 auto;text-align:center;}
.eyebrow{display:inline-flex;align-items:center;gap:10px;background:white;border:1px solid var(--cream-deeper);padding:7px 18px;border-radius:999px;font-size:13px;font-weight:600;color:var(--ink-soft);margin-bottom:22px;box-shadow:0 4px 12px rgba(43,37,32,.04);}
.eyebrow .dot{width:8px;height:8px;border-radius:50%;}
h1{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:500;font-size:clamp(38px,6vw,64px);line-height:1.05;letter-spacing:-.03em;margin-bottom:18px;}
.hero-sub{font-size:16px;color:var(--ink-soft);max-width:500px;margin:0 auto 28px;line-height:1.65;}
.hero-ctas{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;}
.btn{font-family:'Nunito',sans-serif;font-weight:700;font-size:14px;padding:12px 24px;border-radius:999px;border:none;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:6px;transition:transform .2s,box-shadow .2s,background .2s;}
.btn-primary{background:var(--ink);color:var(--cream);box-shadow:0 6px 16px rgba(43,37,32,.13);}.btn-primary:hover{transform:translateY(-2px);box-shadow:0 10px 22px rgba(43,37,32,.2);}
.btn-ghost{background:white;color:var(--ink);border:1.5px solid var(--cream-deeper);}.btn-ghost:hover{transform:translateY(-2px);background:var(--cream-deeper);}
.content-wrap{position:relative;z-index:1;max-width:1060px;margin:0 auto;padding:0 48px 80px;}
.section-head{margin:52px 0 28px;}.section-head h2{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:500;font-size:clamp(28px,3.5vw,38px);letter-spacing:-.03em;line-height:1.1;margin-bottom:6px;}.section-head p{color:var(--ink-soft);font-size:15px;}
.lesson-row{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px;align-items:start;}
.lesson-card{border-radius:28px;padding:30px 28px;transition:transform .22s,box-shadow .22s;}.lesson-card:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(43,37,32,.07);}
.c-peach{background:var(--peach);}.c-mint{background:var(--mint);}.c-lilac{background:var(--lilac);}.c-butter{background:var(--butter);}.c-sky{background:var(--sky);}
.lesson-tag{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;opacity:.55;margin-bottom:12px;display:block;}
.lesson-card h3{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:500;font-size:22px;letter-spacing:-.02em;line-height:1.15;margin-bottom:12px;}
.lesson-card p{font-size:14px;line-height:1.65;opacity:.85;margin-bottom:8px;}.lesson-card p:last-child{margin-bottom:0;}
.key-list{background:rgba(255,255,255,.5);border-radius:14px;padding:13px 17px;margin:10px 0;list-style:none;}
.key-list li{font-size:13.5px;line-height:1.65;padding:5px 0;border-bottom:1px solid rgba(43,37,32,.07);}.key-list li:last-child{border-bottom:none;}.key-list li strong{font-weight:700;}
.example-pill{background:rgba(255,255,255,.6);border-radius:12px;padding:11px 15px;font-size:13px;line-height:1.65;margin-top:10px;display:block;}.example-pill strong{font-weight:700;}
.practice-block{background:white;border:1px solid var(--cream-deeper);border-radius:22px;padding:24px 26px;box-shadow:0 2px 8px rgba(43,37,32,.03);}
.practice-block-title{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-soft);margin-bottom:18px;display:flex;align-items:center;gap:8px;}
.practice-block-title::after{content:'';flex:1;height:1px;background:var(--cream-deeper);}
.question{margin-bottom:18px;}.question:last-child{margin-bottom:0;}
.q-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-soft);margin-bottom:7px;}
.q-text{font-size:14px;font-weight:700;color:var(--ink);margin-bottom:12px;line-height:1.5;}
.choices{display:flex;flex-direction:column;gap:7px;}
.choice-btn{text-align:left;background:var(--cream);border:1.5px solid var(--cream-deeper);border-radius:10px;padding:9px 14px;cursor:pointer;font-size:13.5px;font-weight:500;color:var(--ink);font-family:'Nunito',sans-serif;transition:all .16s;line-height:1.5;}
.choice-btn:hover:not(:disabled){border-color:var(--ink);background:var(--cream-deeper);}
.choice-btn.correct{border-color:#5bb089;background:#eef8f2;color:#1a5c35;font-weight:700;}.choice-btn.incorrect{border-color:var(--coral);background:#fff2f0;color:#8b1f13;}.choice-btn.revealed{border-color:#5bb089;background:#eef8f2;color:#1a5c35;}.choice-btn:disabled{cursor:default;}
.input-row{display:flex;gap:8px;align-items:center;flex-wrap:wrap;}
.input-row input{font-family:'Nunito',sans-serif;font-size:13.5px;font-weight:500;color:var(--ink);background:var(--cream);border:1.5px solid var(--cream-deeper);border-radius:10px;padding:9px 14px;outline:none;min-width:140px;transition:border-color .16s,background .16s;}
.input-row input:focus{border-color:var(--coral);background:white;}.input-row input.correct{border-color:#5bb089;background:#eef8f2;}.input-row input.incorrect{border-color:var(--coral);background:#fff2f0;}
.check-btn{background:var(--ink);color:var(--cream);border:none;border-radius:999px;padding:9px 20px;font-size:12px;font-weight:700;font-family:'Nunito',sans-serif;cursor:pointer;transition:background .2s;}.check-btn:hover{background:var(--coral);}
.feedback{margin-top:8px;font-size:12.5px;font-weight:700;min-height:18px;}.feedback.correct{color:#256b3c;}.feedback.incorrect{color:#8b1f13;}
.video-section{position:relative;z-index:1;max-width:1060px;margin:0 auto;padding:0 48px 48px;}
.video-card{background:var(--ink);border-radius:28px;overflow:hidden;box-shadow:0 10px 32px rgba(43,37,32,.12);}
.video-card-header{padding:20px 28px 16px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;}
.video-card-header h3{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:500;font-size:18px;letter-spacing:-.02em;color:var(--cream);}
.video-tag{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--butter);background:rgba(255,227,155,.12);border:1px solid rgba(255,227,155,.2);padding:4px 12px;border-radius:999px;}
.video-wrapper{position:relative;padding-bottom:56.25%;height:0;overflow:hidden;}.video-wrapper iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:none;}
.lesson-divider{height:1px;background:var(--cream-deeper);margin:36px 0;}
footer{position:relative;z-index:1;border-top:1px solid var(--cream-deeper);padding:32px 48px;max-width:1060px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;color:var(--ink-soft);font-size:13px;}
footer a{color:var(--ink);font-weight:700;text-decoration:none;}footer a:hover{color:var(--coral);}
@media(max-width:760px){.lesson-row{grid-template-columns:1fr;}header{padding:16px 20px;}nav li:not(:last-child){display:none;}.hero,.content-wrap,.video-section{padding-left:20px;padding-right:20px;}footer{padding:24px 20px;}}"""

def js():
    return """let answered={},correct=0,total=0;
function checkMC(btn,qId,isCorrect){if(answered[qId])return;answered[qId]=true;total++;const allBtns=btn.closest('.choices').querySelectorAll('.choice-btn');allBtns.forEach(b=>b.disabled=true);const fb=document.getElementById(qId+'-feedback');if(isCorrect){btn.classList.add('correct');fb.textContent='✓ Correct!';fb.className='feedback correct';correct++;}else{btn.classList.add('incorrect');fb.textContent='✗ Not quite — review the section on the left!';fb.className='feedback incorrect';allBtns.forEach(b=>{if(b.getAttribute('onclick')&&b.getAttribute('onclick').includes('true'))b.classList.add('revealed');});}}
function checkInput(qId,accepted){if(answered[qId])return;const inputEl=document.getElementById(qId+'-input');const fb=document.getElementById(qId+'-feedback');const val=inputEl.value.trim().toLowerCase().replace(/\\s/g,'');const norm=accepted.map(a=>a.toLowerCase().replace(/\\s/g,''));answered[qId]=true;total++;if(norm.includes(val)){inputEl.classList.add('correct');fb.textContent='✓ Correct!';fb.className='feedback correct';correct++;}else{inputEl.classList.add('incorrect');fb.textContent='✗ Correct answer: '+accepted[0];fb.className='feedback incorrect';}inputEl.disabled=true;}"""

BLOB_COLORS = [
    ("var(--mint)","var(--butter)","var(--sky)"),
    ("var(--lilac)","var(--peach)","var(--mint)"),
    ("var(--peach)","var(--sky)","var(--butter)"),
    ("var(--butter)","var(--lilac)","var(--peach)"),
    ("var(--sky)","var(--mint)","var(--lilac)"),
]
CARD_COLORS = ["c-peach","c-mint","c-lilac","c-butter","c-sky"]
DOT_COLORS = ["var(--mint)","var(--peach)","var(--lilac)","var(--butter)","var(--sky)"]

def blobs(idx):
    c = BLOB_COLORS[idx % len(BLOB_COLORS)]
    return f"""<div class="blob" style="top:-120px;right:-80px;width:380px;height:380px;background:{c[0]};animation:float 14s ease-in-out infinite;"></div>
<div class="blob" style="top:400px;left:-160px;width:420px;height:420px;background:{c[1]};animation:float 18s ease-in-out infinite reverse;"></div>
<div class="blob" style="bottom:-100px;right:-120px;width:320px;height:320px;background:{c[2]};animation:float 16s ease-in-out infinite;"></div>"""

def mc(qid, question, choices, correct_idx):
    html = f'<div class="question"><div class="q-label">Q{qid} · Multiple Choice</div><p class="q-text">{question}</p><div class="choices">'
    letters = ["A","B","C","D"]
    for i,(ch,_) in enumerate(choices):
        is_correct = "true" if i==correct_idx else "false"
        html += f'<button class="choice-btn" onclick="checkMC(this,\'q{qid}\',{is_correct})">{letters[i]}) {ch}</button>'
    html += f'</div><div class="feedback" id="q{qid}-feedback"></div></div>'
    return html

def sa(qid, question, accepted):
    acc_str = str(accepted).replace("'",'"')
    return f'<div class="question"><div class="q-label">Q{qid} · Short Answer</div><p class="q-text">{question}</p><div class="input-row"><input type="text" id="q{qid}-input" placeholder="Answer"/><button class="check-btn" onclick="checkInput(\'q{qid}\',{acc_str})">Check</button></div><div class="feedback" id="q{qid}-feedback"></div></div>'

def lesson_row(tag, h3, card_color, body_html, practice_title, q_html):
    return f"""<div class="lesson-row">
  <div class="lesson-card {card_color}">
    <span class="lesson-tag">{tag}</span>
    <h3>{h3}</h3>
    {body_html}
  </div>
  <div class="practice-block">
    <div class="practice-block-title">{practice_title}</div>
    {q_html}
  </div>
</div>"""

def section_head(id_, h2, p, mt=False):
    st = ' style="margin-top:60px;"' if mt else ''
    return f'<div class="section-head" id="{id_}"{st}><h2>{h2}</h2><p>{p}</p></div>'

def build_page(filename, subject, unit_num, grade, unit_title, h1_html, hero_sub, blob_idx, dot_color, fishtank_path, sections):
    badge = f"{subject} · Unit {unit_num}"
    nav_links = "".join(f'<li><a href="#topic-{chr(97+i)}">{t[0]}</a></li>' for i,t in enumerate(sections))
    cta_links = "".join(f'<a href="#topic-{chr(97+i)}" class="btn btn-ghost">{t[0]}</a>' for i,t in enumerate(sections[1:]))
    
    sections_html = ""
    for i,(topic_name, topic_desc, rows) in enumerate(sections):
        topic_id = f"topic-{chr(97+i)}"
        sections_html += section_head(topic_id, topic_name, topic_desc, mt=(i>0))
        for j,row in enumerate(rows):
            sections_html += "\n" + row
            if j < len(rows)-1:
                sections_html += '\n<div class="lesson-divider"></div>'
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>{subject} · Unit {unit_num} Study Guide — crefcalc</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400..700,0..100&family=Nunito:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css()}</style>
</head>
<body>
{blobs(blob_idx)}
<header>
  <a href="https://crefcalc.netlify.app" class="logo"><span class="logo-mark">c</span>crefcalc<span class="logo-badge">{badge}</span></a>
  <nav><ul>{nav_links}<li><a href="https://crefcalc.netlify.app/#book" class="nav-cta">Book free</a></li></ul></nav>
</header>
<div class="hero">
  <div class="eyebrow"><span class="dot" style="background:{dot_color};box-shadow:0 0 0 4px rgba(0,0,0,0.08);"></span> Unit {unit_num} · {grade}</div>
  <h1>{h1_html}</h1>
  <p class="hero-sub">{hero_sub}</p>
  <div class="hero-ctas"><a href="#topic-a" class="btn btn-primary">Start studying</a>{cta_links}</div>
</div>
<div class="video-section">
  <div class="video-card"><div class="video-card-header"><h3>Unit {unit_num} — Lesson Video</h3><span class="video-tag">Placeholder</span></div>
  <div class="video-wrapper"><iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="Unit {unit_num}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></div>
</div>
<div class="content-wrap">
{sections_html}
</div>
<footer>
  <span>© 2026 crefcalc &nbsp;·&nbsp; {subject}, Unit {unit_num} Study Guide</span>
  <span>Based on <a href="https://www.fishtanklearning.org/curriculum/math/{fishtank_path}/" target="_blank">Fishtank Learning</a></span>
</footer>
<script>{js()}</script>
</body>
</html>"""
    
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {filename}")

# ── KEY HELPER ──
def kl(*items):
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'<ul class="key-list">{lis}</ul>'

def ep(text):
    return f'<span class="example-pill">{text}</span>'

def pp(text):
    return f'<p>{text}</p>'

# ════════════════════════════════════════════════════
# ALGEBRA 2 UNITS 5–9
# ════════════════════════════════════════════════════

# ── A2 Unit 5: Exponential Modeling & Logarithms ──
build_page("algebra2-5.html","Algebra 2",5,"11th Grade Mathematics",
  "Exponential Modeling &amp; Logarithms",
  "Exponential Modeling<br>&amp; Logarithms.",
  "Growth, decay, natural base e, logarithm properties, and solving exponential/log equations.",
  0,"var(--mint)","algebra-2",
  [
    ("Topic A: Exponential Functions &amp; Sequences","Lessons 1–5 · Growth, decay, geometric sequences, and base e.",
     [lesson_row("01–03 — Lessons 1–3","Exponential Growth &amp; Decay","c-mint",
       pp("f(x) = a·bˣ models situations that multiply repeatedly.")+
       kl("<strong>a:</strong> initial value (y-intercept, f(0) = a).",
          "<strong>b &gt; 1:</strong> growth factor — increases exponentially.",
          "<strong>0 &lt; b &lt; 1:</strong> decay factor — decreases toward zero.",
          "<strong>Continuous growth:</strong> f(t) = ae^(rt), base e ≈ 2.718.",
          "Doubling time: when f(t) = 2a → solve 2 = b^t.")+
       ep("<strong>Example:</strong> $1,000 at 5% annual growth: f(t) = 1000·(1.05)ᵗ. After 10 years: f(10) ≈ $1,629."),
       "Practice — Lessons 1–3",
       mc(1,"A population of 500 grows at 8% per year. Which function models this?",
          [("f(t) = 500 + 0.08t",0),("f(t) = 500·(1.08)ᵗ",1),("f(t) = 500·0.08ᵗ",0),("f(t) = 500·8ᵗ",0)],1)+
       sa(2,"Using f(t) = 200·(0.5)ᵗ, what is f(3)?",["25"])),
      lesson_row("04–05 — Lessons 4–5","Geometric Sequences &amp; Series","c-butter",
       pp("A geometric sequence multiplies by a constant ratio r each term.")+
       kl("<strong>General term:</strong> aₙ = a₁ · r^(n−1).",
          "<strong>Common ratio:</strong> r = aₙ₊₁/aₙ.",
          "<strong>Finite sum:</strong> Sₙ = a₁(1 − rⁿ)/(1 − r), r ≠ 1.",
          "<strong>Infinite sum (|r|&lt;1):</strong> S = a₁/(1 − r).")+
       ep("Sequence: 3, 6, 12, 24 … → a₁ = 3, r = 2 → a₅ = 3·2⁴ = <strong>48</strong>"),
       "Practice — Lessons 4–5",
       mc(3,"Find the 6th term of the geometric sequence 2, 6, 18, …",
          [("162",0),("486",1),("54",0),("1458",0)],1)+
       sa(4,"For a geometric sequence with a₁ = 5 and r = 3, what is a₄?",["135"]))]
    ),
    ("Topic B: Logarithms","Lessons 6–10 · Definition, properties, and graphing logarithms.",
     [lesson_row("06–07 — Lessons 6–7","Logarithms as Inverses of Exponentials","c-lilac",
       pp("Logarithms undo exponentiation. log_b(x) = y means b^y = x.")+
       kl("<strong>Common log:</strong> log(x) = log₁₀(x).",
          "<strong>Natural log:</strong> ln(x) = log_e(x).",
          "<strong>Inverse relationship:</strong> b^(log_b(x)) = x and log_b(b^x) = x.",
          "Domain of log: x &gt; 0. Range: all reals.")+
       ep("log₂(8) = 3 because 2³ = 8. &nbsp;·&nbsp; ln(e⁵) = 5."),
       "Practice — Lessons 6–7",
       mc(5,"log₃(81) = ?",
          [("4",1),("3",0),("27",0),("9",0)],0)+
       sa(6,"Rewrite as a logarithm: 5² = 25. Write log_?(?) = ?",["log5(25)=2","log_5(25)=2"])),
      lesson_row("08–10 — Lessons 8–10","Properties of Logarithms","c-sky",
       kl("<strong>Product:</strong> log_b(MN) = log_b(M) + log_b(N).",
          "<strong>Quotient:</strong> log_b(M/N) = log_b(M) − log_b(N).",
          "<strong>Power:</strong> log_b(Mⁿ) = n·log_b(M).",
          "<strong>Change of base:</strong> log_b(x) = log(x)/log(b).",
          "Use to expand or condense logarithmic expressions.")+
       ep("log(x²y/z) = 2log(x) + log(y) − log(z)"),
       "Practice — Lessons 8–10",
       mc(7,"Expand: ln(x³/y). Which is correct?",
          [("3·ln(x)/ln(y)",0),("3·ln(x) − ln(y)",1),("ln(x³) · ln(y)",0),("3·ln(x) + ln(y)",0)],1)+
       sa(8,"Use change of base to find log₄(64) exactly.",["3"]))]
    ),
    ("Topic C: Solving Exponential &amp; Log Equations","Lessons 11–16 · Applying log properties to solve equations and model real situations.",
     [lesson_row("11–14 — Lessons 11–14","Solving Exponential &amp; Logarithmic Equations","c-peach",
       pp("Use logarithms to solve equations where the variable is in the exponent.")+
       kl("To solve bˣ = c: take log of both sides → x = log(c)/log(b).",
          "To solve log_b(x) = c: rewrite as b^c = x.",
          "<strong>Check:</strong> for log equations, verify the argument &gt; 0.",
          "Use ln when working with base e.")+
       ep("3ˣ = 20 → x = log(20)/log(3) = ln(20)/ln(3) ≈ <strong>2.73</strong>"),
       "Practice — Lessons 11–14",
       mc(9,"Solve 2ˣ = 32. What is x?",
          [("4",0),("5",1),("6",0),("16",0)],1)+
       mc(10,"Solve log₂(x) = 4. What is x?",
          [("8",0),("16",1),("2",0),("4",0)],1)),
      lesson_row("15–16 — Lessons 15–16","Exponential Modeling in Context","c-mint",
       pp("Apply exponential and log functions to real-world growth, decay, and finance.")+
       kl("<strong>Compound interest:</strong> A = P(1 + r/n)^(nt).",
          "<strong>Continuous compounding:</strong> A = Pe^(rt).",
          "<strong>Half-life:</strong> f(t) = a·(0.5)^(t/h), h = half-life period.",
          "Use logs to find when a quantity reaches a specific value.")+
       ep("Carbon-14 half-life ≈ 5,730 yr. After 11,460 yr (2 half-lives): 1/4 remains."),
       "Practice — Lessons 15–16",
       mc(11,"A substance decays to half its amount every 10 years. After 30 years, what fraction remains?",
          [("1/2",0),("1/4",0),("1/8",1),("1/3",0)],2)+
       sa(12,"$500 invested at 6% continuously compounded. Use A = 500e^(0.06t). After t = 0, A = ?",["500","$500"]))]
    )
  ]
)

# ── A2 Unit 6: Unit Circle & Trigonometric Functions ──
build_page("algebra2-6.html","Algebra 2",6,"11th Grade Mathematics",
  "Unit Circle &amp; Trigonometric Functions",
  "Unit Circle &amp;<br>Trig Functions.",
  "Radian measure, the unit circle, sine, cosine, and graphing trig functions with transformations.",
  1,"var(--lilac)","algebra-2",
  [
    ("Topic A: Right Triangle Trig &amp; Radian Measure","Lessons 1–5 · SOH-CAH-TOA review, converting degrees/radians.",
     [lesson_row("01–03 — Lessons 1–3","Right Triangle Trigonometry","c-lilac",
       kl("<strong>SOH-CAH-TOA:</strong>",
          "sin(θ) = opposite/hypotenuse",
          "cos(θ) = adjacent/hypotenuse",
          "tan(θ) = opposite/adjacent",
          "<strong>Pythagorean identity:</strong> sin²(θ) + cos²(θ) = 1.",
          "Inverse trig: θ = sin⁻¹(x) finds the angle.")+
       ep("In a right triangle, if the opposite side = 3 and hypotenuse = 5: sin(θ) = 3/5 = 0.6."),
       "Practice — Lessons 1–3",
       mc(1,"In a right triangle, cos(θ) = 5/13. What is tan(θ)?",
          [("5/13",0),("12/5",1),("13/12",0),("5/12",0)],1)+
       sa(2,"If sin(θ) = 0.6 and cos(θ) = 0.8, what is tan(θ)?",["0.75","3/4"])),
      lesson_row("04–05 — Lessons 4–5","Radian Measure","c-sky",
       pp("Radians are an alternative unit for measuring angles based on arc length.")+
       kl("<strong>1 radian:</strong> angle where arc length = radius.",
          "<strong>π radians = 180°</strong>",
          "To convert: degrees × π/180 = radians.",
          "To convert: radians × 180/π = degrees.",
          "Full circle: 2π radians = 360°.")+
       ep("90° = π/2 &nbsp;·&nbsp; 45° = π/4 &nbsp;·&nbsp; 60° = π/3 &nbsp;·&nbsp; 30° = π/6"),
       "Practice — Lessons 4–5",
       mc(3,"Convert 270° to radians.",
          [("π",0),("3π/2",1),("2π",0),("3π/4",0)],1)+
       sa(4,"Convert π/3 radians to degrees.",["60","60°"]))]
    ),
    ("Topic B: The Unit Circle","Lessons 6–9 · Unit circle coordinates, reference angles, trig values.",
     [lesson_row("06–09 — Lessons 6–9","The Unit Circle","c-peach",
       pp("The unit circle has radius 1. Every point (x, y) on it gives cos(θ) = x and sin(θ) = y.")+
       kl("Key angles (radians): 0, π/6, π/4, π/3, π/2, π, 3π/2, 2π.",
          "<strong>Quadrant I:</strong> sin &gt; 0, cos &gt; 0.",
          "<strong>Quadrant II:</strong> sin &gt; 0, cos &lt; 0.",
          "<strong>Quadrant III:</strong> sin &lt; 0, cos &lt; 0.",
          "<strong>Quadrant IV:</strong> sin &lt; 0, cos &gt; 0.",
          "ASTC: All Students Take Calculus — which trig values are positive.")+
       ep("cos(π/3) = 1/2 &nbsp;·&nbsp; sin(π/3) = √3/2 &nbsp;·&nbsp; tan(π/3) = √3"),
       "Practice — Lessons 6–9",
       mc(5,"What is sin(π/2)?",
          [("0",0),("1",1),("√2/2",0),("1/2",0)],1)+
       mc(6,"In which quadrant is θ if sin(θ) &lt; 0 and cos(θ) &gt; 0?",
          [("Quadrant I",0),("Quadrant II",0),("Quadrant III",0),("Quadrant IV",1)],3))]
    ),
    ("Topic C: Graphing Trigonometric Functions","Lessons 10–14 · Graphs of sin/cos/tan, amplitude, period, and transformations.",
     [lesson_row("10–12 — Lessons 10–12","Graphs of Sine &amp; Cosine","c-butter",
       kl("f(x) = A·sin(Bx + C) + D",
          "<strong>Amplitude = |A|:</strong> half the vertical distance from min to max.",
          "<strong>Period = 2π/B:</strong> horizontal length of one full cycle.",
          "<strong>Phase shift = −C/B:</strong> horizontal translation.",
          "<strong>Vertical shift = D:</strong> moves midline up/down.",
          "Cosine starts at max; Sine starts at midline.")+
       ep("f(x) = 3sin(2x) → A=3 (amplitude 3), B=2 (period = 2π/2 = π)."),
       "Practice — Lessons 10–12",
       mc(7,"For f(x) = 4cos(πx/2), what is the period?",
          [("π",0),("4",0),("2",0),("4",1)],3)+
       sa(8,"For f(x) = 2sin(3x), what is the amplitude?",["2"])),
      lesson_row("13–14 — Lessons 13–14","The Tangent Function","c-mint",
       pp("The tangent function has a period of π and vertical asymptotes where cos(θ) = 0.")+
       kl("<strong>tan(θ) = sin(θ)/cos(θ)</strong>",
          "<strong>Period:</strong> π.",
          "<strong>Vertical asymptotes:</strong> x = π/2 + nπ for integers n.",
          "Increases from −∞ to ∞ on each period.",
          "No amplitude — unbounded.")+
       ep("tan(0) = 0 &nbsp;·&nbsp; tan(π/4) = 1 &nbsp;·&nbsp; tan(π/2) is undefined."),
       "Practice — Lessons 13–14",
       mc(9,"Where does f(x) = tan(x) have a vertical asymptote?",
          [("x = 0",0),("x = π/2",1),("x = π",0),("x = 2π",0)],1)+
       mc(10,"What is the period of f(x) = tan(x)?",
          [("2π",0),("π",1),("π/2",0),("4π",0)],1))]
    )
  ]
)

# ── A2 Unit 7: Trigonometric Identities & Equations ──
build_page("algebra2-7.html","Algebra 2",7,"11th Grade Mathematics",
  "Trigonometric Identities &amp; Equations",
  "Trig Identities<br>&amp; Equations.",
  "Pythagorean identities, solving trig equations, and sum/difference formulas.",
  2,"var(--butter)","algebra-2",
  [
    ("Topic A: Fundamental Trig Identities","Lessons 1–5 · Pythagorean, reciprocal, and quotient identities.",
     [lesson_row("01–03 — Lessons 1–3","Pythagorean &amp; Reciprocal Identities","c-butter",
       kl("<strong>Pythagorean identity:</strong> sin²θ + cos²θ = 1",
          "Derived: 1 + tan²θ = sec²θ &nbsp;·&nbsp; 1 + cot²θ = csc²θ",
          "<strong>Reciprocal identities:</strong>",
          "csc θ = 1/sin θ &nbsp;·&nbsp; sec θ = 1/cos θ &nbsp;·&nbsp; cot θ = 1/tan θ",
          "<strong>Quotient identities:</strong> tan θ = sin θ/cos θ")+
       ep("If sin θ = 3/5, then cos²θ = 1 − 9/25 = 16/25 → cos θ = 4/5 (if θ in QI)."),
       "Practice — Lessons 1–3",
       mc(1,"Which identity is equivalent to 1 − sin²θ?",
          [("tan²θ",0),("cos²θ",1),("sec²θ",0),("csc²θ",0)],1)+
       sa(2,"If cos θ = 5/13, find sin θ (assume θ in Quadrant I). Write as a fraction.",["12/13"])),
      lesson_row("04–05 — Lessons 4–5","Verifying Trig Identities","c-lilac",
       pp("To verify an identity, transform one side to match the other using known identities.")+
       kl("Work on only ONE side at a time.",
          "Use algebraic skills: factor, combine fractions, multiply by conjugates.",
          "Rewrite everything in terms of sin and cos when stuck.",
          "An identity must hold for ALL values in the domain — one example isn't enough.")+
       ep("Verify: tan²θ + 1 = sec²θ. Left side: sin²θ/cos²θ + cos²θ/cos²θ = (sin²θ + cos²θ)/cos²θ = 1/cos²θ = sec²θ ✓"),
       "Practice — Lessons 4–5",
       mc(3,"When verifying a trig identity, you should:",
          [("Substitute a specific value to test it",0),
           ("Cross-multiply both sides",0),
           ("Manipulate only one side using known identities",1),
           ("Add the same term to both sides",0)],2)+
       mc(4,"Which is a valid first step to verify sin²θ/cos²θ = tan²θ?",
          [("Square both sides",0),
           ("Replace sin²θ/cos²θ with (sinθ/cosθ)² = tan²θ",1),
           ("Divide both sides by sin θ",0),
           ("Substitute θ = 45°",0)],1))]
    ),
    ("Topic B: Solving Trigonometric Equations","Lessons 6–10 · Solving for angle values in a given domain.",
     [lesson_row("06–10 — Lessons 6–10","Solving Trig Equations","c-sky",
       pp("Solve trig equations by isolating the trig function, then using inverse trig or the unit circle.")+
       kl("Step 1: Isolate the trig function (e.g., get sin x = 0.5).",
          "Step 2: Find the reference angle using inverse trig.",
          "Step 3: Find all solutions in the given domain using quadrant analysis.",
          "On [0, 2π): sin x = k usually has 2 solutions; check the quadrant signs.",
          "Factor if multiple trig terms — use the zero product property.")+
       ep("sin x = √3/2, 0 ≤ x &lt; 2π → x = π/3 and x = 2π/3 (both in QI and QII where sin &gt; 0)."),
       "Practice — Lessons 6–10",
       mc(5,"Solve 2cos x = 1 on [0, 2π). How many solutions?",
          [("One solution",0),("Two solutions",1),("Three solutions",0),("No solutions",0)],1)+
       sa(6,"Solve sin x = 0 on [0, 2π). Give the solution between 0 and π exclusive.",["pi","π","3.14"]))]
    ),
    ("Topic C: Sum/Difference &amp; Double Angle Formulas","Lessons 11–16 · Advanced identities and their applications.",
     [lesson_row("11–13 — Lessons 11–13","Sum &amp; Difference Formulas","c-peach",
       kl("<strong>sin(A ± B) = sin A cos B ± cos A sin B</strong>",
          "<strong>cos(A ± B) = cos A cos B ∓ sin A sin B</strong>",
          "<strong>tan(A ± B) = (tan A ± tan B)/(1 ∓ tan A tan B)</strong>",
          "Use to find exact values of angles like 75°, 15°, etc.")+
       ep("cos(75°) = cos(45°+30°) = cos45°cos30° − sin45°sin30°<br>= (√2/2)(√3/2) − (√2/2)(1/2) = (√6−√2)/4"),
       "Practice — Lessons 11–13",
       mc(7,"sin(A + B) = sin A cos B + cos A sin B. If A = π/6, B = π/3, what is sin(π/2)?",
          [("√3/2",0),("1/2",0),("1",1),("√2/2",0)],2)+
       mc(8,"Which formula gives cos(A − B)?",
          [("cos A cos B − sin A sin B",0),
           ("cos A cos B + sin A sin B",1),
           ("sin A cos B − cos A sin B",0),
           ("cos A sin B + sin A cos B",0)],1)),
      lesson_row("14–16 — Lessons 14–16","Double Angle Formulas","c-mint",
       kl("<strong>sin(2A) = 2 sin A cos A</strong>",
          "<strong>cos(2A) = cos²A − sin²A = 2cos²A − 1 = 1 − 2sin²A</strong>",
          "<strong>tan(2A) = 2tan A/(1 − tan²A)</strong>",
          "Derived from the sum formulas by setting B = A.")+
       ep("If sin A = 3/5 and cos A = 4/5:<br>sin(2A) = 2(3/5)(4/5) = 24/25."),
       "Practice — Lessons 14–16",
       mc(9,"If cos θ = 1/2, what is cos(2θ) using cos(2θ) = 2cos²θ − 1?",
          [("0",1),("-1/2",0),("1",0),("1/4",0)],0)+
       sa(10,"If sin A = 4/5 and cos A = 3/5, find sin(2A).",["24/25"]))]
    )
  ]
)

# ── A2 Unit 8: Probability & Statistical Inference ──
build_page("algebra2-8.html","Algebra 2",8,"11th Grade Mathematics",
  "Probability &amp; Statistical Inference",
  "Probability &amp;<br>Statistical Inference.",
  "Conditional probability, normal distributions, and making inferences from data.",
  3,"var(--peach)","algebra-2",
  [
    ("Topic A: Probability","Lessons 1–4 · Conditional probability, independence, and experiments.",
     [lesson_row("01–04 — Lessons 1–4","Conditional &amp; Compound Probability","c-peach",
       kl("<strong>P(A|B):</strong> probability of A given B has occurred = P(A∩B)/P(B).",
          "<strong>Independent events:</strong> P(A|B) = P(A). Knowing B gives no info about A.",
          "<strong>Multiplication rule:</strong> P(A∩B) = P(A)·P(B|A).",
          "<strong>Addition rule:</strong> P(A∪B) = P(A) + P(B) − P(A∩B).",
          "<strong>Complement:</strong> P(not A) = 1 − P(A).")+
       ep("P(rain) = 0.3, P(umbrella | rain) = 0.9 → P(rain ∩ umbrella) = 0.3 × 0.9 = <strong>0.27</strong>"),
       "Practice — Lessons 1–4",
       mc(1,"If P(A) = 0.4 and P(B) = 0.5 and A, B are independent, what is P(A∩B)?",
          [("0.9",0),("0.2",1),("0.1",0),("0.04",0)],1)+
       mc(2,"P(A|B) = P(A) tells us that A and B are:",
          [("Mutually exclusive",0),("Dependent",0),("Independent",1),("Complementary",0)],2))]
    ),
    ("Topic B: Normal Distribution","Lessons 5–9 · Properties of normal distributions and z-scores.",
     [lesson_row("05–09 — Lessons 5–9","The Normal Distribution &amp; Z-Scores","c-mint",
       pp("Many real-world distributions are approximately bell-shaped (normal).")+
       kl("<strong>Normal distribution:</strong> symmetric, bell-shaped, mean = median = mode.",
          "<strong>68-95-99.7 rule:</strong> 68% within 1σ, 95% within 2σ, 99.7% within 3σ.",
          "<strong>Z-score:</strong> z = (x − μ)/σ — how many std. deviations from the mean.",
          "A z-score of 0 is exactly at the mean; ±1 is one std dev away.",
          "Use z-tables or calculator to find percentages.")+
       ep("SAT scores: μ = 1000, σ = 200. Score 1200: z = (1200−1000)/200 = <strong>1.0</strong> → top ~16%."),
       "Practice — Lessons 5–9",
       mc(3,"A normal distribution has μ = 70 and σ = 10. What percentage of data falls between 60 and 80?",
          [("99.7%",0),("95%",0),("68%",1),("50%",0)],2)+
       sa(4,"Score = 85, μ = 75, σ = 5. What is the z-score?",["2"]))]
    ),
    ("Topic C: Statistical Inference","Lessons 10–13 · Sampling distributions, margin of error, and drawing conclusions.",
     [lesson_row("10–13 — Lessons 10–13","Sampling &amp; Statistical Inference","c-sky",
       pp("Statistical inference uses sample data to draw conclusions about a population.")+
       kl("<strong>Sample mean (x̄):</strong> estimate of the population mean (μ).",
          "<strong>Sampling variability:</strong> different samples give different estimates.",
          "<strong>Margin of error:</strong> accounts for the variability — typically ±2·(σ/√n).",
          "<strong>Confidence interval:</strong> range where the true parameter likely falls.",
          "Larger sample size → smaller margin of error → more precise estimate.")+
       ep("Sample of 100, x̄ = 52%, σ = 5%: margin of error ≈ 2(5/10) = 1% → interval (51%, 53%)."),
       "Practice — Lessons 10–13",
       mc(5,"A larger sample size results in:",
          [("A larger margin of error",0),
           ("A smaller margin of error",1),
           ("No change in accuracy",0),
           ("A wider confidence interval",0)],1)+
       mc(6,"A confidence interval of (42%, 58%) for a proportion means:",
          [("The true proportion is definitely 50%",0),
           ("We are confident the true proportion is in this range",1),
           ("The sample was biased",0),
           ("42% and 58% are both impossible values",0)],1))]
    )
  ]
)

# ── A2 Unit 9: Limits & Continuity ──
build_page("algebra2-9.html","Algebra 2",9,"11th Grade Mathematics",
  "Limits &amp; Continuity",
  "Limits &amp;<br>Continuity.",
  "An introduction to calculus: limits graphically and algebraically, continuity, and derivatives.",
  4,"var(--sky)","algebra-2",
  [
    ("Topic A: Limits Graphically","Lessons 1–3 · Understanding limits from graphs and tables.",
     [lesson_row("01–03 — Lessons 1–3","Limits from Graphs","c-sky",
       pp("A limit describes the value a function approaches as x gets close to a point — not necessarily the value AT the point.")+
       kl("<strong>Notation:</strong> lim(x→c) f(x) = L means f(x) approaches L as x → c.",
          "<strong>One-sided limits:</strong> lim(x→c⁻) from the left; lim(x→c⁺) from the right.",
          "A limit exists only if the left-hand and right-hand limits are equal.",
          "The limit can exist even if f(c) is undefined.",
          "<strong>Limits at infinity:</strong> describes end behavior as x → ±∞.")+
       ep("f has a hole at x=2. lim(x→2) f(x) = 5, but f(2) is undefined — the limit still equals 5."),
       "Practice — Lessons 1–3",
       mc(1,"lim(x→3) f(x) exists if and only if:",
          [("f(3) is defined",0),
           ("The left and right limits are both equal to the same value",1),
           ("f(x) is increasing near x = 3",0),
           ("f(3) equals the limit",0)],1)+
       mc(2,"A function has lim(x→2⁻) f(x) = 4 and lim(x→2⁺) f(x) = 7. Does lim(x→2) f(x) exist?",
          [("Yes — take the average: 5.5",0),
           ("Yes — it equals 4",0),
           ("No — the one-sided limits are not equal",1),
           ("Yes — it equals 7",0)],2))]
    ),
    ("Topic B: Limits Algebraically","Lessons 4–6 · Direct substitution, factoring, and indeterminate forms.",
     [lesson_row("04–06 — Lessons 4–6","Evaluating Limits Algebraically","c-peach",
       kl("<strong>Direct substitution:</strong> if f is continuous at c, then lim(x→c) f(x) = f(c).",
          "<strong>Indeterminate form 0/0:</strong> factor, cancel, then substitute.",
          "<strong>Rationalize:</strong> multiply by conjugate when radicals cause 0/0.",
          "<strong>Squeeze theorem:</strong> if g(x) ≤ f(x) ≤ h(x) and both limits equal L, then lim f(x) = L.")+
       ep("lim(x→2) (x²−4)/(x−2) → substitute gives 0/0 → factor: (x+2)(x−2)/(x−2) = x+2 → lim = <strong>4</strong>"),
       "Practice — Lessons 4–6",
       sa(3,"Find lim(x→3) (x² − 9)/(x − 3) by factoring.",["6"])+
       mc(4,"When direct substitution gives 0/0, this is called:",
          [("An undefined limit",0),
           ("An indeterminate form",1),
           ("A removable discontinuity only",0),
           ("Proof the limit doesn't exist",0)],1))]
    ),
    ("Topic C: Continuity &amp; Introduction to Derivatives","Lessons 7–9 · Continuity conditions and the concept of a derivative.",
     [lesson_row("07–09 — Lessons 7–9","Continuity &amp; Derivatives","c-lilac",
       pp("A function is continuous at x = c if: (1) f(c) exists, (2) lim(x→c) f(x) exists, (3) they are equal.")+
       kl("<strong>Types of discontinuity:</strong> removable (hole), jump, infinite (asymptote).",
          "<strong>Derivative:</strong> the instantaneous rate of change at a point.",
          "<strong>f'(x) = lim(h→0) [f(x+h) − f(x)] / h</strong> — the limit of the difference quotient.",
          "The derivative at a point = the slope of the tangent line to f at that point.",
          "If f'(x) &gt; 0, f is increasing; if f'(x) &lt; 0, f is decreasing.")+
       ep("f(x) = x². f'(x) = lim(h→0) [(x+h)² − x²]/h = lim(h→0) (2x+h) = <strong>2x</strong>."),
       "Practice — Lessons 7–9",
       mc(5,"A function is NOT continuous at x = 4 if:",
          [("f(4) = 0",0),
           ("f(4) is defined but ≠ lim(x→4) f(x)",1),
           ("The function has a negative value at x = 4",0),
           ("The derivative is 0 at x = 4",0)],1)+
       mc(6,"The derivative f'(c) represents:",
          [("The average rate of change over an interval",0),
           ("The y-value of f at x = c",0),
           ("The slope of the tangent line to f at x = c",1),
           ("The area under the curve at x = c",0)],2))]
    )
  ]
)

print("Done with Algebra 2 (units 5-9)!")
