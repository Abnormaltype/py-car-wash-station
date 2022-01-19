class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars):
        amount = sum([self.calculate_washing_price(i) for i in list_cars if
                      i.clean_mark <= self.clean_power])
        for i in list_cars:
            self.wash_single_car(i)

        return amount

    def calculate_washing_price(self, other):
        return round(other.comfort_class
                     * (self.clean_power - other.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1
                     )

    def wash_single_car(self, other):
        if self.clean_power > other.clean_mark:
            other.clean_mark = self.clean_power
        return other

    def rate_service(self, income_rating):
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating
             * (self.count_of_ratings - 1)
             + income_rating)
            / self.count_of_ratings, 1
        )
