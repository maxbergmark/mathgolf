from two_arguments import *
from single_argument import *
from zero_arguments import *
from check_type import *
from helper_functions import *

zero_args = {
	"☻" : push_16,
	"♥" : push_32,
	"♦" : push_64,
	"♣" : push_128,
	"♠" : push_256,
	"•" : push_512,
	"◘" : push_1024,
	"○" : push_2048,
	"◙" : push_4096,
	"♂" : push_10,
	"♀" : push_100,
	"♪" : push_1000,
	"♫" : push_10000,
	"☼" : push_100000,
	"►" : push_1000000,
	"◄" : push_10000000,
	"↕" : push_100000000,
	"0" : push_0,
	"1" : push_1,
	"2" : push_2,
	"3" : push_3,
	"4" : push_4,
	"5" : push_5,
	"6" : push_6,
	"7" : push_7,
	"8" : push_8,
	"9" : push_9,
	"b" : push_neg1,
	"c" : push_neg2,
	"d" : push_neg3,
	"e" : push_e,
	"t" : push_unixtime,
	"v" : push_random_int,
	"ƒ" : push_random_float,
	"⌂" : push_asterisk_yield,
	"ª" : push_1_array,
	"º" : push_0_array,
	"╟" : push_60,
	"╚" : push_3600,
	"╔" : push_86400,
	"π" : push_pi,
	"τ" : push_tau,
	" " : push_space,
	"A" : push_11,
	"B" : push_12,
	"C" : push_13,
	"D" : push_14,
	"E" : push_15,
	"F" : push_17,
	"G" : push_18,
	"H" : push_19,
	"I" : push_20,
	"J" : push_21,
	"K" : push_22,
	"L" : push_23,
	"M" : push_24,
	"N" : push_25,
	"O" : push_26,
	"P" : push_27,
	"Q" : push_28,
	"R" : push_29,
	"S" : push_30,
	"T" : push_31,
	"U" : push_33,
	"V" : push_34,
	"W" : push_35,
	"X" : push_36,
	"Y" : push_37,
	"Z" : push_38,
	"φ" : golden_ratio_yield,
	"▄" : alphabet_yield
}

one_arg = {
	"¶": is_prime_yield,
	"!": gamma_yield,
	"$": ord_or_char_yield,
	"(": decrease_yield,
	")": increase_yield,
	";": discard_tos_yield,
	"a": wrap_in_array_yield,
	"f": fibonnaci_yield,
	"h": length_yield,
	"i": cast_to_integer_yield,
	"n": print_lines_yield,
	"o": print_without_popping_yield,
	"p": print_with_newline_yield,
	"q": print_without_newline_yield,
	"r": get_range_yield,
	"s": sort_list_or_string_yield,
	"w": get_random_value_yield,
	"x": reverse_value_yield,
	"y": join_list_without_separator_yield,
	"z": sort_list_or_string_reverse_yield,
	"ü": ceiling_yield,
	"à": to_binary_string_yield,
	"å": from_binary_string_yield,
	"â": to_binary_yield,
	"ä": from_binary_yield,
	"ç": is_truthy_filter_yield,
	"¢": convert_hexadecimal_yield,
	"£": length_with_pop_yield,
	"¥": modulo_2_yield,
	"ó": pow_2_yield,
	"ú": pow_10_yield,
	"ñ": palindromize_yield,
	"Ñ": check_palindrome_yield,
	"½": halve_yield,
	"¼": quarter_yield,
	"░": convert_to_string_yield,
	"▒": split_string_or_int_yield,
	"┤": pop_from_right_yield,
	"╡": discard_from_right_yield,
	"├": pop_from_left_yield,
	"╞": discard_from_left_yield,
	"┐": copy_and_decrease_yield,
	"└": copy_and_increase_yield,
	"┴": check_if_1_yield,
	"┬": check_if_0_yield,
	"─": flatten_or_get_divisors_yield,
	"╦": get_dictionary_words_yield,
	"╤": get_symmetric_range_yield,
	"╨": round_up_to_pow_2_yield,
	"╒": get_range_1_based_yield,
	"╥": round_down_to_pow_2_yield,
	"╫": left_rotate_yield,
	"╪": right_rotate_yield,
	"┘": to_boolean_yield,
	"┌": to_boolean_inverted_yield,
	"▀": get_unique_elements_yield,
	"Σ": get_sum_yield,
	"σ": remove_leading_zeroes_yield,
	"δ": capitalize_string_yield,
	"∞": double_element_yield,
	"⌠": increase_twice_yield,
	"⌡": decrease_twice_yield,
	"°": is_square_yield,
	"_": duplicate,
	"∙": triplicate,
	"·": quadruplicate,
	"√": get_sqrt_yield,
	"ⁿ": get_cube_yield,
	"²": get_square_yield,
	"■": get_self_product_or_collatz_yield,
	"±": get_absolute_value_yield,
	"▓": get_average_of_list_yield,
	"│": get_diff_of_list_yield
}

two_args = {
	"§": get_list_or_string_item_or_concatenate_yield,
	"+": add_yield,
	"-": subtract_yield,
	"*": mult_yield,
	".": reverse_multiply_yield,
	"/": divide_yield,
	"╠": reverse_divide_yield,
	"#": power_yield,
	"u": join_yield,
	"▌": prepend_list_or_string_yield,
	"▐": append_list_or_string_yield,
	"Φ": increase_array_element_yield,
	"Θ": decrease_array_element_yield,
	"Ω": center_string_or_int_yield,
	"<": is_less,
	"=": is_equal,
	">": is_greater,
	"^": zip_yield,
	"¡": is_not,
	"≥": is_geq,
	"≤": is_leq,
	"÷": is_divisible_yield,
	"%": modulo_yield,
	"═": pad_to_equal_length,
	"╧": contains_yield
}
loop_handlers = {
	"↑": while_true_no_pop,
	"↓": while_false_no_pop,
	"→": while_true_pop,
	"←": while_false_pop,
	"∟" : do_while_true_no_pop,
	"↔" : do_while_false_no_pop,
	"▲" : do_while_true_pop,
	"▼" : do_while_false_pop
}
reducers = {
	"*": mult_yield,
	"#": power_yield,
	"+": add_yield,
	"-": subtract_yield,
	"/": divide_yield
}