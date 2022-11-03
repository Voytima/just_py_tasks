# 6) Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
import calendar

date = int(input("Enter week day number 0-6: "))
if date == 5 or date == 6:
    print(f"Day: {date} - {calendar.day_name[date]} - weekend :)")
else:
    print(f"Day: {date} - {calendar.day_name[date]} - not a weekend :(")
