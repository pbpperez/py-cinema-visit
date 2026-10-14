from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer
    from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int = None, hall_number: int = None) -> None:
        resolved_number = number if number is not None else hall_number
        self.number = resolved_number
        self.hall_number = resolved_number

    def movie_session(
        self,
        movie_name: str,
        customers: list[Customer],
        cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
