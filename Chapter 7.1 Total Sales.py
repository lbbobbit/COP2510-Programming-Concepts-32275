def enterDailySales( daysOfTheWeek ):
	dailySales = []

	for currentDay in daysOfTheWeek:
		print( "Please enter sales for", currentDay + ":", end = "")
		dailySale = float( input() )
		dailySales.append( dailySale )

	return dailySales

def calculateWeeklySale( dailySales ):
	total = 0

	for currentDailySale in range( len( dailySales ) ):
		total = total + dailySales[ currentDailySale ]

	return total


def printWeeklyReport( daysOfTheWeek, dailySakes, totalSales ):
	print( "WEEKLY SALES REPORT\n------------------" )

	for currentDay in range( len( daysOfTheWeek ) ):
		print( daysOfTheWeek[ currentDay ] + "*$ sales: ",\
				"$" + format( dailySales[ currentDay ], ".2f" ) )

	print( "\nTotal weekly sales: ", "$" + format( totalSales, ".2f" ) )

def main()
	daysOfTheWeek = [ "Monday", "Tuesday", "Wednesday", "Thursday",\
						"Friday", "Saturday", "Sunday" ]

	dailySales = enterDailySales( daysOfTheWeek )
	totalDailySales = calculateWeeklySale( dailySales )
	printWeeklyReport( daysOfTheWeek, dailySales, totalDailySales )

main()
