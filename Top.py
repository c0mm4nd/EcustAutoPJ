# coding:utf8
from bottle import Bottle
from pj import main as pj

# Bottle 对象命名方法： Url名（用户）
EcustAutoPJ = Bottle()

@EcustAutoPJ.route('/<id>/<pw>')
def EcustAutoPJAPI(id, pw):
	return {'msg': pj(id, pw)}

@EcustAutoPJ.route('/')
def EcustAutoPJIndex():
	return '''
	this is the usage : 
	<br>
	Now you have arrived the URL : http://Ecust.Top/EcustAutoPJ/ 
	<br>
	As you see, its just a guider.
	<br>
	If you wanna continue, you have to the URL : http://Ecust.Top/EcustAutoPJ/<Your Student ID>/<Your Password>
	<br>
	For example :
	<br>
	    http://Ecust.Top/EcustAutoPJ/10142045/HandsomeMan can serve the student who has the '10142045' Student ID and the 'HandsomeMan' Student Password.
	<br>
	Enjoy this little script and let's learn English ^_^  
	'''