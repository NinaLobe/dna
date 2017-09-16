#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "Program za prepoznavanje DNA"

#baza za naso poizvedbo.
hair_color = {"Black":"CCAGCAATCGC", "Brown":"GCCAGTGCCG", "Blonde": "TTAGCTATCGC"}
face_shape = {"Square": "GCCACGG", "Round": "ACCACAA", "Oval": "AGGCCTCA"}
eye_color = {"Blue": "TTGTGGTGGC","Green": "GGGAGGTGGC","Brown": "AAGTAGTGAC"}
gender = {"Female": "TGAAGGACCTTC", "Male": "TGCAGGAACTTC"}
race = {"White": "AAAACCTCA","Black": "CGACTACAG","Asian": "CGCGGGCCG"}

storilec = {}

Eva={"gender": "Female",
"race": "White",
"hair_color": "Blonde",
"eye_color": "Blue",
"face_shape": "Oval"}

Larisa={"Gender": "Female",
"race": "White",
"hair_color": "Brown",
"eye_color": "Brown",
"face_shape": "Oval"}

Matej={"gender": "Male",
"race": "White",
"hair_color": "Black",
"eye_color": "Blue",
"face_shape": "Oval"}

Miha={"gender": "Male","race": "White","hair_color": "Brown","eye_color": "Green","face_shape": "Square"}


#vnos nase dna datoteke v spremenljivko

vzorec = open("dna.txt", "r")
vzorec = vzorec.read()
#print vzorec

#primerjava stringov barva las
while True:
    if vzorec.find(hair_color["Black"])!=-1:
       # print "Black"
        storilec["hair_color"] = "Black"
        break
    elif vzorec.find(hair_color["Brown"])!=-1:
       # print "Brown"
        storilec["hair_color"] = "Brown"
        break
    elif vzorec.find(hair_color["Blonde"]) != -1:
      #  print "Blonde"
        storilec["hair_color"] = "Blonde"
        break
    else:
        print "Ni v bazi"
        break

#primerjava stringov oblika obraza
while True:
    if vzorec.find(face_shape["Square"])!=-1:
       # print "Square"
        storilec["face_shape"] = "Square"
        break
    elif vzorec.find(face_shape["Round"])!=-1:
       # print "Round"
        storilec["face_shape"] = "Round"
        break
    elif vzorec.find(face_shape["Oval"]) != -1:
        storilec["face_shape"] = "Oval"
      #  print "Oval"
        break
    else:
        print "Ni v bazi"
        break

#primerjava barva oci eye_color = {"Blue": "TTGTGGTGGC","Green": "GGGAGGTGGC","Brown": "AAGTAGTGAC"}

while True:
    if vzorec.find(eye_color["Blue"])!=-1:
        storilec["eye_color"] = "Blue"
       # print "Blue"
        break
    elif vzorec.find(eye_color["Green"])!=-1:
        storilec["eye_color"] = "Green"
      #  print "Green"
        break
    elif vzorec.find(eye_color["Brown"]) != -1:
        storilec["eye_color"] = "Brown"
       # print "Brown"
        break
    else:
        print "Ni v bazi"
        break

# spol gender = {"Female": "TGAAGGACCTTC", "Male": "TGCAGGAACTTC"}
while True:
    if vzorec.find(gender["Female"])!=-1:
        storilec["gender"] = "Female"
      #  print "Female"
        break
    elif vzorec.find(gender["Male"])!=-1:
        storilec["gender"] = "Male"
     #   print "Male"
        break
    else:
        print "Ni v bazi"
        break
#race = {"White": "AAAACCTCA","Black": "CGACTACAG","Asian": "CGCGGGCCG"}
while True:
    if vzorec.find(race["White"])!=-1:
        storilec["race"] = "White"
     #   print "White"
        break
    elif vzorec.find(race["Black"])!=-1:
        storilec["race"] = "Black"
      #  print "Black"
        break
    elif vzorec.find(eye_color["Asian"]) != -1:
        storilec["race"] = "Asian"
       # print "Asian"
        break
    else:
        print "Ni v bazi"
        break

# print storilec

#Doloci ime storilca
if storilec == Eva:
    print "Storilec je Eva"
elif storilec == Larisa:
    print "Storilec je Larisa"
elif storilec == Matej:
    print "Storilec je Matej"
elif storilec == Miha:
    print "Storilec je Miha. Našli smo naslednje njegove naslednje lastnosti: "
    print "Spol: " + storilec["gender"]
    print "Barva oči: " + storilec["eye_color"]
    print "Rasa: " + storilec["race"]
    print "Barva las: " + storilec["hair_color"]
    print "Oblika obraza: " + storilec["face_shape"]
else:
    print "Ni ga med vnešenimi primeri :("
