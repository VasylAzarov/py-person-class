from typing import Optional, List


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def get_person_from_list_by_name(
        people: List[Person],
        expected_name: str
    ) -> Optional[Person]:

    for person in people:
        if expected_name == person.name:
            return person
    return None


def create_person_list(people_data: List[dict]) -> List[Person]:
    result: List[Person] = []

    for person_info in people_data:
        result.append(Person(person_info["name"], person_info["age"]))

    for person_info in people_data:
        pers = get_person_from_list_by_name(result, person_info["name"])

        if person_info.get("wife"):
            wife = get_person_from_list_by_name(result, person_info["wife"])
            if pers and wife:
                pers.wife = wife
                wife.husband = pers
        elif person_info.get("husband"):
            husband = get_person_from_list_by_name(result, person_info["husband"])
            if pers and husband:
                pers.husband = husband
                husband.wife = pers

    return result
