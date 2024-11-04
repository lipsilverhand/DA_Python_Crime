print("----------------------------------------------------")
problem_2 = '''SELECT COMMUNITY_AREA_NUMBER , COMMUNITY_AREA_NAME FROM CENSUS_DATA
               WHERE PER_CAPITA_INCOME < 11000
'''
exe_2 = con.execute(problem_2).fetchall()
exe_2_final = [f"{name_2[0]}: {name_2[1]}" for name_2 in exe_2]
print(f"Problem 2: {exe_2}", ", ".join(exe_2_final))