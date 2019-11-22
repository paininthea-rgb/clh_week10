import csv
import matplotlib.pyplot as plt 

# total medal trends ~ sampled years (20 year increments)
# 1924, 1948, 1968, 1984, 2006, 2014
# columns 0 (year) and column 4 (country)

m_1924 = 0
m_1948 = 0
m_1968 = 0
m_1984 = 0
m_2006 = 0
m_2014 = 0

categories = []

with open('OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			# parse that first row of text data out of the file
			categories.append(row)
			line_count += 1 

		else:
			if (row[0] == "1924") and (row[4] == "CAN"):
				print("1924 medal for Canada!")
				m_1924 += 1

			elif (row[0] == "1948") and (row[4] == "CAN"):
				print("1948 medal for Canada!")
				m_1948 += 1

			elif (row[0] == "1968") and (row[4] == "CAN"):
				print("1968 medal for Canada!")
				m_1968 += 1

			elif (row[0] == "1984") and (row[4] == "CAN"):
				print("1984 medal for Canada!")
				m_1984 += 1

			elif (row[0] == "2006") and (row[4] == "CAN"):
				print("2006 medal for Canada!")
				m_2006 += 1

			elif (row[0] == "2014") and (row[4] == "CAN"):
				print("2014 medal for Canada!")
				m_2014 += 1

# output a chart here! a line chart would probably be best
medalCounts = [m_1924, m_1948, m_1968, m_1984, m_2006, m_2014]
years = [1924, 1948, 1968, 1984, 2006, 2014]

plt.plot(years, medalCounts, color="red", linewidth=6.0)
plt.xlabel("Olympic Year")
plt.ylabel("Medals by Year")
plt.title("Medals Sampled by 20 Years Increments")
plt.show()