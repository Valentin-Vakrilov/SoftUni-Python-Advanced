def positive_negative_nums(numbers):
    positive_nums = []
    negative_nums = []

    for number in numbers:
        current_number = int(number)
        if current_number > 0:
            positive_nums.append(current_number)
        else:
            negative_nums.append(current_number)

    print(sum(negative_nums))
    print(sum(positive_nums))

    if sum(positive_nums) > abs(sum(negative_nums)):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers_sequence = input().split()

positive_negative_nums(numbers_sequence)
