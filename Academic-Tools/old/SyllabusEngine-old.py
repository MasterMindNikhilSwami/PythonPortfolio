import requests
import html5lib 
from bs4 import BeautifulSoup as soup

def remove_line (item):
	if item == '\n':
		return ''

def get_html_data(url):
	response=requests.get(url).text
	return response

url="https://jnu.ac.in/se-dual-degree-programmes"
htmlobj=soup(	get_html_data(url)	,'html5lib')
paragraphs = htmlobj.find_all('p')

for i in range(6): #remove last 6
	paragraphs.pop()


paragraphs_text=[]
for i in paragraphs:
	paragraphs_text.append(i.text)

# string='Introduction to VLSI, Manufacturing process of CMOS integrated circuits, CMOS n-well process design rules, packaging integrated circuits, trends in process technology. MOS transistor, Energy band diagram of MOS system, MOS under external bias, derivation of threshold voltage equation, secondary effects in MOSFETS, MOSFET scaling and small geometry effects, MOS capacitances, Modeling of MOS transistors using SPICE, level I II and equations, capacitance models. The Wire: Interconnect parameters: capacitance, resistance and inductance. Electrical wire models: The ideal wire, the lumped model, the lumped RC model, the distributed RC model, The transmission line model, SPICE wire models. MOS inverters: Resistive load inverter, inverter with n type MOSFET load, CMOS inverter: Switching Threshold, Noise Margin, Dynamic behavior of CMOS inverter, computing capacitances, propagation delay, Dynamic power consumption, static power consumption, energy, and energy delay product calculations, stick diagram, IC layout design and tools. Designing Combinational Logic Gates in MOS and CMOS: MOS logic circuits with depletion MOS load .Static CMOS Design: Complementary CMOS, Ratioed logic, Pass transistor logic, BICMOS logic, pseudo nMOS logic, Dynamic CMOS logic, clocked CMOS logic CMOS domino logic, NP domino logic, speed and power dissipation of Dynamic logic, cascading dynamic gates. Designing sequential logic circuits: Timing matrices for sequential circuits, classification of memory elements, static latches and registers, the bistability principle, multiplexer based latches , Master slave Edge triggered register , static SR flip flops, dynamic latches and registers, dynamic transmission gate edge triggered register, the C2 MOS register, Pulse registers, sense amplifier based registers, Pipelining, Latch verses Register based pipelines, NORA-CMOS. Two phase logic structure; VLSI designing methodology – Introduction, VLSI designs flow, Computer aided design technology: Design capture and verification tools, Design Hierarchy Concept of regularity, Modularity & Locality, VLSI design style, Design quality.'
# paragraphs_text=[string]
# print(paragraphs_text)

buffered=[]
for i in paragraphs_text:
	buffered.extend(i.split(','))	
titles=[]
print(buffered)
for i in range(len(buffered)):
	if buffered[i]=='\xa0':
		buffered[i+1]='\n\n_<h1>'+buffered[i+1]+'</h1>'

	elif ('Text/' in buffered[i]) == True:
		buffered[i]='  '

	elif ("<h1>" in buffered[i])==True:
		pass
		
	else:
		buffered[i]='\t\t>>>|<a href="https://www.google.com/search?&q='+buffered[i]+ '" target="_blank">'+buffered[i]+'</a><br>'		
		pass

str111=''
for i in buffered:
	str111+=i

with open('common.html','w+',errors='ignore') as f1:
	f1.write(str111)



