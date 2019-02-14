MAR_ACTION = {
    "Anesthesia Bar Code": "Other",
    "Anesthesia Bolus": "In progress",
    "Anesthesia Hold": "On-hold",
    "Anesthesia Volume Adjustment": "In progress",
    "Applied": "In progress",
    "Automatically Held": "On-hold",
    "Bolus": "Completed",
    "Bolus from Bag": "Completed",
    "Canceled Entry": "Entered-in-error",
    "Chemo Prep Check": "In progress",
    "Completed": "Completed",
    "Dispensed from ED": "In progress",
    "Due": "Active",
    "Given": "Completed",
    "Given During Conversion": "Completed",
    "Given During Downtime": "Completed",
    "Given by Other": "Completed",
    "Handoff": "Other",
    "Held": "On-hold",
    "IV Infusion Continues on Transfer": "In progress",
    "IV Pause": "On-hold",
    "IV Resume": "In progress",
    "IV Stop": "Stopped",
    "Infusion Continues to Floor": "In progress",
    "MAR Hold": "On-hold",
    "MAR Unhold": "In progress",
    "Missed": "Stopped",
    "New Bag": "Other",
    "New Syringe/Cartridge": "Other",
    "Not Given": "Stopped",
    "Patch Removed": "Other",
    "Paused": "On-hold",
    "Pending": "In progress",
    "Rate Change": "Other",
    "Rate Verify": "Other",
    "Rate/Dose Change": "Other",
    "Rate/Dose Change NICU": "Other",
    "Refused": "Refused",
    "Removed": "Other",
    "Restarted": "In progress",
    "Return to Cabinet": "Other",
    "See Alternative": "Other",
    "Start": "In progress",
    "Started During Conversion": "In progress",
    "Started During Downtime": "In progress",
    "Stopped": "Stopped",
    "UBC Duplicate": "Other",
    "Verify Patch Placement": "Other",
    "Verify Waste": "Other"
}

DOSE = ('', '59.25', '1843.2', '11540', '161.8', '3483', '161.2', '161.4', '5985', '153.2', '153.6', '139.175', '153.4', '153.8', '45.9', '45.8', '15.673', '45.3', '45.2', '45.1', '45.7', '45.6', '45.5', '45.4', '300250', '44.55', '147.75', '2.189', '421.8', '6790', '17.33', '421.2', '421.5', '2.185', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '2146', '2.71739130434783', '12012', '251.25', '871.2', '17250', '9525', '9520', '9250', '0.146', '7.887', '7.883', '565.8', '1373', '694.2', '565.2', '565.4', '694.8', '624.6', '0.091', '0.092', '0.093', '0.094', '0.095', '0.096', '0.097', '0.098', '0.099', '28.95', '161.6', '4.133', '3510', '3515', '839.4', '2688', '13.38', '13.36', '2685', '2686', '2680', '13.33', '2682', '0.899', '0.678', '18.14', '0.674', '0.675', '0.892', '0.677', '0.894', '0.671', '0.896', '0.673', '99', '98', '1.044', '1.042', '1.515', '91', '90', '93', '92', '95', '94', '97', '96', '50.55', '1377', '316.4', '15.052', '1293.3', '18702', '36.179', '1.562', '166.667', '36.175', '51.8', '51.9', '14688', '845.4', '85.875', '51.2', '51.3', '51.4', '51.5', '51.6', '51.7', '579.6', '77.9', '16.047', '77.4', '77.5', '77.6', '77.7', '77.1', '77.2', '1177', '1176', '1175', '1174', '1172', '1170', '1179', '1178', '21.33', '31.875', '14.17', '50.977', '98.69', '43.63', '43.65', '876', '40.039', '40.035', '92300', '623', '19.655', '1226', '1225', '3435', '620', '1223', '50.5', '762.4', '8540', '762.6', '626', '9.996', '9.991', '2740', '1220', '126.6', '126.4', '126.5', '2747', '13.939', '2030', '.125', '14.42', '14.47', '114.8', '114.5', '114.4', '114.6', '50.625', '114.2', '0.81', '15552', '393', '392', '735.6', '390', '397', '396', '395', '394', '399', '398', '0.208', '2309', '11.683', '4728', '4725', '2300', '2303', '2305', '4720', '2307', '5845', '403.65', '5840', '143.3333', '0.207', '0.206', '1428.8', '0.973', '3744', '3745', '3740', '3741',
        '4620', '4625', '164.2', '5.717', '11.355', '19560', '19.14', '19.15', '19.13', '74.775', '19.18', '96.117', '179', '178', '177', '176', '175', '174', '173', '172', '171', '170', '.219', '61.95', '20088', '1162.5', '0.461', '0.463', '781.2', '0.465', '0.464', '0.467', '0.466', '0.469', '0.468', '441.6', '17388', '6215', '12220', '6210', '461.4', '461.5', '60.525', '128.8', '9.08', '15876', '128.1', '86.625', '128.4', '406.8', '9750', '406.5', '5487.5', '406.2', '2.78', '422.5', '422.4', '2.71', '12.013', '2.73', '90.56', '2.75', '12.017', '2.77', '8840', '1321.5', '3875', '0.285', '0.284', '100.8', '0.286', '0.281', '3876', '0.283', '0.282', '100.2', '100.3', '13.495', '100.6', '0.288', '100.4', '100.5', '474.6', '1762', '1763', '1760', '1761', '0.2958', '1767', '1764', '1765', '26.023', '26.026', '30.086', '664.5', '664.2', '664.8', '692', '693', '690', '1545', '696', '697', '694', '695', '698', '699', '1.709', '1548', '28350', '3.762', '4.07', '4.04', '4.05', '4.03', '4.01', '165.45', '57.45', '5619', '78.75', '5610', '22.25', '22.27', '5615', '659.5', '659.4', '140.17', '126.075', '53.325', '196.6', '3089', '196.2', '50.4', '11560', '16.66', '3045', '651.9', '81.975', '.0015', '44.743', '592.8', '1.25', '40.8', '40.2', '5.125', '40.1', '40.6', '40.7', '40.4', '40.5', '17.15', '62.9', '62.6', '62.7', '62.4', '62.5', '62.2', '62.1', '109', '9960', '11.18', '11.19', '11.16', '11.14', '11.15', '143.6667', '258', '259', '252', '253', '250', '251', '256', '257', '254', '255', '76.1', '3.86', '3.85', '3.84', '214.33', '3.89', '26.25', '9500', '741.2', '2.574', '828.6', '65.93', '4.333', '3680', '3685', '2519', '2515', '2517', '2510', '2512', '339.5', '0.078', '339.3', '0.076', '0.077', '0.074', '0.075', '0.072', '0.073', '0.071', '3531', '3530', '755.4', '3535', '3537', '7.757', '5056', '5057', '5050', '13.15', '13.18', '10760', '25.075', '5.109', '25.071', '0.618', '0.619', '18.38')

UNIT = ('', 'mEq/hr', 'Tube', 'mEq/kg/hr', 'lozenge', 'mmol/kg', 'tablet', 'cup', 'Units/kg/hr', 'mL/hr', 'mcg/hr', 'mEq', 'L', 'mg/hr', 'capsule', 'Can', 'mcg/kg/hr', 'mL/kg/hr', 'g/m2', 'mL/kg', 'mcg/kg', 'Units/kg', 'drop', 'patch', 'mg/kg', 'each', 'Million Units/m2', 'g/kg/day', 'g/kg', 'packet', 'mg/min', 'mg/kg of ampicillin', 'Units', 'Dose', 'mcg/min', 'mg/kg of piperacillin', 'mL/kg/min', 'mcg/kg/min', 'mg PE', 'pump', 'Units/m2', 'mg/m2', 'mEq/kg', 'Wafer', 'Units/mL', 'mg/day', 'spray', 'enema',
        'mmol', 'g', 'mg PE/kg/day', 'oz', 'Syringe', 'puff', 'cm', 'mg/kg/hr', 'strip', 'Squirt', 'mg PE/kg', 'Stick', 'Device', 'Units/hr', 'g/hr', 'mcg', 'mL', 'Million Cells', 'Bottle', 'mg', 'vial', 'suppository', "Int'l Units", 'Container', 'mg/kg/day', 'Million Units', 'L/min', 'mL/day', 'mcg/day', 'mcg/m2', 'milli-units/min', 'ng', 'application', 'ampule', 'inch', 'Applicatorful', 'Package', 'kit', 'mg/m2/day', 'Act', 'ng/kg/min', 'inhalation', 'm', 'applicator', 'Film', 'Units/min')

REASON = ('', 'Caregiver Judgement', 'Patient sleeping', 'Unable to Swallow', 'Other: Comment', 'Other', 'New Med Order', 'Tachycardia', 'Patient failed swallow study', 'NICU - with feeding', 'Medication not available', 'Family Refused', 'Infiltrated Site', 'Loss of IV access', 'Tachypnea', 'Patient Emesis', 'Transfer to a Procedural area', 'NPO for Procedures', 'Contraindicated', 'Bradypnea',
          'Hypotension', 'Patient/family refused', 'Alternative Route', 'Patient Nauseated', 'Patient Lethargic/Unresponsive', 'Bradycardia', 'NPO', 'Safety Parameters Not Met', 'Patient not available', 'Not in room', 'Went to Standard Admin Times', 'Blood Infusion/To be Infused', 'Unreviewed Transfer Orders', 'Hypertension', 'Order parameters not met', 'Physician Order to Hold', 'IV Infusing')

SITE = ('', 'Port ', 'Perineum', 'Wrist, Left', 'Back, Right Upper', 'Radial, Right', 'Jugular, Internal Right', 'Bladder', 'Abdomen, LLQ', 'Breast, Left', 'Ankle, Left', 'Nare, Left', 'Popliteal, Left', 'Jugular, Internal Left', 'Buttock, Right', 'Breasts, Bilateral', 'Thighs, Bilateral', 'Thigh, Right', 'Buttocks, Bilateral', 'Ear, Left', 'Arm, Left', 'Forehead', 'Eyelids, Bilateral', 'Right Upper Outer Quadrant', 'Ankle, Right', 'Elbow, Left', 'Ears, Bilateral', 'Subclavian, Right', 'Vagina', 'Left Upper Outer Quadrant', 'Abdomen, LUQ', 'Eyelid, Left', 'Breast, Right', 'Back, Left Lower', 'Groin, Left', 'Elbow, Right', 'Groin, Right', 'Wrist, Right', 'Chest, Right', 'Fingers (specify)', 'Leg, Left Lower', 'Nares, Bilateral', 'Toes (specify)', 'Radial, Left', 'Back, Left Upper', 'Eye, Left', 'Arm, Right',
        'Hip, Left', 'Brachial, Right', 'Tibial, Right', 'Quadriceps, Left', 'Left Quadriceps', 'Subclavian, Left', 'Brachial, Left', 'Chest, Left', 'Arms, Bilateral', 'Deltoid, Left', 'Penis', 'Quadriceps, Right', 'Hip, Right', 'Sinus Cavity', 'Eyelid, Right', 'Ventrogluteal, Right', 'Face', 'Tibial, Left', 'Foot, Right', 'Knee, Right', 'Eye, Right', 'Hand, Left', 'Left Arm', 'Ventrogluteal, Left', 'Right Quadriceps', 'Nare, Right', 'Neck', 'Vastus Lateralis, Right', 'Popliteal, Right', 'Back, Right Lower', 'Other', 'Knee, Left', 'Foot, Left', 'Deltoids, Bilateral', 'Right Arm', 'Leg, Right Lower', 'Hand, Right', 'Abdominal Tissue', 'Deltoid, Right', 'Head', 'Buttock, Left', 'Eye, Bilateral', 'Thigh, Left', 'Shoulder, Right', 'Abdomen, RLQ', 'Vastus Lateralis, Left', 'Ear, Right', 'Abdomen, RUQ', 'Throat', 'Shoulder, Left')

MAR_DURATION = ('', '216', '215', '90-240', '213', '210', '6.7', '6.6', '6.5', '130', '7.5', '138', '37.5', '24', '25', '.1-2', '27', '20', '21', '22', '23', '160', '28', '26', '4', '2400', '2.18', '8', '2010', '90-120', '.17', '23.8', '999', '120', '260', '125', '4-5', '14.5', '133', '17', '55', '54', '57', '56', '51', '50', '53', '52', '2.66', '360', '1.5-2', '18', '290', '3000', '14.75', '6.66', '6.67', '7.14', '6.65', '22.25', '700', '190', '192', '115', '3.5', '111', '110', '112', '90-150', '83', '80', '86', '175', '2.5', '85', '20.5', '15-90', '1.75', '3', '7', '170', '60-180', '60-120', '.75', '440', '60-240', '300', '22.5', '60-90', '47', '1545', '240', '102', '103', '100', '3.25', '249', '42.5', '104', '105', '39', '4.2', '33', '32', '31', '30', '36', '35', '23.5', '1245', '13.25', '11.76', '1000', '1.5', '450', '900', '.45', '60',
                '61', '64', '65', '66', '67', '68', '5.45', '250', '198', '21.5', '8.3', '8.5', '5.7', '1638', '180', '2', '162', '6', '.1', '78', '.5', '500', '1035', '2-3', '229.4', '750', '30-90', '2-4', '2-5', '185', '460', '30-120', '168', '90', '95', '97', '96', '11', '10', '13', '12', '15', '14', '4-6', '16', '19', '2.67', '120-180', '13.33', '390', '3.33', '720', '1.45', '11.7', '1.43', '3.3', '151', '150', '153', '155', '600', '156', '400', '1200', '2.3', '8.33', '2-6', '230', '13.3', '.25', '4.5', '22.75', '5.4', '48', '49', '46', '30-60', '44', '45', '42', '43', '40', '41', '1', '320', '5', '1440', '9', '1.33', '1.875', '15-30', '200', '144', '205', '143', '140', '1-3', '1-2', '148', '1-6', '77', '76', '75', '72', '70', '5.72', '1-1.5', '480', '4.3', '350', '3-6', '3-5', '3-4', '10.82', '2.7', '2-10', '1515', '11.5', '800', '1.25', '20-30')

DISCONT_REASON = ('', 'Discontinued by another Health Care Provider', 'Incorrect Medication', 'Anesthesia Stop', 'Returned to ADS', 'Contact Move - Error', 'Therapy Completed', 'Reorder', 'Paradoxical Response', 'Patient Transfer', 'Formulary Change', 'Side Effects', 'Not Needed', 'Patient Discharge', 'Stopped Prior to Admission',
                  'Dose Incorrect', 'Allergic Response', 'Duplicate Order', 'Non Compliance', 'Patient Declined', 'Stop Taking at Discharge', 'Error', 'Cost of Medication', 'Alternate Therapy', 'Provider deems inappropriate for patient', 'Change To Generic', 'Ineffective', 'Pregnancy', 'Surgery', 'Availability', 'Dose Adjustment')
