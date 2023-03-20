days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

weekend = int(input("Сколько дней выходных на неделе вы хотите? "))

weekend_days = days[-weekend:]
weekday_days = days[:-weekend]

print("Ваши выходные дни:", ", ".join(weekend_days))
print("Ваши рабочие дни:", ", ".join(weekday_days))