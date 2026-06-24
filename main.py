import course_service_pb2

# Проверяем наличие классов
print(dir(course_service_pb2))

# Проверяем конкретные классы
try:
    print(course_service_pb2.GetCourseRequest)
    print(course_service_pb2.GetCourseResponse)
    print("Классы найдены!")
except AttributeError as e:
    print(f"Класс не найден: {e}")
