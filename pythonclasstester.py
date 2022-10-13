from pprint import pprint as pretty

class FlightClass:
	def __init__(self, number, airplane):
		if not number[:2].isalpha():
			raise ValueError(f"No airline code in '{number}'")
		if not number[:2].isupper():
			raise ValueError(f"Invalid airline code '{number}'")
		if not (number[2:].isdigit() and int(number[2:]) <= 9999):
			raise ValueError(f"Invalid route number '{number}'")

		self._number = number
		self._airplane = airplane
		rows, seats = self._airplane.seating_plan()
		self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

	def airplane_model(self):
		return self._airplane.model()

	def number(self):
		return self._number


class Airplane:
    def __init__(self, model, num_of_rows, num_of_seats_per_row):
        self._model = model
        self._num_of_rows = num_of_rows
        self._num_of_seats_per_row = num_of_seats_per_row
        
    def model(self):
        return self._model
        
    def seating_plan(self):
        return (range(1, self._num_of_rows + 1),"ABCDEFGHJK"[:self._num_of_seats_per_row])

pretty(FlightClass("DK770", Airplane("Boeing 77", num_of_rows=12, num_of_seats_per_row=4))._seating)