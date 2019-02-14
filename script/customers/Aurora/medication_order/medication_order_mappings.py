FREQUENCY = ('', 'EVERY 15 MIN', '3 TIMES DAILY WITH MEALS', 'EVERY 4 HOURS WHILE AWAKE', 'PRIOR TO DISCHARGE', 'ONCE (CONTINUOUS OVER 168 HOURS)', '4 TIMES DAILY BEFORE MEALS & NIGHTLY', 'EVERY 6 HOURS PRN', 'EVERY 12 HOURS SCHEDULED', 'ONCE (CONTINUOUS OVER 46 HOURS)', '2 TIMES DAILY AFTER MEALS', '3 TIMES PER WEEK', 'EVERY 4 HOURS PRN', 'EVERY 72 HOURS', '2 TIMES DAILY TRANSPLANT', 'EVERY 30 MIN PRN', 'EVERY 2 HOURS PRN', 'ONCE (CONTINUOUS OVER 192 HOURS)', 'PRN', '4 TIMES DAILY RESPIRATORY', '2 TIMES PER WEEK', '6 TIMES PER WEEK', 'EVERY 24 HOURS PRN', 'EVERY 2 MONTHS', 'EVERY 36 HOURS PRN', 'ONCE (CONTINUOUS OVER 24 HOURS)', 'ONCE (CONTINUOUS OVER 120 HOURS)', 'Continuous PN', 'EVERY 4 HOURS WHILE AWAKE RESP',
             '2 TIMES DAILY MON,WED,FRI', 'DAILY BEFORE LUNCH', 'EVERY 2 HOURS', 'EVERY HOUR WHILE AWAKE', 'EVERY 8 HOURS', 'Titrated', 'EVERY 90 MIN PRN', 'EVERY 3 HOURS', '3 TIMES DAILY BEFORE MEALS', 'EVERY 72 HOURS PRN', 'EVERY 7 WEEKS', 'EVERY 6 HOURS RESPIRATORY PRN', 'NIGHTLY', 'EVERY 36 HOURS', 'EVERY 5 MIN', 'EVERY 12 HOURS CVVH', '4 TIMES PER WEEK', 'EVERY 3 HOURS PRN', '2 TIMES/DAY BETWEEN MEALS (AM/PM)', 'WITH SNACKS', '3 TIMES DAILY RESPIRATORY', 'EVERY MORNING', 'EVERY 6 HOURS WHILE AWAKE', 'EVERY 2 HOURS WHILE AWAKE', 'ON CALL PRN', 'IMG ONCE PRN', 'DAILY RESPIRATORY PRN', 'EVERY 12 WEEKS', 'EVERY 3 DAYS PRN', 'EVERY 48 HOURS PRN', 'EVERY 10 MIN', 'EVERY 20 MIN PRN', 'DAILY BEFORE BREAKFAST', 'CONTINUOUS PRN')

DISCRETE_DOSE = ('', '185.75', '896.4', '161.8', '161.2', '161.4', '100-300', '161.6', '153.2', '153.6', '153.4', '153.8', '45.8', '45.2', '45.5', '421.8', '72.25', '421.2', '421.5', '421.6', '270', '271', '272', '273', '274', '275', '276', '327.6', '278', '279', '2146', '757.2', '12-40', '251.25', '5-160', '434.15', '565.9', '565.8', '694.5', '694.2', '694.1', '565.2', '565.5', '565.4', '694.8', '624.6', '332.1562', '839.4', '2688', '2685', '2686', '2680', '2681', '9 ', '99', '98', '91', '90', '93', '92', '95', '94', '97', '96', '431.6', '1293.3', '10.888', '845.4', '51.4', '519', '579.6', '579.5', '77.4', '77.5', '77.6', '77.1', '77.2', '1177', '1175', '100-150', '1170', '1179', '1178', '600-1000', '98.69', '2-14', '2-15', '2-16', '2-10', '2-11', '2-12', '2-13', '1225', '685.5', '1-15', '171.6', '1-16', '1-11', '1-10', '1-12', '24000000', '762.6', '2740', '624', '171.3', '18-103', '126.6', '126.4', '126.2', '126.8', '2000000', '114.9', '114.8', '114.4', '114.6', '114.2', '393', '392', '391', '390', '397', '396', '395', '394', '399', '398', '10-50', '4728', '4725', '2300', '4720', '2307', '403.65', '143.3333', '3744', '3740', '466.65', '4622', '9-18', '9-15', '9-17', '9-11', '9-12', '125-400', '35-48', '179', '178', '35-40', '176', '175', '174', '173', '172', '171', '170', '0-16', '0-17', '0-14', '0-15', '0-12', '0-13', '0-10', '0-11', '781.8', '20-100',
                 '441.6', '0-18', '0-19', '703.8', '461.4', '461.5', '461.2', '429.5', '128.8', '429.6', '277', '128.4', '128.5', '128.6', '406.8', '406.5', '406.4', '406.2', '2.79', '422.5', '422.4', '90.56', '2.75', '.3-.5', '.3-.4', '.3-.6', '.3-.9', '.3-.8', '100.8', '100.2', '100.6', '100.7', '474.6', '474.5', '12-47', '1769', '1760', '1761', '664.5', '664.2', '664.8', '692', '693', '690', '691', '696', '697', '1540', '1541', '698', '699', '231.75', '28-45', '7-19', '7-18', '7-17', '7-16', '7-15', '7-14', '7-12', '7-11', '7-10', '262-524', '659.5', '659.4', '196.6', '196.4', '196.2', '50.4', '196.8', '651.2', '651.6', '651.5', '651.9', '9525', '592.5', '592.2', '40.2', '40.1', '40.5', '.511', '62.6', '62.4', '62.5', '62.1', '109', '11.11', '258', '259', '354.75', '34-51', '252', '253', '250', '251', '256', '35-55', '254', '255', '3.86', '26.25', '5-100', '35-50', '200-300', '808.8', '741.5', '9500', '741.6', '808.2', '741.2', '828.6', '339.5', '339.6', '339.2', '339.3', '339.9', '755.7', '755.4', '5056', '812.4', '217.8', '217.5', '217.4', '217.7', '217.6', '217.2', '474.24', '392.27', '113.25', '150-400', '207.6', '207.4', '207.2', '344.5', '344.8', '0-250', '207.8', '10180', '20-28', '364.8', '364.2', '20-22', '20-23', '20-24', '20-25', '364.4', '364.5', '1158', '515.4', '515.5', '515.6', '1150', '390.8', '390.5', '390.4', '390.3', '446.8', '2-30', '501.3')

DOSE_UNIT = ('', 'micro curie', 'mEq/hr', 'Tube', 'Dose', 'mEq/kg/hr', 'lozenge', 'mmol/kg', 'tablet', 'cup', 'Units/kg/hr', 'mL/hr', 'mcg/hr', 'mEq', 'pg', 'tsp', 'Bar', 'L', 'mg/hr', 'capsule', 'Units/min', 'mcg/kg/hr', 'mL/kg/hr', 'g/m2', 'mL/kg', 'mcg/kg', 'Units/kg', 'drop', 'patch', 'mg/kg', 'each', 'Million Units/m2', 'mg/1.7m2', 'g/kg/day', 'g/kg', 'packet', 'mg/min', 'mg/kg of ampicillin', 'Units', 'g/1.7m2/day', 'mcg/min', 'g/day', 'mg/kg of piperacillin', 'mL/kg/min', 'mcg/kg/min', 'mg PE', 'pump', 'Part', 'Units/m2', 'mg/m2', 'Inhaler', 'mEq/kg', 'Wafer', 'Units/mL', 'mg/day', 'spray', 'mEq/day', 'enema', 'mmol', 'g',
             'mg PE/kg/day', 'oz', 'Syringe', 'puff', 'kcal', 'cm', 'mg/kg/hr', 'strip', 'Squirt', 'DOSE_UNIT', 'mg PE/kg', 'mg of ampicillin', 'Stick', 'Device', 'Units/hr', 'Units/day', 'g/hr', 'mcg', 'mL', "Int'l Units/min", 'Bottle', "Int'l Units/day", 'mg', 'vial', 'mg PE/kg/hr', 'suppository', 'Million Cells', "Int'l Units", 'Container', 'mg/kg/day', 'mL/m2/hr', 'Million Units', 'g/oz', 'mL/day', 'mcg/day', 'mcg/m2', 'Cartridge', 'milli-units/min', 'ng', 'application', 'ampule', 'inch', 'Applicatorful', 'Intra Uterine Device', 'Package', 'kit', 'mg/m2/day', 'Act', 'ng/kg/min', 'inhalation', 'm', 'part.', 'Gallon', 'applicator', 'Film', 'Can')

QUANTITY = ('3months ', '29 capsule', '15 gm', '4230', '473.12 mL', '1.75 mL', '3.27 mL', '64 Syringe', '546 g', '1 weeek', '3 Kit', '2 mth supply', '90 Device', '310', '1-2 pair', '315', '7 Device', '50grams', '41 g', '1lb jar ', '7 Troche', '3601 Tab', '12 Package', '1 dose pack', '36 Each', '1 WEEK SUPPLY', ' 1 vial w syringes', 'as directed', '10 0z', '32 Cap', '57 tablet', '1980 capsule', '40 drop', '90EVERY 30 DAYS', '144 capsule', '4 fl oz', '8.6 tablet', '119 capsule', '100 Troche', '10 prn', '9030 capsule', '10 Syringe', '1.68', '1 1/2 mo', '12000 mg', '2week supply', '29 each', '3 pill packs', '6 weeks supply', '5bottles', '70 Tube', '5 Container', '887 mL', '132 g', 'monthly', '3 momths', 'monthly supply', '476 mL', '78 capsule', '90 day supply, 10ml bottles', '30  GM', '70 ML', '4 x 1/2 oz', '2cans', '37 ampule', '3 months supply)', '135 mL', '3 months supply ', '30 doses.', '2600 mL', '94 tablet', '8.8 g', '30 patch', '2.1 cc', '30-60 gm', 'largest size', '210 capsule', '1 inhalation', 'alrge', '59 mL', '68 lozenge', 'one inj ', '2 pump', '44 mL', '34 patch', '1 month su pply', '120 gram tube', '1 mo3 months', '1054 each', '18 gram', '30 DAYS', '40 Package', '276 capsule', '5.0 ml', ' 180', '1 gallon', '319 tablet', '180 (3 months supply', '42.5 g', '4155 capsule', '30 Dose', '5 ml ', '290 mL', '36 Inhaler', '2.625 g', '16 capsule', '15ml.', '2g x 2', '5 ml.', '2.4ml', '236 capsule', '165 Can', '10 Vial', '3.5 gms', '30 TABS EVERY 30 DAYS', '300 ML ', '810 capsule', 'per ortho', '500 g', 'One kit', '15.08 mL', '59 mg', '12 tablet', '1 plexion', '60 strip', '76 tablet', '108 Inhaler', '686 capsule', '14.7 g', '480 Syringe', 'two ounces', '3.5 gm ', '92 g', '7 Days Supply', '0.25 tablet', '45 suppository', 'OP', '42.5G', '20 caps', '3 SAMPLE BOTTLES', '3-- 5ml bottles', '378 gms', '40 Forty', '464 g', '1 1 UNIT', '8 application', '42.5g', '15g tube', '576 tablet', '558 capsule', '18cc', '275 g', '3 months ', '6 kits', '16 application', '180 (3mo supply)', 'samp.', '50 every 30 days', '960 g', '3 months3', '2 Container', '70gm', '30 vials', '308 tablet', '29 g', '7 g', '20 Patch', '90 tubes', '264 g', '1 month worth', '27 Tab', '7.3 mL', '257 tablet', '1000 mL', '1 month supplyq', 'LARGE BOX', '1 CANNISTER', 'one large tube, ', 'ONE MONTH SUPPLY', '1000 ml', '2030 tablet', '12 Device', '90 capsule', '110 tablet', '1000 mg', '1 month supplyl', 'one year supply, ', '4 BOXS', '524 g',
            '16 Dose', '56.6 g', '360 ', '21 Dose', '56 doses', '150 Cap', ' bottles (90 day supply)', '1 month supply1', '2268 g', '3 each', '30grams, ', '110 mL', '30b grams,', 'only needs 3 tabs', '66 each', '1893 mL', '1 month supply ', '150 Can', '50ML', '14 Cap', '90/3mo', '6.7 Inhaler', ' 180 ', '500 cc', '300 Bottle', '120 gm ', '120 CC', '2 PACK', '8 WEEKS', '66 tablet', '489 tablet', 'pack of 5 pens', '1 pen', '35 gm', '20 ML', '5.0ml bottle ', '3.5 GRAM.', '126 each', '1800 ML', '1180 capsule', '950 ml', '180  FOR  3  MOS', '140 Cap', '340.6 g', '90 Bottle', '82 capsule', '48 Inhaler', '21 each', '28.35', '950 mL', '3 MO', '14ml Sol', '2 ampule', '2 vial ', '25000 mL', '225 mL', '233 mL', '15 Tube', '280 each', '2 WEEK SUPPLY', '28 Packet', '29.6 mL', '640 mg', "330 CC'S", '1.5GM', '2 applications', 'small&nbsp;&nbsp;tube', '2 vials', '4  0z', '127 tablet', '9.5 tablet', '76.5 g', '543 tablet', '4 boxes', 'sample x 1', '460 strip', '6.6 Ml', '20 kit', '1  kit', '10-1 GM', '13.6 mL', '44.3 mL', '6 Ozs.', '2020 tablet', '30g tube', '16200 mL', '3 Suppository', '6.6 ML', '180 grams', '207 mL', '140 ', '221 capsule', '3 cartons', '256 tablet', '7.5gm', '60 gm + tube', '135 Tab', '2 Vial', 'o.p.', '300 Units', '3481 mL', '1/2 liter', '10 Units', '140g', '75 gm', '340gm', '1 monthsupply', '846 mL', '189 g', '850 mL', '3 tube (for 90 d)', '240cc', '1 Inhaler', '2000 mL', '336', '331', '330', '332', '4  penfills', '3 BOTTELS', '36.5 mL', '265 mL', '21 g', '20 grams ', '2000 mg', '2000 ml', '1 right', '28 inhalation', '1.4 mL', '322 tablet', '12690 mL', '35 ampule', '316 tablet', '1 Enema', '283 g', '900 ml', '900 mg', '10 doses ', '45 = 3 months', '5 btl', '1440 capsule', '248 Can', '90ml', '3800 mL', '900 mL', '63. ', '31 Cap', '9000 mL', '26 ampule', '30 gm+', '10 ml.', '30 gm.', '1350 g', '30 gm ', '10 ml ', '8 each', '28 puff', '30 gm?', '150 cc', '90 day supply 3 jars', '18 pens', '312 tablet', '1080 capsule', '631 tablet', '225 each', '90 day', '45.2 g', '1 Large tube', '272 capsule', '3 (90 day supply)', '200cc ', '1 po qd', 'Q', '10.2 g', '45 each', '30 gms', '1 small bottle', '212 tablet', '5 pkges', '30/ Q.S.', '9 Dose', '1 lg tube', '7.5 cc', '3162 g', '1 box cartridges', '14.4 mL', '1 pen with 1 cartridge', '392 tablet', '2 boxes of 5 cartridges', '55 Syringe', '#90/month', '90 Troche', '40 patch', 'small or size pts choice', '120 Dose', '4 units ', '0.3 tablet', '1 trade', '50 grams.', '23 mL')

REFILLS = ('', 'Due for follow up with Dr.Bell. Call office 251-7500 for appointment', '2/ PLS INF PT APPT NEEDED!', 'Pt needs appt for further refills', '2 pairs', 'PRN refills for 1 year', 'PT NEEDS APPT FOR FURTHER REFILLS', 'check lipids ', ' o', 'needs appt in December', '011', '012', 'gm', '00 - check lipids', 'see MD', '2 months', '0-appt needed', ' ', 'APPT NOW', '0 / NEEDS APPT', '0/ Needs appt', 'Due for follow up.', 'pen', '0', 'NEEDS APPT IN OCTOBER', '1 Due for  appt.', '1  mother has', '  ', 'No Refills!', 'recheck tsh', '0 Dr. Cindy', '0/&nbsp;&nbsp;APPOINTMENT NEEDED', ' 2', ' 3', ' 0', ' 1', ' 7', '6   ', '0 needs follow up.', 'Needs follow up with Dr.Pzuio-Bell', '2 Have bp checked in May 05', '`', 'prn X 1', '2 I', '1apply to', '133', 'No further refills. Patient has move out of Wisconsin and needs to establish with another provider.', 'p', '0/ PLEASE INFORM PT APPT IS NEEDED, THANKS', '-0', '48', 'prn x 1year', '6s+6', 'needs appt with MD', '3 FOR 1 YEAR', 'cmp', '1, appt needed with doctor', 'cap', 's+14', '3 (1 year )', 'NO!', '270', '19', 'zero', '0/ NEEDS APPOINTMENT', 'on eyear', '3A', 'n', 'Due for appointment', 's+30', 'Patient', '2 recheck lipids after 3 mo', '3s', '3r', '0 needs labs.', '4r', '3t', 'needs appt!', '0 PLS INF PT APPT NEEDED!', 'pt needs fasting lab tests', '3m', '3f', '11/3 per insurance allowance(1 yrs worth)', 'needs appt.', 'doses', 'qs for 1 year', '0 due for appt.', '0DUE FOR APPT.', 'Pt needs to be seen', '3/ PLEASE INFORM PT APPT NEEDED, THANKS!', '=', '102', 'PRN X 1 year', '100', '0 Needs appointment', '105', '3 (90 Day Supply/Mulitipack)', '3:', '900', '38', '3?', '360',
           'NONE', '33', '32', '31', '30', 'This should help11', '36', '35', '2  Pt needs to make appt with Dr', '2mon', '2  F/U with Dr.Puzio due 6/2008', '3.', 't+30', '3 ', '1  year', '10 months', 'NONE-APPOINTMENT EQUIRED', '2 total', '243', '1/  PT NEEDS APPT', 'no refills until lab work done.', '`3', '`0', '`1', '`5', '9t', 'pt needs lab tests', '0 - DUE TO BE SEEN', '0 follow up due', '1 only', '240', 'bone00', 'MUST be seen for more refills', 'need appt in October', '0 needs physical and labs.', 'call', 'needsan appt in October', '6', 'NO! needs lab work!', 'is', 'No refills until seen by Dr.', 'X1 YR', '0 zero', '`11', '`12', 'PT needs appt for further refills', '3 months', '1/2', '0480', 'mL', '0-needs appt', '99', '98', '1 Please make appointment', '91', '90', '93', 'due for follow up.', '1 yr.', '0p', 'dulera', 'none', 'PRN X 1 YEAR', '5 appt', 'f', 'mm', 'ml', '0 due for follow up', 'NO  NEEDS TO BE SEEN', 'NONE-APPOINTMENT REQUIRED', 'pr', '1 (titrating up on dose)', 'mp', 'X 1 year', '1pend', '.pspp', '1` yr', '6 BOTTLES', 'APPT DUE 3/17/09', '555', '1 needs follow up', 'level needs repeating', '1yr.', 'tab', 'needs appt in August for refills', '0 return for bp check', 'A 0', 'no more refills until seen in F/U', '!', 'needs', 'as needed for one year.', 'no refill until the pt sees the Dr.', 'prn 1 yr.', '6mon', 'ONE', '1', '6mos', '0 check tsh  9/7/07', 'oz', '6mo', '144', '0/ PLS INF PT APPT NEEDED', '999', 'APPT. REQUIRED', '0 Appointment needed before further refills are granted.', 'as needed', 'Needs appointment for additional refills', 'NO- needs an appt.  Please label!', 'wrist', '510', '0-F/U in Jan,08')

RX_MEDS = (('', 'ADALAT CC TBCR 90 MG PO'), ('8727', 'PROMETRIUM 100 MG PO CAPS'), ('18867', 'BENAZEPRIL-HYDROCHLOROTHIAZIDE 5-6.25 MG PO TABS'), ('253172', 'GRAPESEED EXTRACT CAPS 500-50 MG PO'), ('1304122', 'AFLURIA PRESERVATIVE FREE IM SUSP'), ('2551', 'CIPROFLOXACIN 200 MG/20ML IV SOLN'), ('4337', 'FENTANYL 75 MCG/HR TD PT72'), ('8163', 'PHENYLEPHRINE-GUAIFENESIN 30-400 MG PO CP12'), ('114979', 'ACIPHEX TBEC 20 MG OR'), ('235496', 'ENEMA DISPOSABLE RE ENEM'), ('19257', 'URECHOLINE TABS 10 MG PO'), ('6069', 'IVERMECTIN 3 MG PO TABS'), ('', 'RENAL SOFTGELS 1 MG PO CAPS'), ('6750', 'MENTHOL-ASCORBIC ACID 3-60 MG MT LOZG'), ('2623', 'CLOTRIMAZOLE 10 MG MT LOZG'), ('5487', 'ALDORIL-25 TABS 250-25 MG PO'), ('22892', 'MIGRAZONE 325-100-65 MG PO CAPS'), ('', 'ULTRA NATALCARE PO TABS'), ('32675', 'OXYBUTYNIN CHLORIDE TBCR 5 MG PO'), ('7145', 'MYCOPHENOLIC ACID 180 MG PO TBEC'), ('10572', 'NP THYROID 90 MG PO TABS'), ('321064', 'OLMESARTAN-AMLODIPINE-HCTZ 40-5-12.5 MG PO TABS'), ('10582', 'LEVOTHYROXINE SODIUM 112 MCG PO CAPS'), ('4099', 'PREMARIN TABS 0.3 MG OR'), ('103', 'PURINETHOL TABS 50 MG PO'), ('', 'BIOTENE PBF DRY MOUTH MT LIQD'), ('35636', 'RISPERDAL 0.5 MG PO TABS'), ('214582', 'GLATIRAMER ACETATE 40 MG/ML SC SOSY'), ('5032', 'RESPA-GF TBCR 600 MG OR'), ('1520', 'KERLONE 10 MG PO TABS'), ('3640', 'DOXYCYCLINE MONOHYDRATE 75 MG PO TABS'), ('7804', 'OXYCODONE ER 13.5 MG PO C12A'), ('161', 'ESGIC-PLUS 500-50-40 MG PO TABS'), ('37617', 'PIPERACILLIN SOD-TAZOBACTAM SO 2.25 (2-0.25) G IV SOLR'), ('6809', 'AVANDAMET 500-1 MG PO TABS'), ('704', 'AMITRIPTYLINE HCL TABS 10 MG PO'), ('2358', 'PERIDEX 0.12 % MT SOLN'), ('7814', 'OXYMORPHONE HCL 7.5 MG PO TB12'), ('2473', 'GLUCOSAMINE-CHONDROITIN DS 500-400 MG PO TABS'), ('5666', 'IMMUNE GLOBULIN (HUMAN) 10 GM IV SOLR'), ('84857', 'ARIMIDEX TABS 1 MG PO'), ('4077', 'ESTAZOLAM 1 MG PO TABS'), ('30125', 'MODAFINIL 200 MG PO TABS'), ('684879', 'FOLTX TABS 1-2.5-25 MG PO'), ('6932', 'MICONAZOLE 50 MG BU TABS'), ('41493', 'MELOXICAM 7.5 MG PO TABS'), ('', 'FENTANYL 2 MCG/ML-ROPIVACAINE 0.2% EPIDURAL PREMIX'), ('10975', 'GNP CO Q10 200 MG PO CAPS'), ('8896', 'TYLENOL COLD NO DROWSINESS 30-325-15 MG PO TABS'), ('161', 'ACETAMINOPHEN 500 MG PO CHEW'), ('1373037', 'TURMERIC 450 MG PO CAPS'), ('', 'SENTRY SENIOR PO TABS'), ('3288', 'DEXTROAMPHETAMINE SULFATE 10 MG PO TABS'), ('33199', 'PERMETHRIN 5 % EX CREA'), ('4845', 'GLUCOSAMINE 500 MG PO TABS'), ('2400', 'HISTUSSIN HC 5-2-2.5 MG/5ML PO SYRP'), ('1399', 'A/B OTIC 1.4-5.4 % OT SOLN'), ('8704', 'COMPAZINE 5 MG RE SUPP'), ('115698', 'ZIPRASIDONE HCL 60 MG PO CAPS'), ('6472', 'MEVACOR 10 MG PO TABS'), ('21254', 'PSEUDOPHED-CHLOPHEDIANOL-GG 60-25-400 MG PO TABS'), ('8345', 'PYRETHRINS-PIPERONYL BUTOXIDE 0.3-3 % EX SHAM'), ('8591', 'KLOR-CON TBCR 8 MEQ OR'), ('10759', 'TRIAMCINOLONE ACETONIDE (TOP) POWD'), ('', 'DAKINS 0.125% VAC INFUSION SOLUTION (BAG)'), ('4018', 'VITAMIN A & D 10000-400 IU PO CAPS'), ('73494', 'MICARDIS HCT 80-12.5 MG PO TABS'), ('5489', 'HYCODAN 1.5-5 MG PO TABS'), ('6582', 'MAGNESIUM OXIDE-PYRIDOXINE HCL 362-20 MG PO TABS'), ('7052', 'MORPHINE SULFATE 5 MG/ML IV SOLN'), ('8163', 'DURATUSS TBCR 600-120 MG OR'), ('6536', 'L-LYSINE 500 MG PO CAPS'), ('3361', 'BENTYL CAPS 10 MG OR'), ('282357', 'FULVESTRANT 250 MG/5ML IM SOLN'), ('5487', 'LOSARTAN POTASSIUM-HCTZ 50-12.5 MG PO TABS'), ('29365', 'CALCIPOTRIENE 0.005 % EX CREA'), ('8591', 'BSS IO SOLN'), ('36387', 'GNP SENNA PLUS 8.6-50 MG PO TABS'), ('231049', 'ELETRIPTAN HYDROBROMIDE 40 MG PO TABS'), ('135775', 'ZOMIG ZMT 5 MG PO TBDP'), ('11289', 'COUMADIN TABS 7.5 MG PO'), ('5487', 'TRIAMTERENE/HCTZ CAPS 37.5-25 MG PO'),
           ('', 'FOSAPREPITANT IVPB'), ('15202', 'ARGATROBAN 125 MG/125ML IV SOLN'), ('3498', 'PHENYLEPH-DIPHENHYD-DM-APAP 10-37.5-20-575 MG PO TABS'), ('798306', 'DIPHTHERIA-TETANUS TOXOIDS DT 25-5 LFU/0.5ML IM SUSP'), ('9863', 'KCL IN DEXTROSE-NACL 40-5-0.45 MEQ/L-%-% IV SOLN'), ('8896', 'MUCINEX D 120-1200 MG PO TB12'), ('28439', 'LAMOTRIGINE 150 MG PO TABS'), ('7299', 'NEOMYCIN SULFATE 500 MG PO TABS'), ('', 'HORSECHESTNUT EXTRACT POWD'), ('283742', 'ESOMEPRAZOLE SODIUM 40 MG IV SOLR'), ('161', 'BUTALBITAL-APAP 50-325 MG PO TABS'), ('7781', 'SERAX CAPS 15 MG OR'), ('', '2.5% HYDROCORTISONE IN EUCERIN'), ('', 'MULTIVITAMINS/IRON FC TABS   PO'), ('9143', 'ZANTAC TABS 300 MG OR'), ('8163', 'PHENERGAN VC 6.25-5 MG/5ML PO SYRP'), ('8597', 'LUGOLS 5 % PO SOLN'), ('40114', 'INTUNIV 1 MG PO TB24'), ('235496', 'FLEET PHOSPHO-SODA 18-48 GM/100ML PO SOLN'), ('161', 'PHRENILIN FORTE CAPS 650-50 MG OR'), ('8745', 'PROMETHAZINE HCL SUPP 25 MG RE'), ('403712', 'NONI (MORINDA CITRIFOLIA) 400 MG PO CAPS'), ('114202', 'LACTICARE 5 % EX LOTN'), ('4917', 'MINITRAN 0.2 MG/HR TD PT24'), ('', 'ALPRAZOLAM & DIET MANAGE PROD 0.5 MG PO MISC'), ('10759', 'NYSTATIN-TRIAMCINOLONE CREA 100000-0.1 U/GM-% EX'), ('', 'ESTER-C TABS 500-200-110 MG PO'), ('11248', 'FE FUM-VIT C-VIT B12-FA 460-60-0.01-1 MG PO CAPS'), ('38866', 'ASPERCREME/ALOE 10 % EX CREA'), ('3289', 'ROBITUSSIN DM SUGAR FREE 10-100 MG/5ML PO SYRP'), ('11248', 'B-12 50 MCG PO TABS'), ('435', 'VENTOLIN NEBU 0.083 % IN'), ('11248', 'MULTI-DELYN PO LIQD'), ('', 'ERTAPENEM 1 G IVPB'), ('42612', 'CROMOLYN SODIUM 4 % OP SOLN'), ('6932', 'MONISTAT 3 VA KIT'), ('5032', 'HYDROCODONE GF 5-100 MG/5ML PO SYRP'), ('4083', 'VIVELLE PTTW 0.0375 MG/24HR TD'), ('21949', 'CYCLOBENZAPRINE HCL 7.5 MG PO TABS'), ('8410', 'ALTEPLASE 50 MG IV SOLR'), ('', 'OMEGA-3 350 MG PO CPDR'), ('5487', 'MOEXIPRIL-HYDROCHLOROTHIAZIDE 15-25 MG PO TABS'), ('3423', 'DILAUDID 2 MG PO TABS'), ('787390', 'TAPENTADOL HCL 150 MG PO TB12'), ('2418', 'CALCIUM CARB-CHOLECALCIFEROL 500-400 MG-UNIT PO CHEW'), ('161', 'LORCET 10/650 TABS 10-650 MG OR'), ('161', 'PAIN RELIEVER EXTRA STRENGTH 500 MG PO TABS'), ('2403', 'THORAZINE 100 MG PO TABS'), ('', 'LECITH-INOSI-CHOL-B12-LIVER PO TABS'), ('17767', 'NORVASC 5 MG PO TABS'), ('2551', 'CIPRO HC SUSP 0.2-1 % OT'), ('5032', 'HUMIBID LA TBCR 600 MG OR'), ('', 'INV - SWOG S0819 - CETUXIMAB 100 MG/50ML IV SOLN'), ('48937', 'DEXMEDETOMIDINE HCL IN NACL 400 MCG/100ML IV SOLN'), ('484348', 'FISH OIL 1000 MG PO CAPS'), ('24941', 'NORETHINDRON-ETHINYL ESTRAD-FE 1-20/1-30/1-35 MG-MCG PO TABS'), ('6809', 'ACTOPLUS MET 15-500 MG PO TABS'), ('42954', 'VITAMIN B-6 100 MG PO TABS'), ('1244014', 'VITAMIN D3 LIQD'), ('6472', 'NIACIN-LOVASTATIN ER 500-20 MG PO TB24'), ('3289', 'DEXTROMETHORPHAN HBR 15 MG/5ML PO LIQD'), ('5032', 'TUSSIN 100 MG/5ML PO SYRP'), ('8629', 'MINIZIDE 2-0.5 MG PO CAPS'), ('237099', 'PRENEXA 30-1.2-265 MG PO CAPS'), ('', '1-COMPOUNDED MUPIROCIN IN SALINE NASAL SPRAY'), ('21406', 'COENZYME Q10 30 MG/5ML PO LIQD'), ('3638', 'DOXEPIN HCL 100 MG PO CAPS'), ('3289', 'ROBITUSSIN DM 100-10 MG/5ML PO SYRP'), ('6750', 'THERA-GESIC 0.5-15 % EX CREA'), ('704', 'ELAVIL 10 MG PO TABS'), ('10582', 'LEVOXYL TABS 175 MCG PO'), ('1191', 'PERCODAN TABS 325-4.5-0.38 MG PO'), ('5032', 'PSEUDOEPHEDRINE-GUAIFENESIN 120-600 MG PO TB12'), ('36118', 'MIACALCIN 200 UNIT/ML IJ SOLN'), ('2551', 'CIPROFLOXACIN 200 MG IV SOLN'), ('5492', 'HYDROCORTISONE (TOPICAL) GEL 1 % EX'), ('9601', 'BELLATAL TABS   PO'), ('1310520', 'TERIFLUNOMIDE 14 MG PO TABS'), ('19257', 'BETHANECHOL CHLORIDE 10 MG PO TABS'), ('802755', 'FEROCON PO CAPS'))

STATUS = {
    "": '',
    "Canceled": "Stopped",
    "Completed": "Completed",
    "Denied Approval": "Stopped",
    "Discontinued": "Stopped",
    "Dispensed": "Completed",
    "Holding for Referral": "On-hold",
    "Pending": "On-hold",
    "Pending Verify": "On-hold",
    "Resulted": "Completed",
    "Sent": "Active",
    "Suspend": "Stopped",
    "Verified": "Active"
}
