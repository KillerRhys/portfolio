# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
#
# squared_numbers = [n * n for n in numbers]
# result = [n for n in numbers if n % 2 == 0]
#
# print(squared_numbers)
# print(result)


# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# import random
# score = {student:random.randint(1, 100) for student in names}
# passing_score = {student:score for (student, score) in score.items() if score > 70}
# print(score)
# print(passing_score)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
#
#
# print(result)


# weather_c = {
#     'Monday': 12,
#     'Tuesday': 14,
#     'Wednesday':15,
#     'Thursday':14,
#     'Friday':21,
#     'Saturday':22,
#     'Sunday': 24,
# }
#
#
# weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)
