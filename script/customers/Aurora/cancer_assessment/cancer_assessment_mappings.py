PRIMARY_TUMOR = ('', 'T1mic', 'T4a', 'T2a', 'T2c', 'T2b', 'Tis', 'Tis (DCIS)', 'pT3a', 'T2a2', 'pT3b', 'Ta', 'TX', 'pT2c', 'T4d', 'T4c', 'T1b2', 'T1b1', 'pT4', 'pT3', 'pT2', 'pT1', 'pT0',
                 'T1a', 'T1b', 'T1c', 'T3b', 'T4', 'T2', 'T3', 'T0', 'T1', 'T2a1', 'T3c', 'pTX', 'T3a', 'pT2b', 'Tis (LCIS)', 'pT2a', 'T1a2', 'T1a1', "Tis (Paget's)", 'T4b')

LYMPH = ('', 'N0(i+)', 'N1', 'N0(i-)', 'NX', 'N3a', 'N3b', 'N3c', 'N1b', 'N1c', 'N1a', 'N0b (no biopsy)',
         'N0', 'N1mi', 'N2', 'N3', 'N2c', 'N2b', 'N2a', 'N0(mol+)', 'N0(mol-)')

METASTASIS = ('', 'M1a', 'M1c', 'M1b', 'M1', 'M0', 'cM0(i+)', 'MX', 'cM0')

HISTOLOGY = ('', 'Adenoid cystic carcinoma', 'HISTOPATHOLOGIC_TYPE_NAME', 'Desmoplastic melanoma, malignant', 'Papillary squamous cell carcinoma', 'Epithelial-myoepithelial carcinoma', 'Squamous cell carcinoma, keratinizing, NOS', 'Small cell carcinoma, intermediate cell', 'Squamous cell carcinoma, spindle cell', 'Dedifferentiated chondrosarcoma', 'Granular cell carcinoma', 'Adenocarcinoma in situ in tubulovillous adenoma', 'Papillary cystadenocarcinoma', 'Lentigo maligna melanoma', 'Mixed germ cell tumor', 'Tubular adenocarcinoma', 'Burkitt lymphoma, NOS', 'Acinar cell carcinoma', 'Renal cell carcinoma, chromophobe type', 'Papillary squamous cell carcinoma, non-invasive', 'Adenosarcoma', 'Adenocarcinoma in villous adenoma', 'Ductal adenocarcinoma', 'Endometrioid adenocarcinoma, NOS', 'Embryonal carcinoma, NOS', 'Gastrointestinal stromal sarcoma', 'Neoplasm, malignant', 'Leiomyosarcoma, NOS', 'Carcinoma in situ, NOS', 'Mucoepidermoid carcinoma', 'Neuroendocrine carcinoma, NOS', 'Papillary serous cystadenocarcinoma', 'Malignant lymphoma, large B-cell, diffuse, NOS', 'Carcinoid tumor, NOS', 'Adenocarcinoma with cartilaginous and osseous metaplasia', 'Cutaneous T-cell lymphoma, NOS',
             'Merkel cell carcinoma', 'Non-small cell carcinoma', 'Adenocarcinoma in adenomatous polyposis coli', 'Adenocarcinoma, intestinal type', 'Serous cystadenocarcinoma, NOS', 'Squamous cell carcinoma in situ, NOS', 'Carcinoma, undifferentiated, NOS', 'NK/T-cell lymphoma, nasal and nasal-type', 'Verrucous carcinoma, NOS', 'Serous adenocarcinofibroma', 'Sex cord-gonadal stromal tumor, NOS', 'Basaloid squamous cell carcinoma', 'Nodular melanoma', 'Small cell carcinoma, fusiform cell', 'Squamous cell carcinoma, large cell', 'Granulosa cell tumor, adult type', 'Papillary transitional cell carcinoma, non-invasive', 'Rhabdomyosarcoma, NOS', 'Fibrosarcoma, NOS', 'Large cell neuroendocrin carcinoma', 'Follicular lymphoma, NOS', 'Adenocarcinoma, NOS', 'Malignant lymphoma, small B lymphocytic, NOS', 'Hepatocellular carcinoma', 'Intraductal papillary adenocarcinoma with invasion', 'Hodgkin lymphoma, nodular sclerosis, grade 1', 'Mediastinal large B-cell lymphoma', 'Basal cell carcinoma, NOS', 'Alveolar adenocarcinoma', 'Cloacogenic carcinoma', 'Spindle cell carcinoma, NOS', 'Papillary carcinoma, encapsulated', 'Intraductal carcinoma and lobular carcinoma in situ')


STAGE_GROUP = {
    "": "",
    "Stage 0": "0",
    "Stage 0a": "0a",
    "Stage 0is": "0is",
    "Stage I": "I",
    "Stage IA": "IA",
    "Stage IA1": "IA1",
    "Stage IA2": "IA2",
    "Stage IB": "IB",
    "Stage IB1": "IB1",
    "Stage IB2": "IB2",
    "Stage IC": "IC",
    "Stage IE (lymphoma only)": "I",
    "Stage II": "II",
    "Stage IIA": "IIA",
    "Stage IIA2": "IIA2",
    "Stage IIB": "IIB",
    "Stage IIC": "IIC",
    "Stage IIE (lymphoma only)": "II",
    "Stage III": "III",
    "Stage IIIA": "IIIA",
    "Stage IIIB": "IIIB",
    "Stage IIIC": "IIIC",
    "Stage IIIC1": "IIIC1",
    "Stage IIIC2": "IIIC2",
    "Stage IIIE (lymphoma only)": "III",
    "Stage IIIES (lymphoma only)": "III",
    "Stage IIIS (lymphoma only)": "III",
    "Stage IS": "I",
    "Stage IV": "IV",
    "Stage IVA": "IVA",
    "Stage IVB": "IVB",
    "Stage IVC": "IVC",
    "Stage Occult": "Occult",
    "Stage Unknown": "null"
}

BODY_SITE = {
    "": "",
    "Abdomen": "Abdomen",
    "Abdominal part of esophagus": "Abdominal part of esophagus",
    "Accessory sinus": "Accessory sinus",
    "Accessory sinuses (all C31 sites)": "Accessory sinuses (all C31 sites)",
    "Acoustic nerve": "Acoustic nerve",
    "Adrenal Gland": "Adrenal gland, NOS",
    "Adrenal gland (all C74 sites)": "Adrenal gland (all C74 sites)",
    "Ampulla of Vater": "Ampulla of vater",
    "Ampulla of vater": "Ampulla of vater",
    "Anal canal": "Anal canal",
    "Anterior floor of mouth": "Anterior floor of mouth",
    "Anterior mediastinum": "Anterior mediastinum",
    "Anterior surface of epiglottis": "Anterior surface of epiglottis",
    "Anterior two-thirds of tongue": "Anterior two-thirds of tongue",
    "Anterior wall of bladder": "Anterior wall of bladder",
    "Anterior wall of nasopharynx": "Anterior wall of nasopharynx",
    "Anus": "Anus",
    "Anus and anal canal (all C21 sites)": "Anus and anal canal (all C21 sites)",
    "Aortic body & other paraganglia": "Aortic body & other paraganglia",
    "Appendix": "Appendix",
    "Appendix - Carcinoid": "Appendix",
    "Appendix - Carcinoma": "Appendix",
    "Appendix Carcinoma": "Appendix",
    "Aryepiglottic fold": "Aryepiglottic fold",
    "Ascending colon": "Ascending colon",
    "Aurora Term": "Vocab term",
    "Axillary & upper limb lymph nodes": "Axillary & upper limb lymph nodes",
    "Axillary tail of breast": "Axillary tail of breast",
    "Base of tongue": "Base of tongue",
    "Biliary tract": "Biliary tract",
    "Bladder (all C67 sites)": "Bladder (all C67 sites)",
    "Bladder neck": "Bladder neck",
    "Bladder, NOS": "Bladder, NOS",
    "Blood": "Blood",
    "Body of pancreas": "Body of pancreas",
    "Body of penis": "Body of penis",
    "Body of stomach": "Body of stomach",
    "Bone": "Bone & articular cartilage",
    "Bone - Appendicular Skeleton, Trunk, Skull, and Facial Bones": "Bone & articular cartilage",
    "Bone & articular cartilage": "Bone & articular cartilage",
    "Bone & articular cartilage of limb": "Bone & articular cartilage of limb",
    "Bone and articular cartilage (C40-C41)": "Bone and articular cartilage (C40-C41)",
    "Bone and articular cartilage of limbs (all C40 sites)": "Bone and articular cartilage of limbs (all C40 sites)",
    "Bone and articular cartilage of other and unspecified sites (all C41 sites)": "Bone and articular cartilage of other and unspecified sites (all C41 sites)",
    "Bone marrow": "Bone marrow",
    "Bones of skull & face": "Bones of skull & face",
    "Border of tongue": "Border of tongue",
    "Brain (all C71 sites)": "Brain (all C71 sites)",
    "Brain stem": "Brain stem",
    "Brain, NOS": "Brain, NOS",
    "Branchial cleft": "Branchial cleft",
    "Breast": "Breast, NOS",
    "Breast (all C50 sites)": "Breast (all C50 sites)",
    "Breast, NOS": "Breast, NOS",
    "Broad ligament": "Broad ligament",
    "Bronchus and lung (all C34 sites)": "Bronchus and lung (all C34 sites)",
    "Bronchus or lung, NOS": "Bronchus or lung, NOS",
    "Carcinoma of the Lacrimal Gland": "Lachrymal gland & duct",
    "Cardia": "Cardia",
    "Carotid body": "Carotid body",
    "Cauda equina": "Cauda equina",
    "Cecum": "Cecum",
    "Central nervous system": "Central nervous system",
    "Central portion of breast": "Central portion of breast",
    "Cerebellum": "Cerebellum",
    "Cerebral meninges": "Cerebral meninges",
    "Cerebral ventricle": "Cerebral ventricle",
    "Cerebrum": "Cerebrum",
    "Cervical part of esophagus": "Cervical part of esophagus",
    "Cervix Uteri": "Cervix uteri, NOS",
    "Cervix uteri (all C53 sites)": "Cervix uteri (all C53 sites)",
    "Cervix uteri, NOS": "Cervix uteri, NOS",
    "Cheek mucosa": "Cheek mucosa",
    "Choroid": "Choroid",
    "Chronic Lymphocytic Leukemia": "Chronic Lymphocytic Leukemia",
    "Chronic Myeloid Leukemia": "Chronic Myeloid Leukemia",
    "Ciliary body": "Ciliary body",
    "Clitoris": "Clitoris",
    "Cloacogenic zone": "Cloacogenic zone",
    "Colon (all C18 sites)": "Colon (all C18 sites)",
    "Colon and Rectum": "Colon and Rectum",
    "Colon, NOS": "Colon, NOS",
    "Commissure of lip": "Commissure of lip",
    "Conjunctiva": "Conjunctiva",
    "Connective & soft tissue": "Connective & soft tissue",
    "Connective & soft tissue of abdomen": "Connective & soft tissue of abdomen",
    "Connective & soft tissue of head": "Connective & soft tissue of head",
    "Connective & soft tissue of lower limb and hip": "Connective & soft tissue of lower limb and hip",
    "Connective & soft tissue of pelvis": "Connective & soft tissue of pelvis",
    "Connective & soft tissue of thorax": "Connective & soft tissue of thorax",
    "Connective & soft tissue of trunk": "Connective & soft tissue of trunk",
    "Connective & soft tissue of upper limb and shoulder": "Connective & soft tissue of upper limb and shoulder",
    "Cornea": "Cornea",
    "Corpus Uteri - Adenosarcoma": "Corpus uteri, NOS",
    "Corpus Uteri - Carcinoma": "Corpus uteri, NOS",
    "Corpus Uteri - Leiomyosarcoma/Endometrial Stromal Sarcoma": "Corpus uteri, NOS",
    "Corpus uteri (all C54 sites)": "Corpus uteri (all C54 sites)",
    "Corpus uteri, NOS": "Corpus uteri, NOS",
    "Cortex of adrenal gland": "Cortex of adrenal gland",
    "Cranial nerves": "Cranial nerves",
    "Craniopharyngeal duct": "Craniopharyngeal duct",
    "Cutaneous Squamous Cell Carcinoma": "Skin, NOS",
    "Descended testis": "Descended testis",
    "Descending colon": "Descending colon",
    "Digestive organs (C15-C26)": "Digestive organs (C15-C26)",
    "Distal Bile Ducts": "Extrahepatic bile duct",
    "Dome of bladder": "Dome of bladder",
    "Dorsal surface of tongue": "Dorsal surface of tongue",
    "Duodenum": "Duodenum",
    "Endocervix": "Endocervix",
    "Endocrine gland": "Endocrine gland",
    "Endocrine pancreas": "Endocrine pancreas",
    "Endometrium": "Endometrium",
    "Epididymis": "Epididymis",
    "Esophagus (all C15 sites)": "Esophagus (all C15 sites)",
    "Esophagus - Adenocarcinoma": "Esophagus, NOS",
    "Esophagus - Squamous Cell Carcinoma": "Esophagus, NOS",
    "Esophagus, NOS": "Esophagus, NOS",
    "Ethmoidal sinus": "Ethmoidal sinus",
    "Exocervix": "Exocervix",
    "External lip": "External lip",
    "External lower lip": "External lower lip",
    "External upper lip": "External upper lip",
    "Extrahepatic bile duct": "Extrahepatic bile duct",
    "Eye": "Eye",
    "Eye and adnexa (all C69 sites)": "Eye and adnexa (all C69 sites)",
    "Eye, brain and other parts of central nervous system (C69-C72)": "Eye, brain and other parts of central nervous system (C69-C72)",
    "Fallopian Tube": "Fallopian tube",
    "Fallopian tube": "Fallopian tube",
    "Female genital organ": "Female genital organ",
    "Female genital organs (C51-C58)": "Female genital organs (C51-C58)",
    "Floor of mouth (all C04 sites)": "Floor of mouth (all C04 sites)",
    "Floor of mouth, NOS": "Floor of mouth, NOS",
    "Frontal lobe": "Frontal lobe",
    "Frontal sinus": "Frontal sinus",
    "Fundus of stomach": "Fundus of stomach",
    "Fundus uteri": "Fundus uteri",
    "Gallbladder": "Gallbladder",
    "Gastric Stromal Tumor - Gastric Gist": "Stomach, NOS",
    "Gastric Stromal Tumor - Gastric GIST": "Stomach, NOS",
    "Gastric Stromal Tumor - Small Intestine Gist": "Small intestine, NOS",
    "Gastric antrum": "Gastric antrum",
    "Gastrointestinal tract": "Gastrointestinal tract",
    "Gestational Trophoblastic Tumors": "Gestational Trophoblastic Tumors",
    "Glans penis": "Glans penis",
    "Glottis": "Glottis",
    "Greater curvature of stomach": "Greater curvature of stomach",
    "Gum (all C03 sites)": "Gum (all C03 sites)",
    "Gum, NOS": "Gum, NOS",
    "Hard palate": "Hard palate",
    "Head": "Head",
    "Head of pancreas": "Head of pancreas",
    "Heart": "Heart",
    "Heart, mediastinum and pleura (all C38 sites)": "Heart, mediastinum and pleura (all C38 sites)",
    "Hematopoietic and reticuloendothelial systems (all C42 sites)": "Hematopoietic and reticuloendothelial systems (all C42 sites)",
    "Hematopoietic system": "Hematopoietic system",
    "Hepatic flexure of colon": "Hepatic flexure of colon",
    "Hodgkin and Non-Hodgkin Lymphoma": "Hodgkin and Non-Hodgkin Lymphoma",
    "Hypopharynx (all C13 sites)": "Hypopharynx (all C13 sites)",
    "Hypopharynx, NOS": "Hypopharynx, NOS",
    "Ileum": "Ileum",
    "Ill-defined sites within respiratory system": "Ill-defined sites within respiratory system",
    "Ill-defined, other secondary and unspecified sites (C76-C80)": "Ill-defined, other secondary and unspecified sites (C76-C80)",
    "Inguinal & lower limb lymph nodes": "Inguinal & lower limb lymph nodes",
    "Inner aspect of lip": "Inner aspect of lip",
    "Inner aspect of lower lip": "Inner aspect of lower lip",
    "Inner aspect of upper lip": "Inner aspect of upper lip",
    "Intestinal tract": "Intestinal tract",
    "Intra-abdominal lymph nodes": "Intra-abdominal lymph nodes",
    "Intrahepatic Bile Duct": "Intrahepatic bile duct",
    "Intrahepatic bile duct": "Intrahepatic bile duct",
    "Intrathoracic lymph nodes": "Intrathoracic lymph nodes",
    "Isthmus uteri": "Isthmus uteri",
    "Jejunum": "Jejunum",
    "Kidney": "Kidney",
    "Labium majus": "Labium majus",
    "Labium minus": "Labium minus",
    "Lachrymal gland & duct": "Lachrymal gland & duct",
    "Laryngeal cartilage": "Laryngeal cartilage",
    "Larynx (all C32 sites)": "Larynx (all C32 sites)",
    "Larynx - Glottis": "Glottis",
    "Larynx - Subglottis": "Subglottis",
    "Larynx - Supraglottis": "Supraglottis",
    "Larynx, NOS": "Larynx, NOS",
    "Lateral floor of mouth": "Lateral floor of mouth",
    "Lateral wall of bladder": "Lateral wall of bladder",
    "Lateral wall of nasopharynx": "Lateral wall of nasopharynx",
    "Lateral wall of oropharynx": "Lateral wall of oropharynx",
    "Lesser curvature of stomach": "Lesser curvature of stomach",
    "Lingual tonsil": "Lingual tonsil",
    "Lip (all C00 sites)": "Lip (all C00 sites)",
    "Lip and Oral Cavity": "Lip and Oral Cavity",
    "Lip, NOS": "Lip, NOS",
    "Lip, oral cavity and pharynx (C00-C14)": "Lip, oral cavity and pharynx (C00-C14)",
    "Liver": "Liver",
    "Liver (Excluding Intrahepatic Bile Ducts)": "Liver",
    "Liver and intrahepatic bile ducts (all C22 sites)": "Liver and intrahepatic bile ducts (all C22 sites)",
    "Long bones of lower limb and associative joints": "Long bones of lower limb and associative joints",
    "Long bones of upper limb": "Long bones of upper limb",
    "Lower gum": "Lower gum",
    "Lower limb": "Lower limb",
    "Lower lobe": "Lower lobe",
    "Lower third of esophagus": "Lower third of esophagus",
    "Lower-inner quadrant of breast": "Lower-inner quadrant of breast",
    "Lower-outer quadrant of breast": "Lower-outer quadrant of breast",
    "Lung": "Bronchus or lung, NOS",
    "Lymph nodes (all C77 sites)": "Lymph nodes (all C77 sites)",
    "Lymph nodes of head": "Lymph nodes of head",
    "Lymph nodes of multiple regions": "Lymph nodes of multiple regions",
    "Lymph nodes, NOS": "Lymph nodes, NOS",
    "Lymphoid Neoplasms": "Lymphoid Neoplasms",
    "Main bronchus": "Main bronchus",
    "Major Salivary Glands": "Major salivary gland",
    "Major salivary gland": "Major salivary gland",
    "Male genital organ": "Male genital organ",
    "Male genital organs (C60-C63)": "Male genital organs (C60-C63)",
    "Malignant Melanoma of the Conjunctiva": "Conjunctiva",
    "Melanoma of the Conjunctiva": "Conjunctiva",
    "Mandible": "Mandible",
    "Maxillary sinus": "Maxillary sinus",
    "Meckel diverticulum": "Meckel diverticulum",
    "Mediastinum": "Mediastinum",
    "Medulla of adrenal gland": "Medulla of adrenal gland",
    "Melanoma of the Skin": "Skin, NOS",
    "Meninges (all C70 sites)": "Meninges (all C70 sites)",
    "Meninges, NOS": "Meninges, NOS",
    "Merkel Cell Carcinoma": "Skin, NOS",
    "Mesothelial and soft tissue (C45-C49)": "Mesothelial and soft tissue (C45-C49)",
    "Middle ear": "Middle ear",
    "Middle lobe": "Middle lobe",
    "Middle third of esophagus": "Middle third of esophagus",
    "Mouth": "Mouth",
    "Mucosal Melanoma of the Head and Neck": "Head",
    "Multiple Myeloma": "Multiple Myeloma",
    "Mycosis Fungoides": "Mycosis Fungoides",
    "Myometrium": "Myometrium",
    "NULL": "Not Provided",
    "Nasal Cavity and Ethmoid Sinus": "Nasal Cavity and Ethmoid Sinus",
    "Nasal Cavity and Paranasal Sinus - Maxillary Sinus": "Maxillary sinus",
    "Nasal cavity": "Nasal cavity",
    "Nasal cavity and middle ear (all C30 sites)": "Nasal cavity and middle ear (all C30 sites)",
    "Nasopharynx (all C11 sites)": "Nasopharynx (all C11 sites)",
    "Nasopharynx, NOS": "Nasopharynx, NOS",
    "Neuroendocrine Tumor - Colon/Rectum": "Neuroendocrine Tumor - Colon/Rectum",
    "Neuroendocrine Tumor - Duodenum/Ampulla/Jejunum/Illeum": "Small intestine, NOS",
    "Neuroendocrine Tumor - Stomach": "Stomach, NOS",
    "Nipple & areola": "Nipple & areola",
    "Not Provided": "Not Provided",
    "Occipital lobe": "Occipital lobe",
    "Ocular Adnexal Lymphoma": "Overlapping lesion of eye & adnexa",
    "Olfactory nerve": "Olfactory nerve",
    "Optic nerve": "Optic nerve",
    "Orbit": "Orbit",
    "Oropharynx (all C10 sites)": "Oropharynx (all C10 sites)",
    "Oropharynx, NOS": "Oropharynx, NOS",
    "Other and ill-defined digestive organs (all C26 sites)": "Other and ill-defined digestive organs (all C26 sites)",
    "Other and ill-defined sites (all C76 sites)": "Other and ill-defined sites (all C76 sites)",
    "Other and ill-defined sites in the lip, oral cavity and pharynx (all C14 sites)": "Other and ill-defined sites in the lip, oral cavity and pharynx (all C14 sites)",
    "Other and ill-defined sites in the respiratory system and intrathoracic organs (all C39 sites)": "Other and ill-defined sites in the respiratory system and intrathoracic organs (all C39 sites)",
    "Other and unspecified female genital organs (all C57 sites)": "Other and unspecified female genital organs (all C57 sites)",
    "Other and unspecified major salivary glands (all C08 sites)": "Other and unspecified major salivary glands (all C08 sites)",
    "Other and unspecified male genital organs (all C63 sites)": "Other and unspecified male genital organs (all C63 sites)",
    "Other and unspecified parts of biliary tract (all C24 sites)": "Other and unspecified parts of biliary tract (all C24 sites)",
    "Other and unspecified parts of mouth (all C06 sites)": "Other and unspecified parts of mouth (all C06 sites)",
    "Other and unspecified parts of tongue (all C02 sites)": "Other and unspecified parts of tongue (all C02 sites)",
    "Other and unspecified urinary organs (all C68 sites)": "Other and unspecified urinary organs (all C68 sites)",
    "Other connective and soft tissue (all C49 sites)": "Other connective and soft tissue (all C49 sites)",
    "Other endocrine glands and related structures (all C75 sites)": "Other endocrine glands and related structures (all C75 sites)",
    "Other ill-defined sites": "Other ill-defined sites",
    "Other parts of pancreas": "Other parts of pancreas",
    "Other specified female genital organs": "Other specified female genital organs",
    "Other specified male genital organs": "Other specified male genital organs",
    "Ovary": "Ovary",
    "Overlapping lesion of accessory sinuses": "Overlapping lesion of accessory sinuses",
    "Overlapping lesion of biliary tract": "Overlapping lesion of biliary tract",
    "Overlapping lesion of bladder": "Overlapping lesion of bladder",
    "Overlapping lesion of bone & articular cartilage": "Overlapping lesion of bone & articular cartilage",
    "Overlapping lesion of bone & articular cartilage of limbs": "Overlapping lesion of bone & articular cartilage of limbs",
    "Overlapping lesion of brain": "Overlapping lesion of brain",
    "Overlapping lesion of brain & central nervous system": "Overlapping lesion of brain & central nervous system",
    "Overlapping lesion of breast": "Overlapping lesion of breast",
    "Overlapping lesion of bronchus & lung": "Overlapping lesion of bronchus & lung",
    "Overlapping lesion of cervix uteri": "Overlapping lesion of cervix uteri",
    "Overlapping lesion of colon": "Overlapping lesion of colon",
    "Overlapping lesion of connective & soft tissue": "Overlapping lesion of connective & soft tissue",
    "Overlapping lesion of corpus uteri": "Overlapping lesion of corpus uteri",
    "Overlapping lesion of digestive system": "Overlapping lesion of digestive system",
    "Overlapping lesion of endocrine gland": "Overlapping lesion of endocrine gland",
    "Overlapping lesion of esophagus": "Overlapping lesion of esophagus",
    "Overlapping lesion of eye & adnexa": "Overlapping lesion of eye & adnexa",
    "Overlapping lesion of female genital organs": "Overlapping lesion of female genital organs",
    "Overlapping lesion of floor of mouth": "Overlapping lesion of floor of mouth",
    "Overlapping lesion of heart": "Overlapping lesion of heart",
    "Overlapping lesion of hypopharynx": "Overlapping lesion of hypopharynx",
    "Overlapping lesion of ill-defined sites": "Overlapping lesion of ill-defined sites",
    "Overlapping lesion of larynx": "Overlapping lesion of larynx",
    "Overlapping lesion of lip": "Overlapping lesion of lip",
    "Overlapping lesion of lip, oral cavity and pharynx": "Overlapping lesion of lip, oral cavity and pharynx",
    "Overlapping lesion of major salivary glands": "Overlapping lesion of major salivary glands",
    "Overlapping lesion of male genital organs": "Overlapping lesion of male genital organs",
    "Overlapping lesion of nasopharynx": "Overlapping lesion of nasopharynx",
    "Overlapping lesion of oropharynx": "Overlapping lesion of oropharynx",
    "Overlapping lesion of other & unspecified parts of mouth": "Overlapping lesion of other & unspecified parts of mouth",
    "Overlapping lesion of palate": "Overlapping lesion of palate",
    "Overlapping lesion of pancreas": "Overlapping lesion of pancreas",
    "Overlapping lesion of penis": "Overlapping lesion of penis",
    "Overlapping lesion of peripheral nerves & autonomic nervous system": "Overlapping lesion of peripheral nerves & autonomic nervous system",
    "Overlapping lesion of rectum": "Overlapping lesion of rectum",
    "Overlapping lesion of respiratory & intrathoracic organs": "Overlapping lesion of respiratory & intrathoracic organs",
    "Overlapping lesion of retroperitoneum & peritoneum": "Overlapping lesion of retroperitoneum & peritoneum",
    "Overlapping lesion of skin": "Overlapping lesion of skin",
    "Overlapping lesion of small intestine": "Overlapping lesion of small intestine",
    "Overlapping lesion of stomach": "Overlapping lesion of stomach",
    "Overlapping lesion of tongue": "Overlapping lesion of tongue",
    "Overlapping lesion of tonsil": "Overlapping lesion of tonsil",
    "Overlapping lesion of urinary organs": "Overlapping lesion of urinary organs",
    "Overlapping lesion of vulva": "Overlapping lesion of vulva",
    "Palate (all C05 sites)": "Palate (all C05 sites)",
    "Palate, NOS": "Palate, NOS",
    "Pancreas": "Pancreas, NOS",
    "Pancreas (all C25 sites)": "Pancreas (all C25 sites)",
    "Pancreas, NOS": "Pancreas, NOS",
    "Pancreatic duct": "Pancreatic duct",
    "Parametrium": "Parametrium",
    "Parathyroid gland": "Parathyroid gland",
    "Paraurethral glands": "Paraurethral glands",
    "Parietal lobe": "Parietal lobe",
    "Parotid gland": "Parotid gland",
    "Pelvic bones": "Pelvic bones",
    "Pelvic lymph nodes": "Pelvic lymph nodes",
    "Pelvis": "Pelvis",
    "Penis": "Penis, NOS",
    "Penis (all C60 sites)": "Penis (all C60 sites)",
    "Penis, NOS": "Penis, NOS",
    "Perihilar Bile Ducts": "Extrahepatic bile duct",
    "Peripheral nerves & autonomic nervous system": "Peripheral nerves & autonomic nervous system",
    "Peripheral nerves and autonomic nervous system (all C47 sites)": "Peripheral nerves and autonomic nervous system (all C47 sites)",
    "Peripheral nerves of abdomen": "Peripheral nerves of abdomen",
    "Peripheral nerves of head": "Peripheral nerves of head",
    "Peripheral nerves of lower limb and hip": "Peripheral nerves of lower limb and hip",
    "Peripheral nerves of pelvis": "Peripheral nerves of pelvis",
    "Peripheral nerves of thorax": "Peripheral nerves of thorax",
    "Peripheral nerves of trunk": "Peripheral nerves of trunk",
    "Peripheral nerves of upper limb and shoulder": "Peripheral nerves of upper limb and shoulder",
    "Peritoneum": "Peritoneum",
    "Pharynx": "Pharynx",
    "Pharynx - Hypopharynx": "Hypopharynx, NOS",
    "Pharynx - Nasopharynx": "Nasopharynx, NOS",
    "Pharynx - Oropharynx": "Oropharynx, NOS",
    "Pineal gland": "Pineal gland",
    "Pituitary gland": "Pituitary gland",
    "Placenta": "Placenta",
    "Plasma Cell Myeloma and Disorders": "Plasma Cell Myeloma and Disorders",
    "Pleura": "Pleura",
    "Pleural Mesothelioma": "Pleura",
    "Postcricoid region": "Postcricoid region",
    "Posterior mediastinum": "Posterior mediastinum",
    "Posterior wall of bladder": "Posterior wall of bladder",
    "Posterior wall of hypopharynx": "Posterior wall of hypopharynx",
    "Posterior wall of nasopharynx": "Posterior wall of nasopharynx",
    "Posterior wall of oropharynx": "Posterior wall of oropharynx",
    "Prepuce": "Prepuce",
    "Primary Cutaneous Lymphoma": "Primary Cutaneous Lymphoma",
    "Prostate": "Prostate",
    "Pylorus": "Pylorus",
    "Pyriform sinus": "Pyriform sinus",
    "Rectosigmoid junction": "Rectosigmoid junction",
    "Rectum": "Rectum",
    "Renal Pelvis and Ureter": "Renal Pelvis and Ureter",
    "Renal pelvis": "Renal pelvis",
    "Respiratory and intrathoracic organs (C30-C39)": "Respiratory and intrathoracic organs (C30-C39)",
    "Reticuloendothelial system": "Reticuloendothelial system",
    "Retina": "Retina",
    "Retinoblastoma": "Retina",
    "Retromolar area": "Retromolar area",
    "Retroperitoneum": "Retroperitoneum",
    "Retroperitoneum and peritoneum (all C48 sites)": "Retroperitoneum and peritoneum (all C48 sites)",
    "Ribs": "Ribs",
    "Round ligament": "Round ligament",
    "Scrotum": "Scrotum",
    "Short bones of lower limb and associative joints": "Short bones of lower limb and associative joints",
    "Short bones of upper limb and associative joints": "Short bones of upper limb and associative joints",
    "Sigmoid colon": "Sigmoid colon",
    "Skin (all C44 sites)": "Skin (all C44 sites)",
    "Skin of ear & external auricular canal": "Skin of ear & external auricular canal",
    "Skin of eyelid": "Skin of eyelid",
    "Skin of lip": "Skin of lip",
    "Skin of lower limb and hip": "Skin of lower limb and hip",
    "Skin of other & unspecified parts of face": "Skin of other & unspecified parts of face",
    "Skin of scalp & neck": "Skin of scalp & neck",
    "Skin of trunk": "Skin of trunk",
    "Skin of upper limb and shoulder": "Skin of upper limb and shoulder",
    "Skin, NOS": "Skin, NOS",
    "Small Intestine": "Small intestine, NOS",
    "Small intestine (all C17 sites)": "Small intestine (all C17 sites)",
    "Small intestine, NOS": "Small intestine, NOS",
    "Small Intestine - Adenocarcinoma": "Small intestine, NOS",
    "Soft Tissue Sarcoma": "Connective & soft tissue",
    "Soft palate": "Soft palate",
    "Specified parts of peritoneum": "Specified parts of peritoneum",
    "Spermatic cord": "Spermatic cord",
    "Sphenoidal sinus": "Sphenoidal sinus",
    "Spinal cord": "Spinal cord",
    "Spinal cord, cranial nerves and other parts of central nervous system (all C72 sites)": "Spinal cord, cranial nerves and other parts of central nervous system (all C72 sites)",
    "Spinal meninges": "Spinal meninges",
    "Spleen": "Spleen",
    "Splenic flexure of colon": "Splenic flexure of colon",
    "Stomach": "Stomach, NOS",
    "Stomach (all C16 sites)": "Stomach (all C16 sites)",
    "Stomach, NOS": "Stomach, NOS",
    "Subglottis": "Subglottis",
    "Sublingual gland": "Sublingual gland",
    "Submandibular gland": "Submandibular gland",
    "Superior wall of nasopharynx": "Superior wall of nasopharynx",
    "Supraglottis": "Supraglottis",
    "Tail of pancreas": "Tail of pancreas",
    "Temporal lobe": "Temporal lobe",
    "Testis": "Testis, NOS",
    "Testis (all C62 sites)": "Testis (all C62 sites)",
    "Testis, NOS": "Testis, NOS",
    "Thoracic part of esophagus": "Thoracic part of esophagus",
    "Thorax": "Thorax",
    "Thymus": "Thymus",
    "Thyroid - Anaplastic Carcinoma": "Thyroid gland",
    "Thyroid - Differentiated and Anaplastic": "Thyroid gland",
    "Thyroid - Medullary Carcinoma": "Thyroid gland",
    "Thyroid - Papillary or Follicular": "Thyroid gland",
    "Thyroid - Papillary or Follicular (45 years and older)": "Thyroid gland",
    "Thyroid - Papillary or Follicular (Under 45 years)": "Thyroid gland",
    "Thyroid and other endocrine glands (C73-C75)": "Thyroid and other endocrine glands (C73-C75)",
    "Thyroid gland": "Thyroid gland",
    "Tongue": "Tongue",
    "Tonsil (all C09 sites)": "Tonsil (all C09 sites)",
    "Tonsil, NOS": "Tonsil, NOS",
    "Tonsillar fossa": "Tonsillar fossa",
    "Tonsillar pillar": "Tonsillar pillar",
    "Trachea": "Trachea",
    "Transverse colon": "Transverse colon",
    "Trigone of bladder": "Trigone of bladder",
    "Undescended testis": "Undescended testis",
    "Unknown primary site": "Unknown primary site",
    "Upper gum": "Upper gum",
    "Upper limb": "Upper limb",
    "Upper lobe": "Upper lobe",
    "Upper respiratory tract": "Upper respiratory tract",
    "Upper third of esophagus": "Upper third of esophagus",
    "Upper-inner quadrant of breast": "Upper-inner quadrant of breast",
    "Upper-outer quadrant of breast": "Upper-outer quadrant of breast",
    "Urachus": "Urachus",
    "Ureter": "Ureter",
    "Ureteric orifice": "Ureteric orifice",
    "Urethra": "Urethra",
    "Urethra - male and female": "Urethra",
    "Urinary Bladder": "Bladder, NOS",
    "Urinary system": "Urinary system",
    "Urinary tract (C64-C68)": "Urinary tract (C64-C68)",
    "Uterine adnexa": "Uterine adnexa",
    "Uterus": "Uterus",
    "Uvea - Ciliary Body and Choroid": "Uvea - Ciliary Body and Choroid",
    "Uvea - Iris": "Eye",
    "Uvula": "Uvula",
    "Vagina": "Vagina",
    "Vallecula": "Vallecula",
    "Ventral surface of tongue": "Ventral surface of tongue",
    "Vertebral column": "Vertebral column",
    "Vestibule of mouth": "Vestibule of mouth",
    "Vulva": "Vulva, NOS",
    "Vulva (all C51 sites)": "Vulva (all C51 sites)",
    "Vulva, NOS": "Vulva, NOS",
    "Waldeyer's ring": "Waldeyer's ring"
}
