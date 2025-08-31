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

    for dat in people_data:
        pers = get_person_from_list_by_name(result, dat["name"])
        if pers:
            if dat.get("wife"):
                wife = get_person_from_list_by_name(result, dat["wife"])
                if wife:
                    pers.wife = wife
                    wife.husband = pers
            elif dat.get("husband"):
                husband = get_person_from_list_by_name(result, dat["husband"])
                if husband:
                    pers.husband = husband
                    husband.wife = pers

    return result
