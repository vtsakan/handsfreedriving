import RPi.GPIO as GPIO # Εισαγωγή βιβλιοθήκης επαφών GPIO του RPi
import time		# Εισαγωγή βιβλιοθήκης επιστροφής του χρόνου
import speech_recognition as sr # Εισαγωγή βιβλιοθήκης αναγνώρισης φωνής 

class AlphaBot2(object):
	#Αρχικοποίηση τιμών στις θύρες GPIO
	def __init__(self,ain1=12,ain2=13,ena=6,bin1=20,bin2=21,enb=26):
		self.AIN1 = ain1
		self.AIN2 = ain2
		self.BIN1 = bin1
		self.BIN2 = bin2
		self.ENA = ena
		self.ENB = enb
		self.PA  = 30
		self.PB  = 30

		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.AIN1,GPIO.OUT)
		GPIO.setup(self.AIN2,GPIO.OUT)
		GPIO.setup(self.BIN1,GPIO.OUT)
		GPIO.setup(self.BIN2,GPIO.OUT)
		GPIO.setup(self.ENA,GPIO.OUT)
		GPIO.setup(self.ENB,GPIO.OUT)
		self.PWMA = GPIO.PWM(self.ENA,500)
		self.PWMB = GPIO.PWM(self.ENB,500)
		self.PWMA.start(self.PA)
		self.PWMB.start(self.PB)
		self.stop()
	# Ορισμός κίνησης προς τα εμπρός
	def forward(self):
		self.PWMA.ChangeDutyCycle(20)	# Αριθμός περιστροφών δεξί τροχού
		self.PWMB.ChangeDutyCycle(20)	# Αριθμός περιστροφών αριστερού τροχού
		GPIO.output(self.AIN1,GPIO.LOW)
		GPIO.output(self.AIN2,GPIO.HIGH)
		GPIO.output(self.BIN1,GPIO.LOW)
		GPIO.output(self.BIN2,GPIO.HIGH)

	# Ορισμός στάσης
	def stop(self):
		self.PWMA.ChangeDutyCycle(0)	# Αριθμός περιστροφών δεξί τροχού
		self.PWMB.ChangeDutyCycle(0)	# Αριθμός περιστροφών αριστερού τροχού
		GPIO.output(self.AIN1,GPIO.LOW)
		GPIO.output(self.AIN2,GPIO.LOW)
		GPIO.output(self.BIN1,GPIO.LOW)
		GPIO.output(self.BIN2,GPIO.LOW)
		
	# Ορισμός κίνησης προς τα πίσω
	def backward(self):
		self.PWMA.ChangeDutyCycle(20)	# Αριθμός περιστροφών δεξί τροχού
		self.PWMB.ChangeDutyCycle(20)	# Αριθμός περιστροφών αριστερού τροχού
		GPIO.output(self.AIN1,GPIO.HIGH)
		GPIO.output(self.AIN2,GPIO.LOW)
		GPIO.output(self.BIN1,GPIO.HIGH)
		GPIO.output(self.BIN2,GPIO.LOW)

	# Ορισμός κίνησης προς τα αριστερά	
	def left(self):
		self.PWMA.ChangeDutyCycle(20)	# Αριθμός περιστροφών δεξί τροχού
		self.PWMB.ChangeDutyCycle(20)	# Αριθμός περιστροφών αριστερού τροχού
		GPIO.output(self.AIN1,GPIO.HIGH)
		GPIO.output(self.AIN2,GPIO.LOW)
		GPIO.output(self.BIN1,GPIO.LOW)
		GPIO.output(self.BIN2,GPIO.HIGH)

	# Ορισμός κίνησης προς τα δεξιά
	def right(self):
		self.PWMA.ChangeDutyCycle(20)	# Αριθμός περιστροφών δεξί τροχού
		self.PWMB.ChangeDutyCycle(20)	# Αριθμός περιστροφών αριστερού τροχού
		GPIO.output(self.AIN1,GPIO.LOW)
		GPIO.output(self.AIN2,GPIO.HIGH)
		GPIO.output(self.BIN1,GPIO.HIGH)
		GPIO.output(self.BIN2,GPIO.LOW)
		
	# Ορισμός δύναμης κίνησης δεξί τροχού	
	def setPWMA(self,value):
		self.PA = value
		self.PWMA.ChangeDutyCycle(self.PA)
	# Ορισμός δύναμης κίνησης αριστερού τροχού
	def setPWMB(self,value):
		self.PB = value
		self.PWMB.ChangeDutyCycle(self.PB)	
		
	# Ορισμός μετάδοσης κίνησης προς αριστερή ή δεξιά κατεύθυνση	
	def setMotor(self, left, right):
		if((right >= 0) and (right <= 100)):
			GPIO.output(self.AIN1,GPIO.HIGH)
			GPIO.output(self.AIN2,GPIO.LOW)
			self.PWMA.ChangeDutyCycle(right)
		elif((right < 0) and (right >= -100)):
			GPIO.output(self.AIN1,GPIO.LOW)
			GPIO.output(self.AIN2,GPIO.HIGH)
			self.PWMA.ChangeDutyCycle(0 - right)
		if((left >= 0) and (left <= 100)):
			GPIO.output(self.BIN1,GPIO.HIGH)
			GPIO.output(self.BIN2,GPIO.LOW)
			self.PWMB.ChangeDutyCycle(left)
		elif((left < 0) and (left >= -100)):
			GPIO.output(self.BIN1,GPIO.LOW)
			GPIO.output(self.BIN2,GPIO.HIGH)
			self.PWMB.ChangeDutyCycle(0 - left)
# Έναρξη κυρίως προγράμματος
if __name__=='__main__':
	r = sr.Recognizer()	# Μεταβλητή καταχώρησης φωνητικής εντολής
	Ab = AlphaBot2()	
	
	# Έναρξη ηχογράφησης φωνητικής εντολής και μετατροπής σε εντολής κίνησης
	while (True):
		with sr.Microphone() as source:	
			print("Say something!")
			audio = r.listen(source)	# Αρχείο ήχου καταγραφής 
			
	# Κώδικας για Περιβάλλον Spinx
	# recognize speech using Sphinx
	
	#	try:
	#		print("Sphinx thinks you said " + r.recognize_sphinx(audio))
	#		Ab.forward();
	#		time.sleep(1);
	#		Ab.stop();
	##	except sr.UnknownValueError:
	#		print("Sphinx could not understand audio")
	#	except sr.RequestError as e:
	#		print("Sphinx error; {0}".format(e))
	
	# recognize speech using Google Speech Recognition
			try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
				inputtext = r.recognize_google(audio); # Μετατροπή φωνητικής σε κείμενο
				print("Google Speech Recognition thinks you said " + inputtext);
				# Μετατροπή εντολής κειμένου σε κίνηση
				if ('f'and 'w'and 'rd' in inputtext):	# Κίνηση προς τα εμπρός
					Ab.forward();
					time.sleep(1);
					Ab.stop();
				elif ('r' and 'v' and 'r' and 's' in inputtext): # Κίνηση προς τα πίσω 
					Ab.backward();
					time.sleep(1);
					Ab.stop();
				elif ('l' and 'ft'  in inputtext): # Κίνηση προς τα αριστερά
					Ab.left();
					time.sleep(1);
					Ab.stop();
				elif ('right' in inputtext): # Κίνηση προς τα δεξιά
					Ab.right();
					time.sleep(1);
					Ab.stop();
			# Μήνυμα λάθους		
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))
	

