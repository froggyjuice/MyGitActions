# 간단한 대화 코드
user_input = input("안녕하세요! 궁금한 점이 있나요? ")

if "이름" in user_input:
    print("저는 파이썬 대화봇이에요!")
elif "날씨" in user_input:
    print("아직 날씨는 확인할 수 없어요")
elif "취미" in user_input:
    print("저는 프로그래밍과 학습을 좋아해요!")
else:
    print("잘 이해하지 못했어요. 다시 말씀해주시겠어요?")

# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 출력합니다.
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

# 값을 변경합니다.
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])

# 반복문과 리스트 내포
pets = [
    {"name" : "구름", "age" : 5},
    {"name" : "초코", "age" : 4},
    {"name" : "아지", "age" : 3},
    {"name" : "호랑이", "age": 1}
]

pet_names = ", ".join([pet["name"] for pet in pets])
print(f"우리 동네 강아지들의 이름은 {pet_names}입니다.")

for pet in pets:
    name = pet["name"]
    age = pet["age"]
    print(f"이 강아지의 이름은 {name}, 나이는 {age} 입니다.")

character = {
    "name" : "기사",
    "level" : 23,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "강철 갑옷"
    },
    "skills" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    value = character[key]
    if type(value) is str or type(value) is int:
        print(f"{key} : {value}")
    elif type(value) is dict:
        for sub_key, sub_value in value.items():
            print(f"{sub_key} : {sub_value}")
    elif type(value) is list:
        for item in value:
            print(f"{key} : {item}")

character = {
    "name": "기사",
    "level": 23,
    "items": {
        "sword": "불꽃의 검",
        "armor": "강철 갑옷"
    },
    "skills": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    value = character[key]  # 각 키에 대한 값 가져오기
    if isinstance(value, (str, int)):
        # 값이 문자열이나 숫자일 경우 그대로 출력
        print(f"{key} : {value}")
    
    elif isinstance(value, dict):
        # 값이 딕셔너리일 경우 내부 키-값 쌍을 개별적으로 출력
        for sub_key, sub_value in value.items():
            print(f"{sub_key} : {sub_value}")
    
    elif isinstance(value, list):
        # 값이 리스트일 경우 각 요소를 개별적으로 출력
        for item in value:
            print(f"{key} : {item}")


