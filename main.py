import pandas as pd
import sqlite3
from colorama import Fore, init

init(autoreset=True)

con = sqlite3.connect('FinalDB.db')

df_census = pd.read_csv('ChicagoCensusData.csv')
df_census.to_sql("CENSUS_DATA", con, if_exists='replace', index=False)

df_schools = pd.read_csv('ChicagoPublicSchools.csv')
df_schools.to_sql("CHICAGO_PUBLIC_SCHOOLS", con, if_exists='replace', index=False)

df_crime = pd.read_csv('ChicagoCrimeData.csv')
df_crime.to_sql("CHICAGO_CRIME_DATA", con, if_exists='replace', index=False)

con.commit()
print(Fore.GREEN + "Data has been converted into the database")

print("----------------------------------------------------")
problem_1 = '''SELECT COUNT(*) FROM CHICAGO_CRIME_DATA'''
exe_1 = con.execute(problem_1).fetchone()[0]
print(f"Problem 1: {exe_1}")

print("----------------------------------------------------")
problem_2 = '''SELECT COMMUNITY_AREA_NUMBER , COMMUNITY_AREA_NAME FROM CENSUS_DATA
               WHERE PER_CAPITA_INCOME < 11000
'''
exe_2 = con.execute(problem_2).fetchall()
exe_2_final = [f"{name_2[0]} : {name_2[1]}" for name_2 in exe_2]
print(f"Problem 2:", ", ".join(exe_2_final))

print("----------------------------------------------------")
problem_3 = '''SELECT CASE_NUMBER FROM CHICAGO_CRIME_DATA
               WHERE DESCRIPTION LIKE '%MINOR%'
'''
exe_3 = con.execute(problem_3).fetchall()
exe_3_final = [name[0] for name in exe_3]
print(f"Problem 3:", ", ".join(exe_3_final))

print("----------------------------------------------------")
problem_4 = '''SELECT * FROM CHICAGO_CRIME_DATA
               WHERE PRIMARY_TYPE = "KIDNAPPING" AND DESCRIPTION LIKE '%CHILD%'
'''
exe_4 = con.execute(problem_4).fetchmany()

print(f"Problem 4: {exe_4}")

print("----------------------------------------------------")
problem_5 = '''SELECT DISTINCT PRIMARY_TYPE FROM CHICAGO_CRIME_DATA
               WHERE LOCATION_DESCRIPTION LIKE '%SCHOOL%'
'''
exe_5 = con.execute(problem_5).fetchone()[0]

print(f"Problem 5: {exe_5}")

print("----------------------------------------------------")
problem_5 = '''SELECT DISTINCT PRIMARY_TYPE FROM CHICAGO_CRIME_DATA
               WHERE LOCATION_DESCRIPTION LIKE '%SCHOOL%'
'''
exe_5 = con.execute(problem_5).fetchone()[0]

print(f"Problem 5: {exe_5}")


print("----------------------------------------------------")
problem_6 = '''SELECT AVG(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS
               WHERE "Elementary, Middle, or High School" = 'MS'
'''
exe_6 = con.execute(problem_6).fetchone()[0]

print(f"Problem 6: {exe_6}")

print("----------------------------------------------------")
problem_7 = '''SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA
               ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC
               LIMIT 5
'''
exe_7 = con.execute(problem_7).fetchall()
exe_7_final = [name7[0] for name7 in exe_7]
print("Problem 7:", ", ".join(exe_7_final))


print("----------------------------------------------------")
problem_8 = '''SELECT COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA
               GROUP BY COMMUNITY_AREA_NUMBER
               ORDER BY COUNT(*) DESC
               LIMIT 1
               
'''
exe_8 = con.execute(problem_8).fetchone()[0]
print(f"Problem 8: {exe_8}")


print("----------------------------------------------------")
problem_9 = '''SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA
               WHERE HARDSHIP_INDEX IN (SELECT MAX(HARDSHIP_INDEX) FROM CENSUS_DATA)              
'''
exe_9 = con.execute(problem_9).fetchone()[0]
print(f"Problem 9: {exe_9}")

print("----------------------------------------------------")
problem_10 = '''SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA
               WHERE COMMUNITY_AREA_NUMBER = (SELECT COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(*) DESC LIMIT 1)              
'''
exe_10 = con.execute(problem_10).fetchone()[0]
print(f"Problem 10: {exe_10}")