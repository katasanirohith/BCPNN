import csv, time
from collections import defaultdict
drug_reports = {}
adr_reports = {}
start = time.time()
drugs = set()
adrs = set()
num = set()
import math
# g11 = 1
# alp = 2
# bet = 2
# alp1 = 1
# bet1 = 1
start = time.time()

def gamma_fucn(a, b, c, d,alp,alp1,bet,bet1,g11):
    N = a + b + c + d
    numerato = (N + alp) * (N + bet)
    denomo = (b + alp1) * (c + bet1)
    val = numerato / denomo
    val = g11 * val
    return val


def expectation(a, b, c, d, alp, alp1, bet, bet1, g11):
    N = a + b + c + d
    numearto = (a + g11) * (N + alp) * (N + bet)
    denomo = (N + gamma_fucn(a, b, c, d, alp, alp1, bet, bet1, g11)) * (a + b + alp1) * (a + c + bet1)
    val = numearto / denomo
    return math.log(val, 2)


def variance_function(a, b, c, d, alp, alp1, bet, bet1, g11):
    logValue = 1/(math.log(2, math.e)**2)
    N = a + b + c + d
    gam = gamma_fucn(a, b, c, d, alp, alp1, bet, bet1, g11)
    numerator = (N - a + gam - g11)
    d1 = (a + g11) * (1 + N + gam)
    d2num = (N - a - b + alp - alp1)
    d2den = (a + b + alp1) * (1 + N + alp)
    d2 = d2num / d2den
    d3num = (N - a - c + bet - bet1)
    d3den = (a + c + bet1) * (1 + N + bet)
    d3 = d3num / d3den
    denom = d1 + d2 + d3
    val = numerator / denom
    val = val * logValue
    return val


def standard_deviation(value):
    return math.sqrt(value)


def drug_data(fname):
    global drug_reports
    with open(fname, mode='r') as f:
        csv_reader = csv.reader(f, delimiter='$')
        next(csv_reader)
        for l in csv_reader:
            if l[0] in drug_reports:
               drug_reports[l[0]].append(l[4])
               drugs.add(l[4])
            else:
               drug_reports[l[0]] = []
               drug_reports[l[0]].append(l[4])
               drugs.add(l[4])


def adr_data(fname):
	global adr_reports
	with open(fname,mode='r') as f:
		csv_reader = csv.reader(f, delimiter='$')
		next(csv_reader)
		for l in csv_reader:
			if l[0] in adr_reports:
				adr_reports[l[0]].append(l[2])
				adrs.add(l[2])
			else:
				adr_reports[l[0]] = []
				adr_reports[l[0]].append(l[2])
				adrs.add(l[2])

def func():
	return([])

drug_data("C:\\Users\\Rohith Reddy\\Documents\\ADR\\ascii\\drug.txt")
adr_data("C:\\Users\\Rohith Reddy\\Documents\\ADR\\ascii\\adr.txt")
finaldic = {}
count = 0
dcount = {}
acount = {}
n=0
for i in drug_reports.keys():
	for bu in drug_reports[i]:
		try:
			finaldic[bu]
		except KeyError:
			finaldic[bu] = {}
		for k in adr_reports[i]:
			if bu == "ALFADIOL" and k == "Anaemia":
				print("hello")
				print(i)
			try:
				finaldic[bu][k] = finaldic[bu][k] + 1
			except KeyError:
				finaldic[bu][k] = 1
			try:
				acount[k] += 1
			except KeyError:
				acount[k] = 1
			try:
				dcount[bu] += 1
			except KeyError:
				dcount[bu] = 1
			n += 1
print(len(drug_reports))
print("hi")
f = open("adr-drug.txt", "w+")
print("bye")
sl = 0
wl = 0
ml = 0
nl = 0
addic = defaultdict(lambda: defaultdict(func))
with open("adr-drug.csv", mode='r') as f:
	csv_reader = csv.reader(f,delimiter = "$")
	for l in csv_reader:
		addic[l[0]][l[1]].append(float(l[3]))
		addic[l[0]][l[1]].append(float(l[4]))
		addic[l[0]][l[1]].append(float(l[5]))
		addic[l[0]][l[1]].append(float(l[6]))
		addic[l[0]][l[1]].append(float(l[7]))
		if l[0] == "BENTYL"and l[1] =="Muscular weakness":
			print(addic[l[0]][l[1]])
print(addic["BENTYL"]["Muscular weakness"])
for drug in finaldic:
	for adr in finaldic[drug]:
		a = finaldic[drug][adr]
		b = dcount[drug] - a
		c = acount[adr] - a
		d = n - a - b - c
		alp = addic[drug][adr][0]
		alp1 = addic[drug][adr][1]
		bet = addic[drug][adr][2]
		bet1 = addic[drug][adr][3]
		g11 = addic[drug][adr][4]

		exp = expectation(a, b, c, d, alp, alp1, bet, bet1, g11)
		var = variance_function(a, b, c, d, alp, alp1, bet, bet1, g11)
		std = standard_deviation(var)
		ans = exp - (2 * std)


		if 0 < ans <= 1.5:
			wl += 1
		elif 1.5 < ans <= 3.0:
			ml += 1
		elif ans > 3.0:
			sl += 1
		else:
			nl += 1
# with open("adr-drug.csv", mode='w+') as f:
#    csv_reader = csv.reader(f)
#    line = list(csv_reader)
#    for l in line:
# 	   if l[0] == drug and l[1] == adr:
# 		   l[2] = str(a+1)
# 		   l[3]= str(alp+n)
# 		   l[4] = str(alp1+a+b)
# 		   l[5] = str(bet+n)
# 		   l[6] = str(bet1+a+b)
# 		   l[7] = str(g11+a)
# with open('adr-drug.csv', mode='w') as f:
#    writer = csv.writer(f)
#    writer.writerows(line)
print("answers")
print(wl)
print(ml)
print(sl)
print(nl)

print(time.time()-start)




