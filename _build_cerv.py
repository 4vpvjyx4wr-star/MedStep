# -*- coding: utf-8 -*-
import json
from collections import Counter

def mcq(q, lo, diff, opts):
    return {"question": q, "type": "mcq", "difficulty_order": diff, "cited_learning_objective": lo,
            "options": [{"text": t, "isCorrect": c, "rationale": r} for t, c, r in opts]}

def fill(q, lo, diff, answer, rationale, accept=None):
    item = {"question": q, "type": "fill_blank", "difficulty_order": diff, "cited_learning_objective": lo,
            "answer": answer, "rationale": rationale}
    if accept: item["accept"] = accept
    return item

def openq(q, lo, diff, answer, rationale):
    return {"question": q, "type": "open", "difficulty_order": diff, "cited_learning_objective": lo,
            "answer": answer, "rationale": rationale}

qs = []
qs.append(openq(
    "Describe the primary and accessory motions of C0 (the occiput), C1, and C2-C7.",
    "State primary and accessory cervical motions.", "1st",
    "C0 primary motion is flexion and extension. Accessory motion is sidebending and rotation to opposite sides. C1 primary motion is rotation. Accessory motion is sidebending and rotation to opposite sides. For C2-C7, flexion and extension, rotation, and sidebending are all primary motions. Sidebending and rotation are always to the same side. Cervical glide occurs, but it is not assessed or treated with OMT.",
    "Keep OA and AA coupling opposite, and C2-C7 coupling to the same side.",
))
qs.append(mcq(
    "Segmental palpation of the cervical spine most appropriately involves contact of which structures when testing sidebending and rotation?",
    "Name the contact for cervical sidebending and rotation.", "1st",
    [("Transverse processes", False, "Transverse processes are short and less useful for this test."),
     ("Spinous processes", False, "Spinous processes do not localize sidebending and rotation as well."),
     ("Articular pillars", True, "Sidebending and rotation are introduced and monitored on the articular pillars."),
     ("Vertebral bodies", False, "Vertebral bodies are not the palpatory contact for this test."),
     ("Facet joints", False, "The practical contact is the articular pillar, which overlies the facet region.")],
))
qs.append(mcq(
    "A 43-year-old man has mild intermittent headaches for 2 weeks after sleeping on the ground. The occiput translates more easily to the left, and that finding becomes more symmetric in flexion. What is the occipital-atlantal diagnosis?",
    "Diagnose an OA joint from translation and sagittal symmetry.", "3rd",
    [("E SR RR", False, "OA sidebending and rotation are opposite, and the symmetry in flexion names a flexion dysfunction."),
     ("E SR RL", False, "The coupling is right, but symmetry in flexion names flexion, not extension."),
     ("F SR RL", True, "Ease of translation to the left is sidebending right. At the OA, rotation is opposite, so rotation is left. Greater symmetry in flexion names a flexion dysfunction: F SR RL."),
     ("F SL RR", False, "Ease of left translation is sidebending right, not left."),
     ("N SR RR", False, "Symmetry changes in flexion, so this is not neutral, and the rotations are not to the same side."),
     ("N SL RR", False, "A change toward symmetry in flexion means the dysfunction is flexed, not neutral.")],
))
qs.append(mcq(
    "Which position best describes the cervical spine during counterstrain of a right AC7 tender point?",
    "Position the neck for a right AC7 counterstrain point.", "2nd",
    [("Extended, sidebent left, rotated left", False, "AC7 is treated in flexion, not extension."),
     ("Extended, sidebent left, rotated right", False, "AC7 is a flexion point."),
     ("Extended, sidebent right, rotated left", False, "AC7 is a flexion point."),
     ("Extended, sidebent right, rotated right", False, "AC7 is a flexion point."),
     ("Flexed, sidebent left, rotated left", False, "For a right AC7, sidebending is toward the point."),
     ("Flexed, sidebent left, rotated right", False, "Sidebending is toward the tender point and rotation is away."),
     ("Flexed, sidebent right, rotated left", True, "Right AC7 is flexed, sidebent toward (right), and rotated away (left): F ST RA."),
     ("Flexed, sidebent right, rotated right", False, "Rotation is away from the tender point.")],
))
qs.append(mcq(
    "Which position best describes the cervical spine during counterstrain of a right PC5 tender point?",
    "Position the neck for a right PC5 counterstrain point.", "2nd",
    [("Extended, sidebent left, rotated left", True, "The packet groups this with the PC4-8 pattern: extended, sidebent away, and rotated away. For a right PC5 that is extended, sidebent left, and rotated left."),
     ("Extended, sidebent left, rotated right", False, "Rotation is away from the point, so both sidebending and rotation are left."),
     ("Extended, sidebent right, rotated left", False, "Sidebending is away from a right-sided point."),
     ("Extended, sidebent right, rotated right", False, "Both sidebending and rotation are away."),
     ("Flexed, sidebent left, rotated left", False, "PC5 is treated in extension."),
     ("Flexed, sidebent left, rotated right", False, "PC5 is treated in extension."),
     ("Flexed, sidebent right, rotated left", False, "PC5 is treated in extension."),
     ("Flexed, sidebent right, rotated right", False, "PC5 is treated in extension.")],
))
qs.append(openq(
    "Label myofascial release, balanced ligamentous tension, counterstrain, muscle energy, and HVLA as direct, indirect, or either.",
    "Classify common cervical techniques as direct or indirect.", "1st",
    "Myofascial release can be direct or indirect, at the physician's preference. Balanced ligamentous tension and counterstrain are indirect, because the patient is placed into the ease of the dysfunction. Muscle energy and HVLA are direct, because the segment is moved toward the restrictive barrier.",
    "Name the direction relative to the barrier for each technique.",
))
qs.append(mcq(
    "Suboccipital release can help modulate which cranial nerve?",
    "Name the cranial nerve addressed by suboccipital release.", "1st",
    [("CN II", False, "CN II is the optic nerve."),
     ("CN IV", False, "CN IV is the trochlear nerve."),
     ("CN VI", False, "CN VI is the abducens nerve."),
     ("CN VIII", False, "CN VIII is the vestibulocochlear nerve."),
     ("CN X", True, "CN X is the vagus nerve. Suboccipital soft-tissue work can reduce tissue change that affects vagal function."),
     ("CN XII", False, "CN XII is the hypoglossal nerve.")],
))
qs.append({
    "question": "Match each description to the cervical technique.",
    "type": "matching", "difficulty_order": "2nd",
    "cited_learning_objective": "Recognize cervical techniques from the setup.",
    "pairs": [
        {"prompt": "The patient is positioned at the restrictive barrier and pushes against the physician's hand for 3 to 5 seconds", "answer": "Muscle energy"},
        {"prompt": "The segment is positioned at ease and the patient holds a breath at the point of greatest relaxation", "answer": "Balanced ligamentous tension"},
        {"prompt": "Bulky tissue inferior to the occiput is contacted with direct inhibitory pressure and traction", "answer": "Suboccipital pressure and traction"},
        {"prompt": "The patient is positioned at the restrictive barrier, breathes to relax, and a quick thrust is applied", "answer": "HVLA"},
        {"prompt": "The patient is positioned for maximum pain relief and held there for 90 seconds", "answer": "Counterstrain"},
        {"prompt": "Pressure is placed at the superior and medial edge of the scapula until the tissue relaxes", "answer": "Levator scapulae inhibition"},
    ],
})
qs.append(mcq(
    "True or false: the cervical spine follows Fryette mechanics.",
    "State whether Fryette mechanics apply to the cervical spine.", "1st",
    [("True", False, "Fryette mechanics apply to the thoracic and lumbar regions, not the cervical spine."),
     ("False", True, "Fryette's principles apply to the thoracic and lumbar regions. They do not govern the cervical spine.")],
))
qs.append(openq(
    "Describe contraindications for soft tissue, myofascial release, muscle energy, counterstrain, balanced ligamentous tension, and HVLA in the cervical region.",
    "List cervical contraindications by technique.", "3rd",
    "An absolute contraindication to any technique is that the patient declines it. Relative contraindications in the neck include skin infection or an open wound. Soft tissue and myofascial release are low risk and have few contraindications. Muscle energy is contraindicated when the patient cannot follow directions, such as a young child or a comatose patient. Counterstrain is contraindicated when the patient cannot report pain on a scale. Balanced ligamentous tension is low risk and still follows the absolute and relative cervical contraindications. Cervical HVLA is contraindicated with vertebrobasilar insufficiency, Down syndrome, and rheumatoid arthritis affecting the neck, and also with recent trauma, infection, or tumor in the region.",
    "The packet's counterstrain line is included with the other techniques even though the prompt listed balanced ligamentous tension in that slot.",
))

def add(stem, lo, diff, letter, options, why):
    letters = "abcdefgh"
    qs.append(mcq(stem, lo, diff, [
        (text, letters[i] == letter, why if letters[i] == letter else "This is not the keyed choice.")
        for i, text in enumerate(options)
    ]))

add("The occiput is restricted in right rotation. The restriction worsens in flexion and improves in extension. What is the OA diagnosis?",
    "Diagnose OA rotation that improves in extension.", "3rd", "d",
    ["F RR SR", "E RR SR", "F RL SR", "E RL SR", "F RR SL", "E RR SL"],
    "Restriction of right rotation means ease of left rotation. At the OA, sidebending is opposite, so sidebending is right. The restriction improves in extension, so the dysfunction is extended: E RL SR.")
add("The occiput translates more easily to the left than to the right. In flexion, translation becomes more symmetric. What is the OA diagnosis?",
    "Diagnose an OA joint from left translation that improves in flexion.", "3rd", "c",
    ["F RR SR", "E RR SR", "F RL SR", "E RL SR", "F RR SL", "E RR SL"],
    "Ease of translation to the left is sidebending right. OA rotation is opposite, so rotation is left. Symmetry in flexion names a flexion dysfunction: F RL SR.")
add("With the head and neck flexed to 45 degrees to isolate the AA joint, right rotation is restricted. What is the diagnosis?",
    "Diagnose an AA joint from rotation in flexion.", "2nd", "d",
    ["C0-C1 F RL SR", "C0-C1 E RL SR", "C1-C2 rotated right", "C1-C2 rotated left", "C3 F RL SL", "C3 E RR SR"],
    "Flexion to about 45 degrees isolates C1-C2. For students, AA dysfunction is named by rotation only. Restriction of right rotation means the atlas is rotated left.")
add("C4 is restricted when translating from left to right. Translation becomes more symmetric in flexion. What is the C4 diagnosis?",
    "Diagnose C4 from a translation restriction that improves in flexion.", "3rd", "a",
    ["F RR SR", "E RR SR", "F RL SL", "E RL SL", "F RR SL", "E RR SL"],
    "Restriction translating to the right means ease of translation to the left, which is sidebending right. From C2 to C7, rotation follows to the same side. Symmetry in flexion names F RR SR.")
add("C5 is restricted in right rotation and in translation from right to left. The findings do not become more symmetric in flexion or extension. What is the C5 diagnosis?",
    "Diagnose a neutral C5 dysfunction.", "3rd", "c",
    ["F RL SL", "E RL SL", "N RL SL", "N RL SR", "N RR SL", "F RR SR", "E RR SR"],
    "No change in flexion or extension means neutral. Restriction of right rotation and of right sidebending means ease to the left for both. From C2 to C7 they stay on the same side: N RL SL. Cervical segments do not follow Fryette mechanics.")
add("At the OA joint the occiput translates easily to the left and is restricted in right rotation. What is the starting position for HVLA?",
    "Set up OA HVLA at the restrictive barrier.", "3rd", "c",
    ["RL SR", "RL SL", "RR SL", "RR SR"],
    "Ease of left translation is sidebending right, and restriction of right rotation is ease of left rotation, so the dysfunction is RL SR. HVLA engages the barrier, which is the opposite: RR SL.")
add("The OA is positioned into flexion, right rotation, and left sidebending. The patient then moves the head toward neutral against resistance for 3 to 5 seconds. What OA dysfunction is being treated?",
    "Name the OA dysfunction from a muscle-energy setup.", "3rd", "d",
    ["F RR SL", "E RR SL", "F RL SR", "RL SR", "F RR SR", "E RR SR"],
    "This is muscle energy, so the setup is the restrictive barrier: flexion, right rotation, and left sidebending. The dysfunction is the opposite position, extended, rotated left, and sidebent right (E RL SR). The printed choice D is abbreviated RL SR, and the answer line writes E RL SR even though that full name is not its own option.")
add("C6 is restricted in right rotation, and the restriction improves in extension. How would the physician position C6 for balanced ligamentous tension?",
    "Position C6 for an indirect technique.", "3rd", "d",
    ["F RR SR", "E RR SR", "F RL SL", "E RL SL"],
    "Restriction of right rotation means the segment is rotated left, and from C2 to C7 it is sidebent left as well. Improvement in extension names extension. BLT is indirect, so the treatment position is the dysfunction: E RL SL.")
add("C3 is restricted in translation to the left, rotation to the left is greater than rotation to the right, and the findings improve in flexion. If C3 is treated with muscle energy, toward which position does the patient's force go?",
    "Name the direction of the patient's muscle-energy force at C3.", "3rd", "c",
    ["F RR SR", "E RR SR", "F RL SL", "E RL SL", "N RR SL", "N RL SR"],
    "The dysfunction is F RL SL. Muscle energy places the segment at the barrier, and the patient pushes back toward the dysfunction.")
add("C4 is restricted in right rotation, with no improvement in flexion or extension. What is the starting position for HVLA?",
    "Set up HVLA for a neutral C4 rotation restriction.", "3rd", "e",
    ["F RR SR", "E RR SR", "F RL SL", "E RL SL", "N RR SR", "N RL SL"],
    "The dysfunction is N RL SL. HVLA starts at the restrictive barrier, N RR SR.")
qs.append(openq(
    "Explain the differences between typical and atypical cervical vertebrae.",
    "Contrast typical C3-C6 with atypical C1, C2, and C7.", "2nd",
    "Typical vertebrae are C3-C6. They have a body, a bifid spinous process, a disc between vertebrae, a short transverse process, unciform processes, and articular processes. C1 is atypical: no body, no true spinous process, no disc above or below, a posterior arch, an articulation for the dens, and transverse processes palpable posterior to the ramus of the mandible. C2 is atypical: it has the odontoid process, an articular facet for the atlas, and no disc above. C7 is atypical: it is the vertebra prominens, and its spinous process is seldom bifid.",
    "Cover C3-C6, then C1, C2, and C7.",
))
qs.append(openq(
    "Describe the primary and accessory motions of C0, C1, and C2 through C7.",
    "Restate cervical primary and accessory motion by segment.", "1st",
    "C0 primary motion is flexion and extension, and accessory motion is sidebending and rotation to opposite sides. C1 primary motion is rotation, and accessory motion is sidebending and rotation to opposite sides. From C2 through C7, flexion and extension, rotation, and sidebending are all primary, and sidebending and rotation occur to the same side.",
    "Same coupling rules as the opening item.",
))

oa = [
    ("ease of translation to the right, with no change in symmetry in flexion or extension", "N SL RR",
     "Ease of translation to the right is sidebending left. At the OA, rotation is opposite, so rotation is right. No sagittal change means neutral: N SL RR.",
     ["NSLRR", "N SLRR", "neutral sidebent left rotated right"]),
    ("resistance to translation to the right, with no change in symmetry in flexion or extension", "N SR RL",
     "Resistance to right translation means ease of left translation, which is sidebending right and, at the OA, rotation left. Neutral because symmetry does not change: N SR RL.",
     ["NSRRL", "N SRRL", "neutral sidebent right rotated left"]),
    ("resistance to translation to the left, and the motion is more symmetric in extension", "E SL RR",
     "Resistance to left translation is ease to the right, so sidebending is left and rotation is right. Symmetry in extension names extension: E SL RR.",
     ["ESLRR", "E SLRR", "extended sidebent left rotated right"]),
    ("ease of translation to the left, and the motion is less symmetric in flexion", "E SR RL",
     "Ease of left translation is sidebending right and rotation left. Less symmetry in flexion means the dysfunction is named for extension: E SR RL.",
     ["ESRRL", "E SRRL", "extended sidebent right rotated left"]),
    ("resistance to translation to the left, and the motion is less symmetric in extension", "F SL RR",
     "Resistance to left translation is sidebending left and rotation right. Less symmetry in extension means it is named for flexion: F SL RR.",
     ["FSLRR", "F SLRR", "flexed sidebent left rotated right"]),
    ("ease of translation to the left, and the motion is more symmetric in flexion", "F SR RL",
     "Ease of left translation is sidebending right and rotation left. Symmetry in flexion names flexion: F SR RL.",
     ["FSRRL", "F SRRL", "flexed sidebent right rotated left"]),
    ("translation that is symmetrically restricted, with greater palpatory depth bilaterally and no sagittal change", "bilateral flexion",
     "Symmetric restriction with greater bilateral depth is bilateral flexion.",
     ["bilateral flexed", "flexed bilaterally"]),
    ("translation that is symmetrically restricted, with less palpatory depth bilaterally and no sagittal change", "bilateral extension",
     "Symmetric restriction with less bilateral depth is bilateral extension.",
     ["bilateral extended", "extended bilaterally"]),
]
for clue, ans, why, acc in oa:
    qs.append(fill(
        "OA segmental diagnosis. The findings are " + clue + ". Name the dysfunction.",
        "Name an OA dysfunction from the segmental diagnosis table.", "2nd", ans, why, acc))
qs.append(fill(
    "For an AA dysfunction named C1 rotated right, ease of rotation is to the __________ and rotation is resisted to the __________.",
    "Complete the AA rotation findings for C1 rotated right.", "1st", "right, left",
    "C1 rotated right rotates easily to the right and is resisted to the left.",
    ["right and left", "right left"]))
qs.append(fill(
    "For an AA dysfunction named C1 rotated left, ease of rotation is to the __________ and rotation is resisted to the __________.",
    "Complete the AA rotation findings for C1 rotated left.", "1st", "left, right",
    "C1 rotated left rotates easily to the left and is resisted to the right.",
    ["left and right", "left right"]))
c27 = [
    ("the left articular pillar is anterior, and the motion is more symmetric in flexion", "F RL SL",
     "An anterior left articular pillar is rotation left, and from C2 to C7 sidebending is also left. Symmetry in flexion names flexion. The printed C2-C7 answer grid was blank, so this name follows those coupling rules."),
    ("translation is easier to the left, and the motion is more symmetric in extension", "E RR SR",
     "Ease of translation to the left is sidebending right, so rotation is also right. Symmetry in extension names extension. The printed answer grid was blank, so this name follows the packet's C2-C7 rules."),
    ("translation is resisted to the left, and the motion is less symmetric in extension", "F RL SL",
     "Resistance to left translation means ease to the right, which is sidebending left and rotation left. Less symmetry in extension means the dysfunction is named for flexion. The printed answer grid was blank."),
    ("the left articular pillar is posterior, and the motion is less symmetric in flexion", "E RR SR",
     "A posterior left pillar is rotation to the right, with sidebending right. Less symmetry in flexion names extension. The printed answer grid was blank."),
]
for clue, ans, why in c27:
    qs.append(fill(
        "C2-C7 segmental diagnosis. " + clue[0].upper() + clue[1:] + ". Name the dysfunction.",
        "Name a C2-C7 dysfunction from the segmental clues.", "2nd", ans, why,
        [ans.replace(" ", ""), ans.replace(" ", "")]))

add("Where are the fingers placed for suboccipital soft-tissue pressure and traction?",
    "Place the fingers for suboccipital pressure and traction.", "1st", "b",
    ["Posterior to the occiput", "Posterior to the arch of C1", "Posterior to the articular pillars", "Posterior to the inion"],
    "The fingertips are placed posterior to the arch of C1, with anterior inhibitory pressure and traction.")
add("The occiput translates more easily to the left than to the right. The finding is exaggerated in flexion and diminished in extension. What is the OA diagnosis?",
    "Diagnose an OA joint that is more asymmetric in flexion.", "3rd", "b",
    ["E SL RL", "E SR RL", "E SL RR", "E SR RR", "F SL RL", "F SR RL", "F SL RR", "F SR RR"],
    "Asymmetry that is worse in flexion and better in extension is named for extension. Ease of left translation is sidebending right. OA rotation is opposite, so rotation is left: E SR RL.")
add("C2 translates more easily to the left than to the right. The finding is exaggerated in flexion and diminished in extension. What is the C2 diagnosis?",
    "Diagnose C2 from left translation that improves in extension.", "3rd", "d",
    ["E RL SL", "E RL SR", "E RR SL", "E RR SR", "F RL SL", "F RL SR", "F RR SL", "F RR SR"],
    "Ease of translation to the left is sidebending right, and from C2 to C7 rotation is also right. The motion is more symmetric in extension, so the diagnosis is E RR SR.")
add("C4 rotates more easily to the left than to the right. The finding is exaggerated in flexion and diminished in extension. What is the C4 diagnosis?",
    "Diagnose C4 from left rotation that improves in extension.", "3rd", "a",
    ["E RL SL", "E RL SR", "E RR SL", "E RR SR", "F RL SL", "F RL SR", "F RR SL", "F RR SR"],
    "Ease of left rotation is rotation left and, from C2 to C7, sidebending left. Symmetry in extension names E RL SL.")
add("C5 translates more easily to the left than to the right, and the finding becomes more symmetric in flexion. What is the C5 diagnosis?",
    "Diagnose C5 from left translation that improves in flexion.", "2nd", "g",
    ["E RL SL", "E RL SR", "E RR SR", "E RR SL", "F RL SL", "F RL SR", "F RR SR", "F RR SL"],
    "Ease of left translation is sidebending right and rotation right. Symmetry in flexion names F RR SR. Opposite coupling does not occur from C2 to C7.")
add("A 42-year-old man has acute posterior neck pain and headache after minor trauma in a basketball game, with earlier transient visual blurring and dizziness. You are considering cervical manipulation. What is the most appropriate next step in vascular risk screening?",
    "Screen for cervical vascular risk before manipulation.", "3rd", "c",
    ["Perform a vertebral artery positional test in extension and rotation",
     "Rely on a single negative premanipulative vascular test to clear him for manipulation",
     "Conduct a comprehensive history and focused neurologic examination for vascular red flags",
     "Proceed with manipulation since the transient symptoms have resolved",
     "Order routine cervical spine X-rays before manipulation"],
    "Positional vascular tests are unreliable and should not be used alone. Screening uses history and a focused neurologic exam for cervical artery red flags.")
add("A 29-year-old woman with rheumatoid arthritis has neck pain. You plan to evaluate cervical motion and consider manipulation. Which statement best describes cervical stability screening?",
    "Screen for cervical instability before manual treatment.", "3rd", "c",
    ["Routine Sharp-Purser or alar stress tests are sufficient to rule out instability",
     "Pre-manipulative cervical instability can be excluded with a single negative test",
     "A combined review of history, risk factors, physical exam, and, when indicated, imaging is needed to assess instability risk",
     "Cervical instability screening is unnecessary in young patients",
     "Proceed with HVLA if the patient denies trauma or neurologic symptoms"],
    "No single test excludes instability. History, risk factors, examination, and imaging when indicated are used together. Rheumatoid arthritis is one of those risks.")
add("On segmental testing of C5, translation is freer to the left than to the right. The asymmetry lessens in extension and increases in flexion. What is the C5 diagnosis?",
    "Diagnose C5 when translation is more symmetric in extension.", "2nd", "a",
    ["E RR SR", "E RL SL", "F RR SR", "F RL SL", "E RL SR"],
    "Ease of left translation is sidebending right and rotation right. Greater symmetry in extension names E RR SR.")
add("The occiput translates more easily to the left than to the right. The asymmetry decreases in extension and increases in flexion. What is the OA diagnosis?",
    "Diagnose the OA when translation is more symmetric in extension.", "2nd", "b",
    ["E SL RR", "E SR RL", "F SL RR", "F SR RL", "E SR RR"],
    "Ease of left translation is sidebending right. OA rotation is opposite, so rotation is left. Symmetry in extension names E SR RL.")
add("A 48-year-old office worker has a somatic dysfunction at C5. Which statement about this dysfunction is correct?",
    "State the coupling rule at C5.", "1st", "b",
    ["Sidebending and rotation occur to opposite sides",
     "Sidebending and rotation occur to the same side",
     "It follows Fryette type I mechanics",
     "It follows Fryette type II mechanics",
     "Flexion and extension occur to opposite sides"],
    "From C2 to C7, sidebending and rotation couple to the same side. Fryette type I and type II describe thoracic and lumbar mechanics.")
add("When testing intersegmental motion from C2 to C7, where are the monitoring or force-applying fingers best placed to introduce sidebending and rotation?",
    "Choose the contact for C2-C7 sidebending and rotation.", "1st", "b",
    ["Spinous process", "Articular pillar", "Vertebral body", "Uncovertebral joint", "Transverse process"],
    "The articular pillars lie just lateral to the spinous processes and are the contact for sidebending and rotation.")
add("The prominent spinous process most easily palpated at the base of the posterior neck is used as a landmark. Which vertebra lies immediately below it?",
    "Identify the vertebra below vertebra prominens.", "1st", "c",
    ["C6", "C7", "T1", "T2", "C1"],
    "Vertebra prominens is classically C7. The vertebra immediately below it is T1.")
add("The small bony projections along the superolateral margins of typical cervical vertebral bodies form the uncovertebral joints. What are those projections called?",
    "Name the projections that form the uncovertebral joints.", "1st", "b",
    ["Articular pillars", "Uncinate processes", "Transverse processes", "Facet processes", "Spinous processes"],
    "Uncinate processes project upward from the superolateral vertebral body and form the uncovertebral joints, or joints of Luschka.")
add("While testing C6, the segment rotates more freely to the left than to the right. The difference becomes more symmetric in flexion and less symmetric in extension. What is the C6 diagnosis?",
    "Diagnose C6 from left rotation that improves in flexion.", "2nd", "c",
    ["E RL SL", "E RR SR", "F RL SL", "F RR SR", "F RL SR"],
    "Ease of left rotation is rotation left and sidebending left. Symmetry in flexion names F RL SL.")
add("The occiput translates more freely to the right, and the finding becomes more symmetric in flexion. What is the OA diagnosis?",
    "Diagnose the OA from right translation that improves in flexion.", "2nd", "c",
    ["F SR RL", "E SL RR", "F SL RR", "E SR RL", "F SR RR"],
    "Ease of translation to the right is sidebending left. OA rotation is opposite, so rotation is right. Symmetry in flexion names F SL RR.")
add("Which statement correctly characterizes coupled motion of a typical C2-C7 segment?",
    "State C2-C7 coupling.", "1st", "b",
    ["Rotation to one side with sidebending to the opposite side",
     "Rotation and sidebending always to the same side",
     "Pure rotation with no sidebending",
     "Motion governed by Fryette type I principles",
     "Motion governed by Fryette type II principles"],
    "From C2 to C7, rotation and sidebending always couple to the same side, regardless of flexion or extension. Fryette type I and type II do not apply here.")
add("A physician wants to induce translatory sidebending at a typical cervical segment. Contact over which structure most effectively transmits this force?",
    "Choose the contact that transmits cervical sidebending.", "1st", "c",
    ["Transverse process", "Spinous process", "Articular pillar", "Uncinate process", "Lamina"],
    "The articular pillar is the contact for intersegmental sidebending and rotation. Transverse processes are short, and the spinous process localizes this force less well.")
add("Which vertebra is classically identified as the vertebra prominens?",
    "Identify vertebra prominens.", "1st", "d",
    ["C1", "C5", "C6", "C7", "T1"],
    "Vertebra prominens is classically C7, named for its prominent, usually nonbifid spinous process.")
add("The uncovertebral joints, also called the joints of Luschka, are formed by which structures?",
    "Name the structures that form the joints of Luschka.", "1st", "b",
    ["The facets of adjacent articular pillars",
     "The uncinate processes and the adjacent vertebral body",
     "The transverse foramina and the vertebral artery",
     "The dens and the anterior arch of the atlas",
     "The transverse processes of adjacent vertebrae"],
    "Uncinate processes articulate with the inferolateral surface of the vertebral body above.")
add("Translation at C3 is freer to the right than to the left, and the asymmetry is minimized in extension. What is the C3 diagnosis?",
    "Diagnose C3 from right translation that improves in extension.", "2nd", "d",
    ["F RL SL", "F RR SR", "E RR SR", "E RL SL", "E RL SR"],
    "Ease of translation to the right is sidebending left and rotation left. Symmetry in extension names E RL SL.")
add("The occiput resists translation to the left more than to the right, and the asymmetry is least apparent in extension. What is the OA diagnosis?",
    "Diagnose the OA from resistance to left translation.", "3rd", "b",
    ["E SR RL", "E SL RR", "F SL RR", "F SR RL", "E SR RR"],
    "Greater resistance to left translation means ease to the right, which is sidebending left. OA rotation is opposite, so rotation is right. Least asymmetry in extension names E SL RR.")
add("A patient has cervicogenic headaches and a C4 somatic dysfunction. A student asks which Fryette principle governs this segment. What is the best response?",
    "State which Fryette rule applies at C4.", "2nd", "d",
    ["Fryette type I", "Fryette type II", "Fryette type III",
     "None; C2 to C7 couple sidebending and rotation to the same side",
     "None; C2 to C7 couple sidebending and rotation to opposite sides"],
    "Fryette type I and type II do not apply to the cervical spine. From C2 to C7, sidebending and rotation couple to the same side. The third principle describes motion in one plane affecting the others, but it does not name this coupling.")
add("During a C2-C7 segmental exam, which landmark should be contacted to localize rotation to a single segment?",
    "Choose the contact that localizes cervical rotation.", "1st", "a",
    ["Articular pillar", "Vertebral body", "Spinous process tip", "Mastoid process", "Uncovertebral joint"],
    "The articular pillar, or lateral mass, is the preferred contact for localizing rotation and sidebending at one segment.")
add("A student identifies the most prominent spinous process at the cervicothoracic junction as vertebra prominens. Counting one segment cephalad places the finger over which vertebra?",
    "Count one segment above vertebra prominens.", "2nd", "c",
    ["T1", "T2", "C6", "C5", "C7"],
    "Vertebra prominens is C7. One segment cephalad is C6. One segment caudad would be T1.")
add("On a model of a typical cervical vertebra, which structures form the joints of Luschka and help regulate cervical motion?",
    "Identify the structures that form the joints of Luschka.", "1st", "b",
    ["The spinous process", "The uncinate processes", "The transverse foramina",
     "The superior articular facets", "The vertebral body endplate only"],
    "The uncinate processes along the superolateral rims form the uncovertebral joints and help regulate cervical motion.")

out = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\quizzes\omm-b1-cervical.json"
with open(out, "w", encoding="utf-8", newline="\n") as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
    f.write("\n")
bad = 0
for q in qs:
    if "lecture" in q["question"].lower(): bad += 1
    if q["type"] == "mcq" and sum(o["isCorrect"] for o in q["options"]) != 1: bad += 1
print(len(qs), dict(Counter(q["type"] for q in qs)), "bad", bad)
