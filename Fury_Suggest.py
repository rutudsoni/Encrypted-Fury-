#title

print("FURY SUGGESTS")

print("BELOW CRITERIAS ARE CRITERIAS USED TO BE ENTERED IN YOUR BLOOD REPORT")

print("Complete Blood Count (CBC)")

# Hemoglobin Level Checker

gender = input("Enter your gender (Male/Female): ")

def check_hemoglobin(hb, gender):
    if gender.lower() == "male":
        if hb < 13.0:
            return "Low Hemoglobin (Possible Anemia)"
        elif 13.0 <= hb <= 17.0:
            return "Normal Hemoglobin Level "
        else:
            return "High Hemoglobin Level "
    
    elif gender.lower() == "female":
        if hb < 12.0:
            return "Low Hemoglobin (Possible Anemia)"
        elif 12.0 <= hb <= 15.0:
            return "Normal Hemoglobin Level "
        else:
            return "High Hemoglobin Level "
    
    else:
        return "Invalid gender entered."

# User Input

hb = float(input("Enter your Hemoglobin (g/dL): "))

# Output Result
result = check_hemoglobin(hb, gender)
print("\nResult:", result)

# RBC Level Checker

def check_rbc(rbc, gender):
    if gender.lower() == "male":
        if rbc < 4.7:
            return "Low RBC Count (Possible Anemia) "
        elif 4.7 <= rbc <= 6.1:
            return "Normal RBC Count "
        else:
            return "High RBC Count  (Possible Polycythemia)"
    
    elif gender.lower() == "female":
        if rbc < 4.2:
            return "Low RBC Count (Possible Anemia) "
        elif 4.2 <= rbc <= 5.4:
            return "Normal RBC Count "
        else:
            return "High RBC Count (Possible Polycythemia)"
    
    else:
        return "Invalid gender entered."

# User Input

print("\nWHITE BLOOD CELLS PARAMETERS: ")
print()

rbc = float(input("Enter your RBC count (million cells per microliter): "))

# Output Result
result = check_rbc(rbc, gender)
print("\nResult:", result)

print("\n\nEnter WBC Report Values: \n")

wbc = float(input("Total WBC Count (4000-11000): "))
neut = float(input("Neutrophils % (40-70): "))
lymph = float(input("Lymphocytes % (20-40): "))
mono = float(input("Monocytes % (2-8): "))
eos = float(input("Eosinophils % (1-6): "))
baso = float(input("Basophils % (0-1): "))

print("\n--- ANALYSIS ---\n")

# Total WBC
if wbc < 4000:
    print("WBC LOW → Possible viral infection or weak immunity")
elif wbc > 11000:
    print("WBC HIGH → Possible bacterial infection or inflammation")
else:
    print("WBC NORMAL (Safe)")

# Neutrophils
if neut < 40:
    print("Neutrophils LOW → Possible viral infection")
elif neut > 70:
    print("Neutrophils HIGH → Possible bacterial infection")
else:
    print("Neutrophils NORMAL (Safe)")

# Lymphocytes
if lymph < 20:
    print("Lymphocytes LOW → Weak immune response")
elif lymph > 40:
    print("Lymphocytes HIGH → Possible viral infection")
else:
    print("Lymphocytes NORMAL (Safe)")

# Monocytes
if mono < 2:
    print("Monocytes LOW → Bone marrow issue")
elif mono > 8:
    print("Monocytes HIGH → Chronic infection")
else:
    print("Monocytes NORMAL (Safe)")

# Eosinophils
if eos < 1:
    print("Eosinophils LOW → Usually not serious")
elif eos > 6:
    print("Eosinophils HIGH → Allergy or parasitic infection")
else:
    print("Eosinophils NORMAL (Safe)")

# Basophils
if baso < 0:
    print("Basophils LOW → Usually not serious")
elif baso > 1:
    print("Basophils HIGH → Allergy or inflammation")
else:
    print("Basophils NORMAL (Safe)")

print("Blood Sugar Test: ")

# Input values
fasting = float(input("\nEnter Fasting Blood Sugar: "))
pp = float(input("Enter Postprandial (PP) Blood Sugar: "))
random = float(input("Enter Random Blood Sugar: "))
hba1c = float(input("Enter HbA1c value: "))

print("\n--- Results ---")

# Fasting Blood Sugar
if fasting < 100:
    print("Fasting Blood Sugar: Normal")
elif fasting <= 125:
    print("Fasting Blood Sugar: Prediabetes")
else:
    print("Fasting Blood Sugar: Diabetes")

# Postprandial Blood Sugar
if pp < 140:
    print("PP Blood Sugar: Normal")
elif pp <= 199:
    print("PP Blood Sugar: Prediabetes")
else:
    print("PP Blood Sugar: Diabetes")

# Random Blood Sugar
if random < 140:
    print("Random Blood Sugar: Normal")
elif random >= 200:
    print("Random Blood Sugar: Diabetes")
else:
    print("Random Blood Sugar: Borderline")

# HbA1c
if hba1c < 5.7:
    print("HbA1c: Normal")
elif hba1c <= 6.4:
    print("HbA1c: Prediabetes")
else:
    print("HbA1c: Diabetes")

print("\nEnter Lipid Profile Values: \n")

total_chol = float(input("Total Cholesterol (Below 200 mg/dL): "))
ldl = float(input("LDL (Below 100 mg/dL): "))
hdl = float(input("HDL (Above 40 mg/dL): "))
trig = float(input("Triglycerides (Below 150 mg/dL): "))
vldl = float(input("VLDL (5-40 mg/dL): "))

print("\n--- LIPID PROFILE ANALYSIS ---\n")

# Total Cholesterol
if total_chol >= 200:
    print("Total Cholesterol HIGH → Risk of heart disease")
else:
    print("Total Cholesterol NORMAL")

# LDL
if ldl >= 100:
    print("LDL HIGH → Bad cholesterol, heart risk")
else:
    print("LDL NORMAL")

# HDL
if hdl < 40:
    print("HDL LOW → Increased heart risk")
else:
    print("HDL NORMAL (Protective)")

# Triglycerides
if trig >= 150:
    print("Triglycerides HIGH → Risk of heart disease")
else:
    print("Triglycerides NORMAL")

# VLDL
if vldl < 5 or vldl > 40:
    print("VLDL ABNORMAL → Lipid imbalance")
else:
    print("VLDL NORMAL")

print("\nEnter Liver Function Test Values\n")

alt = float(input("ALT (7-56 U/L): "))
ast = float(input("AST (10-40 U/L): "))
alp = float(input("ALP (44-147 U/L): "))
bilirubin = float(input("Total Bilirubin (0.1-1.2 mg/dL): "))
albumin = float(input("Albumin (3.5-5.0 g/dL): "))
protein = float(input("Total Protein (6.0-8.3 g/dL): "))

print("\nLIVER FUNCTION: \n")

# ALT
if alt > 56:
    print("ALT HIGH → Liver damage or hepatitis")
else:
    print("ALT NORMAL")

# AST
if ast > 40:
    print("AST HIGH → Liver or muscle damage")
else:
    print("AST NORMAL")

# ALP
if alp < 44 or alp > 147:
    print("ALP ABNORMAL → Liver or bone disorder")
else:
    print("ALP NORMAL")

# Bilirubin
if bilirubin > 1.2:
    print("Bilirubin HIGH → Jaundice or liver issue")
else:
    print("Bilirubin NORMAL")

# Albumin
if albumin < 3.5:
    print("Albumin LOW → Liver disease or malnutrition")
else:
    print("Albumin NORMAL")

# Total Protein
if protein < 6.0 or protein > 8.3:
    print("Total Protein ABNORMAL → Liver or kidney issue")
else:
    print("Total Protein NORMAL")

print("\nEnter Kidney Function Test Values\n")

creatinine = float(input("Creatinine (0.6-1.2 mg/dL): "))
urea = float(input("Urea (15-40 mg/dL): "))
bun = float(input("BUN (7-20 mg/dL): "))
uric = float(input("Uric Acid (2.4-6.0 mg/dL): "))
sodium = float(input("Sodium (135-145 mEq/L): "))
potassium = float(input("Potassium (3.5-5.0 mEq/L): "))
chloride = float(input("Chloride (96-106 mEq/L): "))

print("\nKIDNEY TEST: \n")

# Creatinine
if creatinine < 0.6:
    print("Creatinine LOW → Low muscle mass or pregnancy")
elif creatinine > 1.2:
    print("Creatinine HIGH → Possible kidney problem")
else:
    print("Creatinine NORMAL")

# Urea
if urea < 15:
    print("Urea LOW → Liver problem or malnutrition")
elif urea > 40:
    print("Urea HIGH → Kidney issue or dehydration")
else:
    print("Urea NORMAL")

# BUN
if bun < 7:
    print("BUN LOW → Liver disease")
elif bun > 20:
    print("BUN HIGH → Kidney problem or dehydration")
else:
    print("BUN NORMAL")

# Uric Acid
if uric < 2.4:
    print("Uric Acid LOW → Usually not serious")
elif uric > 6.0:
    print("Uric Acid HIGH → Gout or kidney issue")
else:
    print("Uric Acid NORMAL")

# Sodium
if sodium < 135:
    print("Sodium LOW → Hyponatremia")
elif sodium > 145:
    print("Sodium HIGH → Dehydration")
else:
    print("Sodium NORMAL")

# Potassium
if potassium < 3.5:
    print("Potassium LOW → Muscle weakness")
elif potassium > 5.0:
    print("Potassium HIGH → Kidney problem")
else:
    print("Potassium NORMAL")

# Chloride
if chloride < 96:
    print("Chloride LOW → Metabolic disorder")
elif chloride > 106:
    print("Chloride HIGH → Dehydration")
else:
    print("Chloride NORMAL")



print("\nTHYROID FUNCTION: \n")
print("\nEnter Thyroid Function Test Values: \n")

tsh = float(input("TSH (0.4-4.0 mIU/L): "))
t3 = float(input("T3 (80-200 ng/dL): "))
t4 = float(input("T4 (5-12 µg/dL): "))

print("\n--- THYROID TEST ANALYSIS ---\n")

# TSH
if tsh < 0.4:
    print("TSH LOW → Possible Hyperthyroidism")
elif tsh > 4.0:
    print("TSH HIGH → Possible Hypothyroidism")
else:
    print("TSH NORMAL")

# T3
if t3 < 80:
    print("T3 LOW → Hypothyroidism")
elif t3 > 200:
    print("T3 HIGH → Hyperthyroidism")
else:
    print("T3 NORMAL")

# T4
if t4 < 5:
    print("T4 LOW → Hypothyroidism")
elif t4 > 12:
    print("T4 HIGH → Hyperthyroidism")
else:
    print("T4 NORMAL")



print("\nINFLAMMATORY AND OTHER MARKER VALUES: \n")
print("Enter Inflammatory & Other Marker Values: \n")

crp = float(input("CRP (0-5 mg/L): "))
esr = float(input("ESR (0-20 mm/hr): "))
vitd = float(input("Vitamin D (20-50 ng/mL): "))
b12 = float(input("Vitamin B12 (200-900 pg/mL): "))
iron = float(input("Serum Iron (60-170 µg/dL): "))
ferritin = float(input("Ferritin (12-150 ng/mL): "))
tibc = float(input("TIBC (240-450 µg/dL): "))
calcium = float(input("Calcium (8.6-10.2 mg/dL): "))

print("\n--- INFLAMMATORY MARKERS ANALYSIS ---\n")

# CRP
if crp > 5:
    print("CRP HIGH → Inflammation or infection")
else:
    print("CRP NORMAL")

# ESR
if esr > 20:
    print("ESR HIGH → Chronic inflammation or infection")
else:
    print("ESR NORMAL")

# Vitamin D
if vitd < 20:
    print("Vitamin D LOW → Bone weakness, low immunity")
elif vitd > 50:
    print("Vitamin D HIGH → Excess supplementation")
else:
    print("Vitamin D NORMAL")

# Vitamin B12
if b12 < 200:
    print("Vitamin B12 LOW → Anemia, nerve weakness")
elif b12 > 900:
    print("Vitamin B12 HIGH → Excess supplementation")
else:
    print("Vitamin B12 NORMAL")

# Iron
if iron < 60:
    print("Iron LOW → Iron deficiency anemia")
elif iron > 170:
    print("Iron HIGH → Iron overload")
else:
    print("Iron NORMAL")

# Ferritin
if ferritin < 12:
    print("Ferritin LOW → Iron deficiency")
elif ferritin > 150:
    print("Ferritin HIGH → Inflammation or iron overload")
else:
    print("Ferritin NORMAL")

# TIBC
if tibc > 450:
    print("TIBC HIGH → Iron deficiency")
elif tibc < 240:
    print("TIBC LOW → Chronic disease")
else:
    print("TIBC NORMAL")

# Calcium
if calcium < 8.6:
    print("Calcium LOW → Bone disorder or deficiency\n")
elif calcium > 10.2:
    print("Calcium HIGH → Parathyroid issue\n")
else:
    print("Calcium NORMAL\n")