# Hands Free Οδήγηση
Α. Σκοπός

Σκοπός του έργου "HandsFreeDriving" είναι η κατασκευή ενός ρομποτικού οχήματος το οποίο θα μπορεί να "ακούει" εντολές από τους χρήστες, όπως κινήσου 20cm ή στρίψε αριστερά και να εκτελεί τις αντίστοιχες κινήσεις.

Β. Υλικό

Για την εκτέλεση του παραπάνω έργου, απαιτείται το εξής hardware:
Ένα Raspberry Pi 3, για να φιλοξενήσει τις υπηρεσίες ήχος - σε - κείμενο και κείμενο - σε - ήχο που περιγράφηκαν παραπάνω.
Μία πλατφόρμα οχήματος σχεδιασμένη για Raspberry Pi 3. Αυτή που θα επιλεχθεί για το έργο είναι η AlphaBot της WaveShare.

Το κόστος του εξοπλισμού αναλύεται ως εξής:
1. ~33.5 ευρώ για την αγορά του raspberry pi 3 (https://www.ebay.com/itm/Original-Raspberry-Pi-3-Model-B-Quad-Core-1-2GHz-64-bit-CPU-wifi-bluetooth/192099353359?epid=24019970648&hash=item2cba03830f:g:C~wAAOSw0ABankhY:rk:6:pf:0)
2. ~58 ευρώ για την ρομποτική πλατφόρμα οδήγησης (https://www.ebay.com/itm/Waveshare-AlphaBot-Raspberry-Pi-Robot-Building-kit-Smart-car-includes-Camera/262732580491?epid=2080456011&hash=item3d2c15068b:g:y5MAAOSwEzxYTneI:rk:1:pf:0)
3. ~3.5 ευρώ για ένα bluetooth ηχείο (https://mobilepoint.gr/index.php?route=product/product&product_id=292)
4. ~1 ευρώ για ένα μικρόφωνο (https://www.ebay.com/itm/Mini-USB-Microphone-Professional-Mini-USB-External-Mic-Microphone-With-Clip/253700094909?hash=item3b11b43bbd:g:9XQAAOSwllpbKgAR:rk:2:pf:0)

Γ. Λογισμικό

Το λογισμικό που θα αναπτυχθεί στα πλαίσια του έργου θα είναι γραμμένο σε Python2.7. Οι βιβλιοθήκες που θα απαιτηθούν για την ολοκλήρωση των διαφόρων υποσυστημάτων θα είναι:
Βιβλιοθήκη οδήγησης του ρομποτικού οχήματος (https://www.waveshare.com/wiki/AlphaBot)
Βιβλιοθήκη για την μετατροπή της ομιλίας σε κείμενο (speech to text) (https://pypi.org/project/SpeechRecognition/)
Βιβλιοθήκη για την μετατροπή κείμενου σε ομιλία (text to speech) (https://pythonprogramminglanguage.com/text-to-speech/)

Δ. Github

Ο σύνδεσμος του github για το έργο βρίσκεται εδώ: https://github.com/vtsakan/handsfreedriving

Ε. Εκπαιδευτικό σενάριο

ΣΤ. Προγραμματισμός υλοποίησης
