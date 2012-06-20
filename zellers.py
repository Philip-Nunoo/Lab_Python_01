print "Philip Afful Nunoo"

firstname = ""
lastname = ""
month = ""
day = ""
year = ""

#############
vara = ""
varb = ""
varc = ""
vard = ""

varw = ""
varx = ""
vary = ""
varz = ""
varr = ""

#############
print "###########################"
print "The year starts from March"
print "eg.  March       = 1"
print "     April       = 2"
print "     May         = 3"
print "     June        = 4"
print "     July        = 5"
print "     August      = 6"
print "     September   = 7"
print "     October     = 8"
print "     November    = 9"
print "     December    = 10"
print "     January     = 11"
print "     February    = 12"
print "###########################"
print " "
firstname = raw_input("Enter your first name    : ")

lastname = raw_input ("Enter your last name     : ")

print "Enter your date of birth : "
month = raw_input ("     Month (1-12)?  ")
day1 = raw_input ("     Day ?    ")
year = raw_input ("     Year?   ")

if (int(month) == 11 or int(month) ==12):
    year = int(year) - 1

vara = int(month);
varb = int(day1);
varc = int(year)%100
vard = int(year)/100

varw = (13*vara - 1)/5
varx = (varc /4)
vary = vard /4
varz = varw + varx + vary + varb + varc - 2*vard
varr = varz % 7

while (varr <0):
    varr + 7
    
if (varr == 0):    
    day = "Sunday"
elif (varr == 1):
    day = "Monday"
elif (varr == 2):
    day = "Tuesday"
elif (varr == 3):
    day = "Wednesday"
elif (varr == 4):
    day = "Thursday"
elif (varr == 5):
    day = "Friday"
else:
    day = "Saturday"
    
print firstname, " " , lastname ," was born on " , month, day1, ",", year," on day,", day
