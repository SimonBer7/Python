from collections import Counter
from generator.timetable import Timetable

class TimetableEvaluator:
    def __init__(self, original_timetable):
        self.original_timetable = original_timetable
        self.penalties = {
            "same_subject_in_day": 1000,
            "room_change": 500,
            "floor_change": 1000,
            "lunch_time": 200,
            "daily_study_hours": 100,
            "max_study_hours": 200,
            "consecutive_lessons": 300,
            "math_profile_penalty": 500,
            "custom_rule_1": 100,  # Your custom rule #1
            "custom_rule_2": 150   # Your custom rule #2
        }

    def evaluate(self, timetable):
        score = 0
        subject_counts = Counter(timetable)

        # Rule 1: Same subject in one day penalty
        same_subject_penalty = sum(count * self.penalties["same_subject_in_day"] for count in subject_counts.values() if count > 1)

        # Rule 2: Room change penalty
        room_change_penalty = self.penalties["room_change"] * self.count_room_changes(timetable)

        # Rule 3: Floor change penalty
        floor_change_penalty = self.penalties["floor_change"] * self.count_floor_changes(timetable)

        # Rule 4: Lunch time penalty
        lunch_time_penalty = self.penalties["lunch_time"] * self.penalty_for_lunch_time(timetable)

        # Rule 5: Daily study hours penalty
        daily_study_hours_penalty = abs(self.penalties["daily_study_hours"] * (self.count_daily_study_hours(timetable) - 5))

        # Rule 6: Maximum study hours penalty
        max_study_hours_penalty = self.penalties["max_study_hours"] * max(self.count_max_study_hours(timetable) - 8, 0)

        # Rule 7: Consecutive lessons penalty
        consecutive_lessons_penalty = self.penalties["consecutive_lessons"] * self.count_consecutive_lessons(timetable)

        # Rule 8: Math and profile penalty
        math_profile_penalty = self.penalties["math_profile_penalty"] * self.math_profile_penalty(timetable)

        # Rule 9: Custom rule #1 penalty
        custom_rule_1_penalty = self.penalties["custom_rule_1"] * self.custom_rule_1(timetable)

        # Rule 10: Custom rule #2 penalty
        custom_rule_2_penalty = self.penalties["custom_rule_2"] * self.custom_rule_2(timetable)

        # Total score
        score = -same_subject_penalty - room_change_penalty - floor_change_penalty - lunch_time_penalty \
                - daily_study_hours_penalty - max_study_hours_penalty - consecutive_lessons_penalty \
                - math_profile_penalty - custom_rule_1_penalty - custom_rule_2_penalty

        return score

    def count_room_changes(self, timetable):
        # Your implementation to count room changes
        return 0

    def count_floor_changes(self, timetable):
        # Your implementation to count floor changes
        return 0

    def penalty_for_lunch_time(self, timetable):
        # Your implementation to calculate penalty for lunch time
        return 0

    def count_daily_study_hours(self, timetable):
        # Your implementation to count daily study hours
        return 0

    def count_max_study_hours(self, timetable):
        # Your implementation to count maximum study hours in a day
        return 0

    def count_consecutive_lessons(self, timetable):
        # Your implementation to count consecutive lessons
        return 0

    def math_profile_penalty(self, timetable):
        # Your implementation for math and profile penalty
        return 0

    def custom_rule_1(self, timetable):
        # Your implementation for custom rule #1 penalty
        return 0

    def custom_rule_2(self, timetable):
        # Your implementation for custom rule #2 penalty
        return 0

# Example usage:
original_timetable = Timetable()
evaluator = TimetableEvaluator(original_timetable.table["Monday"])

# Replace the following line with your generated timetable
variant_timetable = original_timetable.table["Monday"]

score = evaluator.evaluate(variant_timetable)
print(f"Score for the variant timetable: {score}")
