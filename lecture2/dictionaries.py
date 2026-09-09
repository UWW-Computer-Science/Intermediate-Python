import math


# ==========================================
# EXERCISES
# ==========================================

def count_frequent_characters(text: str, min_occurrences: int) -> dict[str, int]:
    """
    Takes a string and an integer threshold. 
    First, counts the frequency of every alphanumeric character (ignoring case).
    Then, returns a dictionary containing ONLY the characters that appear 
    at least `min_occurrences` times.
    """
    # TODO


def invert_mapping(original: dict[str, str]) -> dict[str, list[str]]:
    """
    Takes a dictionary where keys map to a single string value.
    Returns a new dictionary where the values from the original become the keys,
    and the new values are LISTS containing all original keys that mapped to it.
    Example: {"A": "X", "B": "X", "C": "Y"} -> {"X": ["A", "B"], "Y": ["C"]}
    """
    # TODO


def calculate_circle_areas(radii: list[float]) -> list[float]:
    """
    Takes a list of float radii.
    Returns a list using a standard **list comprehension** where each radius 
    is transformed into its corresponding area (pi * r^2).
    Use math.pi and round the result to 2 decimal places. 
    Do not use any conditions or filtering.
    """
    # TODO


def apply_discount_tiers(prices: list[float]) -> list[float]:
    """
    Takes a list of float prices.
    Returns a list using a **list comprehension** with an embedded **ternary operator**.
    If the price is $100.00 or greater, apply a 20% discount.
    Otherwise, apply a 10% discount.
    All resulting prices should be rounded to 2 decimal places.
    """
    # TODO


def extract_complex_words(sentences: list[str]) -> set[str]:
    """
    Takes a list of sentences.
    Returns a set using a **set comprehension** containing all unique words 
    that are strictly longer than 5 characters, converted to lowercase.
    """
    # TODO


def generate_grade_report(scores: list[int]) -> dict[int, str]:
    """
    Takes a list of integer scores.
    Returns a dictionary using a **dict comprehension** where the key is the score, 
    and the value is the corresponding letter grade.
    Grading scale: 90+ -> "A", 80-89 -> "B", 70-79 -> "C", 60-69 -> "D", <60 -> "F".
    """
    # TODO


# ==========================================
# TESTS - DO NOT MODIFY
# ==========================================

def run_test(test_name: str, actual, expected) -> None:
    print(f"--- {test_name} ---")
    print(f"Output: {actual}")
    matches = actual == expected
    GREEN, RED, RESET = '\033[92m', '\033[91m', '\033[0m'
    print(f"Matches expected: {GREEN if matches else RED}{matches}{RESET}" + 
          ("\n" if matches else f"; expected {expected}\n"))


def execute_all():
    print("Starting tests...\n")
    
    # 01. Count Frequent Characters
    run_test("test_01_freq_chars('Hello World!', 2)", count_frequent_characters("Hello World!", 2), {'l': 3, 'o': 2})
    run_test("test_01_freq_chars('No r3peats', 2)", count_frequent_characters("No r3peats", 2), {})
    run_test("test_01_freq_chars('Strawberry fields forever', 4)", count_frequent_characters("Strawberry fields forever", 4), {'r': 5, 'e': 4})
    
    # 02. Invert Mapping
    map_in = {"Alice": "Math", "Bob": "Science", "Charlie": "Math", "Dave": "History"}
    map_out = {"Math": ["Alice", "Charlie"], "Science": ["Bob"], "History": ["Dave"]}
    run_test("test_02_invert_mapping", invert_mapping(map_in), map_out)
    run_test("test_02_invert_mapping_empty", invert_mapping({}), {})

    # 03. Calculate Circle Areas
    run_test("test_03_calculate_circle_areas", calculate_circle_areas([1.0, 2.5, 0.0]), [3.14, 19.63, 0.0])

    # 04. Apply Discount Tiers
    prices_in = [150.0, 50.0, 100.0, 99.99]
    prices_out = [120.0, 45.0, 80.0, 89.99]
    run_test("test_04_apply_discount_tiers", apply_discount_tiers(prices_in), prices_out)

    # 05. Extract Complex Words
    text_data = ["The quick brown fox", "Jumps over the lazy dog", "Absolutely incredible performance"]
    expected_set = {"absolutely", "incredible", "performance"}
    run_test("test_05_extract_complex_words", extract_complex_words(text_data), expected_set)
    
    # 06. Generate Grade Report
    run_test("test_06_generate_grade_report", generate_grade_report([95, 82, 70, 50]), {95: 'A', 82: 'B', 70: 'C', 50: 'F'})


if __name__ == '__main__':
    execute_all()
