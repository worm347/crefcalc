import os, sys
exec(open('/sessions/serene-wonderful-mayer/mnt/outputs/gen_pages.py').read().split('# ════════════════════')[0])
OUTPUT_DIR = "/sessions/serene-wonderful-mayer/mnt/outputs"

# ════════════════════════════════════════════════════
# GEOMETRY UNITS 1–8
# ════════════════════════════════════════════════════

# Unit 1: Constructions, Proof, and Rigid Motion
build_page("geometry-1.html","Geometry",1,"10th Grade Mathematics",
  "Constructions, Proof &amp; Rigid Motion",
  "Constructions, Proof<br>&amp; Rigid Motion.",
  "Compass-and-straightedge constructions, formal geometric proofs, and an introduction to rigid motions.",
  0,"var(--mint)","geometry",
  [
    ("Topic A: Compass &amp; Straightedge Constructions","Lessons 1–6 · Basic constructions using only compass and straightedge.",
     [lesson_row("01–03 — Lessons 1–3","Basic Constructions","c-mint",
       pp("Geometric constructions use only a compass (for circles/arcs) and a straightedge (for lines — no measurements).")+
       kl("<strong>Copy a segment:</strong> use compass to transfer length.",
          "<strong>Copy an angle:</strong> reproduce the angle's arc and chord at a new vertex.",
          "<strong>Perpendicular bisector:</strong> find midpoint of segment; line perpendicular to it.",
          "<strong>Angle bisector:</strong> divide an angle into two equal halves.",
          "Constructions are exact — no measuring with rulers or protractors.")+
       ep("Perpendicular bisector of AB: set compass &gt; AB/2, draw arcs from A and B, connect the intersections."),
       "Practice — Lessons 1–3",
       mc(1,"What is the purpose of the perpendicular bisector of a segment?",
          [("It extends the segment",0),("It finds the midpoint and is perpendicular to the segment",1),("It copies the segment",0),("It measures the segment's length",0)],1)+
       mc(2,"In a construction, a 'straightedge' is used to:",
          [("Measure lengths",0),("Draw arcs",0),("Draw straight lines through points",1),("Mark right angles",0)],2)),
      lesson_row("04–06 — Lessons 4–6","Circle Constructions &amp; Special Figures","c-butter",
       kl("Inscribed circle: tangent to all sides of a triangle (incircle) — constructed using angle bisectors.",
          "Circumscribed circle: passes through all vertices (circumcircle) — constructed using perpendicular bisectors.",
          "<strong>Equilateral triangle:</strong> set compass = side length, draw arcs from endpoints.",
          "<strong>Regular hexagon:</strong> radius = side length, mark 6 points around center circle.",
          "<strong>Square:</strong> use perpendicular bisectors and circle.")+
       ep("To construct an equilateral triangle: draw segment AB, arc from A (radius AB), arc from B — their intersection is C."),
       "Practice — Lessons 4–6",
       mc(3,"The circumscribed circle of a triangle passes through:",
          [("The midpoints of each side",0),("The feet of each altitude",0),("All three vertices",1),("The centroid",0)],2)+
       mc(4,"Which center is found using angle bisectors?",
          [("Circumcenter",0),("Centroid",0),("Incenter",1),("Orthocenter",0)],2))]
    ),
    ("Topic B: Formal Proof","Lessons 7–12 · Two-column proofs, paragraph proofs, and geometric reasoning.",
     [lesson_row("07–09 — Lessons 7–9","Introduction to Geometric Proof","c-lilac",
       pp("Geometric proof uses definitions, postulates, and previously proven theorems to establish that a statement is always true.")+
       kl("<strong>Given:</strong> information you are told is true.",
          "<strong>Prove:</strong> the statement you must show is true.",
          "<strong>Two-column proof:</strong> statements on left, reasons on right.",
          "<strong>Reasons:</strong> definition, postulate, theorem, or given.",
          "Each step follows logically from what came before.")+
       ep("Given: AB ≅ CD, CD ≅ EF. Prove: AB ≅ EF. Reason: Transitive Property of Congruence."),
       "Practice — Lessons 7–9",
       mc(5,"In a two-column proof, the right column lists:",
          [("The conclusion",0),("The given information only",0),("Reasons (definitions, postulates, theorems)",1),("The diagram labels",0)],2)+
       mc(6,"If AB = BC and BC = CD, then AB = CD by the:",
          [("Reflexive Property",0),("Symmetric Property",0),("Transitive Property",1),("Substitution Property",0)],2)),
      lesson_row("10–12 — Lessons 10–12","Angle Relationships &amp; Proofs","c-sky",
       kl("<strong>Vertical angles:</strong> congruent. (Formed by two intersecting lines, across from each other.)",
          "<strong>Linear pair:</strong> supplementary (add to 180°).",
          "<strong>Complementary:</strong> two angles adding to 90°.",
          "<strong>Transversal + parallel lines:</strong> alternate interior angles ≅, corresponding angles ≅, co-interior angles supplementary.",
          "Use these theorems as reasons in proofs.")+
       ep("Given: ∠1 and ∠2 are vertical angles. Prove: ∠1 ≅ ∠2. Reason: Vertical Angles Theorem."),
       "Practice — Lessons 10–12",
       mc(7,"Two parallel lines are cut by a transversal. Alternate interior angles are:",
          [("Supplementary",0),("Complementary",0),("Congruent",1),("Not necessarily related",0)],2)+
       sa(8,"If ∠A and ∠B are supplementary and ∠A = 65°, what is ∠B?",["115","115°"]))]
    ),
    ("Topic C: Rigid Motions","Lessons 13–19 · Translations, reflections, rotations, and composites.",
     [lesson_row("13–15 — Lessons 13–15","Translations &amp; Reflections","c-peach",
       kl("<strong>Rigid motion (isometry):</strong> a transformation that preserves distance and angle measure.",
          "<strong>Translation:</strong> slides a figure. Vector notation (a, b): move right a, up b.",
          "<strong>Reflection:</strong> flips a figure over a line of reflection.",
          "Reflect over x-axis: (x, y) → (x, −y).",
          "Reflect over y-axis: (x, y) → (−x, y).",
          "Reflect over y = x: (x, y) → (y, x).")+
       ep("Point A(3, 5) reflected over x-axis → A'(3, −5). Reflected over y-axis → A'(−3, 5)."),
       "Practice — Lessons 13–15",
       mc(9,"A translation moves a figure 3 right and 2 down. Point (5, 7) maps to:",
          [("(8, 5)",1),("(2, 9)",0),("(8, 9)",0),("(3, 2)",0)],0)+
       sa(10,"Reflect (4, −3) over the y-axis. Give the x-coordinate of the image.",["−4","-4"])),
      lesson_row("16–19 — Lessons 16–19","Rotations &amp; Composition","c-mint",
       kl("<strong>Rotation:</strong> turns a figure around a center point by an angle.",
          "Rotate 90° CCW about origin: (x, y) → (−y, x).",
          "Rotate 180° about origin: (x, y) → (−x, −y).",
          "Rotate 270° CCW (= 90° CW): (x, y) → (y, −x).",
          "<strong>Composition:</strong> apply two or more transformations in sequence.",
          "A glide reflection = translation + reflection.")+
       ep("Rotate (2, 3) by 90° CCW about origin: (2, 3) → (−3, 2)."),
       "Practice — Lessons 16–19",
       mc(11,"Point (5, −2) is rotated 180° about the origin. The image is:",
          [("(2, 5)",0),("(−5, 2)",1),("(−2, −5)",0),("(5, 2)",0)],1)+
       mc(12,"A composition of two reflections over parallel lines is equivalent to a:",
          [("Rotation",0),("Translation",1),("Reflection",0),("Dilation",0)],1))]
    )
  ]
)

# Unit 2: Congruence in Two Dimensions
build_page("geometry-2.html","Geometry",2,"10th Grade Mathematics",
  "Congruence in Two Dimensions",
  "Congruence in<br>Two Dimensions.",
  "Rigid motions and congruence, triangle congruence criteria, and CPCTC proofs.",
  1,"var(--peach)","geometry",
  [
    ("Topic A: Rigid Motions &amp; Congruence","Lessons 1–6 · Defining congruence through transformations.",
     [lesson_row("01–04 — Lessons 1–4","Congruence via Rigid Motions","c-peach",
       kl("<strong>Two figures are congruent</strong> if one can be mapped to the other by a rigid motion (or composition of rigid motions).",
          "Congruent figures have the same shape AND size.",
          "Corresponding parts of congruent figures are congruent.",
          "Write congruence statements in order of corresponding parts: △ABC ≅ △DEF means A↔D, B↔E, C↔F.",
          "Use rigid motions to identify which transformation maps one to the other.")+
       ep("△ABC ≅ △DEF means: ∠A ≅ ∠D, ∠B ≅ ∠E, ∠C ≅ ∠F, AB ≅ DE, BC ≅ EF, AC ≅ DF."),
       "Practice — Lessons 1–4",
       mc(1,"If △ABC ≅ △DEF, which pair of corresponding angles are congruent?",
          [("∠A ≅ ∠E",0),("∠B ≅ ∠D",0),("∠C ≅ ∠F",1),("∠A ≅ ∠F",0)],2)+
       mc(2,"Two figures are congruent if and only if:",
          [("They have the same area",0),("One can be mapped to the other by a rigid motion",1),("They are both triangles",0),("They have the same perimeter",0)],1)),
      lesson_row("05–06 — Lessons 5–6","Properties of Parallelograms","c-mint",
       kl("<strong>Parallelogram:</strong> opposite sides parallel and congruent; opposite angles congruent; diagonals bisect each other.",
          "<strong>Rectangle:</strong> parallelogram with 4 right angles; diagonals are congruent.",
          "<strong>Rhombus:</strong> parallelogram with 4 congruent sides; diagonals are perpendicular.",
          "<strong>Square:</strong> both a rectangle and a rhombus.",
          "Prove it's a parallelogram by showing: 2 pairs of parallel sides, OR 2 pairs of congruent opposite sides, OR diagonals bisect each other.")+
       ep("In parallelogram ABCD: AB ∥ CD, AB ≅ CD, ∠A ≅ ∠C, diagonals AC and BD bisect each other."),
       "Practice — Lessons 5–6",
       mc(3,"In a parallelogram, the diagonals:",
          [("Are perpendicular",0),("Are congruent",0),("Bisect each other",1),("Bisect the angles",0)],2)+
       mc(4,"Which quadrilateral has both perpendicular AND congruent diagonals?",
          [("Rectangle",0),("Rhombus",0),("Parallelogram",0),("Square",1)],3))]
    ),
    ("Topic B: Triangle Congruence Criteria","Lessons 7–12 · SSS, SAS, ASA, AAS, and HL.",
     [lesson_row("07–09 — Lessons 7–9","Triangle Congruence Shortcuts","c-lilac",
       kl("<strong>SSS:</strong> three pairs of congruent sides → triangles congruent.",
          "<strong>SAS:</strong> two sides and the included angle → congruent.",
          "<strong>ASA:</strong> two angles and the included side → congruent.",
          "<strong>AAS:</strong> two angles and a non-included side → congruent.",
          "<strong>HL (Hypotenuse-Leg):</strong> right triangles only — hypotenuse + leg → congruent.",
          "AAA and SSA do NOT prove congruence.")+
       ep("Given two sides AB ≅ DE and BC ≅ EF, and included ∠B ≅ ∠E → △ABC ≅ △DEF by SAS."),
       "Practice — Lessons 7–9",
       mc(5,"Two triangles have all three pairs of angles congruent (AAA). Are they congruent?",
          [("Yes — AAA always gives congruence",0),("No — AAA only gives similarity, not congruence",1),("Only if they are equilateral",0),("Only if one is a right triangle",0)],1)+
       mc(6,"You know AB ≅ DE, BC ≅ EF, and ∠B ≅ ∠E. What congruence criterion applies?",
          [("SSS",0),("SAS",1),("ASA",0),("AAS",0)],1)),
      lesson_row("10–12 — Lessons 10–12","CPCTC Proofs","c-sky",
       pp("Once triangles are proven congruent, CPCTC allows you to conclude that corresponding parts are congruent.")+
       kl("<strong>CPCTC:</strong> Corresponding Parts of Congruent Triangles are Congruent.",
          "Used as a reason AFTER you establish triangle congruence.",
          "Common proof structure: Given → prove triangles congruent (SSS/SAS/etc.) → apply CPCTC.",
          "Can prove segments, angles, or even parallel/perpendicular lines using CPCTC.")+
       ep("Prove △ABD ≅ △CBD by SAS. Then AB ≅ CB by CPCTC."),
       "Practice — Lessons 10–12",
       mc(7,"CPCTC can be used as a reason in a proof:",
          [("Before proving triangles are congruent",0),("Only if SSS was used",0),("After two triangles have been proven congruent",1),("To prove the triangles are congruent",0)],2)+
       mc(8,"CPCTC stands for:",
          [("Congruent Parts Connect Two Circles",0),("Corresponding Parts of Congruent Triangles are Congruent",1),("Congruence Proof Creates Triangle Confirmation",0),("Corresponding Perpendicular Congruent Triangle Criterion",0)],1))]
    ),
    ("Topic C: Quadrilateral Proofs","Lessons 13–18 · Proving quadrilaterals are parallelograms, rectangles, rhombi, or squares.",
     [lesson_row("13–18 — Lessons 13–18","Proving Special Quadrilaterals","c-butter",
       kl("Prove a parallelogram by: opposite sides ∥, opposite sides ≅, diagonals bisect each other, or one pair of sides both ∥ and ≅.",
          "Prove a rectangle: parallelogram + one right angle, OR parallelogram + congruent diagonals.",
          "Prove a rhombus: parallelogram + two consecutive sides ≅, OR parallelogram + perpendicular diagonals.",
          "Prove a square: show it is both a rectangle AND a rhombus.",
          "Use coordinates: slope for parallel/perpendicular, distance formula for congruent sides.")+
       ep("Given that both pairs of opposite sides of ABCD are congruent → ABCD is a parallelogram."),
       "Practice — Lessons 13–18",
       mc(9,"To prove a quadrilateral is a rectangle, you need to show it is a parallelogram and:",
          [("Has four congruent sides",0),("Has one right angle",1),("Has perpendicular diagonals",0),("Has two right angles only",0)],1)+
       mc(10,"In a rhombus, the diagonals are always:",
          [("Congruent",0),("Parallel",0),("Perpendicular bisectors of each other",1),("Equal to the sides",0)],2))]
    )
  ]
)

# Unit 3: Dilations and Similarity
build_page("geometry-3.html","Geometry",3,"10th Grade Mathematics",
  "Dilations &amp; Similarity",
  "Dilations &amp;<br>Similarity.",
  "Dilations, scale factor, similarity criteria, and solving with similar triangles.",
  2,"var(--lilac)","geometry",
  [
    ("Topic A: Dilations","Lessons 1–5 · Scale factor, center of dilation, and properties.",
     [lesson_row("01–03 — Lessons 1–3","Dilations &amp; Scale Factor","c-lilac",
       kl("<strong>Dilation:</strong> a transformation that enlarges or shrinks a figure by a scale factor k, from a center point.",
          "<strong>Scale factor k &gt; 1:</strong> enlargement. <strong>0 &lt; k &lt; 1:</strong> reduction.",
          "The image is similar (same shape) to the pre-image, not congruent (unless k=1).",
          "Dilation from origin: multiply both coordinates by k. (x,y) → (kx, ky).",
          "Distances scale by k; areas scale by k².")+
       ep("Dilation with k=3 from origin: A(2,4) → A'(6,12). Side length triples; area × 9."),
       "Practice — Lessons 1–3",
       mc(1,"A dilation with scale factor 1/2 from the origin maps (8, 6) to:",
          [("(16, 12)",0),("(4, 3)",1),("(8, 3)",0),("(4, 6)",0)],1)+
       mc(2,"If a dilation has scale factor k = 3, how does the area change?",
          [("Triples",0),("Multiplies by 9",1),("Stays the same",0),("Doubles",0)],1)),
      lesson_row("04–05 — Lessons 4–5","Properties of Dilations","c-sky",
       kl("A dilation maps a line through the center of dilation to itself.",
          "A line NOT through the center maps to a parallel line.",
          "Angle measures are preserved under dilation.",
          "The ratio of any two corresponding lengths = k (the scale factor).",
          "Dilations produce similar figures: same shape, different (or equal) size.")+
       ep("△ABC dilated by k=2 to △A'B'C'. All angles equal; all sides doubled. Perimeter doubles; area ×4."),
       "Practice — Lessons 4–5",
       mc(3,"After a dilation, which is preserved?",
          [("Side lengths",0),("Angle measures",1),("Area",0),("Perimeter",0)],1)+
       mc(4,"A line through the center of dilation maps to:",
          [("A parallel line",0),("Itself",1),("A perpendicular line",0),("A point",0)],1))]
    ),
    ("Topic B: Similarity Criteria","Lessons 6–11 · AA, SAS~, SSS~ and proving similarity.",
     [lesson_row("06–08 — Lessons 6–8","Triangle Similarity Shortcuts","c-peach",
       kl("<strong>AA (Angle-Angle):</strong> two pairs of congruent angles → triangles similar.",
          "<strong>SAS~ (Side-Angle-Side):</strong> two sides proportional and included angle ≅ → similar.",
          "<strong>SSS~ (Side-Side-Side):</strong> all three pairs of sides proportional → similar.",
          "Similar triangles: ∠s congruent, sides proportional (ratio = scale factor).",
          "Notation: △ABC ∼ △DEF (order matters — corresponding vertices listed).")+
       ep("△ABC ∼ △DEF with k = 2: if AB = 4, then DE = 8. If ∠A = 50°, then ∠D = 50°."),
       "Practice — Lessons 6–8",
       mc(5,"Two triangles each have angles 40° and 70°. By AA, they are:",
          [("Congruent",0),("Similar",1),("Neither — you need 3 angles",0),("Congruent only if they are right triangles",0)],1)+
       mc(6,"For SAS~ similarity, you need:",
          [("Two congruent angles",0),("Two congruent sides and any angle",0),("Two proportional sides and the included angle congruent",1),("All three sides proportional",0)],2)),
      lesson_row("09–11 — Lessons 9–11","Applying Similar Triangles","c-mint",
       kl("Set up proportions using corresponding sides of similar triangles.",
          "<strong>Cross-multiply</strong> to solve for unknown lengths.",
          "<strong>Altitude to hypotenuse:</strong> creates two smaller triangles, each similar to the original.",
          "<strong>Geometric mean:</strong> altitude h = √(p·q), where p, q are the two segments of the hypotenuse.",
          "Use similar triangles to find indirect measurements (shadow, mirror methods).")+
       ep("△ABC ∼ △DEF. AB/DE = BC/EF = AC/DF. If AB=6, DE=9, BC=8 → EF = 8·(9/6) = 12."),
       "Practice — Lessons 9–11",
       sa(7,"△ABC ∼ △DEF. AB = 4, DE = 10, BC = 6. Find EF.",["15"])+
       mc(8,"You use a mirror on the ground to find a tree's height. The similar triangles method relies on:",
          [("ASA congruence",0),("AA similarity (equal angles of incidence and reflection)",1),("SAS congruence",0),("SSS similarity",0)],1))]
    ),
    ("Topic C: Proportional Relationships","Lessons 12–18 · Triangle proportionality theorem and other results.",
     [lesson_row("12–18 — Lessons 12–18","Proportionality Theorems","c-butter",
       kl("<strong>Triangle Proportionality Theorem:</strong> a line parallel to one side of a triangle divides the other two sides proportionally.",
          "<strong>Converse:</strong> if a line divides two sides proportionally, it is parallel to the third.",
          "<strong>Midsegment:</strong> connects midpoints of two sides; parallel to the third side and half as long.",
          "<strong>Angle bisector theorem:</strong> the bisector of an angle divides the opposite side proportionally.",
          "<strong>Side-splitter:</strong> if two triangles share a common angle and their sides are proportional, they are similar.")+
       ep("In △ABC, midsegment MN (M on AB, N on AC): MN ∥ BC and MN = BC/2."),
       "Practice — Lessons 12–18",
       mc(9,"The midsegment of a triangle is:",
          [("Half the perimeter",0),("Parallel to the third side and half its length",1),("Congruent to the altitude",0),("Equal to the median",0)],1)+
       sa(10,"In a triangle, a midsegment is 7 cm. How long is the parallel base?",["14","14 cm"]))]
    )
  ]
)

# Unit 4: Right Triangles and Trigonometry
build_page("geometry-4.html","Geometry",4,"10th Grade Mathematics",
  "Right Triangles &amp; Trigonometry",
  "Right Triangles &amp;<br>Trigonometry.",
  "Pythagorean theorem, special right triangles, and trigonometric ratios.",
  3,"var(--sky)","geometry",
  [
    ("Topic A: Pythagorean Theorem","Lessons 1–6 · Proof, Pythagorean triples, and distance in coordinates.",
     [lesson_row("01–03 — Lessons 1–3","The Pythagorean Theorem","c-sky",
       kl("<strong>Theorem:</strong> in a right triangle, a² + b² = c² (c = hypotenuse).",
          "<strong>Converse:</strong> if a² + b² = c², the triangle is a right triangle.",
          "<strong>Pythagorean triples:</strong> 3-4-5, 5-12-13, 8-15-17, and their multiples.",
          "<strong>Acute triangle:</strong> a² + b² &gt; c². <strong>Obtuse:</strong> a² + b² &lt; c².",
          "Used to find missing sides in right triangles.")+
       ep("a=5, b=12: c = √(25+144) = √169 = <strong>13</strong>. It's a 5-12-13 triple."),
       "Practice — Lessons 1–3",
       sa(1,"Find the hypotenuse of a right triangle with legs 9 and 12.",["15"])+
       mc(2,"Triangle sides are 7, 10, and 12. Is it acute, right, or obtuse?",
          [("Right — 7²+10² = 12²",0),("Obtuse — 7²+10² &lt; 12²",1),("Acute — 7²+10² &gt; 12²",0),("Can't determine without an angle",0)],1)),
      lesson_row("04–06 — Lessons 4–6","Distance Formula &amp; Coordinate Geometry","c-peach",
       kl("<strong>Distance formula:</strong> d = √[(x₂−x₁)² + (y₂−y₁)²] — derived from Pythagorean theorem.",
          "<strong>Midpoint formula:</strong> ((x₁+x₂)/2, (y₁+y₂)/2).",
          "Use to prove figures are squares, rectangles, parallelograms, etc., on a coordinate plane.",
          "Show perpendicular by: slopes are negative reciprocals (m₁ · m₂ = −1).",
          "Show parallel by: slopes are equal.")+
       ep("Distance from (1, 2) to (4, 6): d = √[(3)²+(4)²] = √25 = 5."),
       "Practice — Lessons 4–6",
       sa(3,"Find the distance from (0, 0) to (5, 12).",["13"])+
       mc(4,"The midpoint of (2, 8) and (6, 4) is:",
          [("(4, 6)",1),("(3, 5)",0),("(8, 12)",0),("(2, 4)",0)],0))]
    ),
    ("Topic B: Special Right Triangles","Lessons 7–12 · 45-45-90 and 30-60-90 triangles.",
     [lesson_row("07–09 — Lessons 7–9","45-45-90 Triangles","c-mint",
       kl("<strong>45-45-90 triangle:</strong> an isosceles right triangle.",
          "Leg : Leg : Hypotenuse = <strong>x : x : x√2</strong>",
          "Hypotenuse = leg × √2. Leg = hypotenuse / √2.",
          "Formed by cutting a square diagonally.",
          "Memorize the ratio — it speeds up many geometry problems.")+
       ep("Leg = 5: hypotenuse = 5√2. &nbsp;·&nbsp; Hypotenuse = 8: leg = 8/√2 = 4√2."),
       "Practice — Lessons 7–9",
       sa(5,"A 45-45-90 triangle has legs of length 6. What is the hypotenuse?",["6√2","6 root 2"])+
       mc(6,"In a 45-45-90 triangle, the hypotenuse is 10. What is each leg?",
          [("5",0),("10√2",0),("5√2",1),("10/√2 = 5√2",0)],2)),
      lesson_row("10–12 — Lessons 10–12","30-60-90 Triangles","c-lilac",
       kl("<strong>30-60-90 triangle:</strong> Short leg : Long leg : Hypotenuse = <strong>x : x√3 : 2x</strong>",
          "Short leg (opp 30°) = hypotenuse / 2.",
          "Long leg (opp 60°) = short leg × √3.",
          "Hypotenuse = 2 × short leg.",
          "Formed by cutting an equilateral triangle in half.")+
       ep("Short leg = 4: long leg = 4√3, hypotenuse = 8. &nbsp;·&nbsp; Hypotenuse = 12: short leg = 6, long leg = 6√3."),
       "Practice — Lessons 10–12",
       sa(7,"In a 30-60-90 triangle, the short leg is 7. What is the hypotenuse?",["14"])+
       mc(8,"In a 30-60-90 triangle, which side is the longest?",
          [("The side opposite 30°",0),("The side opposite 60°",0),("The hypotenuse (opposite 90°)",1),("They are all equal",0)],2))]
    ),
    ("Topic C: Trigonometric Ratios","Lessons 13–19 · SOH-CAH-TOA, inverse trig, and applications.",
     [lesson_row("13–16 — Lessons 13–16","SOH-CAH-TOA","c-butter",
       kl("<strong>sin θ</strong> = opposite / hypotenuse",
          "<strong>cos θ</strong> = adjacent / hypotenuse",
          "<strong>tan θ</strong> = opposite / adjacent",
          "Memory aid: <strong>SOH-CAH-TOA</strong>.",
          "Use a calculator in degree mode to find decimal values.",
          "<strong>Pythagorean identity:</strong> sin²θ + cos²θ = 1.")+
       ep("In a right △ with θ = 30°, hyp = 10: opp = 10·sin30° = 5, adj = 10·cos30° = 5√3."),
       "Practice — Lessons 13–16",
       mc(9,"In a right triangle, sin(θ) = 7/25. What is cos(θ)?",
          [("7/24",0),("24/25",1),("25/7",0),("7/25",0)],1)+
       sa(10,"A ladder leans against a wall, making a 60° angle with the ground. The ladder is 20 ft. How high up the wall? (sin60°=√3/2)",["10√3","10 root 3"])),
      lesson_row("17–19 — Lessons 17–19","Inverse Trig &amp; Angle of Elevation/Depression","c-sky",
       kl("<strong>Inverse trig:</strong> sin⁻¹(x), cos⁻¹(x), tan⁻¹(x) — find the angle given a ratio.",
          "<strong>Angle of elevation:</strong> measured upward from horizontal.",
          "<strong>Angle of depression:</strong> measured downward from horizontal.",
          "Elevation and depression angles are alternate interior angles — they are equal.",
          "Draw a diagram, label, then write the trig ratio.")+
       ep("tan(θ) = 40/30 → θ = tan⁻¹(4/3) ≈ 53.1°."),
       "Practice — Lessons 17–19",
       mc(11,"You're standing 50 m from a tower. The angle of elevation to the top is 35°. Which equation finds the height h?",
          [("h = 50·cos(35°)",0),("h = 50·tan(35°)",1),("h = 50/sin(35°)",0),("h = 50/tan(35°)",0)],1)+
       mc(12,"The angle of depression from a cliff to a boat is 28°. The angle of elevation from the boat to the cliff is:",
          [("62°",0),("28°",1),("90°",0),("Cannot be determined",0)],1))]
    )
  ]
)

# Unit 5: Polygons and Algebraic Relationships
build_page("geometry-5.html","Geometry",5,"10th Grade Mathematics",
  "Polygons &amp; Algebraic Relationships",
  "Polygons &amp;<br>Algebraic Relationships.",
  "Coordinate geometry, slope criteria, and calculating area and perimeter of polygons.",
  4,"var(--butter)","geometry",
  [
    ("Topic A: Coordinate Geometry","Lessons 1–5 · Distance, slope, and proving properties with coordinates.",
     [lesson_row("01–03 — Lessons 1–3","Slope &amp; Parallel/Perpendicular Lines","c-butter",
       kl("<strong>Slope formula:</strong> m = (y₂−y₁)/(x₂−x₁).",
          "<strong>Parallel lines:</strong> equal slopes (m₁ = m₂).",
          "<strong>Perpendicular lines:</strong> slopes are negative reciprocals (m₁ · m₂ = −1).",
          "Horizontal line: slope = 0. Vertical line: undefined slope.",
          "Use coordinates to prove that a quadrilateral is a special type.")+
       ep("Slope of AB = 2/3. A perpendicular line has slope −3/2."),
       "Practice — Lessons 1–3",
       mc(1,"Line 1 has slope 4. A perpendicular line has slope:",
          [("4",0),("−4",0),("−1/4",1),("1/4",0)],2)+
       sa(2,"Are the lines through (0,0)→(3,6) and (0,0)→(6,3) perpendicular? (slopes: 2 and 1/2)",["no","No"])),
      lesson_row("04–05 — Lessons 4–5","Coordinate Proofs","c-sky",
       kl("Place figures strategically on the coordinate plane to simplify proofs.",
          "<strong>Common placements:</strong> put one vertex at origin, one side along an axis.",
          "Use distance formula to show sides are congruent.",
          "Use slope formula to show sides are parallel or perpendicular.",
          "Use midpoint formula to show diagonals bisect each other.")+
       ep("To prove a quadrilateral is a parallelogram: show both pairs of opposite sides have equal slopes."),
       "Practice — Lessons 4–5",
       mc(3,"To prove a quadrilateral is a rectangle using coordinates, you show:",
          [("All sides are equal length",0),("Opposite sides are equal length and parallel",0),("All four angles are 90° by showing adjacent sides have perpendicular slopes",1),("The diagonals are perpendicular",0)],2)+
       mc(4,"Placing a right angle at the origin in a coordinate proof is helpful because:",
          [("It makes all calculations involve zero, simplifying them",1),("It proves the triangle is isosceles",0),("It creates a special right triangle",0),("It guarantees the hypotenuse is horizontal",0)],0))]
    ),
    ("Topic B: Area &amp; Perimeter of Polygons","Lessons 6–10 · Calculating and comparing polygon measurements.",
     [lesson_row("06–08 — Lessons 6–8","Area Formulas","c-mint",
       kl("<strong>Triangle:</strong> A = (1/2)bh.",
          "<strong>Parallelogram:</strong> A = bh.",
          "<strong>Trapezoid:</strong> A = (1/2)(b₁+b₂)h.",
          "<strong>Regular polygon:</strong> A = (1/2)·apothem·perimeter.",
          "On coordinate plane: use the Shoelace formula or decompose into triangles/rectangles.",
          "All altitudes must be perpendicular to the base.")+
       ep("Trapezoid with b₁=6, b₂=10, h=4: A = (1/2)(16)(4) = 32 sq units."),
       "Practice — Lessons 6–8",
       sa(5,"Find the area of a triangle with base 14 and height 9.",["63"])+
       mc(6,"A trapezoid has parallel bases 8 and 12, and height 5. Area = ?",
          [("100",0),("50",1),("40",0),("80",0)],1)),
      lesson_row("09–10 — Lessons 9–10","Perimeter &amp; Composite Figures","c-lilac",
       kl("<strong>Perimeter:</strong> sum of all side lengths.",
          "For composite figures: break into simpler shapes, find each area/perimeter.",
          "When a region is 'removed,' subtract its area from the whole.",
          "<strong>Coordinate perimeter:</strong> use the distance formula for each side.",
          "<strong>Regular polygon perimeter:</strong> n × side length.")+
       ep("L-shaped figure: find total rectangle area, subtract the missing corner area."),
       "Practice — Lessons 9–10",
       mc(7,"A composite figure is formed by adding a triangle to a rectangle. Its area is:",
          [("Rectangle area × triangle area",0),("Rectangle area + triangle area",1),("Rectangle area − triangle area",0),("(Rectangle area + triangle area)/2",0)],1)+
       sa(8,"A regular hexagon has side length 6. Its perimeter is:",["36"]))]
    ),
    ("Topic C: Interior &amp; Exterior Angles","Lessons 11–15 · Angle sums in polygons.",
     [lesson_row("11–15 — Lessons 11–15","Polygon Angle Sums","c-peach",
       kl("<strong>Interior angle sum of n-gon:</strong> S = (n−2)·180°.",
          "<strong>Each interior angle of regular n-gon:</strong> (n−2)·180° / n.",
          "<strong>Exterior angle sum:</strong> always 360° for any convex polygon.",
          "<strong>Each exterior angle of regular n-gon:</strong> 360°/n.",
          "Interior + exterior angle at each vertex = 180°.")+
       ep("Pentagon (n=5): interior sum = (3)(180°) = 540°. Each angle in regular pentagon = 108°."),
       "Practice — Lessons 11–15",
       sa(9,"What is the interior angle sum of an octagon (8 sides)?",["1080","1080°"])+
       mc(10,"Each exterior angle of a regular hexagon measures:",
          [("120°",0),("60°",1),("90°",0),("72°",0)],1))]
    )
  ]
)

# Unit 6: Three-Dimensional Measurement and Application
build_page("geometry-6.html","Geometry",6,"10th Grade Mathematics",
  "Three-Dimensional Measurement",
  "Three-Dimensional<br>Measurement.",
  "Cross sections, volume and surface area of 3D figures, and modeling with shapes.",
  0,"var(--lilac)","geometry",
  [
    ("Topic A: Cross Sections &amp; 3D Figures","Lessons 1–5 · Identifying and analyzing cross sections.",
     [lesson_row("01–03 — Lessons 1–3","Cross Sections of 3D Figures","c-lilac",
       kl("<strong>Cross section:</strong> the 2D shape formed when a plane intersects a 3D solid.",
          "Horizontal cross section of a cylinder → circle.",
          "Vertical cross section of a cylinder → rectangle.",
          "Diagonal cross section of a cube → rectangle or hexagon.",
          "Cross section of a cone → circle (horizontal) or triangle (vertical through apex).",
          "Cross section of a sphere → always a circle.")+
       ep("A square pyramid cut horizontally → smaller square. Cut vertically through apex → triangle."),
       "Practice — Lessons 1–3",
       mc(1,"A vertical cross section through the apex of a cone produces:",
          [("A circle",0),("An ellipse",0),("A triangle",1),("A trapezoid",0)],2)+
       mc(2,"A horizontal cross section of a cylinder is:",
          [("A rectangle",0),("An oval",0),("A circle",1),("A square",0)],2)),
      lesson_row("04–05 — Lessons 4–5","Nets &amp; Surface Area Introduction","c-mint",
       kl("<strong>Net:</strong> an unfolded 2D representation of a 3D solid.",
          "Each face of the 3D solid appears as a polygon in the net.",
          "Surface area = total area of all faces (add up the net's pieces).",
          "Cube net: 6 equal squares.",
          "Rectangular prism net: 3 pairs of rectangles.")+
       ep("A cube with side 4: SA = 6 × (4×4) = 96 sq units."),
       "Practice — Lessons 4–5",
       mc(3,"The net of a triangular prism consists of:",
          [("3 triangles and 2 rectangles",0),("2 triangles and 3 rectangles",1),("5 rectangles",0),("3 triangles and 3 rectangles",0)],1)+
       sa(4,"A cube has side length 5. What is its surface area?",["150"]))]
    ),
    ("Topic B: Volume","Lessons 6–11 · Volume formulas for all standard 3D shapes.",
     [lesson_row("06–08 — Lessons 6–8","Volume of Prisms &amp; Cylinders","c-sky",
       kl("<strong>Prism:</strong> V = Base Area × height = Bh.",
          "<strong>Rectangular prism (box):</strong> V = l × w × h.",
          "<strong>Triangular prism:</strong> V = (1/2)bh × length.",
          "<strong>Cylinder:</strong> V = πr²h.",
          "A prism has two congruent parallel bases. The lateral faces are rectangles.")+
       ep("Cylinder r=3, h=10: V = π(9)(10) = 90π ≈ 283 cu units."),
       "Practice — Lessons 6–8",
       sa(5,"Volume of a rectangular box: l=4, w=6, h=3.",["72"])+
       mc(6,"A cylinder has r = 5 and h = 8. Its volume is:",
          [("40π",0),("200π",1),("80π",0),("25π",0)],1)),
      lesson_row("09–11 — Lessons 9–11","Volume of Pyramids, Cones &amp; Spheres","c-peach",
       kl("<strong>Pyramid:</strong> V = (1/3)Bh. (One-third of the prism with same base and height.)",
          "<strong>Cone:</strong> V = (1/3)πr²h. (One-third of cylinder.)",
          "<strong>Sphere:</strong> V = (4/3)πr³.",
          "Cavalieri's Principle: two solids with same height and cross-sectional areas have equal volume.",
          "Compare: cone = 1/3 cylinder; pyramid = 1/3 prism.")+
       ep("Cone r=3, h=4: V = (1/3)π(9)(4) = 12π. Sphere r=3: V = (4/3)π(27) = 36π."),
       "Practice — Lessons 9–11",
       sa(7,"Volume of a pyramid with square base 6 and height 9.",["108"])+
       mc(8,"How does the volume of a cone compare to a cylinder with the same base and height?",
          [("Equal",0),("Twice",0),("One-third",1),("One-half",0)],2))]
    ),
    ("Topic C: Surface Area &amp; Modeling","Lessons 12–18 · Surface area formulas and real-world applications.",
     [lesson_row("12–15 — Lessons 12–15","Surface Area of 3D Figures","c-butter",
       kl("<strong>Prism SA:</strong> 2(Base Area) + Lateral Area = 2B + Ph (P = perimeter of base).",
          "<strong>Cylinder SA:</strong> 2πr² + 2πrh.",
          "<strong>Pyramid SA:</strong> Base Area + (1/2)·Perimeter·slant height = B + (1/2)Pl.",
          "<strong>Cone SA:</strong> πr² + πrl (l = slant height).",
          "<strong>Sphere SA:</strong> 4πr².")+
       ep("Cylinder r=4, h=7: SA = 2π(16) + 2π(4)(7) = 32π + 56π = 88π."),
       "Practice — Lessons 12–15",
       mc(9,"Surface area of a sphere with radius 6 is:",
          [("36π",0),("144π",1),("72π",0),("288π",0)],1)+
       sa(10,"Total SA of a cube with side 5.",["150"])),
      lesson_row("16–18 — Lessons 16–18","Modeling &amp; Applications","c-lilac",
       kl("Real-world problems involve choosing the correct formula based on context.",
          "Painting a room → surface area. Filling a pool → volume.",
          "When combining shapes: calculate separately, then add or subtract as appropriate.",
          "<strong>Density:</strong> mass = density × volume. Find mass, volume, or density.",
          "Convert units carefully: 1 ft = 12 in, 1 m = 100 cm, etc.")+
       ep("A cylindrical tank (r=2 m, h=5 m) needs paint. SA = 2π(4) + 2π(2)(5) = 8π + 20π = 28π m²."),
       "Practice — Lessons 16–18",
       mc(11,"You need to fill a rectangular pool 8m × 4m × 2m with water. You need to find:",
          [("Surface area",0),("Volume",1),("Perimeter",0),("Cross-sectional area only",0)],1)+
       mc(12,"A composite solid is a cylinder on top of a cone. To find total volume:",
          [("Add the volumes of the cylinder and cone",1),("Multiply the volumes",0),("Find average volume",0),("Subtract cone from cylinder",0)],0))]
    )
  ]
)

# Unit 7: Circles
build_page("geometry-7.html","Geometry",7,"10th Grade Mathematics",
  "Circles",
  "Circles.",
  "Angle and arc relationships, chords, tangents, secants, arc length, and sector area.",
  1,"var(--sky)","geometry",
  [
    ("Topic A: Angles &amp; Arcs in Circles","Lessons 1–5 · Central angles, inscribed angles, and arc relationships.",
     [lesson_row("01–03 — Lessons 1–3","Central &amp; Inscribed Angles","c-sky",
       kl("<strong>Central angle:</strong> vertex at center. Central angle = intercepted arc.",
          "<strong>Inscribed angle:</strong> vertex on circle = <strong>half</strong> the intercepted arc.",
          "<strong>Semicircle:</strong> 180°. Any inscribed angle in a semicircle = 90°.",
          "<strong>Inscribed angles intercepting the same arc are equal.</strong>",
          "<strong>Arc addition:</strong> adjacent arcs add up.")+
       ep("Central angle = 80° → arc = 80°. Inscribed angle intercepting that arc = 40°."),
       "Practice — Lessons 1–3",
       mc(1,"A central angle measures 110°. Its intercepted arc measures:",
          [("55°",0),("110°",1),("220°",0),("70°",0)],1)+
       sa(2,"An inscribed angle intercepts an arc of 160°. The inscribed angle measures:",["80","80°"])),
      lesson_row("04–05 — Lessons 4–5","Angle Relationships in Circles","c-peach",
       kl("<strong>Interior angle (two chords):</strong> = (1/2)(arc₁ + arc₂).",
          "<strong>Exterior angle (two secants, secant+tangent, two tangents):</strong> = (1/2)|arc₁ − arc₂|.",
          "<strong>Tangent-chord angle:</strong> = (1/2)(intercepted arc).",
          "A tangent is perpendicular to the radius at the point of tangency.",
          "Two tangents from an external point are congruent.")+
       ep("Two chords intersect inside circle, intercepting arcs 80° and 120°: angle = (80+120)/2 = 100°."),
       "Practice — Lessons 4–5",
       mc(3,"Two chords intersect inside a circle, creating arcs of 60° and 100°. The angle formed is:",
          [("80°",1),("40°",0),("160°",0),("20°",0)],0)+
       mc(4,"A tangent is drawn to a circle. It is perpendicular to:",
          [("Any chord",0),("The diameter",0),("The radius at the point of tangency",1),("Every secant",0)],2))]
    ),
    ("Topic B: Segments in Circles","Lessons 6–9 · Chord lengths, secants, and tangent-secant relationships.",
     [lesson_row("06–09 — Lessons 6–9","Chord, Secant &amp; Tangent Segment Lengths","c-mint",
       kl("<strong>Two chords intersecting inside:</strong> a·b = c·d (products of segments are equal).",
          "<strong>Two secants from external point:</strong> (whole₁)(external₁) = (whole₂)(external₂).",
          "<strong>Secant + tangent from external point:</strong> (whole)(external) = tangent².",
          "<strong>Perpendicular from center to chord:</strong> bisects the chord.",
          "<strong>Congruent chords:</strong> equidistant from the center.")+
       ep("Chords: segment products 3·8 = 4·x → x = 6."),
       "Practice — Lessons 6–9",
       mc(5,"Two chords intersect inside a circle. The segments are 4, 6 and 3, x. Find x using the chord-chord product rule.",
          [("x = 7",0),("x = 8",1),("x = 6",0),("x = 4",0)],1)+
       mc(6,"A tangent from external point P has length 9. A secant from P has external segment 3. The whole secant length is:",
          [("27",1),("6",0),("12",0),("3",0)],0))]
    ),
    ("Topic C: Arc Length, Sector Area &amp; Equations","Lessons 10–14 · Using central angles to find arc length and sector area.",
     [lesson_row("10–12 — Lessons 10–12","Arc Length &amp; Sector Area","c-lilac",
       kl("<strong>Arc length:</strong> L = (θ/360°)·2πr = rθ (θ in radians).",
          "<strong>Sector area:</strong> A = (θ/360°)·πr².",
          "Think of arc length and sector area as 'fractions' of the full circle.",
          "<strong>Full circle:</strong> circumference = 2πr; area = πr².",
          "<strong>Segment area:</strong> sector area − triangle area.")+
       ep("r=10, central angle=90°: arc length = (90/360)·20π = 5π. Sector area = (1/4)π(100) = 25π."),
       "Practice — Lessons 10–12",
       sa(7,"A circle has radius 6. Central angle = 120°. Find the arc length. (Leave in terms of π.)",["4π"])+
       mc(8,"A sector has central angle 45° and radius 8. Its area is:",
          [("8π",1),("64π",0),("4π",0),("16π",0)],0)),
      lesson_row("13–14 — Lessons 13–14","Equation of a Circle","c-butter",
       kl("<strong>Standard form:</strong> (x − h)² + (y − k)² = r², center (h, k), radius r.",
          "Rewrite by completing the square when given general form: x² + y² + Cx + Dy + E = 0.",
          "Points inside the circle: (x−h)² + (y−k)² &lt; r².",
          "Points outside: (x−h)² + (y−k)² &gt; r².",
          "On circle: (x−h)² + (y−k)² = r².")+
       ep("Center (3, −2), radius 5: equation (x−3)² + (y+2)² = 25."),
       "Practice — Lessons 13–14",
       mc(9,"Which point is on the circle (x−1)² + (y−2)² = 25?",
          [("(6, 2)",1),("(1, 7)",0),("(3, 5)",0),("(1, 2)",0)],0)+
       sa(10,"Write the equation of a circle centered at (0, 0) with radius 7.",["x²+y²=49","x^2+y^2=49"]))]
    )
  ]
)

# Unit 8: Probability
build_page("geometry-8.html","Geometry",8,"10th Grade Mathematics",
  "Probability",
  "Probability.",
  "Compound probability, conditional probability, and permutations and combinations.",
  2,"var(--peach)","geometry",
  [
    ("Topic A: Compound Probability","Lessons 1–3 · AND/OR probability with and without replacement.",
     [lesson_row("01–03 — Lessons 1–3","AND, OR &amp; Complement Rules","c-peach",
       kl("<strong>P(A and B) = P(A)·P(B)</strong> (if A and B are independent).",
          "<strong>P(A or B) = P(A) + P(B) − P(A and B)</strong> (Addition Rule).",
          "<strong>P(A or B) = P(A) + P(B)</strong> (if mutually exclusive — can't happen together).",
          "<strong>P(not A) = 1 − P(A)</strong> (Complement Rule).",
          "<strong>With replacement:</strong> events are independent. <strong>Without replacement:</strong> dependent.")+
       ep("P(ace) = 4/52 = 1/13. P(ace or king) = 4/52 + 4/52 = 8/52 (mutually exclusive)."),
       "Practice — Lessons 1–3",
       mc(1,"P(A) = 0.5 and P(B) = 0.3. If A and B are mutually exclusive, P(A or B) = ?",
          [("0.15",0),("0.8",1),("0.65",0),("0.35",0)],1)+
       mc(2,"You flip a fair coin twice. P(both heads) = ?",
          [("1/2",0),("1/4",1),("1/3",0),("3/4",0)],1))]
    ),
    ("Topic B: Conditional Probability","Lessons 4–7 · P(A|B) and the multiplication rule.",
     [lesson_row("04–07 — Lessons 4–7","Conditional Probability &amp; Independence","c-mint",
       kl("<strong>P(A|B)</strong> = P(A∩B) / P(B) — probability of A given B has occurred.",
          "<strong>Independent events:</strong> P(A|B) = P(A). Knowing B gives no info about A.",
          "<strong>Multiplication rule:</strong> P(A∩B) = P(A)·P(B|A).",
          "Use two-way tables to calculate conditional probabilities.",
          "Test for independence: check if P(A|B) = P(A).")+
       ep("60 students: 30 like math, 20 like both math and science, 40 like science.<br>P(science|math) = P(math∩science)/P(math) = (20/60)/(30/60) = 20/30 = 2/3."),
       "Practice — Lessons 4–7",
       mc(3,"P(A) = 0.4, P(A∩B) = 0.12, P(B) = 0.3. Are A and B independent?",
          [("Yes — P(A|B) = 0.4 = P(A)",1),("No — P(A|B) ≠ P(A)",0),("Yes — P(A∩B) = 0",0),("No — they must be mutually exclusive",0)],0)+
       sa(4,"P(B) = 0.5 and P(A∩B) = 0.2. Find P(A|B).",["0.4","2/5"]))]
    ),
    ("Topic C: Permutations &amp; Combinations","Lessons 8–10 · Counting principles, nPr, and nCr.",
     [lesson_row("08–10 — Lessons 8–10","Counting, Permutations &amp; Combinations","c-lilac",
       kl("<strong>Fundamental Counting Principle:</strong> multiply the number of choices for each step.",
          "<strong>Permutation nPr:</strong> ordered arrangements of r items from n. nPr = n!/(n−r)!",
          "<strong>Combination nCr:</strong> unordered selections of r items from n. nCr = n!/[r!(n−r)!]",
          "Use permutations when ORDER matters (1st, 2nd, 3rd place).",
          "Use combinations when order does NOT matter (choosing a committee).",
          "<strong>n! = n·(n−1)·(n−2)···2·1</strong>")+
       ep("Choose 3 from 8 people for a committee (no order): ₈C₃ = 8!/(3!5!) = 56.<br>Rank 3 from 8 for 1st/2nd/3rd: ₈P₃ = 8!/5! = 336."),
       "Practice — Lessons 8–10",
       mc(5,"You need to choose a president and vice-president from 10 students. Use:",
          [("Combinations (order doesn't matter)",0),("Permutations (order matters)",1),("Fundamental Counting Principle only with 10×10",0),("Combinations divided by 2",0)],1)+
       sa(6,"How many ways can you choose 2 from 6 students for a pair project? (Use ₆C₂)",["15"]))]
    )
  ]
)

print("Done with all Geometry units 1-8!")
