# -*- coding: utf-8 -*-
"""Temporary builder for quizzes/omm-b5-eent.json. Deleted after the quiz is written."""
import json
from pathlib import Path

def fb(question, objective, answer, rationale, accept):
    return {
        "question": question,
        "type": "fill_blank",
        "difficulty_order": "1st",
        "cited_learning_objective": objective,
        "answer": answer,
        "rationale": rationale,
        "accept": accept,
    }

def mcq(question, objective, options):
    # options: list of (text, is_correct, rationale)
    assert sum(1 for _, ok, _ in options if ok) == 1
    assert len(options) >= 2
    return {
        "question": question,
        "type": "mcq",
        "difficulty_order": "1st",
        "cited_learning_objective": objective,
        "options": [
            {"text": text, "isCorrect": ok, "rationale": rationale}
            for text, ok, rationale in options
        ],
    }

def open_q(question, objective, answer, rationale):
    return {
        "question": question,
        "type": "open",
        "difficulty_order": "2nd",
        "cited_learning_objective": objective,
        "answer": answer,
        "rationale": rationale,
    }

JAW_NOTE = (
    "Printed mismatch: the explanation says the mandible deviates toward the hypertonic "
    "lateral pterygoid, which would make the right lateral pterygoid the answer, and also "
    "says right deviation reflects a hypertonic left lateral pterygoid because the contralateral "
    "muscle is the primary protruder. The printed answer letter matches that concluding sentence, "
    "so the left lateral pterygoid is keyed."
)

qs = []

qs.append(fb(
    "Sympathetic supply to the head and neck originates from spinal levels __________ and ascends through the superior cervical ganglion.",
    "State the spinal origin of sympathetic supply to the head and neck.",
    "T1 to T4",
    "Sympathetic supply to the head and neck originates from T1-T4 and ascends through the superior cervical ganglion.",
    ["T1-T4", "T1 through T4", "T1-T4 spinal levels", "T1 to T4"],
))
qs.append(fb(
    "Parasympathetic supply to the lacrimal, nasal, and pharyngeal glands travels via cranial nerve __________ and synapses in the sphenopalatine ganglion.",
    "Name the cranial nerve that supplies parasympathetic fibers to the lacrimal, nasal, and pharyngeal glands.",
    "VII (facial)",
    "Parasympathetic supply to the lacrimal, nasal, and pharyngeal glands travels via cranial nerve VII (facial) and synapses in the sphenopalatine ganglion.",
    ["VII", "7", "facial", "CN VII", "CN 7", "facial nerve", "cranial nerve VII", "cranial nerve 7", "CN VII (facial)"],
))
qs.append(fb(
    "Parasympathetic supply to the larynx and pharynx travels via the __________ nerve, and somatic influence on this pathway is addressed at the __________ region.",
    "Name the nerve and the region used to address parasympathetic supply to the larynx and pharynx.",
    "vagus (CN X); OA-C2",
    "Parasympathetic supply to the larynx and pharynx travels via the vagus nerve (CN X). Somatic influence on this pathway is addressed at OA-C2.",
    ["vagus CN X; OA to C2", "vagus; OA to C2", "vagus; OA-C2", "CN X; OA-C2", "CN X; OA to C2", "vagus nerve; OA-C2", "vagus nerve; OA to C2", "vagus CN X, OA-C2"],
))
qs.append(fb(
    "Sensory innervation to the face, sinuses, nasal cavity, and oropharynx is supplied by cranial nerve __________.",
    "Name the cranial nerve that supplies sensation to the face, sinuses, nasal cavity, and oropharynx.",
    "V (trigeminal)",
    "Sensory innervation to the face, sinuses, nasal cavity, and oropharynx is supplied by cranial nerve V (trigeminal).",
    ["V", "5", "trigeminal", "CN V", "CN 5", "trigeminal nerve", "cranial nerve V", "cranial nerve 5"],
))
qs.append(fb(
    "In a patient with thick, tenacious nasal secretions, the autonomic tone is shifted toward __________ dominance.",
    "Name the autonomic dominance associated with thick, tenacious nasal secretions.",
    "sympathetic",
    "Thick, tenacious nasal secretions reflect a shift toward sympathetic dominance.",
    ["sympathetics", "sympathetic tone"],
))
qs.append(fb(
    "In a patient with thin, watery nasal secretions, the autonomic tone is shifted toward __________ dominance.",
    "Name the autonomic dominance associated with thin, watery nasal secretions.",
    "parasympathetic",
    "Thin, watery nasal secretions reflect a shift toward parasympathetic dominance.",
    ["parasympathetics", "parasympathetic tone"],
))
qs.append(fb(
    "Lymph from the right side of the head and neck drains via the __________ duct into the right subclavian vein.",
    "Name the duct that drains lymph from the right side of the head and neck.",
    "right lymphatic",
    "Lymph from the right side of the head and neck drains via the right lymphatic duct into the right subclavian vein.",
    ["right lymphatic duct", "lymphatic"],
))
qs.append(fb(
    "Lymph from the left side of the head and neck drains via the __________ duct.",
    "Name the duct that drains lymph from the left side of the head and neck.",
    "thoracic",
    "Lymph from the left side of the head and neck drains via the thoracic duct.",
    ["thoracic duct"],
))
qs.append(fb(
    "The Galbreath technique is also known as the __________ pump and is used to support pharyngotympanic tube function.",
    "Give the other name of the Galbreath pump.",
    "mandibular",
    "The Galbreath technique is also known as the mandibular pump and is used to support pharyngotympanic tube function.",
    ["mandibular pump"],
))
qs.append(fb(
    "The Chapman point for the middle ear is located on the superior aspect of the __________ near the midclavicular line.",
    "Locate the middle-ear Chapman point.",
    "clavicle",
    "The Chapman point for the middle ear is on the superior aspect of the clavicle near the midclavicular line.",
    ["clavicles"],
))
qs.append(fb(
    "The posterior Chapman zone for general EENT reflexes is located at the articular pillars of __________.",
    "Locate the posterior Chapman zone for general EENT reflexes.",
    "C2",
    "The posterior Chapman zone for general EENT reflexes is at the articular pillars of C2.",
    ["C2 articular pillars", "the C2 articular pillars"],
))
qs.append(fb(
    "In children, the __________ orientation of the pharyngotympanic tube predisposes to recurrent acute otitis media.",
    "State the pharyngotympanic-tube orientation that predisposes children to recurrent acute otitis media.",
    "horizontal",
    "In children, the horizontal orientation of the pharyngotympanic tube predisposes to recurrent acute otitis media.",
    ["more horizontal"],
))
qs.append(fb(
    "The auditory and vestibular apparatus are housed within the __________ bone.",
    "Name the bone that houses the auditory and vestibular apparatus.",
    "temporal",
    "The auditory and vestibular apparatus are housed within the temporal bone.",
    ["temporal bone"],
))
qs.append(fb(
    "On opening of the mouth, the mandible deviates toward the side of the __________ lateral pterygoid.",
    "Complete the packet statement on mandibular deviation and the lateral pterygoid.",
    "hypertonic",
    "The printed fill-in states that on opening, the mandible deviates toward the side of the hypertonic lateral pterygoid. Later items in this packet conclude that right deviation reflects the contralateral (left) lateral pterygoid; this blank is keyed to the printed word hypertonic.",
    ["hypertonic lateral pterygoid", "the hypertonic"],
))
qs.append(fb(
    "The intraoral technique used for persistent pharyngotympanic tube dysfunction is known as the __________ technique.",
    "Name the intraoral technique used for persistent pharyngotympanic tube dysfunction.",
    "modified Muncie",
    "The intraoral technique used for persistent pharyngotympanic tube dysfunction is the modified Muncie technique.",
    ["Muncie", "modified Muncie technique"],
))
qs.append(fb(
    "The general sequence rule for EENT OMT is __________ before peripherally.",
    "State the general sequence rule for EENT OMT.",
    "centrally",
    "The general sequence rule for EENT OMT is centrally before peripherally.",
    ["central", "central first"],
))
qs.append(fb(
    "In a patient with allergic rhinitis, paraspinal inhibition is targeted at spinal levels __________ to modulate sympathetic outflow to the upper airway.",
    "State the spinal levels for paraspinal inhibition in allergic rhinitis.",
    "T1 to T4",
    "In allergic rhinitis, paraspinal inhibition at T1-T4 is used to modulate sympathetic outflow to the upper airway.",
    ["T1-T4", "T1 through T4"],
))
qs.append(fb(
    "HVLA and forceful cranial work should be avoided in infants who still have open __________.",
    "Name the finding that precludes HVLA and forceful cranial work in infants.",
    "fontanelles",
    "HVLA and forceful cranial work should be avoided in infants who still have open fontanelles.",
    ["fontanels", "anterior fontanelle", "fontanelle"],
))

# Section 2 MCQ
qs.append(mcq(
    "Sympathetic supply to head and neck structures originates from which spinal levels?",
    "Identify the spinal origin of sympathetic supply to the head and neck.",
    [
        ("C3 to C5", False, "Sympathetic preganglionic fibers to the head and neck arise from T1-T4, not C3 to C5."),
        ("T1 to T4", True, "Sympathetic preganglionic fibers to the head and neck arise from T1-T4 and ascend through the sympathetic chain to synapse in the superior cervical ganglion."),
        ("T5 to T9", False, "Sympathetic preganglionic fibers to the head and neck arise from T1-T4, not T5 to T9."),
        ("T10 to L2", False, "Sympathetic preganglionic fibers to the head and neck arise from T1-T4, not T10 to L2."),
    ],
))
qs.append(mcq(
    "Which cranial nerve carries parasympathetic fibers to the lacrimal and nasal glands?",
    "Identify the cranial nerve to the lacrimal and nasal glands.",
    [
        ("CN III", False, "CN III synapses in the ciliary ganglion and supplies the eye, not the lacrimal and nasal glands."),
        ("CN V", False, "The head and neck parasympathetic supply named here is CN III, CN VII, CN IX, and CN X. CN V is not the nerve to the lacrimal and nasal glands."),
        ("CN VII", True, "The greater petrosal branch of the facial nerve (CN VII) carries preganglionic parasympathetic fibers that synapse in the pterygopalatine (sphenopalatine) ganglion before innervating lacrimal, nasal, and palatine glands."),
        ("CN IX", False, "CN IX synapses in the otic ganglion and supplies the parotid, not the lacrimal and nasal glands."),
    ],
))
qs.append(mcq(
    "Which cranial nerve provides sensory innervation to the face, sinuses, nasal cavity, and oropharynx?",
    "Identify the sensory nerve to the face and upper airway.",
    [
        ("CN V", True, "The trigeminal nerve (CN V) supplies general sensation to the face and most of the upper airway through V1 (ophthalmic), V2 (maxillary), and V3 (mandibular)."),
        ("CN VII", False, "General sensation to the face, sinuses, nasal cavity, and oropharynx is supplied by CN V, not CN VII."),
        ("CN IX", False, "General sensation to the face, sinuses, nasal cavity, and oropharynx is supplied by CN V, not CN IX."),
        ("CN X", False, "General sensation to the face, sinuses, nasal cavity, and oropharynx is supplied by CN V, not CN X."),
    ],
))
qs.append(mcq(
    "A child with recurrent acute otitis media is brought in for OMT between episodes. Which technique most directly addresses pharyngotympanic tube function?",
    "Identify the technique that most directly addresses pharyngotympanic tube function between episodes of recurrent otitis media.",
    [
        ("Suboccipital release", False, "The technique described for mobilizing the pharyngotympanic tube is the Galbreath (mandibular pump), not suboccipital release."),
        ("Galbreath (mandibular pump)", True, "The Galbreath technique applies gentle traction and pumping to the mandible to mobilize the pharyngotympanic tube and surrounding soft tissues. Small trials suggest benefit for recurrent pediatric otitis media."),
        ("Pectoral traction", False, "The technique described for mobilizing the pharyngotympanic tube is the Galbreath (mandibular pump), not pectoral traction."),
        ("Pedal pump", False, "The technique described for mobilizing the pharyngotympanic tube is the Galbreath (mandibular pump), not the pedal pump."),
    ],
))
qs.append(mcq(
    "The anterior Chapman point for the middle ear is found in which location?",
    "Locate the anterior Chapman point for the middle ear.",
    [
        ("Anterior 3rd intercostal space, parasternal", False, "The 3rd intercostal point corresponds to the upper lung, not the middle ear."),
        ("Anterior 4th intercostal space, parasternal", False, "The 4th intercostal point corresponds to the lower lung, not the middle ear."),
        ("Superior aspect of the clavicle near the midclavicular line", True, "The anterior Chapman reflex point for the middle ear is palpated on the superior surface of the clavicle near the midclavicular line."),
        ("Tip of the 12th rib", False, "The middle-ear Chapman point is on the superior surface of the clavicle near the midclavicular line, not the tip of the 12th rib."),
    ],
))
qs.append(mcq(
    "A 28-year-old with chronic sinusitis is best treated with which initial OMT step?",
    "Identify the initial OMT step for chronic sinusitis.",
    [
        ("Direct pressure over the maxillary sinuses", False, "The initial step is to open the central lymphatic gateway at the thoracic inlet before facial drainage maneuvers."),
        ("HVLA to the mid thoracic spine", False, "The initial step is myofascial release of the thoracic inlet, not mid-thoracic HVLA."),
        ("MFR thoracic inlet", True, "Open the central lymphatic gateway first. Releasing the thoracic inlet allows subsequent cervical and facial drainage maneuvers to mobilize fluid into a receptive central system."),
        ("Pedal pump", False, "The pedal pump is not the initial central step. The thoracic inlet is opened first."),
    ],
))
qs.append(mcq(
    "Which finding suggests sympathetic dominance in a patient with rhinitis?",
    "Identify the secretory finding of sympathetic dominance in rhinitis.",
    [
        ("Profuse, thin, watery secretions", False, "Thin, watery secretions are described with parasympathetic dominance."),
        ("Thick, tenacious mucus", True, "Sympathetic stimulation reduces and thickens secretions and produces mucosal vasoconstriction."),
        ("Salivary hypersecretion", False, "Salivation is described with parasympathetic dominance."),
        ("Lacrimation", False, "Lacrimation is described with parasympathetic dominance."),
    ],
))
qs.append(mcq(
    "Vagal somatic influence relevant to laryngopharyngeal symptoms is most directly addressed by treatment of which region?",
    "Identify the region treated for vagal somatic influence in laryngopharyngeal symptoms.",
    [
        ("T1 to T4", False, "T1-T4 is the sympathetic origin to the head and neck. Vagal somatic influence is addressed at OA-C2."),
        ("T5 to T9", False, "Vagal somatic influence is addressed at OA-C2, not T5 to T9."),
        ("OA to C2", True, "The vagus nerve exits the jugular foramen between the occiput and the upper cervical spine. Suboccipital release and OA-C2 work modulate vagal somatic influence."),
        ("L1 to L4", False, "Vagal somatic influence is addressed at OA-C2, not L1 to L4."),
    ],
))
qs.append(mcq(
    "Which technique is contraindicated in an infant with recurrent otitis media and an open anterior fontanelle?",
    "Identify the technique contraindicated when an infant has an open anterior fontanelle.",
    [
        ("Gentle suboccipital release", False, "Indirect, low-force techniques such as gentle suboccipital release are preferred when fontanelles are open."),
        ("HVLA to the cervical spine", True, "HVLA and forceful cranial work are contraindicated in infants with open fontanelles."),
        ("Galbreath (mandibular pump)", False, "The Galbreath technique is a low-force mandibular pump and is not the technique contraindicated by an open fontanelle."),
        ("MFR thoracic inlet", False, "Lymphatic techniques such as thoracic-inlet myofascial release are preferred when fontanelles are open."),
    ],
))
qs.append(mcq(
    "On opening of the jaw, deviation to the right suggests hypertonicity of which muscle?",
    "Identify the muscle implicated by rightward jaw deviation on opening.",
    [
        ("Right masseter", False, "The printed conclusion names the left lateral pterygoid, not the right masseter. " + JAW_NOTE),
        ("Left masseter", False, "The printed conclusion names the left lateral pterygoid, not the left masseter. " + JAW_NOTE),
        ("Right lateral pterygoid", False, "The opening clause of the explanation (deviation toward the hypertonic side) would point here, but the printed answer and the explanation's concluding sentence name the left lateral pterygoid. " + JAW_NOTE),
        ("Left lateral pterygoid", True, "The printed answer is the left lateral pterygoid. The explanation concludes that right deviation reflects hypertonicity of the left lateral pterygoid because the contralateral lateral pterygoid is the primary protruder. " + JAW_NOTE),
    ],
))
qs.append(mcq(
    "Which red flag should prompt immediate referral and preclude OMT?",
    "Identify the EENT red flag that precludes OMT and requires immediate referral.",
    [
        ("Mild facial pressure with clear rhinorrhea", False, "The red flag named here is postauricular swelling, fever, and a protruding pinna after recent acute otitis media, suggesting mastoiditis."),
        ("Postauricular swelling, fever, and protruding pinna after recent acute otitis media", True, "These findings suggest mastoiditis, which requires urgent imaging, ENT consultation, and antimicrobial therapy. OMT is contraindicated in this setting."),
        ("Chronic stuffiness with allergic shiners", False, "The red flag named here is postauricular swelling, fever, and a protruding pinna after recent acute otitis media, suggesting mastoiditis."),
        ("Episodic TMJ clicking without pain", False, "The red flag named here is postauricular swelling, fever, and a protruding pinna after recent acute otitis media, suggesting mastoiditis."),
    ],
))
qs.append(mcq(
    "Which cranial structure most directly influences pharyngotympanic tube angulation and venous sinus drainage?",
    "Identify the cranial structure that influences pharyngotympanic tube angulation and venous sinus drainage.",
    [
        ("Pterion", False, "Strain patterns at the sphenobasilar synchondrosis are what this item links to temporal-bone position, tube angulation, and venous sinus drainage."),
        ("Sphenobasilar synchondrosis", True, "Strain patterns at the sphenobasilar synchondrosis alter the relationship of the temporal bones, the angle of the pharyngotympanic tube, and venous sinus dynamics relevant to head and neck drainage."),
        ("Posterior fontanelle", False, "Strain patterns at the sphenobasilar synchondrosis are what this item links to temporal-bone position, tube angulation, and venous sinus drainage."),
        ("Pterygomaxillary fissure", False, "Strain patterns at the sphenobasilar synchondrosis are what this item links to temporal-bone position, tube angulation, and venous sinus drainage."),
    ],
))
qs.append(mcq(
    "Which structure relays parasympathetic fibers destined for the nasal mucosa?",
    "Identify the ganglion that relays parasympathetic fibers to the nasal mucosa.",
    [
        ("Otic ganglion", False, "The otic ganglion is the relay for parotid fibers (CN IX), not the nasal mucosa."),
        ("Submandibular ganglion", False, "The submandibular ganglion relays fibers to the submandibular and sublingual glands, not the nasal mucosa."),
        ("Sphenopalatine ganglion", True, "Preganglionic parasympathetic fibers from the greater petrosal nerve (CN VII) synapse in the sphenopalatine ganglion. Postganglionic fibers then travel to the lacrimal, nasal, and palatine mucosa."),
        ("Ciliary ganglion", False, "The ciliary ganglion relays CN III fibers to the pupil and ciliary muscle, not the nasal mucosa."),
    ],
))
qs.append(mcq(
    "Which technique is best paired with persistent pharyngotympanic tube dysfunction in a cooperative adult, when the operator is appropriately trained?",
    "Identify the technique used by a trained operator for persistent pharyngotympanic tube dysfunction.",
    [
        ("Modified Muncie (intraoral)", True, "Modified Muncie applies an intraoral fingertip contact near the pharyngotympanic tube orifice with gentle traction during swallowing. Appropriately trained operators use it for persistent tube dysfunction with effusion."),
        ("HVLA cervical thrust", False, "The technique named for persistent tube dysfunction with effusion is modified Muncie, not a cervical HVLA thrust."),
        ("Counterstrain to the masseter", False, "The technique named for persistent tube dysfunction with effusion is modified Muncie, not masseter counterstrain."),
        ("Pedal pump only", False, "The technique named for persistent tube dysfunction with effusion is modified Muncie, not the pedal pump alone."),
    ],
))
qs.append(mcq(
    "Which Chapman zone corresponds to general EENT reflexes on the posterior body wall?",
    "Locate the posterior Chapman zone for general EENT reflexes.",
    [
        ("Between T3 and T4 transverse processes", False, "The T3 to T4 zone corresponds to the upper lung, not general EENT reflexes."),
        ("Between T4 and T5 transverse processes", False, "The T4 to T5 zone corresponds to the lower lung, not general EENT reflexes."),
        ("C2 articular pillars", True, "The posterior Chapman zone for the EENT region is located at the articular pillars of C2."),
        ("Tip of the 12th rib", False, "The posterior EENT Chapman zone is at the C2 articular pillars, not the tip of the 12th rib."),
    ],
))
qs.append(mcq(
    "A 35-year-old with seasonal allergic rhinitis presents for adjunctive OMT. Which sequence is most appropriate?",
    "Select an OMT sequence for seasonal allergic rhinitis.",
    [
        ("HVLA T4 to T6, then pedal pump", False, "The described sequence opens the inlet, balances vagal tone at the suboccipital region and sympathetic tone at T1-T4, and ends with sphenopalatine contact."),
        ("MFR thoracic inlet, suboccipital release, paraspinal inhibition T1 to T4, sphenopalatine contact", True, "A sequence aligned with this item opens the inlet, balances autonomic tone (vagal via the suboccipital region, sympathetic via T1-T4), and concludes with sphenopalatine contact. Pharmacotherapy and allergen avoidance remain primary. The printed explanation collapsed the sympathetic range as T1T4; it is restored here as T1-T4."),
        ("Doming of the diaphragm only", False, "The described sequence is not limited to diaphragmatic doming."),
        ("Forceful sinus percussion", False, "The described sequence uses inlet release, suboccipital release, T1-T4 paraspinal inhibition, and sphenopalatine contact, not forceful sinus percussion."),
    ],
))
qs.append(mcq(
    "Which is an absolute contraindication to OMT in a patient with EENT complaints?",
    "Identify an absolute contraindication to OMT in an EENT complaint.",
    [
        ("Mild allergic rhinitis on intranasal steroids", False, "The absolute contraindication named here is suspected basilar skull fracture with clear rhinorrhea."),
        ("Suspected basilar skull fracture with clear rhinorrhea", True, "Clear rhinorrhea after head trauma raises concern for CSF leak and basilar skull fracture. OMT is absolutely contraindicated until the structural injury is excluded and stabilized."),
        ("Stable TMJ clicking", False, "The absolute contraindication named here is suspected basilar skull fracture with clear rhinorrhea."),
        ("Treated chronic sinusitis", False, "The absolute contraindication named here is suspected basilar skull fracture with clear rhinorrhea."),
    ],
))
qs.append(mcq(
    "Which statement about evidence for OMT in EENT conditions is most accurate?",
    "Identify the accurate statement about evidence for OMT in EENT conditions.",
    [
        ("OMT replaces antibiotics in confirmed bacterial sinusitis", False, "OMT is adjunctive and does not replace pharmacotherapy when indicated."),
        ("Adjunctive OMT may reduce recurrence and effusion in pediatric otitis media in small trials", True, "Small RCTs (Mills 2003) and a JAOA effusion trial (Steele 2014) suggest adjunctive OMT may reduce recurrence and middle-ear effusion in children with recurrent acute otitis media. OMT does not replace pharmacotherapy or surgery when indicated."),
        ("OMT cures allergic rhinitis", False, "OMT is adjunctive. This item does not state that OMT cures allergic rhinitis."),
        ("OMT eliminates the need for tympanostomy tubes in all patients", False, "OMT does not replace surgery when indicated."),
    ],
))
qs.append(mcq(
    "Which cranial nerve carries parasympathetic fibers to the pupillary constrictor and ciliary muscle?",
    "Identify the cranial nerve to the pupillary constrictor and ciliary muscle.",
    [
        ("CN II", False, "The oculomotor nerve (CN III), not CN II, carries these parasympathetic fibers."),
        ("CN III", True, "The oculomotor nerve (CN III) carries preganglionic parasympathetic fibers from the Edinger-Westphal nucleus to the ciliary ganglion, which then supplies the pupillary constrictor and ciliary muscle (pupillary miosis and lens accommodation)."),
        ("CN V", False, "The oculomotor nerve (CN III), not CN V, carries these parasympathetic fibers to the ciliary ganglion."),
        ("CN VII", False, "CN VII supplies lacrimal, nasal, and salivary targets in this packet. Pupillary constriction and the ciliary muscle are supplied via CN III."),
    ],
))
qs.append(mcq(
    "Parasympathetic supply to the parotid gland is mediated by which cranial nerve and ganglion?",
    "Identify the cranial nerve and ganglion for parasympathetic supply to the parotid.",
    [
        ("CN VII / pterygopalatine ganglion", False, "CN VII via the pterygopalatine ganglion supplies lacrimal and nasal mucosa, not the parotid."),
        ("CN VII / submandibular ganglion", False, "CN VII via the submandibular ganglion supplies the submandibular and sublingual glands, not the parotid."),
        ("CN IX / otic ganglion", True, "The glossopharyngeal nerve (CN IX) carries preganglionic parasympathetic fibers via the lesser petrosal nerve to the otic ganglion. Postganglionic fibers reach the parotid via the auriculotemporal branch of CN V3."),
        ("CN X / nodose ganglion", False, "Parotid parasympathetic supply in this item is CN IX to the otic ganglion, not CN X to the nodose ganglion."),
    ],
))
qs.append(mcq(
    "Match the parasympathetic ganglion to its target tissue. Which pairing is correct?",
    "Select the correct parasympathetic ganglion-to-target pairing.",
    [
        ("Ciliary ganglion to submandibular gland", False, "The ciliary ganglion supplies the pupil and ciliary muscle (CN III), not the submandibular gland."),
        ("Pterygopalatine ganglion to parotid gland", False, "The pterygopalatine ganglion supplies lacrimal and nasal mucosa (CN VII, greater petrosal). The parotid is supplied via the otic ganglion."),
        ("Submandibular ganglion to lacrimal gland", False, "The submandibular ganglion supplies the submandibular and sublingual glands (CN VII, chorda tympani). The lacrimal gland is supplied via the pterygopalatine ganglion."),
        ("Otic ganglion to parotid gland", True, "The otic ganglion supplies the parotid gland (CN IX, lesser petrosal). The other printed pairings are ciliary to pupil/ciliary muscle, pterygopalatine to lacrimal and nasal mucosa, and submandibular to submandibular and sublingual glands."),
    ],
))

# Section 3 vignettes
qs.append(mcq(
    "A 4-year-old presents with his fourth episode of acute otitis media in twelve months. Examination today shows a dull, retracted left tympanic membrane without bulging or fever. He is up to date on guideline-based pharmacotherapy. Which adjunctive OMT technique most directly addresses pharyngotympanic tube function?",
    "Choose adjunctive OMT for pharyngotympanic tube function between episodes of pediatric otitis media.",
    [
        ("HVLA to the cervical spine", False, "HVLA is contraindicated in children in this vignette."),
        ("Galbreath (mandibular pump)", True, "Galbreath gently mobilizes the mandible and surrounding tissue to support pharyngotympanic tube ventilation."),
        ("Pedal pump only", False, "The pedal pump is peripheral. Central tube mechanics are the priority here."),
        ("Direct pressure over the mastoid", False, "Direct mastoid pressure is inappropriate in this vignette."),
    ],
))
qs.append(mcq(
    "A 32-year-old with seasonal allergic rhinitis reports thick mucus, blocked nasal passages, and sinus pressure. Examination shows TART changes at T2-T4 and in the OA region. Which sequence opens the central pathway first?",
    "Order OMT so the central pathway is opened first in allergic rhinitis.",
    [
        ("Sphenopalatine contact, then HVLA T4", False, "Treat centrally before peripherally. The inlet is opened before facial and sphenopalatine work."),
        ("MFR thoracic inlet, then suboccipital release", True, "Treat centrally before peripherally. Open the inlet, then balance vagal tone at the suboccipital region before progressing to facial and sphenopalatine work. The printed vignette collapsed the thoracic finding as T2T4; it is restored here as T2-T4."),
        ("Direct sinus percussion, then pedal pump", False, "That sequence starts at the face. The central pathway is the thoracic inlet first."),
        ("Counterstrain to the masseter, then the thoracic inlet", False, "That sequence places the thoracic inlet after a peripheral step. Open the inlet first."),
    ],
))
qs.append(mcq(
    "A 6-month-old with otitis media with effusion is brought for adjunctive osteopathic care. The anterior fontanelle is still open. Which approach is most appropriate?",
    "Choose an OMT approach for an infant with an open anterior fontanelle.",
    [
        ("HVLA to C1", False, "Open fontanelles preclude HVLA."),
        ("Forceful cranial vault compression", False, "Open fontanelles preclude forceful cranial work."),
        ("Indirect, low-force suboccipital and gentle cervical lymphatic drainage", True, "Open fontanelles preclude HVLA and forceful cranial work. Indirect, low-force, and lymphatic techniques are preferred."),
        ("Direct mastoid percussion", False, "Direct mastoid percussion has no role in this vignette."),
    ],
))
qs.append(mcq(
    "A 50-year-old with chronic sinusitis returns after completing an antibiotic course. He is afebrile with persistent congestion. TART changes are noted at T1 and the right first rib. Which initial OMT step targets the central drainage gateway?",
    "Identify the initial OMT step for the central drainage gateway in chronic sinusitis.",
    [
        ("Pectoral traction", False, "The thoracic inlet is the central lymphatic gateway named for this step, addressed with myofascial release."),
        ("MFR thoracic inlet", True, "The thoracic inlet is the central lymphatic gateway for head and neck drainage. Restriction at T1, the first rib, the manubrium, and Sibson's fascia is addressed before peripheral pumps will be effective."),
        ("Pedal pump", False, "Peripheral pumps are not effective until the thoracic inlet gateway is addressed."),
        ("HVLA at T8", False, "The central gateway in this vignette is the thoracic inlet at T1 and the first rib, not T8 HVLA."),
    ],
))
qs.append(mcq(
    "A 25-year-old presents with right-sided jaw pain and clicking. On opening, the mandible deviates to the right. Which muscle is most likely hypertonic?",
    "Identify the hypertonic muscle when the mandible deviates to the right on opening.",
    [
        ("Right lateral pterygoid", False, "The opening clause of the explanation would point to the right lateral pterygoid, but the printed answer and concluding sentence name the left. " + JAW_NOTE),
        ("Left lateral pterygoid", True, "The printed answer is the left lateral pterygoid. The explanation says right-sided deviation indicates a hypertonic left lateral pterygoid because the contralateral muscle drives protrusion. " + JAW_NOTE),
        ("Right masseter", False, "The printed conclusion names the left lateral pterygoid, not the right masseter. " + JAW_NOTE),
        ("Left temporalis", False, "The printed conclusion names the left lateral pterygoid, not the left temporalis. " + JAW_NOTE),
    ],
))
qs.append(mcq(
    "A 7-year-old presents with sudden postauricular swelling, fever, and a protruding right pinna following a recent untreated otitis media. What is the most appropriate next step?",
    "Choose the next step for suspected mastoiditis.",
    [
        ("Galbreath technique today and follow up in two weeks", False, "These findings are concerning for mastoiditis. OMT is contraindicated until the acute process is addressed."),
        ("Lymphatic pump and discharge home", False, "These findings are concerning for mastoiditis, an emergency. OMT is contraindicated until the acute process is addressed."),
        ("Urgent imaging and ENT consultation; defer OMT", True, "Sudden postauricular swelling, fever, and a protruding pinna after otitis media are concerning for mastoiditis. This requires imaging, ENT consultation, and antimicrobial therapy. OMT is contraindicated until the acute process is addressed."),
        ("Modified Muncie technique", False, "Intraoral technique is not the next step. Mastoiditis requires urgent imaging and ENT consultation, and OMT is deferred."),
    ],
))
qs.append(mcq(
    "A 40-year-old has clear watery rhinorrhea after a recent fall with head impact. She also reports a salty taste in her throat. Which is the most appropriate next step?",
    "Choose the next step when clear rhinorrhea and a salty taste follow head impact.",
    [
        ("Sphenopalatine ganglion contact", False, "OMT is absolutely contraindicated until CSF leak and basilar skull fracture are excluded and stabilized."),
        ("Suboccipital release", False, "OMT is absolutely contraindicated until CSF leak and basilar skull fracture are excluded and stabilized."),
        ("Defer OMT and obtain neuroimaging to evaluate for CSF leak and basilar skull fracture", True, "Clear rhinorrhea with a salty taste after head trauma raises concern for CSF leak and basilar skull fracture. OMT is absolutely contraindicated until the structural injury is excluded and stabilized."),
        ("Galbreath technique", False, "OMT is absolutely contraindicated until CSF leak and basilar skull fracture are excluded and stabilized."),
    ],
))
qs.append(mcq(
    "A 22-year-old with viral pharyngitis has tender, enlarged anterior cervical nodes and TART at OA-C2. He is afebrile and well-appearing. Which adjunctive OMT step is appropriate?",
    "Choose adjunctive OMT for well-appearing viral pharyngitis.",
    [
        ("HVLA cervical thrust", False, "HVLA in active inflammation is inappropriate in this vignette."),
        ("MFR thoracic inlet and gentle cervical lymphatic drainage", True, "Open the inlet and support central drainage before peripheral work."),
        ("Forceful pharyngeal palpation", False, "Forceful pharyngeal palpation is not indicated for routine viral pharyngitis."),
        ("Modified Muncie technique", False, "Intraoral techniques are not indicated for routine viral pharyngitis."),
    ],
))
qs.append(mcq(
    "A 30-year-old has chronic morning headaches, jaw clicking, and tenderness over the masseter and temporalis. Cervical motion is restricted at the OA region. Which initial OMT approach best addresses the masticatory drivers?",
    "Choose an initial OMT approach for masticatory drivers of jaw pain and headache.",
    [
        ("HVLA to T4", False, "The approach named for the masticatory drivers is counterstrain to the masseter and temporalis, muscle energy for the TMJ, and suboccipital release."),
        ("Counterstrain to the masseter and temporalis, followed by muscle energy for the TMJ and suboccipital release", True, "Counterstrain addresses tender masticatory muscles, muscle energy restores TMJ tracking, and suboccipital release reduces the upper cervical contribution. Behavioral counseling on bruxism and posture is also advised."),
        ("Pedal pump", False, "The pedal pump does not address the masticatory muscles named in this vignette."),
        ("Sphenopalatine ganglion contact", False, "Sphenopalatine contact is not the approach named for masseter and temporalis tenderness and TMJ tracking."),
    ],
))
qs.append(mcq(
    "A 60-year-old smoker presents with persistent unilateral epistaxis, a fixed left cervical lymph node, and weight loss. What is the most appropriate next step?",
    "Choose the next step for red-flag head and neck findings.",
    [
        ("Adjunctive OMT for sinus drainage", False, "Persistent unilateral epistaxis, a fixed lymph node, and weight loss are red flags for head and neck malignancy. Defer regional OMT until evaluation is complete."),
        ("Galbreath technique", False, "These findings require urgent ENT referral. Regional OMT is deferred until evaluation is complete."),
        ("Urgent ENT referral to evaluate for malignancy", True, "Persistent unilateral epistaxis, a fixed lymph node, and weight loss are red flags for head and neck malignancy. Refer urgently and defer regional OMT until evaluation is complete."),
        ("Sphenopalatine ganglion contact", False, "These findings require urgent ENT referral. Regional OMT is deferred until evaluation is complete."),
    ],
))
qs.append(mcq(
    "A 12-year-old with chronic allergic rhinitis has thick tenacious mucus and pale boggy turbinates. Which autonomic state is most consistent with these findings?",
    "Identify the autonomic state associated with thick tenacious nasal mucus.",
    [
        ("Parasympathetic dominance", False, "Parasympathetic dominance more typically produces profuse, thin, watery secretions, lacrimation, and salivation."),
        ("Sympathetic dominance", True, "Sympathetic stimulation thickens secretions and constricts mucosal vessels. The printed answer keys thick tenacious mucus to sympathetic dominance."),
        ("Balanced autonomic tone", False, "The item keys thick tenacious mucus to sympathetic dominance, not balanced tone."),
        ("Adrenal insufficiency", False, "The item keys thick tenacious mucus to sympathetic dominance, not adrenal insufficiency."),
    ],
))
qs.append(mcq(
    "A 9-year-old with recurrent otitis media with effusion has persistent middle ear fluid despite a complete course of antibiotics. The operator is trained in intraoral techniques. Which technique most directly addresses pharyngotympanic tube dysfunction in this setting?",
    "Choose a technique for persistent pharyngotympanic tube dysfunction with effusion when the operator is trained.",
    [
        ("Pedal pump alone", False, "Modified Muncie is the technique named for persistent tube dysfunction with effusion."),
        ("Modified Muncie technique", True, "Modified Muncie applies a gentle intraoral fingertip contact near the pharyngotympanic tube orifice with traction during swallowing. It is reserved for trained operators and persistent tube dysfunction with effusion."),
        ("HVLA to T6", False, "Modified Muncie is the technique named for persistent tube dysfunction with effusion, not HVLA to T6."),
        ("Direct cranial vault compression", False, "Modified Muncie is the technique named for persistent tube dysfunction with effusion, not direct cranial vault compression."),
    ],
))
qs.append(mcq(
    "A 45-year-old presents for adjunctive OMT for recurrent sinusitis. Examination shows restriction along the right first rib, the manubrium, and Sibson's fascia. Which structure is most directly addressed by MFR in this region?",
    "Identify what thoracic-inlet myofascial release addresses when the right first rib, manubrium, and Sibson's fascia are restricted.",
    [
        ("Stellate ganglion alone", False, "Myofascial release in this region is described as addressing the central lymphatic and venous pathway, not the stellate ganglion alone."),
        ("Right lymphatic and venous drainage from the head and neck through the central pathway", True, "The thoracic inlet is the central gateway. Lymph from the right side of the head and neck drains via the right lymphatic duct into the right subclavian vein. Restriction at T1, the first rib, the manubrium, and Sibson's fascia mechanically impairs this terminal pathway."),
        ("The lower thoracic diaphragm", False, "The structures named are at the thoracic inlet, the central gateway for head and neck drainage, not the lower thoracic diaphragm."),
        ("The pelvic diaphragm only", False, "The structures named are at the thoracic inlet, not the pelvic diaphragm."),
    ],
))
qs.append(mcq(
    "A 15-year-old with TMJ pain has tenderness over the lateral pterygoid bilaterally and limited jaw opening. Which OMT category is most appropriate as a first step?",
    "Choose a first OMT step for bilateral lateral pterygoid tenderness and limited jaw opening.",
    [
        ("HVLA to the TMJ", False, "Aggressive HVLA at the TMJ is not indicated."),
        ("Counterstrain and muscle energy to the masticatory muscles and TMJ", True, "Indirect and gentle direct techniques restore mandibular tracking with low risk."),
        ("High-velocity cervical thrust", False, "The first step named for this TMJ presentation is counterstrain and muscle energy, not a high-velocity cervical thrust."),
        ("Forceful intraoral pharyngeal release", False, "Forceful pharyngeal release is unrelated to this TMJ presentation."),
    ],
))
qs.append(mcq(
    "A 70-year-old with sudden painless monocular vision loss and a tender temporal artery presents to the clinic. The patient asks whether OMT could relieve her symptoms. What is the most appropriate next step?",
    "Choose the next step for sudden painless monocular vision loss with temporal artery tenderness.",
    [
        ("Sphenopalatine contact for vasomotor symptoms", False, "This presentation is concerning for giant cell arteritis. OMT has no role until acute pathology is excluded and treated."),
        ("MFR thoracic inlet and reassess in two weeks", False, "This is an ophthalmologic and rheumatologic emergency. OMT has no role until acute pathology is excluded and treated."),
        ("Defer OMT; obtain urgent evaluation for giant cell arteritis and ophthalmologic assessment", True, "Sudden painless monocular vision loss with temporal artery tenderness is concerning for giant cell arteritis with possible anterior ischemic optic neuropathy. This is an ophthalmologic and rheumatologic emergency. OMT has no role until acute pathology is excluded and treated."),
        ("Counterstrain to the temporalis", False, "Temporalis counterstrain is not the next step. Urgent evaluation for giant cell arteritis and ophthalmologic assessment comes first."),
    ],
))
qs.append(mcq(
    "A 29-year-old man presents with acute maxillary sinusitis. On screening for the anterior Chapman point associated with the sinuses, where should the physician most expect to palpate a tender, nodular ganglioform contraction?",
    "Locate the anterior Chapman point for the sinuses.",
    [
        ("The upper edge of the 2nd rib, a few centimeters lateral to the sternum", True, "The anterior Chapman point for the sinuses lies on the upper edge of the 2nd rib near the parasternal region, a few centimeters lateral to the sternum."),
        ("The xiphoid process", False, "The xiphoid is not a Chapman location in this item."),
        ("The spine of the scapula", False, "The scapular spine is not a Chapman location in this item."),
        ("The angle of the mandible", False, "The mandibular angle is not a Chapman location in this item."),
        ("The tip of the transverse process of C2", False, "The C2 transverse process is the posterior sinus point, not the anterior Chapman point."),
    ],
))
qs.append(mcq(
    "A 34-year-old woman is treated for acute sinusitis. The physician performs doming of the abdominal diaphragm. This technique produces its principal therapeutic benefit through which of the following mechanisms?",
    "Identify the principal mechanism of diaphragmatic doming in acute sinusitis.",
    [
        ("Raising sympathetic tone to constrict nasal blood vessels", False, "Doming does not directly change autonomic tone."),
        ("Interrupting nociceptive afferents from the trigeminal nerve", False, "Doming does not interrupt nociception."),
        ("Blocking neurogenic release of inflammatory mediators", False, "Doming does not block neurogenic inflammation."),
        ("Directly lowering parasympathetic outflow to the nasal mucosa", False, "Doming does not directly change autonomic tone."),
        ("Enhancing venous and lymphatic return through increased diaphragmatic excursion", True, "Doming restores diaphragmatic excursion and the pressure differentials that drive central lymphatic and venous return. This lymphatic effect is its principal mechanism."),
    ],
))
qs.append(mcq(
    "A 59-year-old woman with acute viral pharyngitis is treated with rib raising over the upper thoracic region. The intended benefit of this technique is most directly achieved by modulation of which of the following?",
    "Identify the direct target of upper thoracic rib raising.",
    [
        ("Parasympathetic tone", False, "Other techniques address parasympathetic tone at OA-C2. Rib raising most directly modulates sympathetic tone."),
        ("Sympathetic tone", True, "Rib raising over T1-T4 stimulates and then normalizes the paravertebral sympathetic chain, so its most direct effect is modulation of sympathetic tone."),
        ("Lymphatic drainage", False, "Lymphatic drainage is addressed by other techniques. Rib raising most directly modulates sympathetic tone."),
        ("Neurogenic inflammation", False, "Neurogenic inflammation is addressed by other techniques. Rib raising most directly modulates sympathetic tone."),
        ("Mucociliary beat frequency", False, "Mucociliary rate is a downstream rather than direct target of rib raising."),
    ],
))
qs.append(mcq(
    "A 51-year-old man reports right-sided facial pressure over the cheek during a bout of viral rhinitis. The physician applies gentle digital pressure over the right infraorbital foramen. This maneuver most likely benefits the patient by which of the following mechanisms?",
    "Identify the mechanism of inhibitory pressure at the infraorbital foramen.",
    [
        ("Reducing sympathetic vasoconstriction of the sinus mucosa", False, "Infraorbital inhibitory pressure is not intended to directly alter autonomic tone."),
        ("Increasing motion of the maxillary bone", False, "Infraorbital inhibitory pressure is not intended to move bone."),
        ("Directly reducing parasympathetic tone to the sinus mucosa", False, "Infraorbital inhibitory pressure is not intended to directly alter autonomic tone."),
        ("Thickening nasal secretions to reduce postnasal drip", False, "Infraorbital inhibitory pressure is not intended to thicken mucus."),
        ("Reducing neurogenic inflammation by inhibiting the V2 division of the trigeminal nerve", True, "The infraorbital foramen transmits the maxillary (V2) division of the trigeminal nerve. Inhibitory pressure there reduces the neurogenic inflammatory signaling responsible for facial pain and congestion."),
    ],
))
qs.append(mcq(
    "In a patient with acute viral sinusitis, treatment directed at which of the following regions is most likely to influence sympathetically mediated arterial blood flow to the maxillary sinuses?",
    "Identify the region that influences sympathetic vasomotor tone to the maxillary sinuses.",
    [
        ("C3 to C5", False, "C3 to C5 is not the sympathetic origin for the head and neck."),
        ("T10 to L2", False, "T10 to L2 supplies abdominal structures, not sinus vasomotor tone."),
        ("T5 to T9", False, "T5 to T9 supplies lower thoracic structures, not sinus vasomotor tone."),
        ("T1 to T4", True, "Sympathetic supply to the head and neck, including sinus vasomotor tone, originates from T1-T4."),
        ("OA to C2", False, "OA-C2 governs parasympathetic (vagal) tone, not sympathetic arterial flow to the sinuses."),
    ],
))
qs.append(mcq(
    "A 24-year-old patient presents with nasal congestion, facial pressure, and tender anterior cervical lymph nodes. Which of the following treatment sequences best reflects opening the central pathway before mobilizing regional and facial drainage?",
    "Order treatment from the central pathway to regional and facial drainage.",
    [
        ("Anterior cervical myofascial release, thoracic inlet release, thoracic pump, maxillary effleurage", False, "This sequence does not open the thoracic inlet first."),
        ("Submandibular release, maxillary effleurage, thoracic inlet release, anterior cervical myofascial release", False, "This sequence starts peripherally and places the inlet late."),
        ("Thoracic inlet release, anterior cervical myofascial release, submandibular release, maxillary effleurage", True, "Treat centrally first (thoracic inlet), then regionally (anterior cervical and submandibular), then locally (maxillary effleurage)."),
        ("Thoracic pump, maxillary effleurage, submandibular release, thoracic inlet release", False, "This sequence places the thoracic inlet last."),
        ("Maxillary effleurage, submandibular release, anterior cervical myofascial release, thoracic inlet release", False, "This sequence starts at the face and places the inlet last."),
    ],
))
qs.append(mcq(
    "A 44-year-old man has chronic nasal congestion. Sustained, excessive sympathetic stimulation of his nasal mucosa is most likely to produce which of the following changes?",
    "Identify the mucosal change produced by sustained sympathetic stimulation.",
    [
        ("A higher prevalence of goblet cells with thicker secretions", True, "Sympathetic dominance causes vasoconstriction and thick, tenacious secretions, favoring a goblet-cell phenotype."),
        ("Viscerosomatic reflex activity at T5 to T9", False, "The sinus and nasal viscerosomatic reflex maps to T1-T4, not T5 to T9."),
        ("More abundant, watery nasal secretions", False, "Watery secretions indicate parasympathetic dominance."),
        ("Mucosal vasodilation and boggy turbinates", False, "Vasodilation indicates parasympathetic dominance. Sympathetic stimulation causes vasoconstriction."),
        ("Increased density of ciliated epithelial cells", False, "The change named for sympathetic dominance is a goblet-cell phenotype with thicker secretions."),
    ],
))
qs.append(mcq(
    "The postganglionic parasympathetic fibers that supply the mucosa of the paranasal sinuses arise from which of the following structures?",
    "Identify the source of postganglionic parasympathetic fibers to sinus mucosa.",
    [
        ("Superior cervical ganglion", False, "The superior cervical ganglion is sympathetic."),
        ("Sphenopalatine (pterygopalatine) ganglion", True, "CN VII parasympathetic fibers synapse in the sphenopalatine (pterygopalatine) ganglion, whose postganglionic fibers supply the sinus and nasal mucosa and the lacrimal gland."),
        ("Stellate ganglion", False, "The stellate ganglion is sympathetic."),
        ("Nerve of the pterygoid canal", False, "The nerve of the pterygoid canal carries preganglionic fibers, not the postganglionic sinus supply."),
        ("Superior salivary nucleus", False, "The superior salivary nucleus is the brainstem origin of the preganglionic fibers, not the postganglionic source."),
    ],
))
qs.append(mcq(
    "A 31-year-old woman with acute otitis media is treated with the Galbreath technique. This technique most directly improves the patient's condition by which of the following mechanisms?",
    "Identify the principal mechanism of the Galbreath technique in acute otitis media.",
    [
        ("Increasing sympathetic tone to the middle ear", False, "Galbreath is not primarily an autonomic-tone technique."),
        ("Reducing neurogenic inflammation of the tympanic membrane", False, "Galbreath is not primarily an antinociceptive or neurogenic-inflammation technique."),
        ("Increasing parasympathetic tone to the middle ear", False, "Galbreath is not primarily an autonomic-tone technique."),
        ("Promoting Eustachian tube opening and middle ear drainage", True, "The Galbreath (mandibular pump) technique promotes Eustachian tube opening and middle-ear and oropharyngeal drainage, which is its principal benefit in otitis media."),
        ("Interrupting nociceptive afferents from the auricle", False, "Galbreath is not primarily an antinociceptive technique."),
    ],
))
qs.append(mcq(
    "The postganglionic sympathetic fibers that supply the mucosa of the paranasal sinuses originate from which of the following structures?",
    "Identify the source of postganglionic sympathetic fibers to sinus mucosa.",
    [
        ("Sphenopalatine ganglion", False, "The sphenopalatine ganglion is parasympathetic."),
        ("Superior salivary nucleus", False, "The superior salivary nucleus is parasympathetic."),
        ("Superior cervical ganglion", True, "Preganglionic sympathetic fibers from T1-T4 ascend and synapse in the superior cervical ganglion. Its postganglionic fibers follow the carotid plexus to the sinus mucosa."),
        ("Stellate ganglion", False, "The chain and stellate ganglia are not the source of the sinus postganglionic supply in this item."),
        ("T1 to T3 sympathetic chain ganglia", False, "Preganglionic fibers arise from T1-T4, but the postganglionic sinus supply originates in the superior cervical ganglion, not the chain ganglia."),
    ],
))

# Section 4 open
qs.append(open_q(
    "Thoracic inlet and head and neck drainage. Describe how somatic dysfunction at the thoracic inlet can impair lymphatic and venous drainage from the head and neck. How would you assess and treat it?",
    "Explain how thoracic-inlet somatic dysfunction impairs head and neck drainage and how it is assessed and treated.",
    "Lymph from the head and neck converges through the right lymphatic duct (right side) and the thoracic duct (left side) before entering the venous system at the junction of the internal jugular and subclavian veins. Restriction at the thoracic inlet, including fascial tightness, first rib dysfunction, clavicular asymmetry, manubrial restriction, or tension along Sibson's fascia, mechanically compresses these terminal pathways and impairs central drainage. Assessment includes palpation for TART changes at T1 and the first ribs, the sternoclavicular joints, the manubrium, and the cervicothoracic fascia. Treatment commonly begins with myofascial release of the thoracic inlet, followed by suboccipital release and gentle cervical lymphatic drainage to support central flow before any peripheral pumping.",
    "Name the right lymphatic duct and thoracic duct, the inlet structures that compress them, the TART screen, and a central-before-peripheral treatment order.",
))
qs.append(open_q(
    "Autonomic balance in EENT disease. Explain how autonomic imbalance contributes to symptom expression in upper airway conditions. Which spinal and cranial regions would you evaluate, and why?",
    "Explain autonomic contributions to upper-airway symptoms and the regions to evaluate.",
    "Sympathetic supply to head and neck structures arises from T1-T4 and ascends through the superior cervical ganglion. Sympathetic stimulation thickens secretions and constricts mucosal vessels. Parasympathetic supply via CN VII (greater petrosal to the sphenopalatine ganglion) drives lacrimal, nasal, and pharyngeal gland secretion, while vagal influence reaches the laryngopharynx. Evaluate T1-T4 for sympathetic outflow, OA-C2 for vagal influence, and cranial mechanics around the sphenopalatine ganglion. Suboccipital release and paraspinal inhibition at T1-T4 can rebalance autonomic tone in conditions such as allergic rhinitis and sinusitis.",
    "Contrast sympathetic thickening and vasoconstriction with CN VII and vagal parasympathetic secretion, and name T1-T4, OA-C2, and the sphenopalatine region.",
))
qs.append(open_q(
    "Pediatric otitis media. Explain why young children are predisposed to recurrent acute otitis media from an osteopathic perspective. Outline an adjunctive OMT plan.",
    "Explain the osteopathic predisposition to pediatric otitis media and outline adjunctive OMT.",
    "In children, the pharyngotympanic tube is shorter, more horizontal, and more easily obstructed. Cranial base and temporal bone strain patterns can further alter tube angulation and drainage. Adjunctive OMT focuses on improving tube ventilation and central lymphatic drainage. A typical sequence is myofascial release of the thoracic inlet, suboccipital release, gentle temporal bone balancing, Galbreath (mandibular pump), and soft cervical lymphatic drainage. HVLA and forceful cranial work are avoided in infants and patients with open fontanelles. OMT is adjunctive to guideline-based pharmacotherapy and ENT evaluation when indicated.",
    "Include tube shape, cranial-base strain, the inlet-to-Galbreath sequence, and the fontanelle contraindication.",
))
qs.append(open_q(
    "Sinusitis and the central pathway. A patient presents with chronic rhinosinusitis. Outline an evidence-aligned osteopathic approach and explain the sequence.",
    "Outline the osteopathic sequence for chronic rhinosinusitis.",
    "The approach is adjunctive to medical management, including saline irrigation, intranasal steroids, and antibiotics when bacterial infection is confirmed. The osteopathic sequence opens the central pathway first and progresses peripherally. Begin with myofascial release of the thoracic inlet, then suboccipital release to support vagal tone and cervical drainage, then paraspinal inhibition at T1-T4 to modulate sympathetic outflow, then gentle facial effleurage over the frontal, maxillary, and zygomatic regions, and finally sphenopalatine ganglion contact for parasympathetic balance. Reassess after each step. Avoid forceful pressure when orbital or intracranial extension is suspected.",
    "Keep OMT adjunctive, and order the steps from the thoracic inlet to sphenopalatine contact.",
))
qs.append(open_q(
    "Galbreath technique. Describe the rationale, indication, and basic execution of the Galbreath (mandibular pump) technique.",
    "Describe the rationale, indication, and execution of the Galbreath technique.",
    "Galbreath, also known as the mandibular pump, applies a gentle traction and pumping motion at the mandible to mobilize the temporomandibular and parapharyngeal soft tissue and to support pharyngotympanic tube ventilation. Indications include recurrent acute otitis media and otitis media with effusion in pediatric patients between acute episodes. With the patient supine, the operator cradles the mandible, applies gentle inferior and lateral traction toward the affected side, and rhythmically releases the contact. Pratt-Harrington, JAOA 2000, provides a classic description of the technique.",
    "Include the mandibular-pump rationale, the pediatric otitis indication, and the supine traction-and-release setup.",
))
qs.append(open_q(
    "Modified Muncie technique. Describe the rationale, indication, and operator considerations for the modified Muncie technique.",
    "Describe the rationale, indication, and cautions for the modified Muncie technique.",
    "Modified Muncie is an intraoral technique that places a gloved fingertip in contact near the pharyngotympanic tube orifice and applies gentle traction during patient swallowing. The aim is to release fascial and muscular restriction around the tube and improve middle-ear ventilation in persistent pharyngotympanic tube dysfunction with effusion. It is reserved for appropriately trained operators, requires informed consent, and is contraindicated in acute oropharyngeal infection, peritonsillar abscess, or recent oropharyngeal surgery. Channell, JAOA 2008, provides a contemporary description.",
    "Include the intraoral contact, the effusion indication, training and consent, and the stated contraindications.",
))
qs.append(open_q(
    "TMJ dysfunction. Outline an osteopathic assessment and treatment plan for a patient with temporomandibular dysfunction.",
    "Outline assessment and treatment for temporomandibular dysfunction.",
    "Begin with history (clicking, locking, headache, bruxism) and inspection (facial symmetry, mandibular tracking, deviation on opening). Palpate the masseter, temporalis, and lateral pterygoid for tone and tender points. The packet states that the mandible deviates toward the side of the hypertonic lateral pterygoid on opening; a separate board-style item in this packet concludes that right-sided deviation indicates a hypertonic left lateral pterygoid because the contralateral muscle drives protrusion. Assess cervical motion, especially OA-C2. Treat with counterstrain to tender masticatory muscles, muscle energy for TMJ tracking, suboccipital release, and cervical articulation. Trained operators may use intraoral techniques. Add behavioral counseling on bruxism, jaw rest, posture, and sleep hygiene. Avoid aggressive HVLA at the TMJ and refer when septic arthritis, dislocation, or fracture is suspected.",
    "The sample answer states deviation toward the hypertonic lateral pterygoid. A board-style item in the same packet keys right deviation to the left lateral pterygoid. Both statements are kept, and the directional mismatch is noted here.",
))
qs.append(open_q(
    "Chapman points in EENT. Identify the key Chapman reflex points relevant to EENT practice and explain their use.",
    "Identify EENT Chapman points and their use.",
    "Posterior Chapman zones for the EENT region are located at the C2 articular pillars bilaterally. Anterior points sit along the clavicles, the sternoclavicular joints, and the upper rib zones. The middle-ear point is found on the superior aspect of the clavicle near the midclavicular line. Tender, ropy, or boggy tissue at these landmarks suggests segmental viscerosomatic facilitation. Inhibitory contact at these points can serve as a diagnostic and therapeutic adjunct alongside more comprehensive autonomic and lymphatic work.",
    "Name the C2 pillars, clavicular and upper-rib anterior points, and the middle-ear point on the clavicle.",
))
qs.append(open_q(
    "Cranial considerations. Explain how cranial mechanics influence EENT function and which structures merit attention.",
    "Explain cranial mechanics relevant to EENT function.",
    "The temporal bones house the auditory and vestibular apparatus and articulate with the sphenoid and occiput. Sphenobasilar synchondrosis strain patterns alter the position of the temporal bones, the angle of the pharyngotympanic tube, and venous sinus drainage. The occipitomastoid suture lies near the jugular foramen, where cranial nerves IX, X, and XI exit. Gentle balancing of the sphenobasilar synchondrosis, temporal bones, and occipitomastoid region can support drainage and autonomic balance. Indirect, low-force technique is preferred, and forceful cranial work is avoided in children with open fontanelles and in any patient with suspected fracture or intracranial pathology.",
    "Include the temporal bones, sphenobasilar synchondrosis, occipitomastoid suture, and the fontanelle and fracture cautions.",
))
qs.append(open_q(
    "Red flags in EENT practice. List red flags that should prompt immediate referral and preclude OMT in the EENT patient.",
    "List EENT red flags that preclude OMT.",
    "Sudden vision loss, painful red eye, or new diplopia. Sudden sensorineural hearing loss or vertigo with neurologic deficit. Severe headache with focal neurologic findings, papilledema, or meningismus. Postauricular swelling with protruding pinna, suggesting mastoiditis. Suspected basilar skull fracture or CSF rhinorrhea. Orbital cellulitis or abscess. Persistent unilateral epistaxis, fixed cervical lymphadenopathy, or weight loss suggesting head and neck malignancy. Signs of meningitis or peritonsillar abscess. Refer urgently and defer regional OMT until acute pathology is excluded and the patient is stabilized.",
    "List the packet's referral triggers, including mastoiditis, CSF leak, orbital infection, and malignancy flags.",
))
qs.append(open_q(
    "Patient communication. Describe how you would explain to a parent why their child with frequent otitis media might benefit from adjunctive OMT, and how you would set realistic expectations.",
    "Explain adjunctive OMT for frequent pediatric otitis media and set realistic expectations.",
    "In children, the pharyngotympanic tube is shorter, more horizontal, and more easily obstructed, and cranial base and temporal bone strain can further alter tube angulation and drainage. Adjunctive OMT focuses on tube ventilation and central lymphatic drainage. A typical sequence is myofascial release of the thoracic inlet, suboccipital release, gentle temporal bone balancing, Galbreath (mandibular pump), and soft cervical lymphatic drainage. HVLA and forceful cranial work are avoided in infants and in patients with open fontanelles. Small trials (Mills 2003 and Steele 2014) suggest adjunctive OMT may reduce recurrence and middle-ear effusion. OMT does not replace guideline-based pharmacotherapy or surgery, including tympanostomy tubes, when those are indicated, and it does not cure otitis media.",
    "The printed sample answer is cut off after the prompt. This model answer is completed only from earlier items in the same packet: the pediatric otitis media review (tube shape, cranial-base strain, inlet-to-Galbreath sequence, and the open-fontanelle caution) and the evidence item (small trials may reduce recurrence and effusion; OMT is adjunctive and does not replace pharmacotherapy or surgery).",
))

out = Path(__file__).resolve().parent / "quizzes" / "omm-b5-eent.json"
out.write_text(json.dumps(qs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("questions", len(qs))
from collections import Counter
print(Counter(q["type"] for q in qs))
lecture = [i for i, q in enumerate(qs) if "lecture" in q["question"].lower()]
print("lecture stems", lecture)
for i, q in enumerate(qs):
    if q["type"] == "mcq":
        n = sum(1 for o in q["options"] if o["isCorrect"])
        if n != 1 or len(q["options"]) < 2:
            print("bad mcq", i, n, len(q["options"]))
print("wrote", out)
