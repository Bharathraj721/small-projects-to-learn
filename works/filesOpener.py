country_file=open("country.txt",'a')# change r to w a to append
#print(country_file.readable())
#print(country_file.readline())
#print(country_file.readlines()[3])
#for files in country_file.readlines():
#    print(files)
country_file.write("India")
country_file.write("\nAustralia ")
country_file.close