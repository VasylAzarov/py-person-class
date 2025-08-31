from typing import Optional, List


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def get_person_from_list_by_name(
    people: List[Person], expected_name: str
) -> Optional[Person]:
    return next((p for p in people if p.name == expected_name), None)


def create_person_list(people_data: List[dict]) -> List[Person]:
    result: List[Person] = [Person(d["name"], d["age"]) for d in people_data]

    for d in people_data:
        pers = get_person_from_list_by_name(result, d["name"])
        if pers:
            if d.get("wife"):
                wife = get_person_from_list_by_name(result, d["wife"])
                if wife:
                    pers.wife = wife
                    wife.husband = pers
            elif d.get("husband"):
                husband = get_person_from_list_by_name(result, d["husband"])
                if husband:
                    pers.husband = husband
                    husband.wife = pers

    return result
